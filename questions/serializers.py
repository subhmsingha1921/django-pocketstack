from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer

from answers.serializers import AnswerDetailSerializer

from .models import Question


class StringListField(serializers.ListField):
    child = serializers.CharField()
    
    def to_representation(self, data):
        return ' '.join(data.values_list('name', flat=True))


class QuestionCreateSerializer(serializers.ModelSerializer):
    tags = StringListField()

    class Meta:
        model = Question
        fields = (
            'title',
            'body',
            'tags',
        )

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        instance = super(QuestionCreateSerializer, self).create(validated_data)
        instance.tags.set(*tags)
        return instance

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags')
        instance = super(QuestionCreateSerializer, self).create(validated_data)
        instance.tags.set(*tags)
        return instance


class QuestionEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = (
            'title',
            'body',
        )


class QuestionDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    owner = serializers.ReadOnlyField(source='owner.username')
    answers = AnswerDetailSerializer(many=True, read_only=True)
    user_upvoted = serializers.SerializerMethodField()
    user_downvoted = serializers.SerializerMethodField()
    upvote_url = serializers.HyperlinkedIdentityField(
        view_name = 'question_upvote'
    )
    downvote_url = serializers.HyperlinkedIdentityField(
        view_name = 'question_downvote'
    )
    edit_url = serializers.HyperlinkedIdentityField(
        view_name = 'question_edit'
    )
    owner_url = serializers.HyperlinkedRelatedField(
        read_only=True,
        source='owner',
        view_name='user_detail'
    )
    accept_url = serializers.HyperlinkedIdentityField(
        view_name='question_answer_accept'
    )

    class Meta:
        model = Question
        fields = (
            'id',
            'score',
            'is_answered',
            'answer_count',
            'accepted_answer_id',
            'title',
            'tags',
            'body',
            'creation_date',
            'owner',
            'owner_url',
            'user_upvoted',
            'user_downvoted',
            'upvote_url',
            'downvote_url',
            'edit_url',
            'accept_url',
            'answers',
        )

    def get_user_upvoted(self, obj):
        return obj.users_upvote.filter(id=self.context['request'].user.id).exists()

    def get_user_downvoted(self, obj):
        return obj.users_downvote.filter(id=self.context['request'].user.id).exists()


class QuestionListSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    owner = serializers.ReadOnlyField(source='owner.username')
    detail_url = serializers.HyperlinkedIdentityField(
        view_name = 'question_detail'
    )
    owner_url = serializers.HyperlinkedRelatedField(
        read_only=True,
        source='owner',
        view_name='user_detail'
    )

    class Meta:
        model = Question
        fields = (
            'id',
            'score',
            'is_answered',
            'answer_count',
            'title',
            'tags',
            'creation_date',
            'owner',
            'owner_url',
            'detail_url',
        )


class QuestionPostSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name = 'question_detail'
    )

    class Meta:
        model = Question
        fields = (
            'score',
            'title',
            'creation_date',
            'detail_url',
        )


class QuestionUpvoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = (
            'users_upvote',
        )


class QuestionDownvoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = (
            'users_downvote',
        )


class QuestionAnswerAcceptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = (
            'accepted_answer_id',
        )