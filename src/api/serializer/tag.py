from rest_framework import serializers
from api.models import Tag


class TagListSerializers(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields="__all__"


class TagCreateSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Tag
        exclude=("id",)  

class TagPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        exclude=("name",)  
