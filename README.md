# Django Hawk

This package can be used to help create HAWK Authenticated views.

## Installation

```
pip install django-hawk
```

Add the following to your Django Settings:

```python
DJANGO_HAWK = {
    "HAWK_INCOMING_ACCESS_KEY": "xxx",
    "HAWK_INCOMING_SECRET_KEY": "xxx",
}
```

## Example Usage

To use the HAWK Authentication, we need to do 2 things:

1. Make sure the `HawkResponseMiddleware` runs
2. Check the authentication

Add the `HawkResponseMiddleware` to the `MIDDLEWARE` setting in your project like so:

```
MIDDLEWARE = [
    ...
    "django_hawk.middleware.HawkResponseMiddleware",
    ...
]
```

To check the authentication you can call `django_hawk.utils.authenticate_request`, if an exception isn't raised then you know that the request is authenticated, see below for examples.

```python
from django.http import HttpResponse

from django_hawk.utils import DjangoHawkAuthenticationFailed, authenticate_request

def simple_view(request):
    # Try to authenticate with HAWK
    try:
        authenticate_request(request=request)
    except DjangoHawkAuthenticationFailed as e:
        return HttpResponse(status=401)

    # Continue with normal View code...
    return HttpResponse("This is a simple view")
```

## Testing

Tests belong in the `/django_hawk/tests/` directory. You can run the tests by installing the requirements like so:

```
make setup
```

Now you can run the tests using the following command:

```
poetry run python manage.py test
```

### Tox tests

We use [tox](https://pypi.org/project/tox/) to test compatibility across different Django versions.

To run these tests with tox, just run the following:

```
make tox
```

## Pushing to PyPI

- [PyPI Package](https://pypi.org/project/django-hawk/)
- [Test PyPI Package](https://test.pypi.org/project/django-hawk/)

Running `make build-package` will build the package into the `dist/` directory.

Running `make push-pypi-test` will push the built package to Test PyPI.

Running `make push-pypi` will push the built package to PyPI.

### Setting up poetry for pushing to PyPI

First you will need to add the test pypy repository to your poetry config:

```
poetry config repositories.test-pypi https://test.pypi.org/legacy/
```

Then go to https://test.pypi.org/manage/account/token/ and generate a token.

Then add it to your poetry config:

```
poetry config pypi-token.test-pypi XXXXXXXX
```

Then you also need to go to https://pypi.org/manage/account/token/ to generate a token for the real PyPI.

Then add it to your poetry config:

```
poetry config pypi-token.pypi XXXXXXXX
```

Now the make commands should work as expected.
