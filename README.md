# Django Hawk

A descriptive line about the package

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

### Django rest framework

```python
from django_hawk.authentication import HawkAuthentication
from django_hawk.middleware import HawkResponseMiddleware

from django.utils.decorators import decorator_from_middleware

from rest_framework.viewsets import ViewSet


class ExampleViewSet(ViewSet):
    authentication_classes = (HawkAuthentication,)
    permission_classes = ()

    @decorator_from_middleware(HawkResponseMiddleware)
    def list(self, request):
        return super().list(request)
```

## Testing

Tests belong in the `/django_hawk/tests/` directory. You can run the tests by installing the requirements like so:

```
pip install -r dev-requirements.txt
```

Now you can run the tests using the following command:

```
./manage.py test
```

### Tox tests

We use [tox](https://pypi.org/project/tox/) to test compatibility across different Django versions.

To run these tests with tox, just run the following:

```
tox
```

## Pushing to [PyPI](https://pypi.org/)

TODO: update with notes on how to push package to PyPI once we have the package setup.
