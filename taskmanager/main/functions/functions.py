import os


def handle_uploaded_file(f):
    #path = os.getcwd()
    #print("Текущая рабочая директория %s" % path)
    src = 'taskmanager/main/static/upload/'+f.name
    src2 = 'static/upload/'+f.name
    with open(src, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return src2
