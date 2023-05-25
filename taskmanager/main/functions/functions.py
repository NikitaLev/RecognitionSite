import os
import uuid

def handle_uploaded_file(f):
    #path = os.getcwd()
    #print("Текущая рабочая директория %s" % path)
    name = uuid.uuid4().__str__() +'.wav'
    src = 'taskmanager/main/static/upload/'+name#f.name
    src2 = 'static/upload/'+name#f.name
    with open(src, 'wb+') as destination:
        destination.write(f)
    return src2
