from django.urls import path
from django.views.generic import TemplateView

app_name = 'house'

urlpatterns = [
    path('', TemplateView.as_view(template_name='house/index.html'), name='index'),
]