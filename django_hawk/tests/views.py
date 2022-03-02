from django.http import HttpRequest, HttpResponse, JsonResponse
from django.utils.decorators import decorator_from_middleware

from django_hawk.middleware import HawkResponseMiddleware
from django_hawk.utils import DjangoHawkAuthenticationFailed, authenticate_request


@decorator_from_middleware(HawkResponseMiddleware)
def simple_view(request: HttpRequest) -> HttpResponse:
    try:
        authenticate_request(request=request)
    except DjangoHawkAuthenticationFailed as e:
        return JsonResponse(
            status=401,
            data={
                "detail": str(e),
            },
        )
    return HttpResponse("This is a simple view")
