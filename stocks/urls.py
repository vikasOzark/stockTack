from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexHomeView.as_view(), name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('stock-data/', views.get_data, name='portfolio'),
    path('portfolio-stock/', views.data_saving, name='portfolio-stock'),
    path('data_view/', views.data_view, name='data_view'),
    path('excel_upload/', views.ExportImport.as_view(), name='excel_upload'),
    path('feedback/', views.FeedbackEmailView.as_view(), name='feedback'),
    # path('excel_send_email/', views.attachment_send, name='excel_send_email'),
    path('excel_send_email/', views.attachment_send, name='excel_send_email'),
    path('excel/download/', views.download_excel, name='excel_download'),
    path('excel_delete/', views.excel_delete, name='excel_delete'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
