from django import forms
from .models import Residencia, Visita, Prancheta, Justificar_visita, Rota, Estado, Cidade, Bairro, Rua, Trajeto
from django.contrib.auth.models import User, Group


class User_form(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name','username', 'email','password')
		labels = {'username':'CPF', 'first_name':'Nome completo'}
		widgets ={'password':forms.PasswordInput()}
		error_mensagens = {
			'username': {
				'required': 'Este campo é obrigatório',
				'unique': 'O usuário já existe'
			},

			'first_name': {
				'required': 'Este campo é obrigatório'
			},


			'email': {
				'required': 'Este campo é obrigatório',
				'unique': 'O usuário já existe'

			},
			'password': {
				'required' : 'Este campo é obrigatório'
			},

		}


	def save(self, commit= True):
		user = super(User_form, self).save(commit= False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user



class Rota_form(forms.ModelForm):
	class Meta:
		model = Rota
		fields = ('nome','bairro', 'ruas')

		error_mensagens = {
			'nome': {
				'required': 'Este campo é obrigatório'
			},	
			'bairro': {
				'required': 'Este campo é obrigatório'
			},
			'rua':{
				'required':'Este campo é obrigatório'	
			},
	
		}
	'''bairroObject = Bairro.objects.all().order_by('pk')
	ruaObject = Rua.objects.filter(bairro=bairroObject[0])
	bairro = forms.ChoiceField(choices=[(x.pk, x.nome) for x in bairroObject])
	rua = forms.ChoiceField(choices=[(x.pk, x.nome) for x in ruaObject])
	nome = forms.CharField()'''


class Trajeto_form(forms.ModelForm):
	class Meta:
		model= Trajeto
		fields= ['rota',]

		error_mensagens ={
			'rota' :{
				'required':'Este campo é obrigatório'		
			},

		}
	#rota = forms.ModelChoiceField(queryset=Rota.objects.all())




class Residencia_form(forms.Form):
	estadoObject = Estado.objects.all().order_by('pk')
	cidadeObject = Cidade.objects.filter(estado=estadoObject[0])
	bairroObject = Bairro.objects.filter(cidade=cidadeObject[0])
	ruaObject = Rua.objects.filter(bairro=bairroObject[0])
	estado = forms.ChoiceField(choices=[(x.sigla, x.nome) for x in estadoObject])
	cidade = forms.ChoiceField(choices=[(x.pk, x.nome) for x in cidadeObject])
	bairro = forms.ChoiceField(choices=[(x.pk, x.nome) for x in bairroObject])
	rua = forms.ChoiceField(choices=[(x.pk, x.nome) for x in ruaObject])
	responsavel = forms.CharField()
	numero_casa = forms.IntegerField()


class Visita_form(forms.ModelForm):
	class Meta:
		model = Visita
		fields = ('codigo_visita',)



class Prancheta_form(forms.ModelForm):
	class Meta:
		model = Prancheta
		fields = ('tipo_imovel','imoveis_trabalhados','focos',
			'tratamento_larvicida', 'observacao')

		error_mensagens = {
			'tipo_imovel': {
				'required': 'Este campo é obrigatório'
			},

			'imoveis_trabalhados': {
				'required': 'Este campo é obrigatório'
			},

			'focos': {
				'required': 'Este campo é obrigatório'
			},

			'tratamento_larvicida': {
				'required': 'Este campo é obrigatório'
			},

		}


class Justificar_visita_form(forms.ModelForm):
	class Meta:

		model = Justificar_visita
		fields = ('imoveis_fechados','imoveis_recusados','observacao')

		error_mensagens = {
			'imoveis_fechados': {
				'required': 'Este campo é obrigatório'
			},

			'imoveis_recusados': {
				'required': 'Este campo é obrigatório'
			},
			'observacao': {
				'required': 'Este campo é obrigatório'
			},
		}

	estadoObject = Estado.objects.all().order_by('pk')
	cidadeObject = Cidade.objects.filter(estado=estadoObject[0])
	bairroObject = Bairro.objects.filter(cidade=cidadeObject[0])
	ruaObject = Rua.objects.filter(bairro=bairroObject[0])
	residenciasObjects = Residencia.objects.filter(rua=ruaObject[0])
	estado = forms.ChoiceField(choices=[(x.sigla, x.nome) for x in estadoObject])
	cidade = forms.ChoiceField(choices=[(x.pk, x.nome) for x in cidadeObject])
	bairro = forms.ChoiceField(choices=[(x.pk, x.nome) for x in bairroObject])
	rua = forms.ChoiceField(choices=[(x.pk, x.nome) for x in ruaObject])
	casas = forms.ChoiceField(choices=[(x.pk, x.numero_casa) for x in residenciasObjects])

class Grafico_form(forms.Form):
	cidadeObject = Cidade.objects.all()
	cidade = forms.ChoiceField(choices=[(x.pk, x.nome) for x in cidadeObject])
	


