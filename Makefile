# This Makefile requires the following commands to be available:
# * virtualenv
# * python3.6
# * docker
# * docker-compose

REQUIREMENTS_BASE:=requirements/requirements-base.txt
REQUIREMENTS_TEST:=requirements/requirements-testing.txt
REQUIREMENTS_TXT:=requirements.txt

DOCKER_COMPOSE=$(shell which docker-compose)

PIP:=$(shell which pip)
PIP_VENV:="venv/bin/pip"
TOX="venv/bin/tox"
PYTHON=$(shell which python)
PYTHON_VENV="venv/bin/python"

# Empty files used to keep track of installed types of virtualenvs (see rules below)
VENV_NO_SYSTEM_SITE_PACKAGES=venv/.venv_no_system_site_packages
VENV_DEPLOY=venv/.venv_deploy
VENV_BASE=venv/.venv_base
VENV_TEST=venv/.venv_test
VENV_TOX=venv/.venv_tox
VENV_DEV=venv/.venv_dev

# Params for building and installing on the EXA servers

PYPI="https://$(PYPI_HOST)/simple"
PYPI_HOST=pypi.org
PYTHON_VERSION=python3.6
MAKE_MIGRATIONS=`$(shell echo $(PYTHON)) src/manage.py makemigrations;`
MAKE_MIGRATIONS_VENV=`$(shell echo $(PYTHON_VENV)) src/manage.py makemigrations;`
MIGRATIONS_CHECK=`echo $(MAKE_MIGRATIONS_OUTPUT) | awk '{print match($$0, "No changes detected")}'`
PARAMS=src/main/params.py


.PHONY: clean pyclean test lint isort docker setup.py check_forgotten_migrations

tox: $(VENV_TOX)
	$(TOX)


# ********** Cleaning **********

pyclean:
	@find . -name *.pyc -delete
	@rm -rf *.egg-info build
	@rm -rf coverage.xml .coverage
	@rm -f katka-api-*.tgz

clean: pyclean
	@rm -rf venv
	@rm -rf .tox


# ********** Params file **********

# build params file if it does not exist
$(PARAMS): | src/main/params.example.py
	@cp $| $@


# ********** Sanity Checks **********

# base check for forgotten migration
base_check_forgotten_migrations/%:
	$(eval MAKE_MIGRATIONS_OUTPUT:="$(shell echo $($*))")
	@echo $(MAKE_MIGRATIONS_OUTPUT)
	@if [ $(MIGRATIONS_CHECK) -gt 0 ]; then \
		echo "There aren't any forgotten migrations. Well done!"; \
	else \
		echo "Error! You've forgotten to add the migrations!"; \
		exit 1; \
	fi

# check if there is any forgotten migration using venv
check_forgotten_migrations_venv: $(PARAMS) $(VENV_BASE) base_check_forgotten_migrations/MAKE_MIGRATIONS_VENV

# check if there is any forgotten migration without venv
check_forgotten_migrations: $(PARAMS) install_requirement_txt base_check_forgotten_migrations/MAKE_MIGRATIONS


# check if requirements.txt file exists on the project root
check_requirements_txt:
	@if [ ! -f "$(REQUIREMENTS_TXT)" ]; then \
		echo "ERROR: Missing $(REQUIREMENTS_TXT), it should be committed to the repository"; \
		exit 1; \
	fi
	@touch $(REQUIREMENTS_TXT) # to make sure that REQUIREMENTS_TXT is the requirements file with the latest timestamp


# ********** Migrations **********

# migrate on dev environment
migrate_dev: $(VENV_DEV)
	@$(PYTHON_VENV) src/manage.py migrate --noinput
	@echo 'Done!'


# ********** Docker **********

docker/%:
	$(DOCKER_COMPOSE) run --rm app make $*


# ********** Tests **********

# Used by the PR jobs. This target should include all tests necessary
# to determine if the PR should be rejected or not.
test_docker: docker/check_forgotten_migrations docker/tox
	@echo 'tests done'

test: check_forgotten_migrations_venv tox
	@echo 'tests done'

lint: $(VENV_TOX)
	@$(TOX) -e lint
	@$(TOX) -e isort-check

isort: $(VENV_TOX)
	@$(TOX) -e isort-fix


# ********** Setup **********

# set setup.py file
setup.py: $(VENV_DEV)
	$(PYTHON_VENV) setup_gen.py


# ********** Requirements **********

# main requirements file definition
$(REQUIREMENTS_TXT): $(REQUIREMENTS_BASE) | $(VENV_TOX)
	@$(TOX) -e requirements_txt
	@echo "Successfully Updated requirements"

install_requirement_txt:
	@$(PIP) install --index-url $(PYPI) -r $(REQUIREMENTS_TXT)


# ********** Environments definition **********

# create development venv
venv: $(VENV_DEV) $(PARAMS)

$(VENV_NO_SYSTEM_SITE_PACKAGES):
	@rm -rf venv
	@$(PYTHON_VERSION) -m venv venv
	@touch $@

$(VENV_BASE): $(VENV_NO_SYSTEM_SITE_PACKAGES) check_requirements_txt
	@$(PIP_VENV) install --index-url $(PYPI) -r $(REQUIREMENTS_TXT)
	@touch $@

$(VENV_TEST): $(VENV_NO_SYSTEM_SITE_PACKAGES) $(REQUIREMENTS_TEST)
	@$(PIP_VENV) install --index-url $(PYPI) -r $(REQUIREMENTS_TEST)
	@touch $@

$(VENV_TOX): $(VENV_NO_SYSTEM_SITE_PACKAGES)
	@$(PIP_VENV) install --index-url $(PYPI) tox
	@touch $@

$(VENV_DEV): $(VENV_TOX) $(VENV_BASE) $(VENV_TEST)
	@touch $@
