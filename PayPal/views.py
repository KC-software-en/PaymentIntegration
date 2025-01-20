from django.shortcuts import render

# Create your views here.
# create a view for the index template
def index(request):
    return render(request, 'index.html')