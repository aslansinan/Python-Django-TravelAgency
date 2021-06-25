from django.urls import path
from user import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('update/',views.user_update, name='user_update'),
    path('password/',views.change_password, name='change_password'),
    path('orders/',views.orders, name='orders'),
    path('orderdetail/<int:id>',views.orderdetail, name='orderdetail'),
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/

]