from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from rest_framework.generics import RetrieveAPIView

from apps.shorter.forms import LinkForm
from apps.shorter.models import Link
from apps.shorter.serializers import LinkSerializer


class LinkRetrieveAPIView(RetrieveAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    lookup_field = "token"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.link_count += 1
        instance.save(update_fields=["link_count"])

        return redirect(instance.url)


class LinkCreateView(CreateView):
    form_class = LinkForm
    success_url = reverse_lazy("create_link")
    template_name = "link_create.html"


class LinkListView(ListView):
    paginate_by = 10
    queryset = Link.objects.all().order_by("-link_count")
    template_name = "link_list.html"
