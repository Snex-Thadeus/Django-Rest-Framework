from django.urls import path
from . import views 


urlpatterns = [
    path('', views.product_list_create_view, name='product-list'),
    # path('', views.product_mixin_view),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name='product-edit'), 
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view()),
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    # path('<int:pk>/', views.product_mixin_view),
    # path('product/', views.api_post)
    # path('', views.product_alt_view), #Function Based View URL
    # path('<int:pk>/', views.product_alt_view), 
]