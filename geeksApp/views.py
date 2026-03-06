import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from geeksApp.models import GeeksModel


class GeeksList(ListView):
    model = GeeksModel
    template_name = "geeks/geeksmodel_list.html"
    context_object_name = "dataset"
    "object_list"


def geeks_view(request):

    context = {}

    context["dataset"] = GeeksModel.objects.all()
    return render(request, "list_view.html", context)


# def geeks_view(request):
#     now = datetime.datetime.now()
#     html = "Time is {}".format(now)
#     return HttpResponse(html)
#     html = "Time is {}".format(now)
#     return HttpResponse(html)
#     html = "Time is {}".format(now)
#     return HttpResponse(html)
