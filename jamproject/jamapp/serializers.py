#from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Jamapp


class JamappSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jamapp
        fields = ['"__all__"']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']