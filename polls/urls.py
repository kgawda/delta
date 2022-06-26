from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("questions", views.QuestionViewset)
router.register("answers", views.AnswerViewset)
router.register("votes", views.VoteViewset)
router.register("users", views.UserViewset)

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("question", views.QuestionList.as_view(), name="questions"),
    path("question/<int:pk>", views.QuestionDetail.as_view(), name="question"),
    path("question/add", views.QuestionAdd.as_view(), name="question_add"),
    path("question/<int:question_id>/add_answer", views.AnswerAdd.as_view(), name="answer_add"),
    path("vote/<int:answer_id>", views.AddVote.as_view(), name="vote"),
    path("answer_add", views.AnswerAddFullForm.as_view()),
    path("translate_examples", views.TranslateExample.as_view()),
    path("localize_examples", views.LocalizeExample.as_view()),
    path("api/", include(router.urls)),
    path("api-auth/", include('rest_framework.urls'))
]
