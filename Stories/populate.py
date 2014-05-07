import os

def populate():
    add_story(first_name="Taikun", last_name="Kambashi", title="Taikun's Story!", story="This is TK's story.", views=16, likes=1)
    add_story(first_name="Chion", last_name="Kambashi", title="Chion's Story!", story="This is CK's story.", views=8, likes=2)
    add_story(first_name="Seikun", last_name="Kambashi", title="Seikun's Story!", story="This is SK's story.", views=4, likes=3)
    add_story(first_name="Myunghun", last_name="Kambashi", title="Myunghun's Story!", story="This is MK's story.", views=2, likes=4)
    add_story(first_name="Changhun", last_name="Kambashi", title="Changhun's Story!", story="This is CHK's story.", views=1, likes=5)

    # Print out what we have added to the user.
    for s in Story.objects.all():
        print "- {0}".format(str(s))

def add_story(first_name, last_name, title, story, views, likes):
    story = Story.objects.get_or_create(first_name=first_name, last_name=last_name, title=title, story=story, views=views, likes=likes)
    return story

# Start execution here!
if __name__ == '__main__':
    print "Starting Stories population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Stories.settings')
    from story.models import Story
    populate()