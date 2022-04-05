from django.urls.conf import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from . import views

app_name = 'products'
router = routers.DefaultRouter()
# router.register('product_list',views.ProductListView)
# router.register('color_size',views.ItemSizeListView)
router.register('comfy_products', views.ComfyProductView)
# router.register('dimension', views.DimensionView)
# router.register('comfy_sale',views.ComfySaleView)
# router.register('shipping_info',views.ShippingInfoView)
# router.register('product_images', views.ProductImagesView)


urlpatterns = [
    path('',include(router.urls)),
    # path("product_detail/<int:pk>", views.ProductsDetailView.as_view(), name="User by role"),
    path("product_detail/<int:pk>", views.ComfyProductsDetailView.as_view(), name="ComfyProduct Detail"),
    path("image_category/<int:category>",views.ImageCategoryProductsView.as_view(), name="Image Category"),
    path("featured/", views.FeaturedProductsView.as_view(), name="Featured Products"),
    path("newest/", views.NewestProductsView.as_view(), name="Newest Products"),
    path("<int:category>/<int:itemType>", views.ProductsByTypeView.as_view(), name=" Products by Type"),


    path("product_by_category/<int:category>", views.CategoryProductsView.as_view(), name="Products By Category"),


    

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
