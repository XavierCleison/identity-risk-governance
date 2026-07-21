# 📊 Matriz Probabilidade-Impacto - Identity Risk Governance

## Definições

### Escala de Probabilidade

| Nível | Porcentagem | Descrição |
|-------|-------------|-----------|
| **Muito Baixa** | 0-20% | Evento improvável de ocorrer |
| **Baixa** | 21-40% | Evento pode ocorrer raramente |
| **Média** | 41-60% | Evento tem chance moderada |
| **Alta** | 61-80% | Evento tem boa chance de ocorrer |
| **Muito Alta** | 81-100% | Evento é provável de ocorrer |

### Escala de Impacto

| Nível | Score | Descrição |
|-------|-------|-----------|
| **Negligenciável** | 1 | Impacto mínimo na operação |
| **Menor** | 2 | Impacto pequeno, facilmente mitigável |
| **Moderado** | 3-4 | Impacto significativo |
| **Maior** | 5-7 | Impacto severo na operação |
| **Crítico** | 8-10 | Impacto catastrófico |

---

## 📈 Matriz de Risco (Probability x Impact)

\\\
IMPACTO
9-10  │        │ RISK-003 │ RISK-001  RISK-002  │
      │        │  (SoD)   │ (Priv Esc) (Orphan) │
      │        │          │                     │
7-8   │ RISK-004│ RISK-005 │ RISK-009 RISK-006  │
      │(Shadow) │ (Over    │(Provision)(Tokens)│
      │         │ Priv)    │                    │
      │         │          │                    │
5-6   │ RISK-013│ RISK-010 │ RISK-007 RISK-008 │
      │ (Logs)  │ (Revoke) │ (MFA)   (IdP Down)│
      │         │ RISK-012 │                    │
      │         │(Injection)                    │
      │         │          │                    │
3-4   │ RISK-014│ RISK-015 │ RISK-016 RISK-018 │
      │(Classify)(Admin)   │(Vendor) (ISO 27001)
      │         │ RISK-017 │                    │
      │         │ (Audit)  │ RISK-019 RISK-020 │
      │         │          │ (LGPD) (Audit Log)│
      │         │          │                    │
      ├─────────┼──────────┼────────┼──────────→ PROBABILIDADE
     Muito Baixa Baixa    Média    Alta  Muito Alta
      0-20%    21-40%   41-60%  61-80%  81-100%
\\\

---

## 🔴 Zona Crítica (P3 - AÇÃO IMEDIATA)

**Critério:** Probabilidade ≥ 60% + Impacto ≥ 7

| Risk ID | Risco | P | I | Score | Ação |
|---------|-------|---|---|-------|------|
| RISK-001 | Privilege Creep | 80% | 9 | 9.2 | 🔴 IMEDIATO |
| RISK-002 | Contas Órfãs | 75% | 9 | 8.9 | 🔴 IMEDIATO |
| RISK-003 | SoD Violations | 70% | 9 | 8.7 | 🔴 IMEDIATO |

---

## 🟠 Zona Vermelha (P2 - AÇÃO PRIORITÁRIA)

**Critério:** Probabilidade ≥ 40% + Impacto ≥ 5 E Score < 8

| Risk ID | Risco | P | I | Score | Ação |
|---------|-------|---|---|-------|------|
| RISK-004 | Shadow Identities | 65% | 8 | 7.8 | 🟠 SEMANA 1 |
| RISK-005 | Over-privileged | 72% | 8 | 7.6 | 🟠 SEMANA 1 |
| RISK-006 | Tokens | 55% | 8 | 7.2 | 🟠 SEMANA 2 |
| RISK-007 | MFA Disabled | 60% | 8 | 7.0 | 🟠 SEMANA 2 |
| RISK-008 | IdP Downtime | 30% | 8 | 6.0 | 🟠 SEMANA 4 |
| RISK-009 | Provisioning | 50% | 7 | 6.5 | 🟠 SEMANA 2 |

---

## 🟡 Zona Amarela (P3 - AÇÃO PLANEJADA)

**Critério:** Score 3.0 - 4.9

| Risk ID | Risco | P | I | Score | Ação |
|---------|-------|---|---|-------|------|
| RISK-010 | Late Revocation | 60% | 6 | 5.4 | 🟡 MÊS 1 |
| RISK-011 | AI Recommendations | 45% | 7 | 5.6 | 🟡 MÊS 1 |
| RISK-012 | Prompt Injection | 35% | 7 | 4.9 | 🟡 MÊS 1 |
| RISK-013 | Log Leakage | 40% | 6 | 4.8 | 🟡 MÊS 2 |
| RISK-014 | Severity Misclass | 50% | 5 | 4.5 | 🟡 MÊS 2 |
| RISK-015 | Admin Access | 35% | 7 | 4.9 | 🟡 MÊS 2 |
| RISK-016 | IdP Dependency | 25% | 6 | 3.8 | 🟡 MÊS 3 |
| RISK-017 | Audit Failure | 30% | 6 | 3.6 | 🟡 MÊS 3 |

---

## 🟢 Zona Verde (P4 - MONITORAR)

**Critério:** Score < 3.0

| Risk ID | Risco | P | I | Score | Ação |
|---------|-------|---|---|-------|------|
| RISK-018 | ISO 27001 | 20% | 4 | 2.4 | 🟢 MONITORAR |
| RISK-019 | LGPD | 15% | 4 | 2.0 | 🟢 MONITORAR |
| RISK-020 | Audit Log | 25% | 3 | 1.9 | 🟢 MONITORAR |

---

## 🎯 Zonas de Decisão

### Zona 1: CRÍTICA (VERMELHO ESCURO)
- **Critério:** Score > 8.0
- **Riscos:** RISK-001, RISK-002, RISK-003
- **Ação:** Implementar em dias
- **Responsável:** C-Level

### Zona 2: ALTA (VERMELHO)
- **Critério:** Score 6.0 - 8.0
- **Riscos:** RISK-004 a RISK-009
- **Ação:** Implementar em semanas
- **Responsável:** Department Head

### Zona 3: MÉDIA (AMARELA)
- **Critério:** Score 3.0 - 6.0
- **Riscos:** RISK-010 a RISK-017
- **Ação:** Implementar em meses
- **Responsável:** Team Lead

### Zona 4: BAIXA (VERDE)
- **Critério:** Score < 3.0
- **Riscos:** RISK-018 a RISK-020
- **Ação:** Monitorar
- **Responsável:** Ongoing

---

## 📊 Heatmap Visual

\\\
        MUITO BAIXA  BAIXA    MÉDIA    ALTA    MUITO ALTA
         (0-20%)   (21-40%) (41-60%) (61-80%) (81-100%)

CRÍTICO    ███       ███      ███     ████     █████
(8-10)     018,019   015,017  014,011 001,002  -

MAIOR      ██        ██       ███     ███      ██
(5-7)      016       012,013  010     004,005  007,008,009

MODERADO   █         ██       ██      ██       ██
(3-4)      -         -        -       -        -

MENOR      -         -        -       -        -
(2)

NEGLIGENCIÁVEL -    -        -       -        -
(1)
\\\

---

## 📈 Tendência de Riscos

**Mês 1:** 20 riscos identificados
**Mês 2:** Target - Remediação de P1 críticos (3 riscos)
**Mês 3:** Target - Remediação de P2 altos (6 riscos)
**Mês 6:** Target - Remediação de P3 médios (8 riscos)
**Mês 12:** Target - Todos os P4 monitorados (3 riscos)

---

**Versão:** 1.0.0 | **Data:** 2026-07-21
