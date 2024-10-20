from django.urls import path
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from . import views
# from .views import get_csrf_token

urlpatterns = [
    path("add", views.add, name="add"),
    path("get-all-categories", views.getAllCatetories, name="get_all_categories"),
    path('add-article', views.addArticle, name= 'add_article'),
    path('get-all-articles', views.getAllArticles, name= 'get_all_articles'),
    path('get-article', views.getArticleById, name='get_article'),
    path('get-csrf-token', views.get_csrf_token, name='get_csrf_token'),
     path('upload', views.upload_image, name='upload_image'),
     path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]