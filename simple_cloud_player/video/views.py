from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Video


def index(request):
    latest_video_list = Video.objects.order_by('-create_date')[:5]
    context = {'latest_video_list': latest_video_list,}
    return render(request, 'video/index.html', context)


def detail(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return render(request, 'video/detail.html', {'video': video})


def play(request, video_id):
    return HttpResponse("You're looking at play %s." % video_id)
