from django.urls import path
from app1 import views

urlpatterns=[
    path('',views.Home,name="homepage"),
    path('createauthor',views.CreateAuthor,name="author"),
    path('createbook',views.CreateBook,name="book"),
    path('delete',views.deleteView,name="delete")
]