from django.shortcuts import render
from .models import About
from .forms import CollaborateForm

# Create your views here.
def about_view(request):
    """
    Render the about page with the latest About object.
    """
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()
    
    return render(request, 'about/about.html', {
            'about': about,
            'collaborate_form': collaborate_form
        })
