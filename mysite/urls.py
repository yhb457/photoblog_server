from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_root/', include('post.urls')),  # 핵심 부분
]
