from django import forms


class Song(forms.Form):
    file = forms.FileField()  # for creating file input
