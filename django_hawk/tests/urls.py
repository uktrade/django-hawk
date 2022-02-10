from django.urls import path
from django_hawk.tests.views import ExampleViewSet

urlpatterns = [
    path(
        "test-view-set/",
        ExampleViewSet.as_view({"get": "list"}),
        name="test_view_set",
    ),
]
