from django.shortcuts import render
from django.http import JsonResponse
from openpyxl import load_workbook
from .models import Pessoa
from datetime import datetime
from django.http import HttpResponse
from openpyxl import Workbook


def index(request):
    return render(request, 'index.html')


def upload_planilha(request):
    if request.method == 'POST' and request.FILES['file']:
        arquivo = request.FILES['file']
        workbook = load_workbook(arquivo)
        sheet = workbook.active

        #Processo de leitura do excel
        pessoas_ativas = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            nome, email, data_nascimento, ativo = row

            # Verifica se data_nascimento é um objeto datetime, se não, converte a string
            if isinstance(data_nascimento, str):
                data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
            elif isinstance(data_nascimento, datetime):
                data_nascimento = data_nascimento.date()

            idade = (datetime.now().date() - data_nascimento).days // 365

            #Validação de idade e idade perante valor
            if idade < 18:
                ativo = False

            if ativo:
                if idade < 21:
                    valor = 100.00
                elif idade < 60:
                    valor = 150.00
                else:
                    valor = 200.00

                pessoa = Pessoa.objects.create(
                    nome=nome,
                    email=email,
                    data_nascimento=data_nascimento,
                    ativo=True,
                    valor=valor
                )

                pessoas_ativas.append({
                    "nome": nome,
                    "email": email,
                    "data_nascimento": data_nascimento,
                    "ativo": ativo,
                    "valor": valor
                })

        return JsonResponse(pessoas_ativas, safe=False)


def download_planilha(request):
    pessoas = Pessoa.objects.filter(ativo=True)
    workbook = Workbook()
    sheet = workbook.active

    # Cabeçalho
    sheet.append(["Nome", "Email", "Data de Nascimento", "Ativo", "Valor"])

    # Dados
    for pessoa in pessoas:
        sheet.append([
            pessoa.nome,
            pessoa.email,
            pessoa.data_nascimento,
            pessoa.ativo,
            pessoa.valor
        ])

    # Resposta HTTP
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=pessoas_ativas.xlsx'
    workbook.save(response)
    return response
