from django.urls import path
from notes import views
urlpatterns=[path("",views.index,name="index"),path("add/",views.add_note,name="add"),path("delete/<int:pk>/",views.delete_note,name="delete")]
