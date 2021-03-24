from django import forms
from .models import Post,Tag

class PostForm(forms.ModelForm):
    # def save(self,commit=True):
    #     instance=super(PostForm,self).save(commit=False)
    #     if not Post.objects.filter(title=self.cleaned_data['title']):
    #         instance.save()
    #     return instance   
    class Meta:
        model=Post
        exclude=("id","author")

class TagForm(forms.ModelForm):
     class Meta:
        model=Tag
        exclude=("id",)

