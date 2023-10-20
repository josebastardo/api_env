from django.http import HttpResponse, JsonResponse
from .models import Post

def index(request):
    html="<h1> Api django </h1> <p> Tutorial </p>"
    return HttpResponse(html)


def blogJson(request):
    posts=Post.objects.all()
    # Converting `QuerySet` to list
    blog = list(posts.values("id","title", "content"))
    print(blog)
    #person={"name":"joe", "apellido":"bast"}
    return JsonResponse(blog, safe =False)


def blogDetail(request, id):
  post = Post.objects.filter(id=id)
  return JsonResponse(list(post.values("id","title", "content")), safe=False)
