from django.shortcuts import render

# Create your views here.
def profilepage(request):
    
    return render(request,'profile.html')