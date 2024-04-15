from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="getRoutes"),
    path('nfts/', views.getNftsInfo, name="ntfs"),
    path('nfts/<str:pk>', views.getNftInfo, name="ntf"),
    path('build_nft/', views.build_nft, name="build_nft"),
]