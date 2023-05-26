from django.shortcuts import get_object_or_404, render
import requests
from .models import Song, ConfigTTS
from .functions.functions import handle_uploaded_file
from django.http import HttpResponse
import json
import logging
import tempfile
import uuid
import os
  
logger = logging.getLogger(__name__)


def index(request):
    #print('!!!!!!!!!', response.text)
    if request.method == 'POST':
        audio = Song(request.POST, request.FILES)
        if audio.is_valid():
            lang = audio.cleaned_data['lang']
            model = audio.cleaned_data['model']
            version = audio.cleaned_data['version']
            sample_rate = audio.cleaned_data['sample_rate']
            
            config = {
                "model": "{}".format(model),
                "version": version,
                "lang": "{}".format(lang),
                "sample_rate": sample_rate
            }
            print(request)
            file = request.FILES['file'].read()
            data = {
                'config':config,
                'file': file
            }
            response = requests.post('http://web_api-flask-1:5000/v1/stt', files={'file': file}, data=config)
            data = {'src': file,
                    'text': response.text}
            return render(request, "out_audio.html", data)
        else:
            data = {'text': 'error'}
            return render(request, "out_audio.html",data)
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
    if request.method == 'GET':
        student = ConfigTTS()
        return render(request, "index.html", {'form': student})
    else:
        url = "http://web_api-flask-1:5000/v1/tts"
        logger.critical('nor this')
        form = ConfigTTS(request.POST)
        choice1=''
        choice2=''
        choice3=''
        text=''
        if form.is_valid():
            choice1 = form.cleaned_data['lang']
            choice2 = form.cleaned_data['model']
            choice3 = form.cleaned_data['version']
            text = form.cleaned_data['text']
        print(request)
        logger.critical('lang '+choice1 )
        logger.critical('model '+choice2 )
        logger.critical('version '+choice3 )
        logger.critical('text '+text )
        #config = {"lang": choice1, "model": choice2, "version": choice3}
        payload={'config': '{{"lang": "{}", "model": "{}", "version": "{}" }}'.format(choice1,choice2,choice3),
        'text': text}

        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload)
        filename = ''

        src = 'taskmanager/main/static/upload/tmp/'
        if not os.path.exists(src):
            os.makedirs(src)
        ct=response.content
        filename = handle_uploaded_file(ct)
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
