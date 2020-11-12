
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

    # url(r'^api/messages$', views.messages_list),
    # url(r'^api/messages(?P<pk>[0-9]+)$', views.messages_detail),
    # url(r'^api/messages/published$', views.messages_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
