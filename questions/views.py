from rest_framework import generics, status
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .models import Question
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    QuestionListSerializer, 
    QuestionDetailSerializer, 
    QuestionCreateSerializer,
    QuestionEditSerializer,
    QuestionUpvoteSerializer,
    QuestionDownvoteSerializer,
    QuestionAnswerAcceptSerializer
)

# Create your views here.
class QuestionAnswerAcceptView(generics.RetrieveUpdateAPIView):
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = QuestionAnswerAcceptSerializer


class QuestionCreateView(generics.CreateAPIView):
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = QuestionCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class QuestionEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = QuestionEditSerializer


class QuestionDetailView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = QuestionDetailSerializer


class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = QuestionListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'body']


# @api_view(['GET', 'PUT'])
# def question_upvote_view(request, pk):
#     pass


class QuestionUpvoteView(APIView):
    permission_classes = [IsAuthenticated,]

    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionUpvoteSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        if question.users_upvote.filter(id=request.user.id).exists():
            # return Response({"message": "User already upvoted this question"})
            question.users_upvote.remove(request.user)
        else:
            if question.users_downvote.filter(id=request.user.id).exists():
                question.users_downvote.remove(request.user)
            question.users_upvote.add(request.user)
        serializer = QuestionUpvoteSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDownvoteView(APIView):
    permission_classes = [IsAuthenticated,]

    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionDownvoteSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        if question.users_downvote.filter(id=request.user.id).exists():
            # return Response({"message": "User already upvoted this question"})
            question.users_downvote.remove(request.user)
        else:
            if question.users_upvote.filter(id=request.user.id).exists():
                question.users_upvote.remove(request.user)
            question.users_downvote.add(request.user)
        serializer = QuestionDownvoteSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)