from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'song/main.html')

def pictures(request):
    return render(request, 'song/pictures.html')
def video(request):
    return render(request,'song/video.html')