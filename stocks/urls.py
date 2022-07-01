from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexHomeView.as_view(), name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('stock-data/', views.get_data, name='portfolio'),
    path('portfolio-stock/', views.data_saving, name='portfolio-stock'),
    # path('get-data/', views.get_data, name='get-data'),
    path('data_view/', views.data_view, name='data_view'),
    path('excel_upload/', views.ExportImport.as_view(), name='excel_upload'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
