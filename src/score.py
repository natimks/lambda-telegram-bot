from datetime import datetime


# IDADE: 22
# TEM DIVIDA: SIM (150 reais no dia 04/06/2020)
# CONSULTA NOS ÚLTIMOS 3 MESES: SIM (1)

def calcular(nome, idade):
    score = 1000
    resumo = {
        "nome": nome,
        "score": score,
        "variaveis": {
            'idade': idade,
            'consultado': True,
            'dividas': [
                {
                    'valor_original': 150
                }
            ]
        }
    }

    score = calcular_indicador_idade(idade, score)
    score = calcular_indicador_consulta(score)
    score = calcular_indicador_dividas_atrasos(score, resumo)

    return int(score)


def calcular_indicador_idade(idade, score):
    if idade < 18:
        score = 0
    elif 18 >= idade <= 19:
        score /= 3
    elif 20 >= idade <= 21:
        score /= 2
    elif idade >= 22:
        score /= 1.5
    return score


def calcular_indicador_consulta(score):
    qtd_consultas = 1
    score -= (qtd_consultas * 50)
    return score


def calcular_indicador_dividas_atrasos(score, resumo):
    dividas = resumo['variaveis']['dividas']
    if len(dividas) > 0:
        for divida in dividas:
            data_divida = datetime.strptime('04/06/2020', '%d/%m/%Y').date()
            dias_atraso = (datetime.now().date() - data_divida).days
            valor_divida_atual = divida['valor_original'] + dias_atraso
            divida['dias_atraso'] = dias_atraso
            divida['valor_atual'] = valor_divida_atual
            score -= dias_atraso
    return score


class TestNatalia:

    def test_idade_negativa(self):
        assert calcular_indicador_idade(idade=-1, score=10) == 0

    def test_idade_dezoito_anos(self):
        assert calcular_indicador_idade(idade=18, score=12) == 4

    def test_idade_vinte_anos(self):
        assert calcular_indicador_idade(idade=20, score=10) == 5

    def test_idade_trinta_anos(self):
        assert calcular_indicador_idade(idade=30, score=3) == 2

    def test_calcular_indicador_consulta(self):
        assert calcular_indicador_consulta(score=1000) == 950

    def test_calcular_indicador_dividas_atrasos(self):
        resumo = {
            'variaveis':{
                'dividas': [
                    {
                        'valor_original': 150
                    }
                ]
            }
        }
        assert calcular_indicador_dividas_atrasos(score=1000, resumo=resumo) == 995
