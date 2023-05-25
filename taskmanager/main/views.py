from django.shortcuts import get_object_or_404, render
import requests
from .models import Song
from .functions.functions import handle_uploaded_file
from django.http import HttpResponse
import json
import logging
import tempfile
import uuid
import os
  
logger = logging.getLogger(__name__)


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


def tts(request):
    url = "http://web_api-flask-1:5000/tts"

    logger.critical('nor this')
    logger.critical('nor this')

    payload={'json_param': '{"model": "speecht5", "version": 1, "lang": "en" }',
    'text': 'The birch canoe slid on the smooth planks. Glue the sheet to the dark blue background. It\'s easy to tell the depth of a well. Four hours of steady work faced us.'}

    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    filename = ''

    src = 'taskmanager/main/static/upload/tmp/'
    if not os.path.exists(src):
        os.makedirs(src)
    filename = handle_uploaded_file(response.content)
    #with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as f:
        #f.write(response.content)
        #filename = f.name
    """src = 'data/wav/'
    if not os.path.exists(src):
        os.makedirs(src)
    name = uuid.uuid4().__str__()
    temp = tempfile.TemporaryFile(suffix='.wav')
    temp.write(response.content.decode())
    file = temp.read()
    temp.close()
    logger.critical("file")
    logger.critical(file)
    data = {
        'url' : file,
        'text': payload['text'],
    }
    logger.critical("data")
    logger.critical(data)"""
    
    data = {
        'src' : filename,
        'text': payload['text'],
    }
    logger.critical("data")
    logger.critical(data)
    return render(request, "out_audio.html", data)

    """jsonC = {
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
            response = requests.post('http://web_api-flask-1:5000/tts', files={'file': file}, data=jsonC)
            data = {'src': file,
                    'text': response.text}
            return render(request, "out_audio.html", data)
    else:
        student = Song()
        return render(request, "index.html", {'form': student})"""
