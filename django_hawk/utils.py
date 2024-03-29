import logging
from typing import TYPE_CHECKING

from django.http import HttpRequest
from mohawk.exc import HawkFail

from django_hawk.authentication import authorise
from django_hawk.settings import django_hawk_settings

if TYPE_CHECKING:
    from mohawk import Receiver

logger = logging.getLogger(__name__)


class DjangoHawkAuthenticationFailed(Exception):
    pass


def authenticate_request(request: HttpRequest) -> "Receiver":
    if "HTTP_AUTHORIZATION" not in request.META:
        raise DjangoHawkAuthenticationFailed(
            django_hawk_settings.NO_CREDENTIALS_MESSAGE
        )

    try:
        hawk_receiver = authorise(request)
    except HawkFail as e:
        logger.warning(
            "Failed authentication {e}".format(
                e=e,
            )
        )
        raise DjangoHawkAuthenticationFailed(
            django_hawk_settings.INCORRECT_CREDENTIALS_MESSAGE
        )
    setattr(request, django_hawk_settings.REQUEST_ATTR_NAME, hawk_receiver)
    return hawk_receiver
