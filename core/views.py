from django.shortcuts import render
from django.views.generic.base import TemplateView

from core.models import Pelicula

# Create your views here.

class HomePageView(TemplateView):

    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['peliculas'] = Pelicula.objects.all()
        return context


from django.http import JsonResponse

def change_fav(request):
    pelicula = request.GET.get('pelicula', None)

    pelicula_obj = Pelicula.objects.get(nombre=pelicula)
    
    if ( pelicula_obj.favorita ):
        pelicula_obj.favorita = False
    else:
        pelicula_obj.favorita = True

    pelicula_obj.save()

    data = {
        'is_fav': pelicula_obj.favorita,
        'nombre': pelicula
    }
    return JsonResponse(data)