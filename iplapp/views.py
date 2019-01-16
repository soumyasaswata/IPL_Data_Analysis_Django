from django.conf import settings
import json
from django.shortcuts import render
from .models import Matches, Deliveries
from django.http import HttpResponse, JsonResponse
from django.db.models import Count,Sum, DecimalField
from django.db.models import DateTimeField, ExpressionWrapper, F, Q
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# Create your views here.

def home(request):
    return render(request, 'base.html', {})

@cache_page(CACHE_TTL)
def get_matches_per_seasons(request):
    matches_per_seasons = Matches.objects.values("season").annotate(matches = Count("season")).order_by("season")
    context = {'matches_per_seasons':matches_per_seasons}
    return render(request, 'matches-per-season.html', context)

def get_matches_per_seasons_object(request):
    matches_per_seasons = Matches.objects.values("season").annotate(matches = Count("season")).order_by("season")
    return JsonResponse(list(matches_per_seasons), safe = False)

@cache_page(CACHE_TTL)
def get_winner_by_season(request):
    winner_per_season = Matches.objects.values("season", "winner").annotate(matches = Count('winner')).order_by("season")
    context = {'winner_per_season': json.dumps(list(winner_per_season))}
    return render(request, 'wins-per-season.html', context)

def get_winner_by_season_object(request):
    winner_per_season = Matches.objects.values("season", "winner").annotate(matches = Count('winner')).order_by("season")
    return JsonResponse(list(winner_per_season), safe = False)

@cache_page(CACHE_TTL)
def get_extra_runs_per_season(request):
    extra_runs = Matches.objects.values("deliveries__bowling_team").annotate(total_extra_runs = Sum("deliveries__extra_runs")).filter(season = 2016).order_by("season","deliveries__bowling_team")
    context = {'extra_runs':extra_runs}
    return render(request, 'extra-runs.html', context)

def get_extra_runs_per_season_object(request):
    extra_runs = Matches.objects.values("deliveries__bowling_team").annotate(total_extra_runs = Sum("deliveries__extra_runs")).filter(season = 2016).order_by("season","deliveries__bowling_team")
    return JsonResponse(list(extra_runs), safe = False)

@cache_page(CACHE_TTL)
def get_top_economical_bowlers(request):
    top_ten_bowlers = Matches.objects.values("deliveries__bowler").annotate(economy =ExpressionWrapper(Sum("deliveries__total_runs")/ (Count("deliveries__ball", filter= Q(deliveries__noball_runs= 0) & Q(deliveries__wide_runs = 0))/6),output_field = DecimalField())).filter(season = 2015).order_by("economy")[:10]
    top_ten_bowlers = [{"bowler":query["deliveries__bowler"], "economy": round(float(query["economy"]),2)} for query in top_ten_bowlers]  #round to count balls
    context = {'top_ten_bowlers':top_ten_bowlers}
    return render(request, 'top-economical-bowlers.html', context)

def get_top_economical_bowlers_object(request):
    top_ten_bowlers = Matches.objects.values("deliveries__bowler").annotate(economy =ExpressionWrapper(Sum("deliveries__total_runs")/ (Count("deliveries__ball", filter= Q(deliveries__noball_runs= 0) & Q(deliveries__wide_runs = 0))/6),output_field = DecimalField())).filter(season = 2015).order_by("economy")[:10]
    top_ten_bowlers = [{"bowler":query["deliveries__bowler"], "economy": round(float(query["economy"]),2)} for query in top_ten_bowlers]  #round to count balls
    return JsonResponse(top_ten_bowlers, safe = False)

@cache_page(CACHE_TTL)
def get_wins_by_venue(request):
    wins_per_venue = Matches.objects.values("winner").annotate(matches = Count('winner')).filter(venue = 'M Chinnaswamy Stadium')
    context = {'wins_per_venue':wins_per_venue}
    return render(request, 'wins-by-venue.html', context)

def get_wins_by_venue(request):
    wins_per_venue = Matches.objects.values("winner").annotate(matches = Count('winner')).filter(venue = 'M Chinnaswamy Stadium')
    return JsonResponse(list(wins_per_venue), safe = False)
