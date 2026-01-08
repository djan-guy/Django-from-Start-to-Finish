from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    path('', views.notes_list, name="list"),
    path('note-new/', views.note_new, name="note-new"),
    path('<int:pk>/delete/', views.note_delete, name='note-delete'),
    path('<slug:slug>', views.note_page, name="page"),
]