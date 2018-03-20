from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
	todo_list = Todo.objects.all().order_by("id")
	form = TodoForm()
	context = {'todo_list': todo_list, 'form': form,}
	return render(request, "todo/index.html", context)

@require_POST
def add_todo(request):
	form = TodoForm(request.POST)
	if form.is_valid():
		new_todo = Todo(text=request.POST['text'])
		new_todo.save()

	#print(request.POST['text'])  Value of the form input
	return redirect('index')

def complete_todo(request, todo_id):
	todo = Todo.objects.get(pk=todo_id)
	todo.complete = True
	todo.save()

	return redirect('index')

def delete_completed(request):
	Todo.objects.filter(complete__exact=True).delete()

	return redirect('index')

def deleteAll(request):
	Todo.objects.all().delete()

	return redirect('index')