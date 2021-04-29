from django.shortcuts import render
from core.models import Post

def post_list(request):
    posts = Post.objects.all()
    posts_json = [post.to_json() for post in posts]
    return JsonResponse(posts_json, safe=False)

def post_detail(request,post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(post.to_json())

