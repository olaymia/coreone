from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.view_home, name='home'),
    path('about', views.about_view, name='about'),
    path('neet', views.neet_view, name='neet'),
    path('self_assessor', views.selassor_view, name='self'),
    path('fmcg', views.fmcg_view, name='fmcg'),
    path('contact_us', views.contact_view, name='contact'),
    path('pricing', views.pricing_view, name='plan'),
    path('login', views.login_view, name="login"),
]