# 📊 Matriz Probabilidade x Impacto

[![Matrix](https://img.shields.io/badge/type-Risk%20Assessment%20Matrix-blue.svg)]()
[![Risks](https://img.shields.io/badge/risks_analyzed-23-red.svg)]()

## 🎯 Matriz de Priorização

```
                                IMPACTO
                    BAIXO    MÉDIO    ALTO    CRÍTICO
                  ┌─────────┬─────────┬─────────┬─────────┐
                  │ 1 | 2   │ 2 | 4   │ 4 | 8   │ 8 | 16  │
            BAIXA │         │         │         │         │
          (0-0.3) │ R020    │ R021    │ R023    │         │
                  │ R022    │         │         │         │
                  ├─────────┼─────────┼─────────┼─────────┤
                  │ 2 | 4   │ 4 | 8   │ 8 | 16  │ 16 | 32 │
            MEDIA │         │         │         │         │
          (0.3-6) │ R018    │ R013    │ R010    │ R001    │
                  │ R024    │ R014    │ R009    │ R002    │
                  │         │ R015    │ R011    │ R003    │
                  │         │ R019    │ R012    │ R005    │
                  │         │ R022    │ R008    │ R004    │
                  ├─────────┼─────────┼─────────┼─────────┤
                  │ 4 | 8   │ 8 | 16  │ 16 | 32 │ 32 | 64 │
             ALTA │         │         │         │         │
          (0.6-1) │         │ R007    │ R006    │         │
                  │         │         │         │         │
                  └─────────┴─────────┴─────────┴─────────┘
                                  ▲
                        VERY ALTA (0.75-1.0)
                        ALTA (0.5-0.75)
                        MÉDIA (0.25-0.5)
                        BAIXA (0-0.25)
```

## 📋 Distribuição de Riscos

### Por Quadrante

#### 🟢 VERDE - Baixo Risco (Aceitar)

```
Quadrante: Probabilidade BAIXA × Impacto BAIXO

Riscos:
├─ R020: Falta documentação (1.0)
├─ R021: Comunicação deficiente (1.5)
└─ R023: Falta monitoramento 24/7 (2.6)

Ação: Aceitar (monitorar apenas)
Revisão: Trimestral
```

#### 🟡 AMARELO - Risco Moderado (Mitigar)

```
Quadrante: Probabilidade MÉDIA × Impacto MÉDIO-ALTO

Riscos:
├─ R010: Classificação incorreta (2.6)
├─ R013: Shadow Identities (3.6)
├─ R014: Falha auditoria (2.8)
├─ R015: ISO 27001 (2.2)
├─ R019: Retenção inadequada (3.7)
├─ R022: Excesso privilégios grupos (4.2)
└─ R007: Prompt Injection (3.7)

Ação: Mitigar (implementar controles)
Timeline: 60-90 dias
```

#### 🟠 LARANJA - Risco Elevado (Mitigar Urgente)

```
Quadrante: Probabilidade ALTA × Impacto ALTO

Riscos:
├─ R006: MFA Desabilitado (6.0)
├─ R008: Revogação Tardia (6.0)
├─ R009: Tokens Comprometidos (4.4)
├─ R011: Vazamento Logs (4.3)
├─ R012: Provisionamento Incorreto (4.3)
└─ R007: Prompt Injection (3.7)

Ação: Mitigar urgentemente (30-45 dias)
Owner: Security Director
```

#### 🔴 VERMELHO - Risco Crítico (Evitar/Mitigar Imediato)

```
Quadrante: Probabilidade MÉDIA-ALTA × Impacto CRÍTICO

Riscos:
├─ R001: SoD Violation (6.2) ⭐ PRIORIDADE #1
├─ R002: Privilege Creep (5.4) ⭐ PRIORIDADE #2
├─ R003: Contas Órfãs (5.2) ⭐ PRIORIDADE #3
├─ R004: IdP Indisponível (1.47) - Raro mas crítico
├─ R005: IA Recomendações Incorretas (4.25)
└─ R016: LGPD Não Conformidade (4.75)

Ação: Resposta imediata (0-30 dias)
Owner: CIO / CISO
Escalação: Board se necessário
```

---

## 📊 Scoring de Prioridade

### Fórmula

```
Prioridade = Probabilidade × Impacto

Exemplo:
R001: SoD = 0.65 × 0.95 = 0.62 → Prioridade: 1
R002: Privilege Creep = 0.60 × 0.90 = 0.54 → Prioridade: 2
R010: Classificação = 0.55 × 0.78 = 0.43 → Prioridade: 10
```

### Ranking Completo

| Rank | ID | Risco | P | I | Score | Severity |
|------|---|------|---|---|-------|----------|
| 🥇 1 | R-001 | SoD Violation | 0.65 | 0.95 | **0.62** | 🔴 CRÍTICO |
| 🥈 2 | R-002 | Privilege Creep | 0.60 | 0.90 | **0.54** | 🔴 CRÍTICO |
| 🥉 3 | R-003 | Contas Órfãs | 0.55 | 0.95 | **0.52** | 🔴 CRÍTICO |
| 4 | R-016 | LGPD Non-Compliance | 0.50 | 0.95 | **0.48** | 🔴 CRÍTICO |
| 5 | R-005 | IA Bad Recommendations | 0.50 | 0.85 | **0.43** | 🔴 CRÍTICO |
| 6 | R-006 | MFA Disabled | 0.75 | 0.80 | **0.60** | 🟠 ALTO |
| 7 | R-007 | Prompt Injection | 0.45 | 0.82 | **0.37** | 🟠 ALTO |
| 8 | R-008 | Revogação Tardia | 0.80 | 0.75 | **0.60** | 🟠 ALTO |
| 9 | R-009 | Tokens Comprometidos | 0.50 | 0.88 | **0.44** | 🟠 ALTO |
| 10 | R-010 | Classificação Incorreta | 0.55 | 0.78 | **0.43** | 🟠 ALTO |
| 11 | R-011 | Vazamento Logs | 0.50 | 0.85 | **0.43** | 🟠 ALTO |
| 12 | R-012 | Provisionamento Incorreto | 0.60 | 0.72 | **0.43** | 🟠 ALTO |
| 13 | R-013 | Shadow Identities | 0.55 | 0.65 | **0.36** | 🟡 MÉDIO |
| 14 | R-014 | Falha Auditoria | 0.30 | 0.92 | **0.28** | 🟡 MÉDIO |
| 15 | R-015 | ISO 27001 Gap | 0.25 | 0.88 | **0.22** | 🟡 MÉDIO |
| 16 | R-017 | Acesso Admin Indevido | 0.50 | 0.90 | **0.45** | 🟠 ALTO |
| 17 | R-018 | Dependência IdP | 0.25 | 0.98 | **0.25** | 🟡 MÉDIO |
| 18 | R-019 | Retenção Inadequada | 0.55 | 0.68 | **0.37** | 🟡 MÉDIO |
| 19 | R-020 | Falta Documentação | 0.20 | 0.45 | **0.09** | 🟢 BAIXO |
| 20 | R-021 | Comunicação Deficiente | 0.30 | 0.50 | **0.15** | 🟢 BAIXO |
| 21 | R-022 | Excesso Privilégios Grupos | 0.60 | 0.70 | **0.42** | 🟠 ALTO |
| 22 | R-023 | Falta Monitoramento 24/7 | 0.35 | 0.75 | **0.26** | 🟡 MÉDIO |
| 23 | R-024 | Falta Training Segurança | 0.40 | 0.60 | **0.24** | 🟡 MÉDIO |

---

## 🎨 Mapa de Calor

```
IMPACT (Vertical Axis)
CRÍTICO  ┌─────────────────────────────────────────┐
         │ 🟢 GREEN       🟢 GREEN       🟠 ORANGE   │
0.95     │                               R-003     │
         │ (Raro)                        R-004     │
         ├─────────────────────────────────────────┤
ALTO     │ 🟢 GREEN       🟡 YELLOW      🟠 ORANGE   │
0.80     │ R-015          R-017          R-001     │
         │ R-014          R-010          R-002     │
         │                R-009          R-005     │
         ├─────────────────────────────────────────┤
MÉDIO    │ 🟢 GREEN       🟡 YELLOW      🟠 ORANGE   │
0.70     │ R-024          R-013          R-006     │
         │ R-021          R-019          R-008     │
         │                R-023          R-022     │
         ├─────────────────────────────────────────┤
BAIXO    │ 🟢 GREEN       🟡 YELLOW      🟡 YELLOW   │
0.50     │ R-020          R-007          R-011     │
         │                R-012          R-018     │
         │                               │         │
         └─────────────────────────────────────────┘
           BAIXA             MÉDIA         ALTA
            (0.2)            (0.5)         (0.8)
           PROBABILITY (Horizontal Axis)
```

---

## 🎯 Curva de Risco Agregado

```
Risk Score Timeline (12 months)

Linha Agregada de Risco:
┌─────────────────────────────────────┐
│                   ╱╲                │
│                 ╱    ╲              │
│               ╱        ╲            │
│             ╱            ╲          │
│           ╱                ╲        │
│         ╱                    ╲      │
│       ╱                        ╲    │
│     ╱                            ╲  │
│   ╱                                ╲│
└─────────────────────────────────────┘
  Jul  Aug  Sep  Oct  Nov  Dec  Jan

Tendência: ↘️ Risco diminuindo (controles implementados)
Meta Q4: Score < 0.35
Meta Q1: Score < 0.25
```

---

## 📈 Análise de Tendências

### Evolução Semanal

| Semana | Total Score | Críticos | Altos | Tendência |
|--------|------------|----------|-------|-----------|
| Sem 28 | 8.24 | 5 | 9 | ↗️ +5% |
| Sem 29 | 8.11 | 5 | 8 | ↘️ -1.6% |
| Sem 30 | 7.95 | 4 | 9 | ↘️ -2.0% |
| Sem 31 | 7.73 | 4 | 8 | ↘️ -2.8% |

**Insight**: Risco geral diminuindo com implementação de controles.

---

## ✅ Verificação de Validação

### Critério de Classificação

Probabilidade:
- ✅ BAIXA: 0-0.35
- ✅ MÉDIA: 0.35-0.70
- ✅ ALTA: 0.70-1.0

Impacto:
- ✅ BAIXO: 0-0.40
- ✅ MÉDIO: 0.40-0.70
- ✅ ALTO: 0.70-0.90
- ✅ CRÍTICO: 0.90-1.0

Prioridade:
- ✅ CRÍTICO: Score > 0.50
- ✅ ALTO: 0.35-0.50
- ✅ MÉDIO: 0.20-0.35
- ✅ BAIXO: < 0.20

---

## 📋 Recomendações por Quadrante

### Quadrante 1: BAIXO/BAIXO (Aceitar)
```
Ação: ACEITAR ou MONITORAR
├─ Revisão: Trimestral
├─ Owner: Risk Manager
└─ Escalação: Não necessária
```

### Quadrante 2: MÉDIO/BAIXO (Monitorar)
```
Ação: MITIGAR (low priority)
├─ Revisão: Mensal
├─ Timeline: 90-180 dias
└─ Owner: Team Lead
```

### Quadrante 3: MÉDIO/MÉDIO-ALTO (Mitigar)
```
Ação: MITIGAR (medium priority)
├─ Revisão: Semanal
├─ Timeline: 60-90 dias
└─ Owner: Department Manager
```

### Quadrante 4: ALTO/CRÍTICO (Responder Imediato)
```
Ação: EVITAR ou MITIGAR URGENTE
├─ Revisão: Diária
├─ Timeline: 0-30 dias
├─ Owner: Director/CISO
└─ Escalação: CIO/Board se necessário
```

---

## 🚨 Top 5 Riscos - Ação Imediata

### 1️⃣ SoD Violation (R-001)

**Score**: 0.62 | **Prioridade**: 1  
**Status**: 🔴 ATIVO  
**Ação**: Evitar + Mitigar  
**Timeline**: 0-90 dias  
**Owner**: GRC Manager  

```
Dia 1-7:     Audit SoD atual
Dia 8-30:    Remediação de violações
Dia 31-60:   Implementar enforcement
Dia 61-90:   Validação + Ajustes
```

---

### 2️⃣ Privilege Creep (R-002)

**Score**: 0.54 | **Prioridade**: 2  
**Status**: 🔴 ATIVO  
**Ação**: Mitigar  
**Timeline**: 0-60 dias  

```
Implementar:
├─ Quarterly access reviews
├─ IA monitoring de escalations
├─ Auto-revocation de unused perms
└─ Dashboard de trending
```

---

### 3️⃣ Orphan Accounts (R-003)

**Score**: 0.52 | **Prioridade**: 3  
**Status**: 🔴 DETECTADO  
**Ação**: Evitar urgente  
**Timeline**: 0-30 dias  

```
Imediato:
├─ Disable contas órfãs críticas (24h)
├─ Auditoria completa (7 dias)
├─ Deprovisioning (14 dias)
└─ Implement lifecycle (30 dias)
```

---

### 4️⃣ LGPD Non-Compliance (R-016)

**Score**: 0.48 | **Prioridade**: 4  
**Status**: 🔴 ATIVO  
**Ação**: Mitigar + Transferir  
**Timeline**: 0-45 dias  

---

### 5️⃣ Bad AI Recommendations (R-005)

**Score**: 0.43 | **Prioridade**: 5  
**Status**: 🟠 MITIGANDO  
**Ação**: Mitigar  
**Timeline**: 0-45 dias  

```
Implementado:
├─ ✅ Confidence scoring
├─ ✅ Human validation workflow
├─ ⏳ Feedback loop (em progresso)
└─ ⏳ Fine-tuning (próximo mês)
```

---

## 📊 Métricas de Acompanhamento

### Dashboard KPIs

```
┌─────────────────────────────────┐
│ Risk Score Agregado: 7.73       │
│ Target Q3: 8.00                 │
│ Status: 🟢 On Track             │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ Riscos Críticos: 5 (↓ 1 week)   │
│ Target: 2                       │
│ Status: 🟠 Behind               │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ Riscos Fechados: 2              │
│ Target Sem: 3                   │
│ Status: 🟡 Slightly Behind      │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ Ações Completadas: 8 de 15      │
│ Completion %: 53%               │
│ Status: 🟡 On Schedule          │
└─────────────────────────────────┘
```

---

**Última Atualização**: Julho 21, 2026  
**Próxima Revisão**: Julho 28, 2026  
**Proprietário**: GRC Manager  
**Aprovação**: CIO / CISO

