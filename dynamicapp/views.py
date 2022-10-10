from django.shortcuts import render

# Create your views here.
def home(request):
    context={'name':'prashanth','course':'python','number':'2'}
    return render(request,'app/home.html',context)