import pandas as pd
import random
from datetime import datetime, timedelta

# Parâmetros básicos
departamentos = ["Tecnologia", "RH", "Financeiro", "Marketing", "Vendas"]
generos = ["Feminino", "Masculino", "Outro"]
motivos_saida = ["Pedido de demissão", "Desligamento", "Fim de contrato", "Transferência", "Aposentadoria", None]
regioes = ["Sudeste", "Sul", "Centro-Oeste", "Nordeste", "Norte"]
data_atual = datetime.now()

# Gerar dados simulados de 100 colaboradores
data = []
for i in range(100):
    nome = f"Colaborador {i+1}"
    genero = random.choice(generos)
    departamento = random.choice(departamentos)
    regiao = random.choice(regioes)
    
    # Data de admissão entre 1/1/2020 e data atual
    data_admissao = datetime(2020, 1, 1) + timedelta(days=random.randint(0, (data_atual - datetime(2020, 1, 1)).days))
    
    # 40% de chance de ter data de saída
    if random.random() < 0.4:
        dias_pos_admissao = (data_atual - data_admissao).days
        
        # Garante que há pelo menos 30 dias entre admissão e saída
        if dias_pos_admissao >= 30:
            data_saida = data_admissao + timedelta(days=random.randint(30, dias_pos_admissao))
            motivo_saida = random.choice([m for m in motivos_saida if m is not None])
        else:
            # Se não houver 30 dias disponíveis, não gera saída
            data_saida = None
            motivo_saida = None
    else:
        data_saida = None
        motivo_saida = None
    
    faltas = random.randint(0, 12) if random.random() < 0.7 else 0

    data.append([
        nome,
        genero,
        departamento,
        regiao,
        data_admissao.strftime('%d/%m/%Y'),
        data_saida.strftime('%d/%m/%Y') if data_saida else "",
        motivo_saida if motivo_saida else "",
        faltas
    ])

# Criar DataFrame
df = pd.DataFrame(data, columns=[
    "Nome", "Gênero", "Departamento", "Região",
    "Data de Admissão", "Data de Saída", "Motivo da Saída", "Faltas"
])

# Salvar como Excel
file_path = r"indicadores_rh.xlsx"
df.to_excel(file_path, index=False)

print(f"Arquivo gerado com sucesso: {file_path}")