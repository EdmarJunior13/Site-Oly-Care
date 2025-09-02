#!/usr/bin/env python3
"""
Cálculo de ROI e Métricas Financeiras - OLY Care
Análise detalhada dos investimentos e retornos esperados
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class ROICalculatorOlyCare:
    def __init__(self):
        # Investimentos Iniciais (em R$)
        self.investimentos = {
            'ferramentas_equipamentos': 45000,  # Equipamentos especializados
            'veiculos': 85000,                  # Van equipada + equipamentos móveis
            'mao_obra_inicial': 36000,          # 6 meses de salários iniciais
            'treinamento_capacitacao': 12000,   # Treinamento da equipe
            'marketing_lancamento': 15000,      # Marketing inicial
            'capital_giro': 25000,              # Capital de giro inicial
            'licencas_seguros': 8000,           # Licenças e seguros
            'outros': 5000                      # Outros custos
        }
        
        # Custos Operacionais Mensais (em R$)
        self.custos_mensais = {
            'salarios_encargos': 18000,         # 6 colaboradores
            'combustivel_manutencao': 3500,     # Veículos
            'materiais_produtos': 2800,         # Produtos de limpeza/manutenção
            'seguros_licencas': 800,            # Seguros mensais
            'marketing_digital': 2000,          # Marketing contínuo
            'administrativo': 1200,             # Custos administrativos
            'outros_operacionais': 800          # Outros custos
        }
        
        # Projeções de Receita
        self.projecoes_receita = {
            2025: {'atendimentos': 150, 'ticket_medio': 400},
            2026: {'atendimentos': 300, 'ticket_medio': 420},
            2027: {'atendimentos': 450, 'ticket_medio': 450}
        }
    
    def calcular_investimento_total(self):
        """Calcula o investimento total inicial"""
        return sum(self.investimentos.values())
    
    def calcular_custos_anuais(self, ano):
        """Calcula custos operacionais anuais"""
        custos_mensais_total = sum(self.custos_mensais.values())
        
        # Ajuste de inflação (5% ao ano)
        anos_desde_2025 = ano - 2025
        fator_inflacao = (1.05) ** anos_desde_2025
        
        return custos_mensais_total * 12 * fator_inflacao
    
    def calcular_receita_anual(self, ano):
        """Calcula receita anual baseada nas projeções"""
        if ano in self.projecoes_receita:
            dados = self.projecoes_receita[ano]
            return dados['atendimentos'] * dados['ticket_medio'] * 12
        return 0
    
    def calcular_roi_periodo(self, anos=3):
        """Calcula ROI para um período específico"""
        investimento_inicial = self.calcular_investimento_total()
        
        resultados = []
        lucro_acumulado = 0
        
        for ano in range(2025, 2025 + anos):
            receita = self.calcular_receita_anual(ano)
            custos = self.calcular_custos_anuais(ano)
            lucro_anual = receita - custos
            lucro_acumulado += lucro_anual
            
            # ROI acumulado
            roi_acumulado = (lucro_acumulado / investimento_inicial) * 100
            
            resultados.append({
                'ano': ano,
                'receita': receita,
                'custos': custos,
                'lucro_anual': lucro_anual,
                'lucro_acumulado': lucro_acumulado,
                'roi_acumulado': roi_acumulado
            })
        
        return resultados
    
    def calcular_payback(self):
        """Calcula o período de payback"""
        investimento_inicial = self.calcular_investimento_total()
        lucro_acumulado = 0
        
        for mes in range(1, 37):  # 3 anos = 36 meses
            ano = 2025 + (mes - 1) // 12
            receita_mensal = self.calcular_receita_anual(ano) / 12
            custos_mensais = self.calcular_custos_anuais(ano) / 12
            lucro_mensal = receita_mensal - custos_mensais
            lucro_acumulado += lucro_mensal
            
            if lucro_acumulado >= investimento_inicial:
                return mes
        
        return None  # Payback não atingido em 3 anos
    
    def gerar_relatorio_completo(self):
        """Gera relatório completo de ROI e métricas"""
        investimento_total = self.calcular_investimento_total()
        resultados_roi = self.calcular_roi_periodo(3)
        payback_meses = self.calcular_payback()
        
        relatorio = f"""
# RELATÓRIO DE ROI E MÉTRICAS FINANCEIRAS - OLY CARE

## 1. INVESTIMENTO INICIAL

### Detalhamento dos Investimentos:
"""
        
        for item, valor in self.investimentos.items():
            relatorio += f"- {item.replace('_', ' ').title()}: R$ {valor:,.2f}\n"
        
        relatorio += f"\n**TOTAL INVESTIMENTO INICIAL: R$ {investimento_total:,.2f}**\n\n"
        
        relatorio += """
## 2. CUSTOS OPERACIONAIS MENSAIS

### Detalhamento dos Custos:
"""
        
        for item, valor in self.custos_mensais.items():
            relatorio += f"- {item.replace('_', ' ').title()}: R$ {valor:,.2f}\n"
        
        total_custos_mensais = sum(self.custos_mensais.values())
        relatorio += f"\n**TOTAL CUSTOS MENSAIS: R$ {total_custos_mensais:,.2f}**\n\n"
        
        relatorio += """
## 3. PROJEÇÕES FINANCEIRAS (2025-2027)

| Ano  | Receita Anual | Custos Anuais | Lucro Anual | Lucro Acumulado | ROI Acumulado |
|------|---------------|---------------|-------------|-----------------|---------------|
"""
        
        for resultado in resultados_roi:
            relatorio += f"| {resultado['ano']} | R$ {resultado['receita']:,.0f} | R$ {resultado['custos']:,.0f} | R$ {resultado['lucro_anual']:,.0f} | R$ {resultado['lucro_acumulado']:,.0f} | {resultado['roi_acumulado']:.1f}% |\n"
        
        relatorio += f"""

## 4. MÉTRICAS PRINCIPAIS

### 4.1. Período de Payback
"""
        
        if payback_meses:
            anos = payback_meses // 12
            meses = payback_meses % 12
            relatorio += f"**{payback_meses} meses** ({anos} anos e {meses} meses)\n"
        else:
            relatorio += "**Payback não atingido em 3 anos**\n"
        
        roi_final = resultados_roi[-1]['roi_acumulado']
        relatorio += f"""
### 4.2. ROI Final (3 anos)
**{roi_final:.1f}%**

### 4.3. Margem de Contribuição Média
**58%** (conforme projeção inicial)

### 4.4. EBITDA Projetado 2027
**34%** (conforme planejamento estratégico)

## 5. ANÁLISE DE VIABILIDADE

### 5.1. Pontos Positivos:
- ROI atrativo em 3 anos
- Payback em período razoável
- Sinergia com empresas existentes do grupo
- Mercado em crescimento para serviços premium

### 5.2. Riscos Identificados:
- Dependência da base de clientes da OLY Planejados
- Concorrência no mercado de assistência técnica
- Necessidade de manutenção da qualidade dos serviços

### 5.3. Recomendações:
- Monitorar mensalmente as métricas de performance
- Investir em treinamento contínuo da equipe
- Desenvolver parcerias estratégicas com arquitetos
- Implementar sistema de CRM para controle de clientes

## 6. MÉTRICAS DE ACOMPANHAMENTO

### 6.1. Métricas Operacionais:
- Número de atendimentos mensais
- Ticket médio por atendimento
- Taxa de conversão de leads
- Índice de satisfação do cliente (NPS)
- Tempo médio de atendimento

### 6.2. Métricas Financeiras:
- Receita mensal
- Margem de contribuição
- Custos operacionais
- EBITDA mensal
- Fluxo de caixa

### 6.3. Métricas de Qualidade:
- Taxa de retrabalho
- Tempo de resolução de problemas
- Avaliação dos clientes
- Taxa de indicação de novos clientes
"""
        
        return relatorio

# Executar cálculos
if __name__ == "__main__":
    calculator = ROICalculatorOlyCare()
    relatorio = calculator.gerar_relatorio_completo()
    
    # Salvar relatório
    with open('/home/ubuntu/oly-planejamento-site/relatorio_roi_oly_care.md', 'w', encoding='utf-8') as f:
        f.write(relatorio)
    
    print("Relatório de ROI gerado com sucesso!")
    print(f"Investimento Total: R$ {calculator.calcular_investimento_total():,.2f}")
    print(f"Payback: {calculator.calcular_payback()} meses")
    
    resultados = calculator.calcular_roi_periodo(3)
    print(f"ROI 3 anos: {resultados[-1]['roi_acumulado']:.1f}%")

