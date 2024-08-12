from django.urls import path
from .views import index, upload_planilha, exibir_json, download_planilha

urlpatterns = [
    path('', index, name='index'),
    path('upload-planilha/', upload_planilha, name='upload_planilha'),
    path('exibir-json', exibir_json, name='exibir_json'),
    path('download-planilha/', download_planilha, name='download_planilha'),
]
