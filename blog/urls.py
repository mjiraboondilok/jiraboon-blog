from django.urls import path

from .views import IndexView

urlpatterns = [
    # ex: /blog/
    path('', IndexView.as_view(), name='index'),
]