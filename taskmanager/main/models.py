from django import forms


class Song(forms.Form):
    lang = forms.ChoiceField(choices=(("en", "en"),))
    model = forms.ChoiceField(choices=(("speecht5", "speecht5"), 
                                       ("silero", "silero"),))
    version = forms.ChoiceField(choices=((1, "1"),))
    sample_rate = forms.ChoiceField(choices=((16000, "16000"),))
    file = forms.FileField()  # for creating file input


class ConfigTTS(forms.Form):
    lang = forms.ChoiceField(choices=(("en", "en"),))
    model = forms.ChoiceField(choices=(("speecht5", "speecht5"), 
                                       ("silero", "silero"),))
    version = forms.ChoiceField(choices=((1, "1"),))
    text = forms.CharField() 
