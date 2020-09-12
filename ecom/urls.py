from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views
from order import views as OrderViews
from user import views as UserViews
urlpatterns = [
    path('product/', include('product.urls')),
    path('', include('home.urls')),
    path('order/', include('order.urls')),
    path('user/', include('user.urls')),
    path('login/', UserViews.login_form, name='login_form'),
    path('logout/', UserViews.logout_func, name='logout_func'),
    path('signup/', UserViews.signup_form, name='signup_form'),
    path('shopcart/', OrderViews.shopcart, name='shopcart'),

    path('home/', include('home.urls')),
    path('search/', views.search, name='search'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('contact/',views.contactus, name='contactus'),
    path('about/', views.aboutus, name='aboutus'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('category/<int:id>/<slug:slug>', views.category_products, name='category_products'),
    path('product/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),

]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)