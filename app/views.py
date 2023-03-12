from django.shortcuts import render

# Create your views here.
def looping(request):
    d={'name':'suresh','profession':'bussinessman'}
    return render(request,'looping.html',d)