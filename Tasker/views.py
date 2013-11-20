from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from Tasker.models import Task



# Create your views here.
def index(request):
    current_tasks = Task.objects.order_by('duedate').exclude(complete=True)
    template = loader.get_template('Tasker/index.html')
    context = {'current_tasks': current_tasks}
    
    return render(request, 'Tasker/index.html', context)

def add(request):
    t = Task(title=request.POST.get('form_title'), body=request.POST.get('form_body'), duedate=request.POST.get('form_duedate'))
    t.save()
    
    return HttpResponseRedirect(reverse('index'))

def complete(request, id):
    t = Task.objects.get(pk=id)
    t.complete = True
    t.save()
    return HttpResponseRedirect(reverse('index'))

def edit(request, id):
    t = Task.objects.get(pk=id)
    if request.POST.get('form_title') != '':
        t.title = request.POST.get('form_title')
    if request.POST.get('form_body') != '':
        t.body = request.POST.get('form_body')
    if request.POST.get('form_duedate') != '':
        t.duedate = request.POST.get('form_duedate')
    t.save()
    return HttpResponseRedirect(reverse('index'))