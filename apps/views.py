from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, FormView, CreateView

from apps.forms import RegisterForm
from apps.models import Category, Product


class HomePageListView(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'index.html'
    context_object_name = 'categories'

    def get_context_data(self, object_list=None, **kwargs):
        data = super().get_context_data(object_list=object_list, **kwargs)
        data['products'] = Product.objects.all()
        return data


class AboutPageTemplateView(TemplateView):
    template_name = 'about.html'


class ContactPageTeplateView(TemplateView):
    template_name = 'contact.html'


class ShopPageListView(ListView):
    template_name = 'shop.html'
    model = Product
    context_object_name = 'products'

class AddProductView(CreateView):
    template_name = 'template_parts/header.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop-single.html'
    context_object_name = 'detail'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

        # def get_context_data(self, **kwargs):
        #     context = super().get_context_data()
        #     product = context['detail']


class RelatedProductsView(ListView):
    template_name = 'shop-single.html'
    context_object_name = 'products'
    queryset = Product.objects.all()


class SignUpView(FormView):
    template_name = 'sign_up_page.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)\


class LoginPage(CreateView):
    template_name = 'login.html'
    






