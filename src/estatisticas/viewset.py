from django.db.models import Sum, Count
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response
from tabelas_legado.models import (Curtida, FormularioPublicado,
                                   Posicionamento, Resposta)


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class StatisticsView(APIView):
    permission_classes = [ReadOnly]

    def get(self, request):
        responses = Resposta.objects.values_list(
            'ide_usuario', flat=True).all()
        likes = Curtida.objects.values_list('ide_usuario', flat=True).all()
        users_participations = count_participants(responses, likes)

        return Response({'count_responses': len(responses),
                         'count_likes': len(likes),
                         'users_participations': users_participations})


class StatisticsYearView(APIView):
    permission_classes = [ReadOnly]

    def get(self, request, year=None):
        pools = count_polls_by_month(year)
        votes = count_votes_by_month(year)
        positioning = count_positioning_by_month(year)
        return Response({'pools': pools,
                         'votes': votes,
                         'positioning': positioning})


def count_participants(responses, likes):

    users_participations = set(list(responses)+list(likes))

    return len(users_participations)


def count_polls_by_month(year):
    count_polls = FormularioPublicado.objects.filter(
        dat_publicacao__year=year).values('dat_publicacao__month').annotate(
        count_response=Count('dat_publicacao__month'))

    return count_polls


def count_votes_by_month(year):
    count_votes = Resposta.objects.filter(dat_resposta__year=year).values(
        'dat_resposta__month').annotate(
        count_response=Count('dat_resposta__month'))

    return count_votes


def count_positioning_by_month(year):
    list_positioning = Posicionamento.objects.filter(
        dat_posicionamento__year=year).values(
        'dat_posicionamento', 'qtd_curtidas', 'qtd_descurtidas')

    count_positing = list_positioning.values(
        'dat_posicionamento__month').annotate(
            count_likes=Sum('qtd_curtidas'),
            count_dislikes=Sum('qtd_descurtidas'),
            count_positing=Count('dat_posicionamento__month'))

    return count_positing
