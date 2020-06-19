from rest_framework import serializers
from .models import (Curtida, FormularioPublicado,
                     ItemResposta, Posicionamento, RelatorioGeral, Resposta)


class CurtidaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curtida
        fields = '__all__'


class FormularioPublicadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FormularioPublicado
        fields = '__all__'


class ItemRespostaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItemResposta
        fields = '__all__'


class PosicionamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posicionamento
        fields = '__all__'


class RelatorioGeralSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RelatorioGeral
        fields = '__all__'


class RespostaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resposta
        fields = '__all__'
