from rest_framework import viewsets

from .models import (Curtida, FormularioPublicado,
                     ItemResposta, Posicionamento, RelatorioGeral, Resposta)

from .serializer import (CurtidaSerializer, FormularioPublicadoSerializer,
                         ItemRespostaSerializer, PosicionamentoSerializer,
                         RelatorioGeralSerializer, RespostaSerializer)

from .filters import (CurtidaFilter, FormularioPublicadoFilter,
                      ItemRespostaFilter, PosicionamentoFilter,
                      RelatorioGeralFilter, RespostaFilter)


class CurtidaViewSet(viewsets.ModelViewSet):
    queryset = Curtida.objects.all()
    serializer_class = CurtidaSerializer
    filterset_class = CurtidaFilter


class FormularioPublicadoViewSet(viewsets.ModelViewSet):
    queryset = FormularioPublicado.objects.all()
    serializer_class = FormularioPublicadoSerializer
    filterset_class = FormularioPublicadoFilter


class ItemRespostaViewSet(viewsets.ModelViewSet):
    queryset = ItemResposta.objects.all()
    serializer_class = ItemRespostaSerializer
    filterset_class = ItemRespostaFilter


class PosicionamentoViewSet(viewsets.ModelViewSet):
    queryset = Posicionamento.objects.all()
    serializer_class = PosicionamentoSerializer
    filterset_class = PosicionamentoFilter


class RelatorioGeralViewSet(viewsets.ModelViewSet):
    queryset = RelatorioGeral.objects.all()
    serializer_class = RelatorioGeralSerializer
    filterset_class = RelatorioGeralFilter


class RespostaViewSet(viewsets.ModelViewSet):
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer
    filterset_class = RespostaFilter
