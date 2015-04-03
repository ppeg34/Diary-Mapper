from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from pointDiary.models import Diary
from django.core.urlresolvers import reverse
from pointDiary.forms import PointForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    diaryList = list(Diary.objects.filter(user='phil'))
    return render(request, 'pointDiary/index.html', {'diaryList': diaryList})


@login_required(redirect_field_name='accounts/login')
def addPost(request):
    diaryList = list(Diary.objects.filter(user=request.user))
    return render(request, 'pointDiary/addPost.html', {'diaryList': diaryList})

@login_required(redirect_field_name='accounts/login')
def post(request):
    d = Diary(title=request.POST['title'], text=request.POST['content'], loc="POINT(" + request.POST['lng'] + " " + request.POST['lat'] + ")", user=request.user)
    d.save()
    diaryList = list(Diary.objects.all())
    return HttpResponseRedirect(reverse('pointDiary:addPost'))

@login_required(redirect_field_name='accounts/login')
def deletePost(request):
    d = Diary.objects.get(id=request.POST['id'])
    d.delete()
    return HttpResponseRedirect(reverse('pointDiary:addPost'))
