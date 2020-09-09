from django.shortcuts import render
from models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404

# Create your views here.
def index(request):
	return render_to_response('index.html',{
		'category': Category.objects.all()
		'post': Blog.objects.all()
		})

def view_post(request, slug):
	return render_to_response(
		"view_post.html", {
		'post': get_object_or_404(Blog, slug = slug)
		})


def view_post(request, slug):
	category = get_object_or_404(Category, slug = slug)
	return render_to_response(
		'view_category.html',{
		'category': category,
		'post':Blog.objects.filter(category = category)[:5]
		})