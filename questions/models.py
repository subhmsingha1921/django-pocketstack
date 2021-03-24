from django.db import models

from taggit.managers import TaggableManager

from users.models import CustomUser

# Create your models here.
class Question(models.Model):
    tags = TaggableManager()
    owner = models.ForeignKey(CustomUser, related_name='questions', on_delete=models.CASCADE)
    is_answered = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0, null=True, blank=True)
    users_upvote = models.ManyToManyField(CustomUser, related_name='question_upvotes', blank=True)
    users_downvote = models.ManyToManyField(CustomUser, related_name='question_downvotes', blank=True)
    down_vote_count = models.IntegerField(default=0, null=True, blank=True)
    up_vote_count = models.IntegerField(default=0, null=True, blank=True)
    score = models.IntegerField(default=0, null=True, blank=True)
    closed_date = models.DateTimeField(null=True, blank=True)
    accepted_answer_id = models.IntegerField(null=True, blank=True)
    # answer_count = models.IntegerField(default=0, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_edit_date = models.DateTimeField(auto_now=True)
    closed_reason = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    body = models.TextField()

    @property
    def answer_count(self):
        return self.answers.count()

    @property
    def get_is_answered(self):
        return self.answer_count > 0

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)
        else:
            # self.answer_count = self.answers.count()
            self.is_answered = self.get_is_answered
            self.down_vote_count = self.users_downvote.count()
            self.up_vote_count = self.users_upvote.count()
            self.score = self.up_vote_count - self.down_vote_count
            super().save(*args, **kwargs)