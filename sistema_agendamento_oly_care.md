# Sistema de Agendamento - OLY Care

## 1. Visão Geral

O sistema de agendamento da OLY Care deve ser prático, eficiente e integrado com a disponibilidade dos técnicos, permitindo que os clientes agendem serviços de assistência técnica de forma simples e rápida.

## 2. Ferramenta Sugerida: Calendly (Inspirado na Alfa)

### 2.1. Por que Calendly?
- **Interface intuitiva**: Fácil de usar tanto para clientes quanto para técnicos
- **Integração com calendários**: Google Calendar, Outlook, etc.
- **Disponibilidade em tempo real**: Evita conflitos de horários
- **Notificações automáticas**: Lembretes por email e SMS
- **Personalização**: Pode ser customizado com a identidade visual da OLY

### 2.2. Alternativas Consideradas
- **Acuity Scheduling**: Mais recursos, mas interface mais complexa
- **Setmore**: Gratuito, mas limitações na versão free
- **Agendor**: Nacional, mas foco em vendas, não agendamentos

## 3. Implementação Prática

### 3.1. Configuração Inicial

#### Tipos de Serviços Disponíveis:
1. **Manutenção Preventiva** (2h) - R$ 350
2. **Ajuste de Portas e Gavetas** (1h) - R$ 180
3. **Limpeza Especializada** (3h) - R$ 450
4. **Pequenos Reparos** (1.5h) - R$ 280
5. **Impermeabilização** (4h) - R$ 600
6. **Avaliação Técnica** (1h) - R$ 150

#### Horários de Funcionamento:
- **Segunda a Sexta**: 8h às 18h
- **Sábado**: 8h às 14h
- **Domingo**: Fechado

### 3.2. Integração com Disponibilidade dos Técnicos

#### Equipe Técnica (6 colaboradores):
1. **João Silva** - Técnico Sênior (Especialista em móveis planejados)
2. **Maria Santos** - Técnica Especializada (Limpeza e impermeabilização)
3. **Carlos Oliveira** - Técnico Geral (Ajustes e pequenos reparos)
4. **Ana Costa** - Técnica de Qualidade (Avaliações e inspeções)
5. **Pedro Lima** - Técnico Móvel (Atendimento domiciliar)
6. **Lucia Ferreira** - Coordenadora Técnica (Supervisão e casos complexos)

#### Distribuição de Horários:
- **Manhã (8h-12h)**: 3 técnicos disponíveis
- **Tarde (13h-18h)**: 3 técnicos disponíveis
- **Sábado (8h-14h)**: 2 técnicos disponíveis

### 3.3. Fluxo de Agendamento

```
1. Cliente acessa o site da OLY Care
   ↓
2. Clica em "Agendar Serviço"
   ↓
3. Seleciona o tipo de serviço
   ↓
4. Escolhe data e horário disponível
   ↓
5. Preenche dados pessoais e endereço
   ↓
6. Confirma agendamento
   ↓
7. Recebe confirmação por email/SMS
   ↓
8. Técnico recebe notificação
   ↓
9. Sistema atualiza agenda automaticamente
```

## 4. Recursos Técnicos Necessários

### 4.1. Integração com Site
- **Widget de agendamento** incorporado na página principal
- **Botão de CTA** destacado: "Agende Seu Atendimento"
- **Formulário simplificado** com campos essenciais

### 4.2. Integração com CRM
- **Sincronização automática** com banco de dados de clientes
- **Histórico de atendimentos** por cliente
- **Controle de periodicidade** para manutenções preventivas

### 4.3. Sistema de Notificações
- **Email de confirmação** imediato
- **SMS de lembrete** 24h antes
- **Notificação para técnico** com detalhes do serviço
- **Confirmação de conclusão** do atendimento

## 5. Configuração Detalhada

### 5.1. Campos do Formulário de Agendamento
1. **Dados Pessoais**:
   - Nome completo
   - Telefone (WhatsApp)
   - Email
   - CPF/CNPJ

2. **Endereço do Atendimento**:
   - CEP
   - Rua e número
   - Complemento
   - Bairro
   - Cidade

3. **Detalhes do Serviço**:
   - Tipo de móvel/ambiente
   - Descrição do problema
   - Urgência (Normal/Urgente)
   - Observações especiais

### 5.2. Regras de Negócio
- **Antecedência mínima**: 24h para agendamentos
- **Reagendamento**: Até 4h antes do horário marcado
- **Cancelamento**: Até 2h antes sem cobrança
- **Atendimento urgente**: Taxa adicional de 30%

### 5.3. Integração com Pagamento
- **Pagamento online**: PIX, cartão de crédito/débito
- **Pagamento no local**: Dinheiro, PIX, cartão
- **Desconto**: 5% para pagamento antecipado

## 6. Métricas de Acompanhamento

### 6.1. Métricas Operacionais
- **Taxa de conversão** do agendamento
- **Taxa de no-show** (não comparecimento)
- **Tempo médio** entre agendamento e atendimento
- **Utilização da agenda** por técnico

### 6.2. Métricas de Satisfação
- **NPS** pós-atendimento
- **Avaliação do agendamento** (1-5 estrelas)
- **Facilidade de uso** do sistema
- **Tempo de resposta** para confirmação

## 7. Implementação por Fases

### Fase 1 (Semanas 1-2): Configuração Básica
- Criação da conta no Calendly
- Configuração dos tipos de serviços
- Definição de horários e disponibilidade
- Testes internos

### Fase 2 (Semanas 3-4): Integração com Site
- Incorporação do widget no site
- Customização visual
- Testes de funcionalidade
- Treinamento da equipe

### Fase 3 (Semanas 5-6): Lançamento e Ajustes
- Lançamento oficial
- Monitoramento de métricas
- Ajustes baseados no feedback
- Otimização do processo

## 8. Custos Estimados

### 8.1. Calendly Pro
- **Valor**: R$ 45/mês por usuário
- **Total para 6 técnicos**: R$ 270/mês
- **Recursos inclusos**: Integrações, notificações, relatórios

### 8.2. Customização e Integração
- **Desenvolvimento**: R$ 3.500 (uma vez)
- **Manutenção mensal**: R$ 200/mês

### 8.3. Total Mensal
- **R$ 470/mês** (após implementação)

## 9. Benefícios Esperados

### 9.1. Para os Clientes
- **Conveniência**: Agendamento 24/7
- **Transparência**: Horários disponíveis em tempo real
- **Flexibilidade**: Reagendamento fácil
- **Comunicação**: Notificações automáticas

### 9.2. Para a OLY Care
- **Eficiência**: Redução de ligações para agendamento
- **Organização**: Agenda centralizada e automatizada
- **Produtividade**: Otimização do tempo dos técnicos
- **Dados**: Métricas para tomada de decisão

## 10. Próximos Passos

1. **Aprovação do plano** pela diretoria
2. **Contratação do Calendly Pro**
3. **Início da configuração** dos serviços
4. **Desenvolvimento da integração** com o site
5. **Treinamento da equipe** técnica
6. **Testes piloto** com clientes selecionados
7. **Lançamento oficial** do sistema

