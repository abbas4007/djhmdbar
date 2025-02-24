from django.contrib.auth import views
from django.urls import path
from django.conf.urls import include

from .views import (
    ArticleList,
    ArticleCreate,
    ArticleUpdate,
    ArticleDelete,
    AddVakil,
    vakileList,
    Riyasatlist,
    vakil_image_view,
    add_comision,
    ComisionDetail, CustomLoginView, ComisionView, VakilUpdateView, VakilDeleteView, RiyasatDeleteView,CategoryListView,CategoryCreateView,
    add_riyasat, comision_edit, comision_delete, contact_view,success_page,MessageUpdateView,MessageListView,CategoryUpdateView,CategoryDeleteView,
upload_image
)


app_name = 'account'

urlpatterns = [
	path('', ArticleList.as_view(), name="home"),
	path('vakillist', vakileList.as_view(), name="vakil_list"),
    path('vakil/edit/<int:pk>/', VakilUpdateView.as_view(), name = 'vakil_edit'),
    path('vakil/delete/<int:pk>/', VakilDeleteView.as_view(), name = 'vakil_delete'),
    path('comisiondetail/<int:id>', ComisionDetail.as_view(), name="comision_detail"),
	path('riyasatlist', Riyasatlist.as_view(), name="riyasat_list"),
	path('addvakil', AddVakil.as_view(), name="vakil_add"),
    path('add-riyasat/', add_riyasat, name = 'add_riyasat'),
    path('addcomision', add_comision, name="comision_add"),
    path('article/create', ArticleCreate.as_view(), name="create_article"),
    path('comision/', ComisionView.as_view(), name = "comision"),
    path('article/update/<int:pk>', ArticleUpdate.as_view(), name="article_update"),
	path('article/delete/<int:pk>', ArticleDelete.as_view(), name="article_delete"),
    path('image_upload/<int:id>', vakil_image_view.as_view(), name = 'image_upload'),
    path('article/upload_image/', upload_image, name='upload_image'),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('comision/edit/<int:pk>/', comision_edit, name='comision_edit'),
    path('comision/delete/<int:pk>/', comision_delete, name='comision_delete'),
    path('riyasat/delete/<int:pk>/', RiyasatDeleteView.as_view(), name = 'riyasat_delete'),
    path('categories/', CategoryListView.as_view(), name = 'category_list'),
    path('categories/add/', CategoryCreateView.as_view(), name = 'category_add'),
    path('categories/edit/<int:pk>/', CategoryUpdateView.as_view(), name = 'category_edit'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name = 'category_delete'),
    path('contact/', contact_view, name = 'contact'),
    path('contact/success/', success_page, name = 'success_page'),
    path('messages/', MessageListView.as_view(), name = 'message_list'),
    path('admin/messages/<int:pk>/', MessageUpdateView.as_view(), name = 'message_update')

]