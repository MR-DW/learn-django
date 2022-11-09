# Models imports
from heroe.models import Hero


def hayHeroe(heroe):
    try:
        heroe = Hero.objects.get(id = pk)

        return (True, heroe)

    except:
        return (False)

















