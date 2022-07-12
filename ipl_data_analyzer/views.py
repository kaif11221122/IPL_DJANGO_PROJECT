import dis
from distutils.debug import DEBUG
from itertools import count
from unittest import result
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ipl_data_analyzer.models import Matches, Deliveries
from . fetcher import CsvFetcher
import os
from django.db.models import Count, Sum, FloatField
from django.db.models.functions import Cast, Round


# matches_file_path = os.getcwd()+'/resources/matches.csv'
# deliveries_file_path = os.getcwd()+'/resources/deliveries.csv'
# CsvFetcher.fetchMatchesDataFile(matches_file_path)
# CsvFetcher.fetchDeliveriesDataFile(deliveries_file_path)


# Create your views here.

def problem1(request):

    result = (
        Matches.objects.values_list('season')
        .annotate(number_of_matches_won=Count('season'))
        .order_by('season')
    )
    return render(request, 'ipl_data_analyzer/index.html', {'result': result})


def problem2(request):

    result = (
        Matches.objects.values_list('season', 'winner')
        .annotate(Count('season'))
        .order_by('season', 'winner')
    )
    return render(request, 'ipl_data_analyzer/index.html', {'result': result})


def problem3(request):

    result = (
        Deliveries.objects.select_related()
        .values_list('bowling_team')
        .annotate(extra_runs=Sum('extra_runs'))
        .filter(match_id__season=2016)
    )

    return render(request, 'ipl_data_analyzer/index.html', {'result': result})


def problem4(request):

    result = (
        Deliveries.objects.select_related()
        .filter(match_id__season=2015)
        .values_list('bowler')
        .annotate(economy_of_bowler=Cast(Cast(Sum('total_runs'), FloatField()) / Cast(Count('bowler'), FloatField()), FloatField()))
        .order_by('economy_of_bowler')
    )[:10]

    return render(request, 'ipl_data_analyzer/index.html', {'result': result})
