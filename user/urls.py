from django.urls import path
from user import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    #path('addcomment/<int:id>',views.addcomment, name='addcomment')
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/

]