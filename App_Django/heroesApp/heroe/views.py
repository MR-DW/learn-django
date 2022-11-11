# rest - view imports
from ast import Delete
from dataclasses import dataclass
from http.client import ResponseNotReady
from rest_framework.views import APIView
# REst import
from rest_framework.response import Response
from rest_framework import status
# Import de Respuesta http front
from django.http import HttpResponse
# Render import para el template front
from django.shortcuts import render
# Models imports
from heroe.models import Hero

# Serializers imports
from heroe.serializer import HeroSerializer

# Helpers
from heroe.helpers.heroeErrors import hayHeroe

# Create your views here.
def Index(request):
    
   
    return render(request, 'lista.html', {})

def lista(request):
    
    heroes = Hero.objects.all()
    return render(request, 'lista.html',{
         'heroes':heroes,
    })

def crear(request):
    return render(request, 'crear.html',{})

def delete(request):
    return render(request, 'delete.html',{})

class HeroApiView(APIView):

    def get(self, request):
        """Retorna un listado con todos los heroes almacenados en la base"""

        heroes = Hero.objects.all()
        heroes_serializer = HeroSerializer(heroes, many=True)

        return Response(
           data = heroes_serializer.data,
           status=status.HTTP_200_OK
        )

    
    # def post(self, request):
        # """crea un nuevo registro/heroes"""
        # print('Primer post')
        # #Primer ejemplo*
        # # print("ESTAMOS EN EL METODO POST !!!") 

        # # EJEMPLO 2*
        # serializer = HeroSerializer(data = request.data)
        # # print(serializer)
        # # print(type(serializer))
        
        # # 3 EJEMPLO*
        # if serializer.is_valid():
        #     serializer.save()
        #     data = {
        #         'men': 'todo ok'
        #     }

        #     return Response(
        #         data = data,
        #         status = status.HTTP_201_CREATED
        #     )
        # return Response(
        #     data = serializer.errors,
        #     status=status.HTTP_400_BAD_REQUEST
        # )
       

     
# Nueva vista, class con un metodo idependiente

class CreateHeroApiView(APIView):
    
    def post(self, request):

        """Descripción de que va a registrar en la base de datos"""
        print('Segundo post')

        serializer = HeroSerializer(data = request.data) 
        if serializer.is_valid():    
            serializer.save()
            data = {
                'men': 'Tu heroe fue creado correctamente'
            }

            return Response(
                data = data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            data = serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )









# Crear un get de uno solo hereo
class HeroDetailApiView(APIView):
    

    def get(self, request, pk):
        """Nos devuelve mas info de un heroe en particular"""

        try:
            heroe = Hero.objects.get(id = pk)
            heroe_serializer = HeroSerializer(heroe)
            return Response(
                data = heroe_serializer.data,
                status=status.HTTP_200_OK
            )
        except:    
            data ={
                'mensaje':'Heroe no encontrado'
            }
            return Response(
                data = data,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk):
        """Modifica el registro"""
        
        respuesta = hayHeroe(pk)
        if hayHeroe(pk)[0]: 
            heroe_serializer = HeroSerializer(hayHeroe(pk)[1], data = request.data)

            if heroe_serializer.is_valid():
                heroe_serializer.save() 
                data ={
                     'mensage':'El hereo fue modificado de forma correcta',
                }
                return Response(
                    data=data,
                    status=status.HTTP_200_OK,
                )   

        return Response(
            data = heroe_serializer.errors,
            status=status.HTTP_404_NOT_FOUND
        )

    def delete(self, request, pk):
        """Elimina un registro"""
        heroe = Hero.objects.get(id = pk)
        heroe.delete()
        data ={
                'mensage':'El hereo fue eliminado de forma correcta',
        }
        return Response(
                data=data,
                status=status.HTTP_200_OK,
        )