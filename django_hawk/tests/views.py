from django.http import HttpResponse
from django.utils.decorators import decorator_from_middleware
from django_hawk.authentication import HawkAuthentication
from django_hawk.middleware import HawkResponseMiddleware
from rest_framework.viewsets import ViewSet


class ExampleViewSet(ViewSet):
    authentication_classes = (HawkAuthentication,)
    permission_classes = ()

    @decorator_from_middleware(HawkResponseMiddleware)
    def list(self, request):
        return HttpResponse()
