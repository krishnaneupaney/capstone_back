  
from django.urls import path, include
from .views import ProductViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('users', UserViewSet)





urlpatterns = [
    path('capstoneapi/', include(router.urls)),
    # path('products/', ProductList.as_view()),
    # path('products/<int:id>/', ProductDetails.as_view)
    # path('products/', product_list),
    # path('products/<int:id>/', product_details),
]