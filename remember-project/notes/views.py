from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from django.contrib.auth.decorators import login_required
from .forms import NoteForm

@login_required(login_url="/users/login/")
def notes_list(request):
    notes = Note.objects.filter(user=request.user).order_by('-date')
    return render(request, 'notes/notes_list.html', {'notes': notes})

@login_required(login_url="/users/login/")
def note_page(request, slug):
    note = get_object_or_404(Note, slug=slug, user=request.user)
    return render(request, 'notes/note_page.html', {'note': note})

@login_required(login_url="/users/login/")
def note_new(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect("notes:list")
    else:
        form = NoteForm()
    return render(request, 'notes/note_new.html', {'form': form})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == "POST":
        note.delete()
        return redirect('notes:list')
    return redirect('notes:list')
