# This Makefile requires the following commands to be available:
# * virtualenv
# * python3.6
# * docker
# * docker-compose

DOCKER_HUB_NAMESPACE=kpnnv
REPOSITORY_TEST=katka-api-test

REQUIREMENTS_BASE:=requirements/requirements-base.txt
REQUIREMENTS_TEST:=requirements/requirements-testing.txt
REQUIREMENTS_TXT:=requirements.txt

DOCKER_COMPOSE=$(shell which docker-compose)

PYTHON_VERSION=python3.6
MAKE_MIGRATIONS=`$(shell echo $(PYTHON)) src/manage.py makemigrations;`
MIGRATIONS_CHECK=`echo $(MAKE_MIGRATIONS_OUTPUT) | awk '{print match($$0, "No changes detected")}'`
PARAMS=src/main/params.py


.PHONY: clean pyclean test lint isort docker setup.py check_forgotten_migrations venv $(REQUIREMENTS_TXT)


# ********** Cleaning **********

pyclean:
	@find . -name *.pyc -delete
	@rm -rf *.egg-info build
	@rm -rf coverage.xml .coverage

clean: pyclean
	@rm -rf venv
	@rm -rf .tox


# ********** Params file **********

# build params file if it does not exist
$(PARAMS): | src/main/params.example.py
	@cp $| $@


# ********** Migrations **********

# check if there is any forgotten migration
check_forgotten_migrations: $(PARAMS) install_requirement_txt
	$(eval MAKE_MIGRATIONS_OUTPUT:="$(shell echo $(MAKE_MIGRATIONS))")
	@echo $(MAKE_MIGRATIONS_OUTPUT)
	@if [ $(MIGRATIONS_CHECK) -gt 0 ]; then \
		echo "There aren't any forgotten migrations. Well done!"; \
	else \
		echo "Error! You've forgotten to add the migrations!"; \
		exit 1; \
	fi

# migrate on dev environment
migrate_dev:
	python src/manage.py migrate --noinput
	@echo 'Done!'


# ********** Docker **********
docker/build/test_image:
	docker build -f Dockerfile-test -t $(DOCKER_HUB_NAMESPACE)/$(REPOSITORY_TEST):latest .

docker/push/test_image:
	docker push $(DOCKER_HUB_NAMESPACE)/$(REPOSITORY_TEST):latest

docker/%:
	$(DOCKER_COMPOSE) run --rm test-app make $*


# ********** Tests **********

# Used by the PR jobs. This target should include all tests necessary
# to determine if the PR should be rejected or not.
tox:
	tox

test: docker/check_forgotten_migrations docker/tox
	@echo 'tests done'

test_local: check_forgotten_migrations tox
	@echo 'tests done'


# ********** Requirements **********

# main requirements file definition
$(REQUIREMENTS_TXT):
	tox -e requirements_txt
	@echo "Successfully Updated requirements"

# check if requirements.txt file exists on the project root
check_requirements_txt:
	@if [ ! -f "$(REQUIREMENTS_TXT)" ]; then \
		echo "ERROR: Missing $(REQUIREMENTS_TXT), it should be committed to the repository"; \
		exit 1; \
	fi
	@touch $(REQUIREMENTS_TXT) # to make sure that REQUIREMENTS_TXT is the requirements file with the latest timestamp

install_requirement_txt:
	pip install -r $(REQUIREMENTS_TXT)


# ********** Virtual environment **********
venv:
	@rm -rf venv
	@$(PYTHON_VERSION) -m venv venv
	@venv/bin/pip install -r $(REQUIREMENTS_TXT)
	@venv/bin/pip install -r $(REQUIREMENTS_TEST)
	@touch $@
