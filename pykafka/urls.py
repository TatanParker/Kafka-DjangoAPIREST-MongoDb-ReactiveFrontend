
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from django.conf.urls import url 
from apikafka import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
 	path('api/messages', views.MessagesList.as_view(),name = 'list-create'),
 	path('api/messages/<int:pk>/', views.MessagesList.as_view(),name = 'list-create'),
 	path('api/person/', views.PersonAPIView.as_view(),name = 'color-create'),
 	path('api/consumertrend/', views.ColortrendsAPIView.as_view(),name = 'color-get'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
