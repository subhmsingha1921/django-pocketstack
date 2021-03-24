from django.db import models

from answers.models import Answer
from questions.models import Question
from users.models import CustomUser

# Create your models here.
class Comment(models.Model):
    owner = models.ForeignKey(CustomUser, related_name='%(class)s_comments', on_delete=models.CASCADE)
    edited = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"Comment by {self.owner}"


class CommentOnQuestion(Comment):
    question = models.ForeignKey(Question, related_name='comments', on_delete=models.CASCADE)


class CommentOnAnswer(Comment):
    answer = models.ForeignKey(Answer, related_name='comments', on_delete=models.CASCADE)