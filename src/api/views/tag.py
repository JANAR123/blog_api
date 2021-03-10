from django.shortcuts import render,redirect
from django.http import JsonResponse
from api.models import Post,Tag
from api.serializer import TagListSerializers, PostListSerializers,PostDetailSerializers,TagCreateSerialiser,TagPostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.forms import PostForm,TagForm
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateAPIView

class TagListView(ListAPIView):
    serializer_class=TagListSerializers
    queryset=Tag.objects.all()

class TagDetailView(ListAPIView):
    serializer_class=PostListSerializers
    queryset=Post.objects.all()
    lookup_field='tags__id'
    lookup_url_kwarg='tag_id'

class TagCreateView(CreateAPIView):
    serializer_class=TagCreateSerialiser 


# @api_view(["GET","POST"])
# def tag_list(request):
#     tags=Tag.objects.all()
#     ser=TagListSerializers(tags,many=True)
#     return Response({"data":ser.data})

@api_view(["GET","POST"])     
def tag_post(request,tag_id):
    posts=Post.objects.filter(tags__id=tag_id)
    ser=PostListSerializers(posts,many=True)
    return Response({"data":ser.data})


def tag_html(request):
    tags=Tag.objects.all()
    return render(request,'tag.html',{'tags':tags})

def tag_post_html(request,tag_id):
    posts=Post.objects.filter(tags__id=tag_id) 
    return render(request,'post.html',{'posts':posts})  

def tag_form(request):
    form=TagForm()
    if request.method=='POST':
        save_form=TagForm(request.POST)
        save_form.save()
        return redirect("api:tag_html")
    return render(request,'tag_form.html',{'form':form})    

def tag_delete(request,tag_id):
    tags=Tag.objects.filter(id=tag_id).delete()
    return redirect("api:tag_html")     


 
