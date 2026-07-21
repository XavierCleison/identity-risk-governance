# 🤖 Prompt: Relatório para Stakeholders

**Versão:** 1.0.0  
**Objetivo:** Comunicação estratégica com stakeholders de risco  
**Público:** Security Committee, Department Heads, Project Sponsors  

---

## Prompt Estruturado

\\\
SISTEMA:
Você é um comunicador estratégico criando um relatório de risco para múltiplos stakeholders.
Foco: Transparência, ação clara, contexto de negócio.

CONTEXTO:
- Audience: Heterogênea (técnicos + business)
- Objetivo: Informar e mobilizar para ação
- Frequência: Semanal/Mensal
- Dados: Risk register, remediação progress, métricas

RESTRIÇÕES:
1. Linguagem acessível (evitar jargão técnico)
2. Incluir contexto de negócio
3. Ações claras e acionáveis
4. Indicar progress e momentum
5. Celebrar vitórias

TAREFA:
Criar relatório estruturado contendo:
1. Status resumido (🟢/🟡/🔴)
2. Top 3 riscos desta semana
3. Progress de remediação
4. Blockers ou escalações
5. Próximas ações (by role)
6. Success stories

OUTPUT:
Formato: Markdown com seções visuais, badges de status, e calls-to-action claros.
\\\

---

## Template de Output

\\\markdown
# 📊 Relatório de Risco IAM - Semana XX

## Status Geral

- 🟢 Riscos Críticos: 3 → **Plano de Ação Ativo**
- 🟠 Riscos Altos: 6 → **Remediação em andamento**
- 🟡 Riscos Médios: 8 → **Planejados para próximas semanas**
- 🟢 Riscos Baixos: 3 → **Monitorados**

## Top 3 Riscos Desta Semana

### 1. RISK-001: Privilege Creep
- **Status:** ⏳ In Progress
- **Owner:** Identity Manager
- **Progress:** 40% (Phase 2 starting)
- **Action needed from:** Department Heads
- **Next step:** Manager access reviews (by Friday)

### 2. RISK-002: Contas Órfãs
- **Status:** 🟢 Discovery Complete
- **Owner:** HR & IT
- **Progress:** 45 contas identificadas
- **Action needed from:** HR para confirmação
- **Next step:** Disable 30 contas (by EOW)

### 3. RISK-003: SoD Violations
- **Status:** ⏳ In Progress
- **Owner:** Compliance
- **Progress:** 15% (mapping complete)
- **Blocker:** Awaiting business process documentation
- **Next step:** Escalate to CFO office

## 📈 Progress vs. Plan

\\\
Semana 1:  ████░░░░░░ 40% (Target: 30%)
Semana 2:  ██████░░░░ 60% (Target: 60%)
Semana 3:  █████░░░░░ 50% (Target: 70%) ⚠️ Behind
Semana 4:  ████████░░ 80% (Target: 90%)
\\\

## ✅ Vitórias Desta Semana

- MFA enforcement: 95% of users compliant (+15%)
- Admin access review: 50 violations remediated
- Orphaned accounts: 20 disabled

## ⚠️ Blockers & Escalações

| Item | Owner | Impact | Action |
|------|-------|--------|--------|
| SoD mapping | CFO Office | CRITICAL | Escalate today |
| IdP licensing | Procurement | HIGH | Follow-up needed |

## 🎯 Próximas Ações por Role

**Para CIO:**
- [ ] Approve SoD exceptions (by tomorrow)

**Para Department Heads:**
- [ ] Complete access reviews (by Friday)

**Para Security Team:**
- [ ] Start Phase 2 of privilege creep fix

**Para HR:**
- [ ] Confirm 45 identified orphaned accounts

## 📞 Escalação se Necessário

**Contato:** security@company.com | **Phone:** Ext. 1001
\\\

---

## Variações por Stakeholder

### Para Security Committee
- Foco: Conformidade, risk metrics
- Detalhes: Técnicos e regulatórios

### Para Business Stakeholders
- Foco: Impacto de negócio
- Detalhes: Ações necessárias, timelines

### Para Project Sponsor
- Foco: Progress vs. plan
- Detalhes: Budget, timeline, risks

---

## Frequência Recomendada

- **Diária:** Para riscos CRÍTICOS (P1)
- **Semanal:** Para riscos ALTOS (P2)
- **Bi-semanal:** Para riscos MÉDIOS (P3)
- **Mensal:** Para riscos BAIXOS (P4)

---

**Versão:** 1.0.0
