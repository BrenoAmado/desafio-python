from django.urls import path
from .views import index, upload_planilha, download_planilha

urlpatterns = [
    path('', index, name='index'),
    path('upload-planilha/', upload_planilha, name='upload_planilha'),
    path('download-planilha/', download_planilha, name='download_planilha'),
]
