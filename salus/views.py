from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core import serializers
from django.db.models import Count
from .models import Residencia, Estado, Cidade, Bairro, Rua, Visita, Trajeto, Prancheta
from django.contrib import messages



from django.contrib import messages
from django.contrib.auth import authenticate, login



#EU, LUCAS, DEVO FAZER AS CONDICIONAIS DE RENDERIZAÇÃO DE PÁGINA PARA CADA TIPO DE USUÁRIO
@login_required
@csrf_protect
def usuario(request):
    if request.user.is_superuser or request.user.groups.filter(name='Supervisor').exists() : #Se o usuário for o superuser 0 , responsável por criar o primeiro gerente,ou for um gerente, então o site será renderizado na página de cadastro
        if request.method =='POST':
            usuario = forms.User_form(request.POST)
            usuario_extra =forms.Trajeto_form(request.POST)
            if usuario.is_valid() and usuario_extra.is_valid() : #O cadastro aqui é direto, pois o usuário só é válido quando todas as informações são preenchidas
                usuario.save(commit=False)
                u= usuario.cleaned_data['username'] #Salvando o atributo username(equivalente a cpf) na variável 'u'
                usuario.save()
                us= User.objects.get(username = u) #'Pegando' todos os usuários pelo seu cpf
                my_group = Group.objects.get(name='Agente') #Pegando o grupo 'Agente'
                my_group.user_set.add(us) #Inserindo o grupo 'Agente' na variável us, que representa todos os usuários
                extra = usuario_extra.save(commit=False)
                extra.user = us #a informãção extra está sendo vinculada ao cpf foi cadastrado, mais especificamente, extra.user irá referenciar o usuário que tomará as informações preenchidas no extra
                extra.save() #impede o envio automático pra o banco de dados, pois a informação extra ainda n foi preenchida
                return redirect('listar_usuarios')
        else: # se o método n for post
            usuario = forms.User_form()
            usuario_extra =forms.Trajeto_form()
        return render(request, 'salus/cadastroUsuario.html', {'formUser': usuario, 'formTrajeto': usuario_extra}) #

    else:
        return redirect('main') #O parâmetro será o nome da página principal, no caso, o menu de início







@login_required
@csrf_protect
def prancheta(request, id_visita):
    if request.user.is_superuser or request.user.groups.filter(name='Agente').exists():
        visita= Residencia.objects.get(id=id_visita)
        if request.method == 'POST':
            prancheta = forms.Prancheta_form(request.POST)
            if prancheta.is_valid():
                p = prancheta.save(commit=False)
                p.dados_da_visita = visita
                print(p)
                print("\n\n\n\n\n")
                p.save()
                return redirect('main')
        else:
            prancheta = forms.Prancheta_form()
        return render(request, 'salus/pranchetaVisita.html',{'formprancheta': prancheta, 'visitation': visita })
    else:
        return redirect('main')


@login_required
@csrf_protect
def residencia(request):
    if request.user.is_superuser or request.user.groups.filter(name='Supervisor').exists() :
        if request.method =='POST':
            residencia = forms.Residencia_form(request.POST)
            residencia.fields['cidade'].choices = [(x.pk, x.nome) for x in Cidade.objects.all()]
            residencia.fields['bairro'].choices = [(x.pk, x.nome) for x in Bairro.objects.all()]
            residencia.fields['rua'].choices = [(x.pk, x.nome) for x in Rua.objects.all()]
            if residencia.is_valid():
                res = Residencia()
                res.responsavel = residencia.cleaned_data.get('responsavel')
                res.numero_casa = residencia.cleaned_data.get('numero_casa')
                res.cidade = Cidade.objects.get(pk=int(residencia.cleaned_data.get('cidade')))
                res.bairro = Bairro.objects.get(pk=int(residencia.cleaned_data.get('bairro')))
                res.rua = Rua.objects.get(pk=int(residencia.cleaned_data.get('rua')))
                res.save()
                return redirect('main')
        else:
            residencia = forms.Residencia_form()
        return render(request, 'salus/cadastrarresidencia.html', {'formresidencia': residencia})
    else:
        return redirect('main')


@login_required
@csrf_protect
def visita(request):
    if request.user.is_superuser or request.user.groups.filter(name='Agente').exists():
        if request.method == 'POST':
            visita = forms.Visita_form(request.POST)
            visitation= int(request.POST.get('codigo_visita'))
            if visita.is_valid():
                v = visita.save(commit=False)
                v.agente_da_visita = request.user
                print(request.user)
                casa = visita.cleaned_data['codigo_visita']
                v.residencia_da_visita = Residencia.objects.get(id=casa)
                #my_group = Group.objects.get(name='Agente')  DEVO REFERENCIAR O AGENTE QUE ESTÁ EM LOGIN
                visita.save()
                return redirect('prancheta_visita/%d' %visitation)
        else:
            # visita = forms.Visita_form()
            # return render(request, 'salus/inicialAgente.html', {'formvisita': visita})
            return redirect('main')
    else:
        return redirect('main')


@login_required
@csrf_protect
def justificar_visita(request):
    if request.user.is_superuser or request.user.groups.filter(name='Agente').exists():
        if request.method == 'POST':
            justificar_visita = forms.Justificar_visita_form(request.POST)
            if justificar_visita.is_valid():
                a = justificar_visita.save(commit=False)
                a.estado = str(request.POST.get('estado'))
                city = int(request.POST.get('cidade'))
                a.cidade = Cidade.objects.get(id=city).nome
                bairro_ = int(request.POST.get('bairro'))
                a.bairro = Bairro.objects.get(id=bairro_).nome
                street = int(request.POST.get('rua'))
                a.rua = Rua.objects.get(id=street).nome
                a.agente= request.user
                print(a)
                a.save()
                return HttpResponse('ok')
            else:
                return HttpResponse('Deu errado')
        else:
            justificar_visita = forms.Justificar_visita_form()
            return render(request, 'salus/justificar_visita.html', {'formjustificar_visita':justificar_visita})
    else:
        return redirect('main')



@login_required
@csrf_protect
def main(request):
    #iNTERFACE DO SUPERVISOR
    if request.user.groups.filter(name='Supervisor').exists():
        if request.method == 'POST':
            grafico = forms.Grafico_form(request.POST)
            cidade = request.POST.get('cidade')
            city = Cidade.objects.get(id=int(cidade))
            city = city.nome
            if grafico.is_valid():
                return redirect('graficos/%s' %city)
            else:
                return HttpResponse('DEU ERRO')
        else:
            grafico = forms.Grafico_form()
            return render(request, 'salus/inicialChefe.html',{'graph':grafico})
    
    #INTERFACE PRINCIPAL DO AGENTE
    if request.user.groups.filter(name='Agente').exists():
        if request.method == 'POST':
            if request.POST.get('cidade'):
                grafico = forms.Grafico_form(request.POST)
                cidade = request.POST.get('cidade')
                city = Cidade.objects.get(id=int(cidade))
                city = city.nome
                if grafico.is_valid():
                    return redirect('graficos/%s' %city)
                else:
                    return HttpResponse('DEU ERRO')
            elif request.POST.get('codigo_visita'):
                visita = forms.Visita_form(request.POST)
                visitation= int(request.POST.get('codigo_visita'))
                if visita.is_valid():
                    v = visita.save(commit=False)
                    v.agente_da_visita = request.user
                    casa = visita.cleaned_data['codigo_visita']
                    try:
                        v.residencia_da_visita = Residencia.objects.get(id=casa)
                    except:
                        messages.error(request, 'Residência inválida!')
                        return redirect('main')
                    #my_group = Group.objects.get(name='Agente')  DEVO REFERENCIAR O AGENTE QUE ESTÁ EM LOGIN
                    visita.save()
                    return redirect('prancheta_visita/%d' %visitation)
            else:
                return redirect('main')
        grafico = forms.Grafico_form()
        return render(request, 'salus/inicialAgente.html', {'graph':grafico})
    return HttpResponse('erro')


@login_required
@csrf_protect
def listar_usuarios(request):
    valor=User.objects.all()
    return render(request, 'salus/listar_agentes.html',{'user': valor})

@login_required
@csrf_protect
def listar_rota(request):
    trabalho=Trajeto.objects.filter(user=request.user)
    return render(request, 'salus/listar_rota.html',{'horario': trabalho})

@login_required
@csrf_protect
def apagar(request, id):
    pegar = User.objects.get(id = id)
    pegar.delete()
    return redirect('listar_usuarios')


@login_required
@csrf_protect
def editar(request, usuario):
    guardar=User.objects.get(username=usuario)
    if request.user.is_superuser or request.user.groups.filter(name='Supervisor').exists() : #Se o usuário for o superuser 0 , responsável por criar o primeiro gerente,ou for um gerente, então o site será renderizado na página de cadastro
        if request.method =='POST':
            usuario = forms.User_form(request.POST, instance=guardar)
            usuario_extra = forms.Trajeto_form(request.POST, instance=guardar)
            #usuario_extra =forms.Extra_form(request.POST)
            if usuario.is_valid() : #O cadastro aqui é direto, pois o usuário só é válido quando todas as informações são preenchidas
                u= usuario.cleaned_data['username']
                us = usuario.save(commit=False)
                us.username = u
                us.first_name = usuario.cleaned_data['first_name']
                us.email = usuario.cleaned_data['email']
                us.save()
                user=User.objects.get(username = u)
                my_group = Group.objects.get(name='Agente')
                my_group.user_set.add(user)
                extra = usuario_extra.save(commit=False)
                extra.user = user #a informãção extra está sendo vinculada ao cpf foi cadastrado, mais especificamente, extra.user irá referenciar o usuário que tomará as informações preenchidas no extra
                extra.save()
                return redirect('listar_usuarios')        

        else: # se o método n for post
            usuario = forms.User_form(instance=guardar)
            extra_form = forms.Trajeto_form(instance=guardar)
            return render(request, 'salus/cadastroUsuario.html', {'formUser': usuario, 'formTrajeto': extra_form}) #

    else:
        return redirect('main') #O parâmetro será o nome da página principal, no caso, o menu de início
    return redirect('listar_usuarios')

@login_required
@csrf_exempt
def ajax_cidades(request, estado_id):
    cidades = Cidade.objects.filter(estado=Estado.objects.get(sigla=estado_id)).values('pk', 'nome')

    return JsonResponse(list(cidades), safe=False)

@login_required
@csrf_exempt
def ajax_bairros(request, cidade_id):
    bairros = Bairro.objects.filter(cidade=cidade_id).values('pk', 'nome')

    return JsonResponse(list(bairros), safe=False)

def ajax_ruas(request, bairro_id):
    ruas = Rua.objects.filter(bairro=bairro_id).values('pk', 'nome')

    return JsonResponse(list(ruas), safe=False)

def ajax_casas(request, rua_id):
    casas = Residencia.objects.filter(rua=rua_id).values('pk', 'numero_casa')

    return JsonResponse(list(casas), safe=False)

# @login_required
def grafico(request, cidade):
    city = get_object_or_404(Cidade, nome=cidade)
    return render(request, 'salus/grafico.html', {'bairrosLista': Bairro.objects.filter(cidade=city), 'cidade': city.nome,'bairros': Bairro.objects.values('nome').filter(cidade=city, residencia__prancheta__focos='1-Sim').annotate(focos=Count('residencia__prancheta')), 'locais': Prancheta.objects.filter(dados_da_visita__cidade=city, focos='1-Sim').values('tipo_imovel').annotate(focos=Count('focos'))})

# @login_required
def graficoBairro(request, cidade, bairro_id):
    city = get_object_or_404(Cidade, nome=cidade)
    bairro = get_object_or_404(Bairro, cidade=city, pk=bairro_id)

    return render(request, 'salus/graficoBairro.html', {'bairro': bairro, 'bairroLocais': Prancheta.objects.filter(dados_da_visita__bairro = bairro, focos='1-Sim').values('tipo_imovel').annotate(focos=Count('focos'))})


@login_required
@csrf_protect
def inspecionar_trabalho(request, id):
    informacoes = Visita.objects.filter(agente_da_visita=id)
    print("oi")
    print(informacoes)
    return render(request, 'salus/inspecionar.html', {'info': informacoes})

@login_required
@csrf_protect
def inspecionar_justificativa(request, id):
    informacoes = Visita.objects.filter(agente_da_visita=id)
    print("oi")
    print(informacoes)
    return render(request, 'salus/inspecionar.html', {'info': informacoes})










