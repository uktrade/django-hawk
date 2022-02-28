from django.urls import path
from django_hawk.tests.views import ExampleViewSet, simple_view

urlpatterns = [
    path(
        "test-view-set/",
        ExampleViewSet.as_view({"get": "list"}),
        name="test_view_set",
    ),
    path(
        "test-simple-view/",
        simple_view,
        name="test_simple_view",
    ),
]
