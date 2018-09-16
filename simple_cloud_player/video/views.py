from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Video


class IndexView(generic.ListView):
    template_name = 'video/index.html'
    context_object_name = 'latest_video_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Video.objects.order_by('-create_date')[:5]


class DetailView(generic.DetailView):
    model = Video
    template_name = 'video/detail.html'


class PlayView(generic.DetailView):
    model = Video
    template_name = 'video/play.html'
