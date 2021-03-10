from django.urls import path
from api.views import (
    tag_post,
    post,
    post_html ,
    PostListView,
    PostDetailView,
    TagDetailView,
    TagListView,
    PostCreateView,
    TagCreateView,
    post_detail,
    tag_html,
    tag_post_html,
    post_form,
    tag_form,
    post_delete,
    tag_delete)

app_name="api"
urlpatterns = [
    path("api1/tags/",TagListView.as_view()),
    path("api1/tag/<int:tag_id>",TagDetailView.as_view()),
    path("api1/posts/",PostListView.as_view()),
    path("api1/post/<int:post_id>",PostDetailView.as_view()),
    path("api1/post_create/",PostCreateView.as_view()),
    path("api1/tag_create/",TagCreateView.as_view()),
    
    path("post_detail/<int:post_id>",post_detail,name="post_detail"),
    path("tag_post/<int:tag_id>",tag_post),
    path("post_html/",post_html,name="post_html"),
    path("tag_html/",tag_html),
    path("tag_post_html/<int:tag_id>",tag_post_html),
    path("post_form/",post_form,name="form_html"),
    path("tag_form/",tag_form,name="tag_html"),
    path("post_delete/<int:post_id>",post_delete,name="post_delete"),
    path("tag_delete/<int:tag_id>",tag_delete)
]