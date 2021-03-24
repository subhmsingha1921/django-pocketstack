from django.db import models
from django.contrib.auth.models import AbstractUser


# GENDER_SELECTION = [
#     ('M', 'Male'),
#     ('F', 'Female'),
#     ('NS', 'Not Specified'),
# ]


class CustomUser(AbstractUser):
    view_count = models.IntegerField(default=0, null=True, blank=True)
    down_vote_count = models.IntegerField(default=0, null=True, blank=True)
    up_vote_count = models.IntegerField(default=0, null=True, blank=True)
    # answer_count = models.IntegerField(default=0, null=True, blank=True)
    # question_count = models.IntegerField(default=0, null=True, blank=True)
    timed_penalty_date = models.DateTimeField(null=True, blank=True)
    reputation = models.IntegerField(default=0, null=True, blank=True)
    about_me = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    website_url = models.URLField(max_length=255, null=True, blank=True)
    link = models.URLField(max_length=255, null=True, blank=True)
    # profile_image = models.FileField(upload_to=None, max_length=100)

    class Meta(object):
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_user')
        ]
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @property
    def answer_count(self):
        return self.answers.count()

    @property
    def question_count(self):
        return self.questions.count()

    @property
    def get_up_vote_count(self):
        user_question_up_vote_count = sum(question.up_vote_count for question in self.questions.all())
        user_answer_up_vote_count = sum(answer.up_vote_count for answer in self.answers.all())
        return user_question_up_vote_count + user_answer_up_vote_count

    @property
    def get_down_vote_count(self):
        user_question_down_vote_count = sum(question.down_vote_count for question in self.questions.all())
        user_answer_down_vote_count = sum(answer.down_vote_count for answer in self.answers.all())
        return user_question_down_vote_count + user_answer_down_vote_count

    @property
    def get_reputation_score(self):
        total_up_vote_score = self.get_up_vote_count * 10
        total_down_vote_score = self.get_down_vote_count * (-2)
        return total_up_vote_score + total_down_vote_score

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        self.up_vote_count = self.get_up_vote_count
        self.down_vote_count = self.get_down_vote_count
        self.reputation = self.get_reputation_score
        super().save(*args, **kwargs)