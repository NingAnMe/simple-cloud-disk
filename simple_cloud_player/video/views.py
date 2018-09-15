from django.http import HttpResponse
from django.shortcuts import render

from .models import Video


def index(request):
    latest_video_list = Video.objects.order_by('-create_date')[:5]
    context = {'latest_video_list': latest_video_list,}
    return render(request, 'video/index.html', context)


def detail(request, video_id):
    return HttpResponse("You're looking at video %s." % video_id)


def play(request, video_id):
    return HttpResponse("You're looking at play %s." % video_id)
