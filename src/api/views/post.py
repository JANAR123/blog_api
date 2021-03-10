from django.shortcuts import render,redirect
from django.http import JsonResponse
from api.models import Post,Tag
from api.serializer import TagListSerializers, PostListSerializers,PostDetailSerializers,PostCreateSerialiser,TagPostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.forms import PostForm
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView

class PostListView(ListAPIView):
    serializer_class=PostListSerializers
    queryset=Post.objects.all()

class PostDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class=PostDetailSerializers
    queryset=Post.objects.all()
    lookup_field='pk'
    lookup_url_kwarg='post_id'

class PostCreateView(CreateAPIView):
    serializer_class=PostCreateSerialiser 

# @api_view(["GET","POST"])
# def post_list(request):
#     posts=Post.objects.all()
#     ser=PostListSerializers(posts,many=True)
#     return Response({"data":ser.data})

# @api_view(["GET","POST"])
# def post(request,post_id):
#     post=Post.objects.get(id=post_id) 
#     ser=PostDetailSerializers(post) 
#     return Response({"data":ser.data})


def post_html(request):
    posts=Post.objects.order_by("-id")
    print(posts)
    return render(request,'post.html',{'posts':posts})

def post_detail(request,post_id):
    post=Post.objects.get(id=post_id)
    return render(request,'post_detail.html',{'post':post})

def post_form(request):
    form=PostForm()
    if request.method=='POST':
        save_form=PostForm(request.POST)
        save_form.save()
        return redirect("api:post_html")
    return render(request,'post_form.html',{'form':form})

def post_delete(request,post_id):
    posts=Post.objects.filter(id=post_id).delete()
    return redirect("api:post_html") 



