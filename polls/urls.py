from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('',views.homepage, name='home'),
    path('<int:question_id>/',views.detail, name='detail'),
    path('<int:question_id>/Results/', views.results, name='results'),
    path('<int:question_id>/vote/',views.vote, name='vote'),

]