from django.urls import path

from answers.views import AnswerCreateView

from .views import (
    QuestionListView, 
    QuestionDetailView, 
    QuestionCreateView,
    QuestionEditView,
    QuestionUpvoteView,
    QuestionDownvoteView,
    QuestionAnswerAcceptView
)


urlpatterns = [
    path('create/', QuestionCreateView.as_view(), name='question_create'),
    path('', QuestionListView.as_view(), name='question_list'),
    path('<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    path('<int:pk>/edit/', QuestionEditView.as_view(), name='question_edit'),
    path('<int:pk>/upvote/', QuestionUpvoteView.as_view(), name='question_upvote'),
    path('<int:pk>/downvote/', QuestionDownvoteView.as_view(), name='question_downvote'),
    path('<int:pk>/answer/accept/', QuestionAnswerAcceptView.as_view(), name='question_answer_accept'),
    path('<int:pk>/answer/create/', AnswerCreateView.as_view(), name='question_answer_create'),
]