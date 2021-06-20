from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('addtocart/<int:id>',views.addtocart, name='addtocart'),
    path('deleteformcart/<int:id>', views.deleteformcart, name='deleteformcart'),
    path('rezervationproduct/', views.rezervationproduct, name='rezervationproduct'),
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/

]