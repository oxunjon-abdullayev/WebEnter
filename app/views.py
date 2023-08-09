from django.shortcuts import render

from app.models import Blog


def index_view(request):
    return render(request=request,
                  template_name="app/index.html")


def blogs_view(request):
    blogs = Blog.objects.all()[:3]
    return render(request=request,
                  template_name="app/blog_main/blogs.html",
                  context={"blogs":blogs})


def blog_detail(request,blog_id):
    blog_single = Blog.objects.filter(id=blog_id).first()
    return render(request=request,
                  template_name="app/blog_main/blog-detail.html",
                  context={"blog_single": blog_single})
