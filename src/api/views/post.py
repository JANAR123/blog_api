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
    print(request.user)
    posts=Post.objects.order_by("-id")
    return render(request,'post.html',{'posts':posts})

def post_detail(request,post_id):
    post=Post.objects.get(id=post_id)
    return render(request,'post_detail.html',{'post':post})



 

def post_form(request):
    if request.user.is_authenticated:
        form=PostForm()
        if request.method=='POST':
            save_form=PostForm(request.POST)
            if save_form.is_valid():
                note = save_form.save(commit=False)
                note.author = request.user
                note.save()
            return redirect("api:post_html")
        return render(request,'post_form.html',{'form':form})
    return redirect("authe:login")    
   

      
        
    

def post_delete(request,post_id):
    posts=Post.objects.filter(id=post_id).delete()
    return redirect("api:post_html") 


# def post_author(request):
#     print(request.user)
#     post=Post.objects.filter(author=request.user)
#     return render(request,'post.html',{'post':post})

def post_author(request):
    posts=Post.objects.filter(author=request.user)
    return render(request,'post.html',{'posts':posts})
    

    




