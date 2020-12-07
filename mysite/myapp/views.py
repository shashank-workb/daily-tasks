from django.shortcuts import render, redirect
from .models import task
from .forms import TodoForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

'''
def add(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'default name')
        pr = request.POST.get('priority', 'default priority')
        t = task(name=name, priority=pr)
        t.save()
        return redirect('/')

    return render(request, template_name='myapp/add.html')
'''
def index(request):
    task_list = task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', 'default name')
        pr = request.POST.get('priority', 'default priority')
        date = request.POST.get('date')
        t = task(name=name, priority=pr)
        t.save()
        return redirect('/')
    return render(request, template_name = 'myapp/index.html', context={'task_list':task_list})

def delete(request, task_id):
    '''
    if request.method == 'POST':
        task.objects.filter(id=task_id).delete()
        return redirect('/')
    return render(request, 'myapp/delete.html', {'task_id':task_id})
    '''
    task.objects.filter(id=task_id).delete()

    return redirect('/')

def update(request, id):
    t = task.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=t)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'myapp/edit.html',{'form':form, 'task':task})

def deleteall(request):
    task.objects.all().delete()
    return redirect('/')

### Class based Generic Views ###
class Tasklistview(ListView):
    model = task
    template_name = 'myapp/index.html'
    context_object_name = 'task_list' \

class Taskdetailview(DetailView):
    model = task
    template_name = 'myapp/detail.html'
    context_object_name = 'task'

class Taskupdateview(UpdateView):
    model = task
    template_name = 'myapp/classupdate.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk' : self.object.id})

class Taskdeleteview(DeleteView):
    model = task
    template_name = 'myapp/classdelete.html'
    success_url = reverse_lazy('cbvlist')
    #https: // stackoverflow.com / questions / 17475324 / django - deleteview - without - confirmation - template
