from typing import Optional

from django.http import HttpRequest
from mohawk import Receiver


# There's likely a way better way to type this
# TODO: Figure out how to type this
class DjangoHawkRequest(HttpRequest):
    django_hawk_auth: Optional[Receiver] = None
