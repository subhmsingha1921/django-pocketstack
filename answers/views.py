from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from questions.permissions import IsOwnerOrReadOnly

from .models import Answer
from .serializers import (
    AnswerCreateSerializer, 
    AnswerEditSerializer,
    AnswerDownvoteSerializer,
    AnswerUpvoteSerializer
)

# Create your views here.
class AnswerCreateView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = AnswerCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AnswerEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = AnswerEditSerializer


class AnswerUpvoteView(APIView):
    permission_classes = [IsAuthenticated,]

    def get_object(self, pk):
        try:
            return Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        answer = self.get_object(pk)
        serializer = AnswerUpvoteSerializer(answer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        answer = self.get_object(pk)
        if answer.users_upvote.filter(id=request.user.id).exists():
            # return Response({"message": "User already upvoted this answer"})
            answer.users_upvote.remove(request.user)
        else:
            if answer.users_downvote.filter(id=request.user.id).exists():
                answer.users_downvote.remove(request.user)
            answer.users_upvote.add(request.user)
        serializer = AnswerUpvoteSerializer(answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerDownvoteView(APIView):
    permission_classes = [IsAuthenticated,]

    def get_object(self, pk):
        try:
            return Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        answer = self.get_object(pk)
        serializer = AnswerDownvoteSerializer(answer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        answer = self.get_object(pk)
        if answer.users_downvote.filter(id=request.user.id).exists():
            # return Response({"message": "User already upvoted this answer"})
            answer.users_downvote.remove(request.user)
        else:
            if answer.users_upvote.filter(id=request.user.id).exists():
                answer.users_upvote.remove(request.user)
            answer.users_downvote.add(request.user)
        serializer = AnswerDownvoteSerializer(answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)