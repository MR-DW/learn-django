# Rest imports
from dataclasses import fields
from rest_framework import serializers

# Models imports
from heroe.models import Hero


# Creación serializers

class HeroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hero
        fields = '__all__'



