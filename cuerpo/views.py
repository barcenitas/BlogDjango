from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
"""
todas las vistas reciben una petición
"""
def listadoPosts(request):
    posts = Post.objects.filter(fechaPublicacion__lte= timezone.now()).order_by('fechaPublicacion')
    return render(request, 'cuerpo/listadoPosts.html', {'posts':posts})


"""
regreso el query set como contexto -> que es un diccionario 
"""