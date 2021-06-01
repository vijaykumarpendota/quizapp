from django.http import HttpResponseRedirect

from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import SignUpForm
from django.core. paginator import PageNotAnInteger, Page, Paginator, EmptyPage
from django.contrib.auth.decorators import login_required
import datetime
import time


from django.http import JsonResponse


# Create your views here.

def index(request): # Index page
    results=Course.objects.all() # will get list of available quizs  
    return render(request, 'testapp/index.html',{'results':results})
@login_required
def quiz_detail(request,id): # will get the specified quiz details page
    quiz_detail.start_time = datetime.datetime.now()#.strftime('%H:%M:%S') # Starting time of Quiz
    details=Question.objects.filter(course=id)
    l=len(details)

    print(l)

    paginator=Paginator(details,1)#its is the paginator object. and for a page will display 1 posts from post_list.
    page_num=request.GET.get('page')
    try:
        details=paginator.page(page_num)
    except PageNotAnInteger:
        details=paginator.page(1)# for displaying 1st page details
    except EmptyPage:
        details=paginator.page(paginator.num_pages)

    context={'details':details,'l':l}
    
    return render(request, 'testapp/quiz_detail.html', context)
    #op=request.GET['ans']#reading data from detail.html
def results_view(request):

    ending_time = datetime.datetime.now()#.strftime#('%H:%M:%S')
    diff= (ending_time - quiz_detail.start_time)# will get total time taken by the user
    #diff=int(ending_time-start_time)
    context={'time':diff}

        
    return render(request, 'testapp/results.html',context)
def signup_view(request):
    #from testapp.forms import SignUpForm
    form=SignUpForm()
    if request.method =='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
        #return render(request, 'testapp/index.html')
            return HttpResponseRedirect('/accounts/login')
    return render(request, 'testapp/signup.html',{'form':form})  

def logout_view(request):
    return render(request,'testapp/logout.html')  


