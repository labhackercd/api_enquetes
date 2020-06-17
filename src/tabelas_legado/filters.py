import django_filters
from .models import (Curtida, FormularioPublicado,
                     ItemResposta, Posicionamento, RelatorioGeral, Resposta)


YEAR_FILTERS = ['lt', 'gt', 'lte', 'gte',
                'year__gt', 'year__lt', 'year__exact']


class CurtidaFilter(django_filters.FilterSet):
    class Meta:
        model = Curtida
        fields = {
            'ide_posicionamento': ['exact'],
            'ide_usuario': ['exact'],
            'ide_formulario_publicado': ['exact'],
            'ind_positivo': ['exact'],
        }


class FormularioPublicadoFilter(django_filters.FilterSet):
    class Meta:
        model = FormularioPublicado
        fields = {
            'ide_formulario_publicado': ['exact'],
            'ide_usuario': ['exact'],
            'nom_titulo_formulario_publicado': ['exact'],
            'dat_inicio_vigencia': YEAR_FILTERS,
            'dat_publicacao': YEAR_FILTERS,
            'dat_fim_vigencia': YEAR_FILTERS,
        }


class ItemRespostaFilter(django_filters.FilterSet):
    class Meta:
        model = ItemResposta
        fields = {
            'ide_item_resposta': ['exact'],
            'ide_resposta': ['exact'],
            'num_indice_opcao': ['exact'],
            'num_indice_linha_tabela': ['exact'],
        }


class PosicionamentoFilter(django_filters.FilterSet):
    class Meta:
        model = Posicionamento
        fields = {
            'ide_posicionamento': ['exact'],
            'ide_formulario_publicado': ['exact'],
            'ide_resposta': ['exact'],
            'ide_usuario': ['exact'],
            'nom_usuario': ['exact'],
            'ind_positivo': ['exact'],
            'qtd_curtidas': ['exact', 'lt', 'gt'],
            'des_conteudo': ['exact'],
            'dat_posicionamento': YEAR_FILTERS,
            'cod_autorizado': ['exact'],
            'qtd_descurtidas': ['exact', 'lte', 'gte'],
        }


class RelatorioGeralFilter(django_filters.FilterSet):
    class Meta:
        model = RelatorioGeral
        fields = {
            'ide_relatorio_geral': ['exact'],
            'ide_formulario_publicado': ['exact'],
            'num_indice_campo': ['exact'],
            'num_indice_opcao': ['exact'],
            'num_indice_linha_tabela': ['exact'],
            'sig_uf': ['exact'],
            'qtd_total': ['exact', 'lte', 'gte'],
        }


class RespostaFilter(django_filters.FilterSet):
    class Meta:
        model = Resposta
        fields = {
            'ide_resposta': ['lt', 'gt'],
            'ide_formulario_publicado': ['exact'],
            'ide_usuario': ['exact'],
            'dat_resposta': YEAR_FILTERS
        }
