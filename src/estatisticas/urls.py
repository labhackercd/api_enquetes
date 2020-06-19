from django.urls import path
from .viewset import (StatisticsView, StatisticsYearView)

urls_statistics = [
    path('statistics/', StatisticsView.as_view()),
    path('statistics-year/<int:year>/', StatisticsYearView.as_view()),
]
