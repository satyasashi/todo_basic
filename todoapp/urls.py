from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add-todo/$', views.add_todo, name="add_todo"),
    url(r'^complete-todo/(?P<todo_id>\d+)/$', views.complete_todo, name="complete_todo"),
    url(r'^delete-completed/$', views.delete_completed, name="delete_completed"),
    url(r'^delete-all/$', views.deleteAll, name="deleteAll"),
]
