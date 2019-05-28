from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Brasil > Estado > Cidade > Bairro > Rua > Residência
class Estado(models.Model):
	nome = models.CharField(max_length=30)
	sigla = models.CharField(max_length=2, unique=True)

	def __str__(self):
		return self.nome + ' - ' + self.sigla

class Cidade(models.Model):
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=1)
	nome = models.CharField(max_length=200, unique=True)

	def __str__(self):
		return self.nome


class Bairro(models.Model):
	cidade = models.ForeignKey(Cidade, on_delete= models.CASCADE, default='')
	nome = models.CharField(max_length=200)

	def __str__(self):
		return self.nome


class Rua(models.Model):
	nome = models.CharField(max_length=200, unique=True)
	bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, default='')

	def __str__(self):
		return self.nome


class Residencia(models.Model):
	responsavel = models.CharField(max_length=200)
	numero_casa = models.PositiveIntegerField()
	rua = models.ForeignKey(Rua, on_delete=models.CASCADE, default='')
	bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, default='')
	cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, default='')

	def __str__(self):
		return ' Rua: ' +str(self.rua) + '   Bairro: ' + str(self.bairro)+ '  Cidade  '+str(self.cidade)+ '   Número da casa:  ' + str(self.numero_casa)


class Rota(models.Model):
	nome = models.CharField(max_length=25, unique=True, default='Área x')
	bairro= models.ForeignKey(Bairro, on_delete=models.CASCADE, default='')  #Rota é o nome do atributo que especifica as ruas onde o agente deverá trabalhar
	ruas = models.ManyToManyField(Rua)
	def __str__(self):
		return ' Nome: ' + str(self.nome) + '--- Cidade:'+ str(self.bairro.cidade)

class Trajeto(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	rota = models.ForeignKey(Rota, on_delete=models.CASCADE, default='')
	def __str__(self):
		return self.rota.nome


class Visita(models.Model):
	data=models.DateTimeField(auto_now_add=True)
	codigo_visita=models.PositiveIntegerField()
	agente_da_visita=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	residencia_da_visita=models.ForeignKey('Residencia', on_delete=models.CASCADE, null=True)
	def __str__(self):
		return  ' residencia: ' +str(self.residencia_da_visita) + '  código da casa:' + str(self.codigo_visita)

class Prancheta (models.Model):
		dados_da_visita=models.ForeignKey('Residencia', on_delete=models.SET_NULL, null=True)
		tipo_imovel_choices= (
				('1-Residência', 'residência'),
				('2-Comercio' ,'comercio'),
				('3-Terreno', 'terreno'),
				('4-Outros(Hospitais,Escolas, Órgãos publicos)','Outros')
			)
		tipo_imovel=models.CharField(
				max_length=100,
				choices= tipo_imovel_choices
				 )
		imoveis_trabalhados_choices=(
			('1-Sim','sim'),
			('2-Não','nao')
			)
		imoveis_trabalhados=models.CharField(
				max_length=5,
				choices= imoveis_trabalhados_choices
				 )
		focos_choices=(
			('1-Sim','sim'),
			('2-Não','nao')
			)
		focos=models.CharField(
				max_length=5,
				choices= focos_choices
				 )
		tratamento_larvicida_choices=(
			('1-Sim','sim'),
			('2-Não','nao')
			)
		tratamento_larvicida=models.CharField(
				max_length=5,
				choices=tratamento_larvicida_choices
				 )

		observacao = models.TextField()

class Justificar_visita(models.Model):
	agente = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	imoveis_fechados_choices=(
			('1-Sim','sim'),
			('2-Não','nao')
			)
	imoveis_fechados=models.CharField(
				max_length=10,
				choices= imoveis_fechados_choices
				 )
	imoveis_recusados_choices=(
			('1-Sim','sim'),
			('2-Não','nao')
			)
	imoveis_recusados=models.CharField(
				max_length=10,
				choices= imoveis_recusados_choices
				 )
	observacao = models.TextField()

	estado = models.CharField(max_length=100, null=False, default='')
	cidade = models.CharField(max_length=100, null=False, default='')
	bairro = models.CharField(max_length=100, null=False, default='')
	rua = models.CharField(max_length=100, null=False, default='')
	
