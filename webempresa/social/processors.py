from .models import Link

def ctx_dict(request):
    ctx={'test':'hola'}
    links = Link.objects.all()
    for link in links:
        ctx[link.key]=link.url
    return ctx # el return cierra el for ojo 

    #como session en php 