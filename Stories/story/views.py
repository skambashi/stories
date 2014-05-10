from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from story.models import Story
from story.forms import story_form
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    # TODO: Add boostrap to landing page (need to be able to serve static media and make base html page)
    context = {}
    liked_stories = Story.objects.order_by('-likes')[:5]
    popular_stories = Story.objects.order_by('-views')[:5]
    context['liked_stories'] = liked_stories
    context['popular_stories'] = popular_stories
    return render(request, 'story/index.html', context)

def view_story(request, story_id):
    context = {}

    try:
        read = Story.objects.get(pk=story_id)
        read.views += 1
        read.save()
        context['story'] = read
    except Story.DoesNotExist:
        raise Http404

    return render(request, 'story/story.html', context)

def new_story(request):
    if request.method == 'POST':
        form = story_form(data=request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.save()
            return HttpResponseRedirect(reverse('story:view_story', args=(story.id,)))
        else:
            print form.errors
    else:
        form = story_form()

    context = {
        'form':form
    }

    return render(request, 'story/new_story.html', context)

def about(request):
    return HttpResponse("You have reached the about page. LOL there's nothing here yet, chill...")