from django.shortcuts import get_object_or_404, render
import requests
from .models import Song
from .functions.functions import handle_uploaded_file
from django.http import HttpResponse


def index(request):
    response = requests.get('http://[::1]:5000/', params={'key': 'value_test'})
    print('!!!!!!!!!', response.text)
    if request.method == 'POST':
        file = Song(request.POST, request.FILES)
        print(request)
        if file.is_valid():
            print(str(request.FILES['file']).endswith('.wav'))
            src = handle_uploaded_file(request.FILES['file'])
            data = {'src': src}
            print(src)
            return render(request, "out_audio.html", data)
            #return HttpResponse("File uploaded successfuly")
    else:
        student = Song()
        return render(request, "index.html", {'form': student})


def upload_audio(request):
    return render(request, 'upload_audio.html')


def out_audio(request):
    return render(request, 'out_audio.html')
