from django.db import models

# Create your models here.
class Story(models.Model):

    id = models.AutoField(primary_key=True, verbose_name="Story ID")

    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)

    title = models.CharField(max_length=63)

    story = models.TextField()

    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name = "story"
        verbose_name_plural = "stories"
        ordering = ("-id", "likes", "views", "created_on", "title", "last_name", "first_name")

    def __unicode__(self):
        return self.title