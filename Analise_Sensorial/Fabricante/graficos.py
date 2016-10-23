from django.shortcuts import render
from Fabricante.forms import *
from Fabricante.models import *
from Fabricante.views import *
from django.template.context_processors import request
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#O ID da analise é requerido
def graficoTeste(request, id):
    #Pegando os testes daquela análise

    masculino = 0
    feminino = 0
    testes = Teste.objects.filter(analise = id)
    for teste in testes:
        if teste.provador:
            if teste.provador.sexo == "1":
                masculino +=1
            else:
                feminino += 1


    data = ((masculino, feminino), ('r', '#00FF33'), ('Masculino', 'Feminino'))
    xPositions = np.arange(len(data[0]))
    barWidth = 0.50  # Largura da barra

    _ax = plt.axes()  # Cria axes

    # bar(left, height, width=0.8, bottom=None, hold=None, **kwargs)
    _chartBars = plt.bar(xPositions, data[0], barWidth, color=data[1],
                         yerr=5, align='center')  # Gera barras

    for bars in _chartBars:
        # text(x, y, s, fontdict=None, withdash=False, **kwargs)
        _ax.text(bars.get_x() + (bars.get_width() / 2.0), bars.get_height() + 5,
                 bars.get_height(), ha='center')  # Label acima das barras

    _ax.set_xticks(xPositions)
    _ax.set_xticklabels(data[2])

    plt.xlabel('Sexo')
    plt.ylabel('Quantidade')
    plt.grid(True)
    plt.legend(_chartBars, data[2])

    canvas = FigureCanvas(plt.figure(1))
    response =  HttpResponse(content_type="image/png")
    canvas.print_png(response)
    return response

"""Esse método será utilizado para calcular a idade, pode ser utilizado
aqui, nos gráficos, como também para verificar se a análise sensorial é
para pessoas maiores de 18 anos"""
def calculaIdade(birthday):
    today = date.today()
    y = today.year - birthday.year
    if today.month < birthday.month or today.month == birthday.month and today.day < birthday.day:
        y -= 1
    return y

def graficoIdade(request, id):
    zeroDoze = 0
    trezeVinte = 0
    vinteUmTrinta = 0
    trintaUmQuarenta = 0
    quarentaUmCinquenta =0
    cinquentaSessenta = 0
    maisSessenta = 0

    #Verifica as idades válidas
    valido = True
    testes = Teste.objects.filter(analise = id)
    for teste in testes:
        if teste.provador is not None:
            idade = calculaIdade(teste.provador.data_nascimento)
            if idade > 0:
                if idade >= 0 and idade <= 12:
                    zeroDoze +=1
                elif idade > 12 and idade <= 20:
                    trezeVinte +=1
                elif idade > 20 and idade <= 30:
                    vinteUmTrinta +=1
                elif idade > 30 and idade <= 40:
                    trintaUmQuarenta += 1
                elif idade > 40 and idade <= 50:
                    quarentaUmCinquenta += 1
                elif idade > 50 and idade <= 60:
                    cinquentaSessenta += 1
                elif idade > 60:
                    maisSessenta += 1
            else:
                valido = False


    labels = '0 a 12 anos','13 a 20 anos','21 a 30 anos','31 a 40 anos', '41 a 50 anos', '51 a 60 anos','60 > anos'
    fracs=[zeroDoze, trezeVinte, vinteUmTrinta, trintaUmQuarenta,
        quarentaUmCinquenta, cinquentaSessenta, maisSessenta]
    explode = (0,0,0,0,0,0,0)
    pie = plt.pie(fracs, explode=explode, labels=labels, shadow=True, autopct='%1.1f%%',startangle=90)
    plt.legend(pie[0], labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    canvas = FigureCanvas(plt.figure(1))
    response =  HttpResponse(content_type="image/png")
    canvas.print_png(response)
    return response

def graficoPerguntasBolleanas(request, id):
    respostasBooleanas = Boolean.objects.filter(analise = id)
    sim = 0
    nao = 0
    for i in respostasBooleanas:
        if i.tipo=="PSN":
            if i.resposta == True:
                sim +=1
            else:
                nao += 1
    data = ((nao, sim), ('r', '#00FF33'), ('Não', 'Sim'))
    xPositions = np.arange(len(data[0]))
    barWidth = 0.50  # Largura da barra

    _ax = plt.axes()  # Cria axes

    # bar(left, height, width=0.8, bottom=None, hold=None, **kwargs)
    _chartBars = plt.bar(xPositions, data[0], barWidth, color=data[1],
                         yerr=5, align='center')  # Gera barras

    for bars in _chartBars:
        # text(x, y, s, fontdict=None, withdash=False, **kwargs)
        _ax.text(bars.get_x() + (bars.get_width() / 2.0), bars.get_height() + 5,
                 bars.get_height(), ha='center')  # Label acima das barras

    _ax.set_xticks(xPositions)
    _ax.set_xticklabels(data[2])

    plt.xlabel('Resposta')
    #plt.ylabel('Quantidade')
    plt.grid(True)
    plt.legend(_chartBars, data[2])

    canvas = FigureCanvas(plt.figure(1))
    response =  HttpResponse(content_type="image/png")
    canvas.print_png(response)
    return response

def graficoHedonica(request, id):
    respostasHedonicas = Hedonica.objects.filter(analise = id)
    desgosteiExtremamente = 0
    desgosteiMuito = 0
    desgosteiModeradamente = 0
    desgosteiLigeiramente = 0
    neutro = 0
    gosteiLigeiramente = 0
    gosteiModeradamente = 0
    gosteiMuito = 0
    gosteiExtremamente = 0
    contadorProvador = 0
    testes = Teste.objects.filter(analise = id)
    for teste in testes:
        if teste.provador is not None:
            contadorProvador += 1
    
    
    for i in respostasHedonicas:
        if i.tipo=="PHD":
            if i.resposta == 1:
                desgosteiExtremamente +=1
            elif i.resposta == 2:
                desgosteiMuito += 2
            elif i.resposta == 3:
                desgosteiModeradamente += 3
            elif i.resposta == 4:
                desgosteiLigeiramente += 4
            elif i.resposta == 5:
                neutro += 5
            elif i.resposta == 6:
                gosteiLigeiramente += 6
            elif i.resposta == 7:
                gosteiModeradamente += 7
            elif i.resposta == 8:
                gosteiMuito += 8
            elif i.resposta == 9:
                gosteiExtremamente += 9
    aceitacao = []
    aceitacao.append((desgosteiExtremamente + desgosteiMuito + desgosteiModeradamente+ desgosteiLigeiramente+
               neutro+ gosteiLigeiramente+ gosteiModeradamente+ gosteiMuito + gosteiExtremamente)/contadorProvador)
    cor = ('r')
        
    data = (aceitacao, cor, "Aceitação")
    barWidth = 0.50  # Largura da barra

    _ax = plt.axes()  # Cria axes

    # bar(left, height, width=0.8, bottom=None, hold=None, **kwargs)
    _chartBars = plt.bar(aceitacao, data[0], barWidth, color=data[1],
                         yerr=5, align='center')  # Gera barras

    for bars in _chartBars:
        # text(x, y, s, fontdict=None, withdash=False, **kwargs)
        _ax.text(bars.get_x() + (bars.get_width() / 2.0), bars.get_height() + 5,
                 bars.get_height(), ha='center')  # Label acima das barras

    _ax.set_xticks(aceitacao)
    _ax.set_xticklabels(data[2])

    #plt.xlabel('Sexo')
    plt.ylabel('Aceitação Hedonica')
    plt.grid(True)
    

    canvas = FigureCanvas(plt.figure(1))
    response =  HttpResponse(content_type="image/png")
    canvas.print_png(response)
    return response

def graficoIntencaoCompra(request, id):
    respostasIntencao = IntencaoCompra.objects.filter(analise = id)
    testes = Teste.objects.filter(analise = id)
    certamenteNao = 0
    possivelmenteNao = 0
    talvez = 0
    certamenteSim = 0
    possivelmenteSim = 0
    contadorProvador = 0
    for teste in testes:
        if teste.provador is not None:
            contadorProvador += 1
    
    for i in respostasIntencao:
        if i.tipo=="PIC":
            if i.resposta == 1:
                certamenteNao +=1
            elif i.resposta == 2:
                possivelmenteNao +=1
            elif i.resposta == 3:
                talvez += 1
            elif i.resposta == 4:
                possivelmenteSim += 1
            elif i.resposta == 5:
                certamenteSim += 1
                
    context = (certamenteNao, possivelmenteNao,talvez, possivelmenteSim, certamenteSim)
    cor = ('#ff00cb','#873c43','#643c87', '#3c8784','#f4f4f4')
    label = ('Certamente Não', 'Possivelmente Não', 'Talvez', 'Possivelmente Sim', 'Certamente Sim')
        
    data = (context, cor, label)
    
    xPositions = np.arange(len(data[0]))
    barWidth = 0.50  # Largura da barra

    _ax = plt.axes()  # Cria axes

    # bar(left, height, width=0.8, bottom=None, hold=None, **kwargs)
    _chartBars = plt.bar(xPositions, data[0], barWidth, color=data[1],
                         yerr=5, align='center')  # Gera barras

    for bars in _chartBars:
        # text(x, y, s, fontdict=None, withdash=False, **kwargs)
        _ax.text(bars.get_x() + (bars.get_width() / 2.0), bars.get_height() + 5,
                 bars.get_height(), ha='center')  # Label acima das barras

    _ax.set_xticks(xPositions)
    _ax.set_xticklabels(data[2])

    #plt.xlabel('Sexo')
    plt.ylabel('Intenção de Compra')
    plt.grid(True)
    plt.legend(_chartBars, data[2])

    canvas = FigureCanvas(plt.figure(1))
    response =  HttpResponse(content_type="image/png")
    canvas.print_png(response)
    return response
