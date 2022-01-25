from django.shortcuts import render

def home(request):
    return render(request, 'omscatalogue/home.html')
def about(request):
    return render(request, 'omscatalogue/about.html')
def multi(request, pk):
    return render(request, 'omscatalogue/multi.html')