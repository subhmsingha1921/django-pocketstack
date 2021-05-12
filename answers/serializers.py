from rest_framework import serializers

from .models import Answer


class AnswerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = (
            # 'question',
            'body',
        )


class AnswerDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    edit_url = serializers.HyperlinkedIdentityField(
        view_name='answer_edit'
    )
    owner_url = serializers.HyperlinkedRelatedField(
        read_only=True,
        source='owner',
        view_name='user_detail'
    )
    user_upvoted = serializers.SerializerMethodField()
    user_downvoted = serializers.SerializerMethodField()
    upvote_url = serializers.HyperlinkedIdentityField(
        view_name = 'answer_upvote'
    )
    downvote_url = serializers.HyperlinkedIdentityField(
        view_name = 'answer_downvote'
    )
    is_accepted = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = (
            'id',
            'score',
            'is_accepted',
            'body',
            'creation_date',
            'last_edit_date',
            'owner',
            'owner_url',
            'user_upvoted',
            'user_downvoted',
            'upvote_url',
            'downvote_url',
            'edit_url',
        )

    def get_user_upvoted(self, obj):
        return obj.users_upvote.filter(id=self.context['request'].user.id).exists()

    def get_user_downvoted(self, obj):
        return obj.users_downvote.filter(id=self.context['request'].user.id).exists()

    def get_is_accepted(self, obj):
        return obj.question.accepted_answer_id == obj.id


class AnswerEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = (
            'body',
        )


class AnswerPostSerializer(serializers.ModelSerializer):
    score = serializers.ReadOnlyField(source='question.score')
    title = serializers.ReadOnlyField(source='question.title')
    question_url = serializers.HyperlinkedRelatedField(
        read_only=True,
        source='question',
        view_name='question_detail'
    )

    class Meta:
        model = Answer
        fields = (
            'score',
            'title',
            'question_url',
        )


class AnswerUpvoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = (
            'users_upvote',
        )


class AnswerDownvoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = (
            'users_downvote',
        )