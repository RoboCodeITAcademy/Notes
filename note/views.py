from django.shortcuts import render, redirect
from .models import Notes
from django.views.generic.edit import UpdateView
# Create your views here.

from .forms import AddNotesForm, UpdateNotesForm

def notes(request):
	if request.method == 'POST':
	
		form = AddNotesForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		
		form = AddNotesForm()
	notes = Notes.objects.all()
	context = {
		'notes':notes,
		'add_form':form,
	
	}
	return render(request, 'notes.html', context)

def deleteNote(request, note_id):
	note = Notes.objects.get(id=note_id)
	note.delete()
	return redirect('note:notes')


class UpdateNoteView(UpdateView):
	model = Notes 
	fields = ['title','body','color']
	success_url = '/'
