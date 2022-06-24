from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("question", views.QuestionList.as_view(), name="questions"),
    path("question/<int:pk>", views.QuestionDetail.as_view(), name="question"),
    path("question/add", views.QuestionAdd.as_view(), name="question_add"),
    path("question/<int:question_id>/add_answer", views.AnswerAdd.as_view(), name="answer_add"),
    path("vote/<int:answer_id>", views.AddVote.as_view(), name="vote"),
]
