from django.contrib import admin
from django.urls import path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from loader.views import calculThePower

urlpatterns = [
    path('admin/', admin.site.urls),

    path('productionplan/', calculThePower),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
]
