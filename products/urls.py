from django.urls.conf import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from . import views

app_name = 'products'
router = routers.DefaultRouter()
router.register('product_list',views.ProductListView)
router.register('color_size',views.ItemSizeListView)


urlpatterns = [
    path('',include(router.urls)),
    path("product_detail/<int:pk>", views.ProductsDetailView.as_view(), name="User by role"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
