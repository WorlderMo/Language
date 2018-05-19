import glob
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WQSiteNavigator.settings")


django.setup()


def readDocument(filename):
    from main.models import Document
    with open(filename, 'rb') as f:
        content = f.read()
    title = os.path.splitext(filename.split('/')[-1])[0]
    Document.objects.create(tilte=title, content=content)


def function(path):
    for filename in glob.glob(path + os.sep + '*'):
        if os.path.isdir(filename):
            function(filename)
        else:
            readDocument(filename)


function(r'/Users/worlder/Documents/Language/Python2/WQSiteNavigator/main/static/files/')
