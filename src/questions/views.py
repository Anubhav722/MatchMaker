from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import Http404
from .forms import UserResponseForm

# Create your views here.
def single(request, id):
	if request.user.is_authenticated():
		form = UserResponseForm(request.POST or None)
		if form.is_valid():
			print(request.POST)
			print (form.cleaned_data)
			question_id = form.cleaned_data.get('question_id')
			answer_id = form.cleaned_data.get('answer_id')
			question_instance = Question.objects.get(id=id)
			answer_instance = Question.objects.get(id=id)
			print (question_instance.text, answer_instance.text)
			next_q = Question.objects.all().order_by('?').first()
			return redirect("question_single", id=next_q.id)

		queryset = Question.objects.all().order_by('-timestamp')
		# instance = queryset[0]
		instance = get_object_or_404(Question, id=id)	
		context = {
			"form": form,
			"instance": instance,
			# "queryset": queryset
		}
		return render(request, "questions/single.html", context)
	else:
		raise Http404

def home(request):

	if request.user.is_authenticated():
		form = UserResponseForm(request.POST or None)
		if form.is_valid():
			print (form.cleaned_data)
			question_id = form.cleaned_data.get('question_id')
			answer_id = form.cleaned_data.get('answer_id')

		queryset = Question.objects.all().order_by('-timestamp')
		instance = queryset[0]
		context = {
			"form": form,
			"instance": instance,
			# "queryset": queryset
		}
		return render(request, "questions/home.html", context)
	else:
		raise Http404