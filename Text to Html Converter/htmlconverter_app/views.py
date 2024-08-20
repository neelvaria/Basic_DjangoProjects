from django.shortcuts import render
from .models import post
from .forms import Postform

# Create your views here.
def home(request):
    form = Postform()
    return render(request, 'index.html', {'form': form})
