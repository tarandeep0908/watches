from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings
from staunishing import views as my
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my.Home, name='home'),
    path('shop/<str:cn>/', my.Shop, name='shop'),
    path('product/<int:num>/', my.ProductDetails, name='product'),
    path('cart/', my.CartDetails, name='cart'),
    path('checkout/', my.CheckoutForm, name='checkout'),
    path('login/', my.Login, name='login'),
    path('signup/', my.SignUp, name="signup"),
    path('addproduct/', my.AddProduct, name='addproduct'),
    path('adminpage/', my.AdminPage, name="adminpage"),
    path('logout/', my.logout, name='logout'),
    path('delete/<int:num>', my.DeleteProduct, name='deleteproduct'),
    path('deletecart/<int:num>', my.cartdelete, name='deletecart'),
    path('edit/<int:num>', my.editProduct, name='edit'),
    path('contact/', my.contact, name='contact'),
    path('about/', my.aboutus, name='about'),
    #path('handlerequest/', my.handlerequest, name='HandleRequest'),
   ]
urlpatterns=urlpatterns+staticfiles_urlpatterns()
urlpatterns=urlpatterns+static(settings.MEDIA_URL,
                               document_root=settings.MEDIA_ROOT)