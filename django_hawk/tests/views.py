from django.http import HttpRequest, HttpResponse, JsonResponse

from django_hawk.utils import DjangoHawkAuthenticationFailed, authenticate_request


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
