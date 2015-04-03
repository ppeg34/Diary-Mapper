from django.conf.urls import patterns, url

from pointDiary import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^addPost/', views.addPost, name='addPost'),
    url(r'^post/', views.post, name='post'),
    url(r'^deletePost/', views.deletePost, name='deletePost'),
)
