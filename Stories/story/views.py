from django.shortcuts import render
from django.http import HttpResponse
from story.models import Story

# Create your views here.
def index(request):
    # TODO: Add boostrap to landing page (need to be able to serve static media and make base html page)
    context = {}
    liked_stories = Story.objects.order_by('-likes')[:5]
    popular_stories = Story.objects.order_by('-views')[:5]
    context['liked_stories'] = liked_stories
    context['popular_stories'] = popular_stories
    return render(request, 'story/index.html', context)

def story(request, story_id):
    context = {}

    try:
        read = Story.objects.get(pk=story_id)
        context['story'] = read
    except Story.DoesNotExist:
        pass

    return render(request, 'story/story.html', context)