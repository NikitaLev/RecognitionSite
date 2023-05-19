from django.shortcuts import get_object_or_404, render
import requests
from .models import Song
from .functions.functions import handle_uploaded_file
from django.http import HttpResponse
import json

def index(request):
    jsonC = {
        "model": "speecht5",
        "version": 1,
        "lang": "en",
        "sample_rate": 16000
    }
    #print('!!!!!!!!!', response.text)
    if request.method == 'POST':
        print(request)
        audio = Song(request.POST, request.FILES)
        if audio.is_valid():
            file = request.FILES['file'].read()
            data = {
                'json_param':jsonC,
                'file': file
            }
            response = requests.post('http://web_api-flask-1:5000/stt', files={'file': file}, data=jsonC)
            data = {'src': file,
                    'text': response.text}
            return render(request, "out_audio.html", data)
        """file = Song(request.POST, request.FILES)
        
        if file.is_valid():
            print(str(request.FILES['file']).endswith('.wav'))
            src = handle_uploaded_file(request.FILES['file'])
            data = {
                'json_param':config,
                'file': src
            }
            response = requests.get('http://web_api-flask-1:5000/stt', data=data)
            data = {'src': src,
                    'text': response.text}
            print(src)
            return render(request, "out_audio.html", data)
            #return HttpResponse("File uploaded successfuly")"""
    else:
        student = Song()
        return render(request, "index.html", {'form': student})


def upload_audio(request):
    return render(request, 'upload_audio.html')

def test(request):
    data = {
        'text':'Test text',
    }
    return render(request, "out_audio.html", data)

def test2(request):
    response = requests.get('http://web_api-flask-1:5000/test')
    data = {
        'text':response.text,
    }
    return render(request, "out_audio.html", data)


def out_audio(request):
    return render(request, 'out_audio.html')
