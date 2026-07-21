# 📋 Plano de Resposta de Riscos - Segundo PMBOK

[![Framework](https://img.shields.io/badge/framework-PMBOK%206th%20Edition-blue.svg)]()
[![Process](https://img.shields.io/badge/process-Plan%20Risk%20Responses-green.svg)]()

## 📚 Referência PMBOK

Segundo o **PMBOK 6ª Edição**, o processo "Plan Risk Responses" (11.5) define quatro estratégias principais para ameaças:

1. **EVITAR** - Eliminar a ameaça ou condição
2. **MITIGAR** - Reduzir probabilidade ou impacto
3. **TRANSFERIR** - Passar a responsabilidade para terceiros
4. **ACEITAR** - Reconhecer o risco sem ação proativa

---

## 🎯 Estratégias de Resposta

### 1. EVITAR (Avoid)

**Definição PMBOK**: Alterar o escopo, cronograma, orçamento ou abordagem do projeto para eliminar completamente a ameaça ou a condição que a causa.

#### Critérios de Aplicação

✅ **Quando usar**:
- Risco tem impacto crítico e probabilidade média/alta
- Existem alternativas viáveis
- Custo de evitar < Impacto potencial
- Não compromete objetivos principais

❌ **Quando NÃO usar**:
- Impossível eliminar completamente
- Custo proibitivo
- Impacto na funcionalidade crítica
- Prazo insuficiente

#### Exemplos Práticos em IAM

```
RISK-003: Contas Órfãs em Sistemas Críticos

Ameaça: Contas sem proprietário = acesso não autorizado

Estratégia EVITAR:
├─ Implementar Automated Lifecycle Management
│  └─ Desabilitar automaticamente contas após término
├─ Eliminar contas órfãs existentes (47 contas)
│  └─ Deprovisioning imediato
└─ Política de "zero-orphan" obrigatória
   └─ Nenhuma conta sem owner designado

Resultado:
├─ Elimina 100% do risco
├─ Custo: R$ 45,000 (uma vez)
└─ ROI: R$ 500K (incidentes evitados)
```

### 2. MITIGAR (Mitigate)

**Definição PMBOK**: Reduzir a probabilidade de ocorrência, o impacto da ameaça, ou ambos, para um nível aceitável.

#### Critérios de Aplicação

✅ **Quando usar**:
- Risco não pode ser evitado completamente
- Existem controles viáveis
- ROI é positivo
- Timeline permite implementação

#### Exemplos Práticos em IAM

```
RISK-001: Violação de Segregação de Deveres (SoD)

Ameaça: Combinações de permissões conflitantes → fraude

Estratégia MITIGAR:

Reduzir PROBABILIDADE:
├─ 1. Enforce SoD policies automaticamente
│  └─ Regex validation em atribuição de permissões
├─ 2. Access review trimestral obrigatória
│  └─ Validação manual de exceptions
└─ 3. IA monitoring contínua
   └─ Alertas de violações potenciais em tempo real

Reduzir IMPACTO:
├─ 1. Segregação de sistemas críticos
│  └─ Audit teams isoladas de transaction teams
├─ 2. Approval workflow para exceções
│  └─ Necessário CIO approval
└─ 3. Auditoria intensiva de usuários com exceções
   └─ Mensal ao invés de trimestral

Resultado:
├─ Probabilidade: ALTA (0.75) → MÉDIA (0.40)
├─ Impacto: CRÍTICO (0.95) → ALTO (0.70)
├─ Score: 0.62 → 0.28 (↓ 55%)
└─ Custo: R$ 120,000 + R$ 50,000/ano (operacional)
```

#### Matriz de Mitigation Techniques

| Técnica | Probabilidade | Impacto | Custo | Prazo |
|---------|---|---|---|---|
| Controle técnico automático | ↓↓ | - | M | 30d |
| Policy & Enforcement | ↓ | ↓ | L | 45d |
| Training & Awareness | ↓ | - | L | 60d |
| Redundância/Failover | - | ↓↓ | H | 90d |
| Insurance | - | ↓ | M | 15d |
| Monitoring & Alerting | ↓ | ↓ | M | 30d |

### 3. TRANSFERIR (Transfer)

**Definição PMBOK**: Delegação a terceiros (ex: seguradoras, fornecedores) da responsabilidade financeira ou operacional.

#### Critérios de Aplicação

✅ **Quando usar**:
- Organização carece de expertise
- Custo é preocupação principal
- Terceiro pode gerenciar melhor
- Relacionamento estabelecido

#### Exemplos Práticos em IAM

```
RISK-004: Identity Provider Indisponível

Ameaça: IdP down → 8000+ usuários sem acesso

Estratégia TRANSFERIR:

1. Contratar SLA Premium com Okta
   ├─ 99.99% uptime guarantee
   ├─ Backup region automaticamente
   ├─ RTO: 5 minutos
   ├─ RPO: < 1 minuto
   └─ Custo: R$ 150,000/ano

2. Contrato de Disaster Recovery
   ├─ Failover automático para backup IdP
   ├─ Okta + Azure AD redundancy
   └─ Custo: R$ 80,000/ano

3. Insurance - Cyber Liability
   ├─ Cobertura de business interruption
   ├─ Coverage: R$ 10M
   └─ Custo: R$ 120,000/ano

4. Managed Service Provider (MSP)
   ├─ 24/7 monitoring & support
   ├─ SLA response time: 15 min críticos
   └─ Custo: R$ 200,000/ano

Total Risk Transfer:
├─ Probabilidade: BAIXA (0.15) → MUITO BAIXA (0.05)
├─ Impacto: Parcialmente absorvido por insurance
└─ Custo anual: R$ 550,000 (vs R$ 500K/hour downtime)
```

#### Instrumentos de Transferência

| Instrumento | Aplicação | Custo |
|-----------|-----------|-------|
| **Service Level Agreement (SLA)** | IdP uptime, Response time | Included |
| **Insurance Policy** | Business interruption, Cyber liability | 2-3% premium |
| **Vendor Guarantees** | Performance warranties | Included |
| **Outsourcing/MSP** | 24/7 management, Expertise | 5-10% overhead |

### 4. ACEITAR (Accept)

**Definição PMBOK**: Reconhecer o risco e planejar contingências caso ocorra, sem reduzir proativamente a probabilidade ou impacto.

#### Critérios de Aplicação

✅ **Quando usar**:
- Risco é residual após mitigação
- Impacto aceitável para organização
- Custo de resposta > Impacto potencial
- Probabilidade muito baixa

#### Exemplos Práticos em IAM

```
RISK-020: Falta de Documentação de Políticas

Ameaça: Políticas não documentadas → Falta de compliance

Status: ACEITAR
├─ Probabilidade: BAIXA (0.20)
├─ Impacto: BAIXO (0.45)
├─ Score: 0.09
└─ Mitigação: Informação armazenada em Wikis/Confluence

Contingência:
├─ Se policy gap detectado → 30-day remediation
├─ Owner: Compliance Officer
└─ Monitoring: Quarterly audits

Custo: R$ 0 (não proativo)
Risk Budget: Monitoramento apenas
```

```
RISK-024: Falta de Training de Segurança

Ameaça: Equipe não treinada → Erros de segurança

Status: ACEITAR (Monitorar)
├─ Probabilidade: BAIXA (0.40)
├─ Impacto: MÉDIO (0.60)
├─ Score: 0.24
└─ Racional: Training planejado para Q4

Contingência:
├─ Se incidente relacionado à falta de training
├─ Então: Immediate remedial training + refresher
├─ Owner: CISO/HR
└─ Timeline: < 48 horas

Custo: R$ 0 (já planejado em orçamento)
```

---

## 🔄 Matriz de Decisão PMBOK

```
                    PROBABILIDADE
           BAIXA              MÉDIA              ALTA
CRÍTICO  ┌──────────────┬──────────────┬──────────────┐
IMPACTO  │  TRANSFERIR  │   EVITAR     │    EVITAR    │
0.95     │   + MITIGAR  │   ou MITIGAR │   Urgente    │
         ├──────────────┼──────────────┼──────────────┤
ALTO     │   ACEITAR    │   MITIGAR    │   MITIGAR    │
IMPACTO  │   ou MONIT.  │   Urgente    │   Urgente    │
0.80     ├──────────────┼──────────────┼──────────────┤
MÉDIO    │   ACEITAR    │   ACEITAR    │   MITIGAR    │
IMPACTO  │              │   ou MITIGAR │              │
0.60     ├──────────────┼──────────────┼──────────────┤
BAIXO    │   ACEITAR    │   ACEITAR    │   ACEITAR    │
IMPACTO  │              │              │   ou MONIT.  │
0.45     └──────────────┴──────────────┴──────────────┘
```

---

## 📋 Planos de Resposta Detalhados

### Risk-001: SoD Violation

```yaml
Risk ID: R-001
Strategy: MITIGAR
Rationale PMBOK: 
  "Risco crítico com probabilidade média pode ser significativamente
   reduzido através de controles técnicos e policies. Evitar completamente
   não é viável em contexto corporativo."

Action Plan:
  Phase 1 - Detection (0-30 days):
    - Scan de 8000 usuários vs matriz SoD
    - Identificar 100% de violações
    - Owner: GRC Manager
    - Effort: 160h
  
  Phase 2 - Remediation (30-60 days):
    - Remover violações identificadas
    - Criar roles balanceados
    - Approval workflow para exceções
    - Owner: IAM + GRC Teams
    - Effort: 240h
  
  Phase 3 - Enforcement (60-90 days):
    - Implementar regras no sistema
    - Alertas em tempo real
    - Auditoria automática semanal
    - Owner: Security Ops
    - Effort: 80h

Success Criteria:
  - 100% compliance com SoD
  - Zero novos incidentes
  - Audit validate approve
  - MTTD < 1 minuto

Budget: R$ 120,000
Timeline: 90 dias
Owner: GRC Manager
```

### Risk-004: IdP Unavailability

```yaml
Risk ID: R-004
Strategy: TRANSFERIR + MITIGAR
Rationale PMBOK:
  "Risco raro (15% prob) mas impacto crítico. Melhor estratégia é
   transferir para fornecedor confiável com SLA garantido, mantendo
   failover automático para redundância."

Action Plan:
  1. SLA Premium com Okta (99.99% uptime)
     - Dual-region active-active
     - Auto-failover < 5 min
     - Cost: R$ 150K/year
  
  2. Backup IdP (Azure AD)
     - Cache tokens locais (emergency)
     - Test failover monthly
     - Cost: R$ 80K/year
  
  3. Insurance - Business Interruption
     - Coverage R$ 10M
     - Cyber liability included
     - Cost: R$ 120K/year
  
  4. MSP 24/7 Monitoring
     - Response SLA 15 min critical
     - Cost: R$ 200K/year

Contingency Trigger:
  IF IdP responsiveness > 1 second for 5 min
  THEN trigger failover process
  AND notify on-call team

Total Cost Transfer: R$ 550K/year
ROI: vs R$ 500K/hour potential downtime

Timeline: 90 dias
Owner: Infrastructure Manager
```

---

## 🎯 Mapeamento de Riscos para Estratégias

| Risk | Estratégia | Prioridade | Timeline | Custo |
|------|-----------|-----------|----------|-------|
| R-001 | MITIGAR | 1 | 90d | R$ 120K |
| R-002 | MITIGAR | 2 | 60d | R$ 85K |
| R-003 | EVITAR | 3 | 30d | R$ 45K |
| R-004 | TRANSFERIR | 4 | 90d | R$ 550K/year |
| R-005 | MITIGAR | 5 | 45d | R$ 80K |
| R-006 | MITIGAR | 6 | 30d | R$ 15K |
| R-007 | MITIGAR | 7 | 60d | R$ 40K |
| R-008 | MITIGAR | 8 | 45d | R$ 60K |
| R-009 | MITIGAR | 9 | 60d | R$ 70K |
| R-010 | MITIGAR | 10 | 30d | R$ 25K |
| R-011 | MITIGAR | 11 | 45d | R$ 50K |
| R-012 | MITIGAR | 12 | 45d | R$ 35K |
| R-013 | MITIGAR | 13 | 60d | R$ 30K |
| R-014 | MITIGAR | 14 | 90d | R$ 40K |
| R-015 | MITIGAR | 15 | 60d | R$ 35K |
| R-016 | MITIGAR | 16 | 45d | R$ 50K |
| R-017 | MITIGAR | 17 | 60d | R$ 45K |
| R-018 | TRANSFERIR | 18 | 90d | R$ 200K |
| R-019 | MITIGAR | 19 | 60d | R$ 30K |
| R-020 | ACEITAR | 20 | N/A | R$ 0 |
| R-021 | ACEITAR | 21 | N/A | R$ 0 |
| R-022 | MITIGAR | 22 | 45d | R$ 35K |
| R-023 | ACEITAR | 23 | N/A | R$ 0 |

---

## 📊 Orçamento de Resposta

### Por Estratégia

```
EVITAR:        R$ 45,000 (1 risco)
MITIGAR:       R$ 870,000 (18 riscos)
TRANSFERIR:    R$ 750,000/year (2 riscos)
ACEITAR:       R$ 0 (2 riscos)
─────────────────────────
TOTAL CAPEX:   R$ 1,665,000
TOTAL OPEX:    R$ 750,000/year
```

### Benefícios Esperados

```
Incidentes Evitados:     R$ 5,000,000/year
Multas Regulatórias:     R$ 2,000,000/year
Downtime Evitado:        R$ 500,000/year
Eficiência Operacional:  R$ 800,000/year
─────────────────────────
TOTAL BENEFÍCIO:         R$ 8,300,000/year

ROI: (8,300,000 - 750,000) / 1,665,000 = 4.57x
Payback Period: 2.4 meses
```

---

## 🔄 Monitoramento de Resposta

### Indicadores de Efetividade (PMBOK)

```
Para cada resposta implementada:

1. Efetiveness Indicator
   └─ Baseline → Target → Actual
   
2. Timeliness Indicator
   └─ Planejado → Executado
   
3. Cost Indicator
   └─ Orçado → Gasto
   
4. Quality Indicator
   └─ Aprovação em audit
```

### Dashboard de Acompanhamento

```
R-001 (SoD) - MITIGAR
├─ Phase 1 (Detection):     ████████░░ 80% | On time
├─ Phase 2 (Remediation):   ░░░░░░░░░░  0% | Scheduled
├─ Phase 3 (Enforcement):   ░░░░░░░░░░  0% | Scheduled
└─ Overall:                 ██░░░░░░░░ 27% | On track

R-004 (IdP) - TRANSFERIR
├─ SLA Setup:               ██████████ 100% | Complete
├─ MSP Contract:            ████░░░░░░  40% | In progress
├─ Testing:                 ░░░░░░░░░░   0% | Q3
└─ Overall:                 ████░░░░░░  47% | On schedule
```

---

## ✅ Critérios de Sucesso

### Por Estratégia

**EVITAR**: 
- ✅ Risco completamente eliminado
- ✅ Zero incidentes relacionados
- ✅ Validação em audit

**MITIGAR**:
- ✅ Probabilidade reduzida ≥ 50%
- ✅ Impacto reduzido ≥ 30%
- ✅ Score agregado ↓ ≥ 40%

**TRANSFERIR**:
- ✅ SLA assinado e ativo
- ✅ Failover testado com sucesso
- ✅ Insurance policy em vigor

**ACEITAR**:
- ✅ Contingency plan documentado
- ✅ Monitoramento em funcionamento
- ✅ Trigger events definidos

---

## 📚 Referências PMBOK

**Process**: Plan Risk Responses (11.5)  
**Knowledge Area**: Project Risk Management  
**Input**: Risk Register  
**Output**: Risk Response Plan

**Estratégias Adicionais (Oportunidades)**:
- Explorar (Explore)
- Melhorar (Enhance)
- Compartilhar (Share)
- Aceitar (Accept)

---

**Última Atualização**: Julho 21, 2026  
**Aprovado por**: CIO / CISO / PMO  
**Próxima Revisão**: Agosto 21, 2026

