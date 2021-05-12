from dj_rest_auth.serializers import PasswordResetSerializer
from rest_framework import serializers

from questions.serializers import QuestionPostSerializer
from answers.serializers import AnswerPostSerializer

from .models import CustomUser


class CustomPasswordResetSerializer(PasswordResetSerializer):

    def get_email_options(self):
        return {
            'html_email_template_name': 'custom_password_reset_email.html',
        }


class CustomUserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'id', 
            'email', 
            'username', 
            'first_name', 
            'last_name', 
            'about_me',
            'location',
            'website_url',
        )


class CustomUserListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'user_detail'
    )

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'location',
            'reputation',
            'date_joined',
            'url',
        )


class CustomUserDetailSerializer(serializers.ModelSerializer):
    questions = QuestionPostSerializer(many=True, read_only=True)
    answers = AnswerPostSerializer(many=True, read_only=True)
    up_vote_count = serializers.ReadOnlyField(source='get_up_vote_count')
    down_vote_count = serializers.ReadOnlyField(source='get_down_vote_count')
    reputation_score = serializers.ReadOnlyField(source='get_reputation_score')

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'location',
            'reputation_score',
            'about_me',
            'website_url',
            'answer_count',
            'question_count',
            'up_vote_count',
            'down_vote_count',
            'questions',
            'answers',
        )