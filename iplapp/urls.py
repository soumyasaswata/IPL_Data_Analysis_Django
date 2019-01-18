"""ipldata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from iplapp import views
urlpatterns = [
    path('', views.home, name="home"),
    path('matches-per-season/', views.get_matches_per_seasons, name = "match_per_season"),
    path('wins-per-season/', views.get_winner_by_season, name = "winners_per_season"),
    path('wins-by-venue/', views.get_wins_by_venue, name = "get_wins_by_venue"),
    path('extra-runs-per-season/', views.get_extra_runs_per_season, name = "get_extra_runs_per_season"),
    path('top-economical-bowlers/', views.get_top_economical_bowlers, name = 'get_top_economical_bowlers'),
    path('matches-per-season-json/', views.get_matches_per_seasons_object, name = 'match_per_season_objects'),
    path('wins-per-season-json/', views.get_winner_by_season_object, name = 'winners_per_season_objects'),
    path('extra-runs-json/', views.get_extra_runs_per_season_object, name = 'get_extra_runs_per_season_objects'),
    path('top-economical-bowloers-json/', views.get_top_economical_bowlers_object, name = 'get_wins_by_venue_objects'),
    path('wins-per-venue-json/', views.get_wins_by_venue_object, name = 'wins_per_venue_objects')
]