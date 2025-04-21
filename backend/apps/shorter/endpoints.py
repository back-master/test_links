from django.urls import path

from apps.shorter.views import LinkRetrieveAPIView, LinkCreateView, LinkListView


urlpatterns = [
    path("link/<str:token>/", LinkRetrieveAPIView.as_view(), name="link-retrieve"),
    path("create_link/", LinkCreateView.as_view(), name="create_link"),
    path("list_link/", LinkListView.as_view(), name="list_link"),
]
