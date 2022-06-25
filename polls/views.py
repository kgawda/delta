from django.shortcuts import redirect, get_object_or_404, reverse
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.views import View


from .models import Question, Answer, Vote

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
        user = request.user
        answer = get_object_or_404(Answer, id=answer_id)
        vote = Vote(user=user, answer=answer)
        vote.save()
        return redirect("question", answer.question.id)
