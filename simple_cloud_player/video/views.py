from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, video_id):
    return HttpResponse("You're looking at video %s." % video_id)


def play(request, video_id):
    return HttpResponse("You're looking at play %s." % video_id)
