# Katka API

Katka API provides a Restful API to manage CI/CD on a tech organization.

## Contribute

### Workflow
1. [Fork this project](https://help.github.com/articles/fork-a-repo/) to your account.
2. [Create a branch](https://help.github.com/articles/creating-and-deleting-branches-within-your-repository/) 
for the change you intend to make.
3. Make your changes to your fork.
4. [Send a pull request](https://help.github.com/articles/using-pull-requests/) 
from your fork’s branch to the `master` branch of this project.

## Environment

Make virtual environment

```
$ make venv
```

Activate virtual environment

```
$ source venv/bin/activate
```

Launch Django development server

```
./src/manage.py runserver
```

## Requirements Handling

The project has automated handling of production requirements, the idea behind it is that
you should always use the latest versions of every requirement, a Makefile target is in place
to update the `requirements.txt` file (`make requirements.txt` will do).

In case you need a specific version of a library, the protocol should be:

* Place the needed fixed version using pip notation in any of the requirements/* files
* Put a comment over the fixed requirement explaining the reason for fixing it (usually with a link to an issue/bug)
* Run `make requirements.txt`, the resulting requirements file will include the fixed version of the package

For some more advanced uses, a manual edit of the requirements.txt can be done but make sure to document it 
somewhere because `make requirements.txt` *will* overwrite this file.

# Testing against latest versions

By default, `tox` and `make test` will only test against production requirements, 
in order to test against latest versions of the dependencies on `latest36` environment.

It can be run via `tox -e latest36` or also with `make test_latest`




Test2
