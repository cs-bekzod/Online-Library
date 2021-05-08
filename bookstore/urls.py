from django.urls import path, include
from . import views

urlpatterns = [
 path('', views.UBookListView.as_view(), name='publisher'),
 path('uabook_form/', views.uabook_form, name='uabook_form'),
 path('uabook/', views.uabook, name='uabook'),
]
