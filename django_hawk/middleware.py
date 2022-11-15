from typing import Callable, Optional, cast

from django.http import HttpRequest, HttpResponse
from django.utils.deprecation import MiddlewareMixin

from django_hawk.types import DjangoHawkRequest


class HawkResponseMiddleware(MiddlewareMixin):
    def __init__(self, get_response: Optional[Callable] = None) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        if not self.get_response:
            raise Exception("get_response is not defined")

        response = self.get_response(request)

        if hasattr(request, "django_hawk_auth"):
            request = cast(DjangoHawkRequest, request)
            if request.django_hawk_auth:
                response["Server-Authorization"] = request.django_hawk_auth.respond(
                    content=response.content,
                    content_type=response["Content-Type"],
                )

        return response
