from django.shortcuts import render

from django.http.response import HttpResponse, JsonResponse

posts = [
    {
        'id': i,
        'name': f'Post {i}',
        'price': i * 1000
    }
    for i in range(1, 10)
]

def post_list(request):
    return JsonResponse(posts, safe=False)

def post_detail(request, post_id):
    for post in posts:
        if post['id'] == post_id:
            return JsonResponse(post, status=200)
    return JsonResponse({'message': 'Post not found with selected ID'}, status=400)