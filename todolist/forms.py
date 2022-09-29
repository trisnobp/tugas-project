from django import forms
from todolist.models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(label='Judul Task', max_length=100)
    description = forms.CharField(label='Deskripsi Task')

    class Meta:
        model = Task
        fields = ['title','description']