from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('user/', include('user.urls', namespace='user')),
    path('crt_rec', views.crt_rec, name='crt_rec'),
    path('category/<str:ctg_slug>/', views.category_detail, name='category'),
    path('recipe/<str:rec_slug>/', views.recipe, name='recipe'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('recipe/', views.recipe, name='recipe'),
    path('category_detail/', views.category_detail, name='category_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
