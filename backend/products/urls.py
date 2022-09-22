from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list_create_view),
    path('<int:pk>/', views.ProductDetailAPIView.as_view()), 
    # path('product/', views.api_post)
    # path('', views.product_alt_view), #Function Based View URL
    # path('<int:pk>/', views.product_alt_view), 
]