from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Note,Etudiant,Cour

User=get_user_model()
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields={'username','first_name','last_name','email'}

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

class CourForm(forms.ModelForm):
    class Meta:
        model = Cour
        fields = '__all__'

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = '__all__'

class ModifierEtudiantForm(forms.Form):
    etudiant_form = EtudiantForm()
    cour_form = CourForm()
    note_form = NoteForm()