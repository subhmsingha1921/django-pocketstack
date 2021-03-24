from django.db import models

from questions.models import Question
from users.models import CustomUser

# Create your models here.
class Answer(models.Model):
    owner = models.ForeignKey(CustomUser, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    users_upvote = models.ManyToManyField(CustomUser, related_name='answer_upvotes', blank=True)
    users_downvote = models.ManyToManyField(CustomUser, related_name='answer_downvotes', blank=True)
    down_vote_count = models.IntegerField(default=0, null=True, blank=True)
    up_vote_count = models.IntegerField(default=0, null=True, blank=True)
    # is_accepted = models.BooleanField(default=False)
    score = models.IntegerField(default=0, null=True, blank=True)
    locked_date = models.DateTimeField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_edit_date = models.DateTimeField(auto_now=True)
    body = models.TextField()

    def __str__(self):
        return f"{self.owner.username}'s answer on question id {self.question.id}"
    
    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)
        else:
            self.down_vote_count = self.users_downvote.count()
            self.up_vote_count = self.users_upvote.count()
            self.score = self.up_vote_count - self.down_vote_count
            super().save(*args, **kwargs)