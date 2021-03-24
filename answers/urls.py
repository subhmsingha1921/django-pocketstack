from django.urls import path

from .views import (
    AnswerCreateView, 
    AnswerEditView,
    AnswerDownvoteView,
    AnswerUpvoteView
)


urlpatterns = [
    path('create/', AnswerCreateView.as_view(), name='answer_create'),
    path('<int:pk>/edit/', AnswerEditView.as_view(), name='answer_edit'),
    path('<int:pk>/upvote/', AnswerUpvoteView.as_view(), name='answer_upvote'),
    path('<int:pk>/downvote/', AnswerDownvoteView.as_view(), name='answer_downvote'),
]