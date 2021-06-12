from django.urls import path

from .views import HomePageView, AboutPageView
from .views import KorolIShutPageView
from .views import SektorGazaPageView
from .views import KinoPageView
from .views import LeningradPageView
from .views import ZveriPageView
from .views import SplinPageView
from .views import DDTPageView
from .views import CommentCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('korolishut/', KorolIShutPageView.as_view(), name='korolishut'),
    path('sektorgaza/', SektorGazaPageView.as_view(), name='sektorgaza'),
    path('kino/', KinoPageView.as_view(), name='kino'),
    path('leningrad/', LeningradPageView.as_view(), name='leningrad'),
    path('zveri/', ZveriPageView.as_view(), name='zveri'),
    path('splin/', SplinPageView.as_view(), name='splin'),
    path('ddt/', DDTPageView.as_view(), name='ddt'),
    path('comment_new/', CommentCreateView.as_view(), name='comment_new'),        
]
