from typing import Callable

from django.http import HttpRequest, HttpResponse
from django.utils.deprecation import MiddlewareMixin


class HawkResponseMiddleware(MiddlewareMixin):
    def __init__(self, get_response: Callable) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        assert self.get_response

        response = self.get_response(request)

        response["Server-Authorization"] = request.auth.respond(  # type: ignore
            content=response.content,
            content_type=response["Content-Type"],
        )
        return response
