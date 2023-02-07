from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')


def create(requests):
    if requests.method == 'POST':
        link = requests.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(requests, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect('http://' + url_details.link)