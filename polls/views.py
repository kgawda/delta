import logging

from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, reverse, render
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.views import View
from django.core.mail import send_mail
from django.utils.translation import gettext as _
from django.utils.translation import pgettext, ngettext

from .models import Question, Answer, Vote

logger = logging.getLogger(__name__)


class HomeView(TemplateView):
    template_name = "polls/home.html"


class QuestionList(ListView):
    model = Question


class QuestionDetail(DetailView):
    model = Question


class QuestionAdd(CreateView):
    model = Question
    fields = ['text']


class AnswerAdd(CreateView):
    model = Answer
    fields = ['text']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = get_object_or_404(Question, id=self.kwargs["question_id"])
        return context

    def form_valid(self, form):
        question = get_object_or_404(Question, id=self.kwargs["question_id"])
        form.instance.question = question
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('question', args=(self.kwargs["question_id"],))


class AnswerAddFullForm(CreateView):
    model = Answer
    fields = ['text', 'question']

    def get_success_url(self):
        return reverse('question', args=(self.object.question.id,))


class AddVote(View):
    def post(self, request, answer_id):
        logger.info("Rozpoczęto dodawanie głosu user=%s __name__=%s", request.user, __name__)
        user = request.user
        answer = get_object_or_404(Answer, id=answer_id)
        vote = Vote(user=user, answer=answer)
        vote.save()
        send_mail(
            _("You have just voted"),
            _("You have just voted for %s") % answer,
            None,  # from_email: If None, Django will use the value of the DEFAULT_FROM_EMAIL setting.
            [user.email],
            fail_silently=True,
        )
        return redirect("question", answer.question.id)

        # Odpalanie testowego serwera SMTP drukującego na konsoli:
        # pip install aiosmtpd
        # python -m aiosmtpd -n -l localhost:25


class TranslateExample(View):
    def get(self, request):
        text = ""
        text += pgettext('money', 'Save') + "\n"
        text += pgettext('write to disk', 'Save') + "\n"
        text += ngettext("\nWe have one Poll:\n", "\nWe have %(polls_count)s Polls:\n", 0) % {'polls_count': 0}
        text += ngettext("\nWe have one Poll:\n", "\nWe have %(polls_count)s Polls:\n", 1) % {'polls_count': 1}
        text += ngettext("\nWe have one Poll:\n", "\nWe have %(polls_count)s Polls:\n", 2) % {'polls_count': 2}
        text += ngettext("\nWe have one Poll:\n", "\nWe have %(polls_count)s Polls:\n", 5) % {'polls_count': 5}
        return HttpResponse(text)

class LocalizeExample(View):
    def get(self, request):
        import datetime
        from django.utils import timezone
        context = {
            'number': 10000000.5,
            'date': datetime.datetime.now(),  # nie używać kiedy USE_TZ = True
            'date_tz': timezone.now()
        }
        return render(request, 'polls/localization_example.html', context)