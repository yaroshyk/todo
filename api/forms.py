import datetime

from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
    user_id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    title = forms.CharField()
    details = forms.CharField(widget=forms.Textarea)
    date = forms.DateTimeField(initial=datetime.datetime.now())
    group = forms.ChoiceField(choices=(
        ('', 'Choose...'),
        ('0', 'Home'),
        ('1', 'Work')
    ))

