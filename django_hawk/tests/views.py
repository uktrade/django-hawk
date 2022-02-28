from django.http import HttpResponse, JsonResponse
from django.utils.decorators import decorator_from_middleware
from django_hawk.drf.authentication import HawkAuthentication
from django_hawk.middleware import HawkResponseMiddleware
from django_hawk.utils import DjangoHawkAuthenticationFailed, authenticate_request
from rest_framework.viewsets import ViewSet

"""
Base Django
"""


@decorator_from_middleware(HawkResponseMiddleware)
def simple_view(request):
    try:
        authenticate_request(request=request)
    except DjangoHawkAuthenticationFailed as e:
        return JsonResponse(
            status=401,
            data={
                "detail": "Incorrect authentication credentials.",
            },
        )
    return HttpResponse("This is a simple view")


"""
Django Rest Framework
"""


class ExampleViewSet(ViewSet):
    authentication_classes = (HawkAuthentication,)
    permission_classes = ()

    @decorator_from_middleware(HawkResponseMiddleware)
    def list(self, request):
        return HttpResponse("This is a DRF view")
