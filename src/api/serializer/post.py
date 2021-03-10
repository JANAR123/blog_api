from rest_framework import serializers
from api.models import Post,Tag
from .tag import TagListSerializers,TagPostSerializer


class PostListSerializers(serializers.ModelSerializer):
    class Meta:
        model=Post
        exclude=("tags","body",)   

class PostDetailSerializers(serializers.ModelSerializer):
    def update(self,instance,data):
        tags=data.pop('tags',[])
        instance=super(PostDetailSerializers,self).update(instance,data)
        if tags:
            post_tags=instance.tags.all()
            for tag in tags:
                if  tag not in post_tags:
                    instance.tags.add(tag)
                    instance.save
        return instance  

    
    class Meta:
        model=Post
        exclude=("id",) 

          







class PostCreateSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Post
        exclude=("id",) 
      

