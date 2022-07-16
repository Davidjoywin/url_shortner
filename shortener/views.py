from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, reverse
from .models import Dispatcher
from .helper import url_uid
import json

def index(request):
    return render(request, "index.html") 

def create_url(request):
    if request.method == "POST":
        url = request.POST.get("url")
        if url:
            uuid = url_uid()
            dispatch = Dispatcher.objects.create(uuid=uuid, url=url)
            dispatch.save()
            referer = request.META["HTTP_REFERER"]
            get_uuid = f"{referer}{dispatch.uuid}"
            return JsonResponse({"uuid": get_uuid})
        else:
            return redirect("home")


def get_real_url(request, uuid):
    get_url = Dispatcher.objects.get(uuid=uuid)

    return redirect(get_url.url)