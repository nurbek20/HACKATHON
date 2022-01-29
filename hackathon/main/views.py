from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from main.models import ContacTT
# Create your views here.
def home(request):
    data = ContacTT.objects.all()
    return render(request, 'index.html', {'data' :data})

def sendMessage(request):
    if request.method == 'POST':
        send=ContacTT()
        send.name = request.POST.get("name")
        send.email = request.POST.get("email")
        send.address = request.POST.get("address")
        send.message = request.POST.get("message")
        send.save()
        return HttpResponseRedirect('/')