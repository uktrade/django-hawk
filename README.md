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
