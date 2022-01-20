
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.requisicao_form, name='requisicao_insert'), # get and post request insert operations.
    path('<int:id>/', views.requisicao_form, name='requisicao_update'), # get and post request for update operations.
    path('delete/<int:id>/', views.requisicao_delete,name="requisicao_delete"),
    path('list/', views.requisicao_list, name='requisicao_list') # get request to retrieve and display all records.
]