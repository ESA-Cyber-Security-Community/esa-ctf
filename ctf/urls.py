from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('404', views.error, name='error'),
    path('register', views.signup, name='signup'),
    path('about', views.about, name='about'),
    path('login', views.login1, name='login1'),
    path('instructions', views.inst, name='inst'),
    path('QUEST', views.Quest, name='Quest'),
    path('logout', views.logout, name='logout'),
    path('check', views.check, name='check'),
    path('hint', views.hint, name='hint'),
    path('leaderboard', views.leaderboard, name='leaderboard')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
