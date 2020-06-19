from rest_framework.routers import DefaultRouter
from .viewset import (CurtidaViewSet, FormularioPublicadoViewSet,
                      ItemRespostaViewSet, PosicionamentoViewSet,
                      RelatorioGeralViewSet, RespostaViewSet)


router = DefaultRouter()
router.register(r'curtidas', CurtidaViewSet)
router.register(r'formularios', FormularioPublicadoViewSet)
router.register(r'itens-resposta', ItemRespostaViewSet)
router.register(r'posicionamentos', PosicionamentoViewSet)
router.register(r'relatorios', RelatorioGeralViewSet)
router.register(r'repostas', RespostaViewSet)
