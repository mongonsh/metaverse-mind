from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from django.http import JsonResponse
from .models import Categories, Articles, Image
import json
from cloudinary.uploader import upload
import uuid


# from django.shortcuts import get_object_or_404
@csrf_exempt
def add(request):
    print('irsenu',request)
    if request.method =='POST':
        res =json.loads(request.body)
        print(res['category'])
        category = Categories(name=res['category'])
        category.save()
        return HttpResponse(status=201)
    return HttpResponse(status=200, content='created')

def getAllCatetories(request):
    categories = Categories.objects.all()
    categories_list = []
   
    for category in categories:
        categories_list.append({
            'name': category.name,
            'name_jp': category.name_jp,
            'path_name': category.path_name
        })
    return JsonResponse(categories_list, safe=False)

def getAllArticles(request):
    request.encoding ='utf-8'
    articles = Articles.objects.all()
    
    article_list = []
    for article in articles:
        article_list.append({
            'id': str(article.id),
            'title_mn': article.title_mn,
            'title_jp': article.title_jp,
            'content_jp': article.content_jp,
            'content_mn': article.content_mn,
            'writer_id': article.writer_id,
            'state': article.state,
            'views_count': article.views_count,
            'media_id': article.media_id,
            'category_id': article.category_id,
            'delete_flag': article.delete_flag,
            'impression_id': article.impression_id,
            'media_url': article.media_url,
            'thumbnail_url': article.thumbnail_url,
            'short_desc': article.short_desc,
            'status' :article.status
        })
    return JsonResponse(article_list, safe=False)

def getArticleById(request):
    request.encoding ='utf-8'
    id = request.GET.get('id')
    article = Articles.objects.get(id=str(id))
    
    data = {
        'id': str(article.id),
        'title': article.title_mn,
        'content': article.content_mn,
        'media_url': article.media_url
    }
    return JsonResponse(data, safe=False)

@csrf_exempt
def addArticle(request):
    if request.method =='POST':
        res =json.loads(request.body)
        article = Articles(title_mn=res['title'], content_mn=res['content'],category_id=res['category'], media_url=res['media_url'])
        article.save()
        # elif res['language'] == '2':
        #     article = Articles(title_jp=res['title'], content_jp=res['content'],category_id=int(res['category']))
        #     article.save()
        return HttpResponse(status=201)
    return HttpResponse(status=200, content='Get request')


@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        image = request.FILES.get('file')
        print('zurag:', image)
        if image:
            unique_image_name = f"{uuid.uuid4().hex}_{image.name}"
            result = upload(image, public_id=unique_image_name)
            media_url = result.get('secure_url')
            
            if media_url:
                Image.objects.create(media_url=media_url)
                return JsonResponse({'media_url': media_url}, status=201)
            else:
                return JsonResponse({'error': 'Failed to upload image to Cloudinary'}, status=500)
        return JsonResponse({'error': 'No file uploaded'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})