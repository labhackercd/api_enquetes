from django.db import models


class Curtida(models.Model):
    ide_posicionamento = models.OneToOneField(
        'Posicionamento', db_column='ide_posicionamento',
        primary_key=True, on_delete=models.PROTECT)
    ide_usuario = models.CharField(max_length=64)
    ide_formulario_publicado = models.ForeignKey(
        'FormularioPublicado', db_column='ide_formulario_publicado',
        on_delete=models.PROTECT)
    ind_positivo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Curtida'
        unique_together = (('ide_posicionamento', 'ide_usuario'),)


class FormularioPublicado(models.Model):
    ide_formulario_publicado = models.BigAutoField(primary_key=True)
    ide_usuario = models.CharField(max_length=10)
    tex_url_formulario_publicado = models.CharField(
        unique=True, max_length=100)
    nom_titulo_formulario_publicado = models.CharField(max_length=255)
    des_formulario_publicado = models.TextField(blank=True, null=True)
    cod_tipo = models.SmallIntegerField()
    cod_divulgacao = models.SmallIntegerField()
    dat_publicacao = models.DateTimeField()
    dat_inicio_vigencia = models.DateTimeField()
    dat_fim_vigencia = models.DateTimeField(blank=True, null=True)
    ind_permite_varias_respostas = models.BooleanField(blank=True, null=True)
    des_conteudo = models.TextField()
    des_informacao_adicional_1 = models.CharField(
        max_length=255, blank=True, null=True)
    des_informacao_adicional_2 = models.CharField(
        max_length=255, blank=True, null=True)
    des_informacao_adicional_3 = models.CharField(
        max_length=255, blank=True, null=True)
    des_url_post = models.CharField(max_length=1000, blank=True, null=True)
    ind_enquete_automatica = models.BooleanField(blank=True, null=True)
    ind_enquete_com_posicionamentos = models.BooleanField(
        blank=True, null=True)
    tex_url_link_externo = models.CharField(
        max_length=500, blank=True, null=True)
    tex_label_link_externo = models.CharField(
        max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Formulario_Publicado'


class ItemResposta(models.Model):
    ide_item_resposta = models.BigAutoField(primary_key=True)
    ide_resposta = models.ForeignKey(
        'Resposta', db_column='ide_resposta', on_delete=models.PROTECT)
    num_indice_campo = models.IntegerField()
    num_indice_opcao = models.IntegerField(blank=True, null=True)
    num_indice_linha_tabela = models.IntegerField(blank=True, null=True)
    tex_texto_livre = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Item_Resposta'


class Posicionamento(models.Model):
    ide_posicionamento = models.BigAutoField(primary_key=True)
    ide_formulario_publicado = models.ForeignKey(
        FormularioPublicado, db_column='ide_formulario_publicado',
        on_delete=models.PROTECT)
    ide_resposta = models.ForeignKey(
        'Resposta', db_column='ide_resposta', on_delete=models.PROTECT)
    ide_usuario = models.CharField(max_length=64)
    nom_usuario = models.CharField(max_length=200)
    ind_positivo = models.BooleanField()
    qtd_curtidas = models.IntegerField()
    des_conteudo = models.TextField()
    dat_posicionamento = models.DateTimeField()
    cod_autorizado = models.IntegerField(blank=True, null=True)
    qtd_descurtidas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Posicionamento'


class RelatorioGeral(models.Model):
    ide_relatorio_geral = models.BigAutoField(primary_key=True)
    ide_formulario_publicado = models.ForeignKey(
        FormularioPublicado, db_column='ide_formulario_publicado',
        on_delete=models.PROTECT)
    num_indice_campo = models.IntegerField()
    num_indice_opcao = models.IntegerField()
    num_indice_linha_tabela = models.IntegerField(blank=True, null=True)
    sig_uf = models.CharField(max_length=2, blank=True, null=True)
    qtd_total = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'Relatorio_Geral'
        unique_together = (('ide_formulario_publicado', 'num_indice_campo',
                            'num_indice_opcao', 'num_indice_linha_tabela',
                            'sig_uf'),)


class Resposta(models.Model):
    ide_resposta = models.BigAutoField(primary_key=True)
    ide_formulario_publicado = models.ForeignKey(
        FormularioPublicado, db_column='ide_formulario_publicado',
        on_delete=models.PROTECT)
    ide_usuario = models.CharField(max_length=64)
    dat_resposta = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Resposta'
