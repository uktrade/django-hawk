from typing import Callable, Optional

from django.http import HttpRequest, HttpResponse
from django.utils.deprecation import MiddlewareMixin
from mohawk import Receiver

from django_hawk.settings import django_hawk_settings


class HawkResponseMiddleware(MiddlewareMixin):
    def __init__(self, get_response: Optional[Callable] = None) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        if not self.get_response:
            raise Exception("get_response is not defined")

        response = self.get_response(request)

        hawk_receiver: Optional[Receiver] = getattr(
            request,
            django_hawk_settings.REQUEST_ATTR_NAME,
            None,
        )
        if hawk_receiver:
            response["Server-Authorization"] = hawk_receiver.respond(
                content=response.content,
                content_type=response["Content-Type"],
            )

        return response
