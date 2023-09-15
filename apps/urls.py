from django.urls import path

from apps.views import AboutPageTemplateView, ContactPageTeplateView, HomePageListView, \
    ShopPageListView, ProductDetailView, SignUpView, RelatedProductsView, AddProductView, LoginPage

urlpatterns = [

    path('about/', AboutPageTemplateView.as_view(), name='about'),
    path('contact/', ContactPageTeplateView.as_view(), name='contact'),
    path('', HomePageListView.as_view(), name='index'),
    path('shop/', ShopPageListView.as_view(), name='shop'),
    path('single/<slug:slug>', ProductDetailView.as_view(), name='single'),
    path('signup/', SignUpView.as_view(), name='sign_up_page'),
    path('admin/apps/product/add/', AddProductView.as_view(), name='create'),
    path('login/', LoginPage.as_view(), name='login'),

]
