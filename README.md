# 📊 Dashboard de People Analytics - Power BI

![Dashboard Preview](./images/dashboard_preview.png)

## 📌 Visão Geral
Dashboard interativo para análise estratégica de RH, desenvolvido em Power BI, que monitora:

- **Indicadores-chave**: Turnover, headcount, absenteísmo
- **Diversidade**: Gênero, tempo de empresa, distribuição geográfica
- **Custos**: Impacto financeiro da rotatividade

## 🔍 Principais Insights
- Taxa de turnover anual: 25%
- Departamento crítico: Financeiro (26.56% de rotatividade)
- Principal motivo de saída: Aposentadoria (25% dos casos)
- Correlação entre faltas e pedidos de demissão

## 🛠️ Tecnologias Utilizadas
- **Power BI** (DAX, Power Query, Modelagem de Dados)
- **Visualizações Interativas**:
  - Mapas de calor departamentais
  - Linha do tempo de contratações
  - Gráficos de dispersão com correlações

## ⚙️ Medidas DAX Destacadas

```dax
// Cálculo preciso de turnover
Turnover = 
VAR Desligamentos = COUNTROWS(FILTER('Colaboradores', NOT(ISBLANK([Data de Saída])))
VAR MediaColaboradores = ([Headcount Inicial] + [Headcount Final])/2
RETURN DIVIDE(Desligamentos, MediaColaboradores, 0)

// Headcount com contexto temporal
Headcount Acumulado = 
COUNTROWS(
    FILTER('Colaboradores',
        [Data de Admissão] <= SELECTEDVALUE('Calendario'[Data]) &&
        (ISBLANK([Data de Saída]) || [Data de Saída] > SELECTEDVALUE('Calendario'[Data]))
    )
)
