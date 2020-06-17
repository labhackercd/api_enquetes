from rest_framework import viewsets
from .models import (Curtida, FormularioPublicado,
                     ItemResposta, Posicionamento, RelatorioGeral, Resposta)

from .serializer import (CurtidaSerializer, FormularioPublicadoSerializer,
                         ItemRespostaSerializer, PosicionamentoSerializer,
                         RelatorioGeralSerializer, RespostaSerializer)


class CurtidaViewSet(viewsets.ModelViewSet):
    queryset = Curtida.objects.all()
    serializer_class = CurtidaSerializer


class FormularioPublicadoViewSet(viewsets.ModelViewSet):
    queryset = FormularioPublicado.objects.all()
    serializer_class = FormularioPublicadoSerializer


class ItemRespostaViewSet(viewsets.ModelViewSet):
    queryset = ItemResposta.objects.all()
    serializer_class = ItemRespostaSerializer


class PosicionamentoViewSet(viewsets.ModelViewSet):
    queryset = Posicionamento.objects.all()
    serializer_class = PosicionamentoSerializer


class RelatorioGeralViewSet(viewsets.ModelViewSet):
    queryset = RelatorioGeral.objects.all()
    serializer_class = RelatorioGeralSerializer


class RespostaViewSet(viewsets.ModelViewSet):
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer
