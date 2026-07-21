# 🎯 Plano de Resposta aos Riscos - Identity Risk Governance

**Baseado em:** PMBOK (Project Management Body of Knowledge)  
**Data:** 2026-07-21  
**Status:** Active

---

## 1. Estratégias de Resposta (PMBOK)

### 1.1 EVITAR (Avoid)
**Objetivo:** Eliminar a probabilidade do risco ocorrer

**Quando usar:**
- Risco tem probabilidade muito alta
- Impacto potencial é catastrófico
- Existem alternativas viáveis

**Exemplo - RISK-008 (IdP Downtime):**
- Implementar redundância de IdP
- Garantir 99.95% de disponibilidade
- Resultado: Probabilidade reduzida de 30% para 5%

---

### 1.2 MITIGAR (Mitigate)
**Objetivo:** Reduzir probabilidade e/ou impacto do risco

**Quando usar:**
- Risco é significativo mas gerenciável
- Ações de redução são viáveis
- Custo-benefício é favorable

**Exemplo - RISK-001 (Privilege Creep):**
- Implementar periodic access reviews (quarterly)
- Automate revocation de permissions não-utilizadas
- Real-time privilege monitoring
- Resultado: Probabilidade reduzida de 80% para 40%

---

### 1.3 TRANSFERIR (Transfer)
**Objetivo:** Passar a responsabilidade do risco para terceiro

**Quando usar:**
- Risco pode ser controlado por especialista externo
- Insurance ou vendor pode gerenciar melhor
- Custo de transferência é menor que impacto

**Exemplo - RISK-016 (IdP Dependency):**
- Contratar SLA da Azure AD/Okta com 99.99% uptime
- Vendor responsável por conformidade LGPD/GDPR
- Seguro de cyber liability para breach
- Resultado: Responsabilidade transferida, impacto mitigado

---

### 1.4 ACEITAR (Accept)
**Objetivo:** Reconhecer o risco e estar preparado

**Quando usar:**
- Risco tem baixa probabilidade
- Impacto é aceitável
- Custo de mitigação > impacto potencial

**Exemplo - RISK-020 (Audit Log Break):**
- Probabilidade: 25%
- Impacto: Baixo (3/10)
- Ação: Monitorar com alertas
- Plano: Response imediata se ocorrer
- Resultado: Aceito e monitorado

---

## 2. Plano de Resposta por Risco

### RISK-001: Privilege Creep
**Estratégia:** MITIGAR

**Ações:**
1. Week 1-2: Implementar periodic access reviews
   - Quarterly reviews obrigatórias
   - Managers aprovam/rejeitam acessos
2. Week 2-3: Automação de revogação
   - Revogar permissões não-utilizadas > 90 dias
   - Alert para managers
3. Week 3-4: Real-time monitoring
   - Dashboard de privilege escalation
   - Alert instantâneo

**Owner:** Identity Manager  
**Timeline:** 30 dias  
**Budget:** \  
**Success Criteria:**
- 0 privilege creep violations
- 100% manager review compliance
- < 7 dias para remediação

---

### RISK-002: Contas Órfãs
**Estratégia:** MITIGAR

**Ações:**
1. Week 1: HR Integration
   - API connection com HR system
   - Auto-detection de ex-funcionários
2. Week 2-3: Disable automático
   - Disable contas > 90 dias inativas
   - Alert antes de disable
3. Week 4: Cleanup process
   - Quarterly manual review
   - Cleanup de contas legacy

**Owner:** HR & IT Lead  
**Timeline:** 45 dias  
**Success Criteria:**
- 100% orphaned accounts identified
- Auto-disable working
- 0 inactive accounts

---

### RISK-003: SoD Violations
**Estratégia:** MITIGAR

**Ações:**
1. Week 1-2: Map SoD rules
   - Identificar conflitos críticos
   - Define SoD matrix
2. Week 2-4: Implement rules
   - Programar automated enforcement
   - Test em non-prod
3. Week 4-6: Remediation
   - Fix existing violations
   - Manager approval
4. Week 6+: Continuous monitoring
   - Real-time validation
   - Alert para violations

**Owner:** Compliance Officer  
**Timeline:** 60 dias  
**Success Criteria:**
- 100% SoD rules implemented
- 0 violations in production
- 100% compliance

---

### RISK-004: Shadow Identities
**Estratégia:** MITIGAR

**Actions:**
1. Discovery & Inventory
   - Scan systems para undocumented accounts
   - Create inventory
2. Centralize Management
   - Provisioning governance
   - Documentation requirement
3. Monitoring
   - Alert para new shadow accounts
   - Quarterly audit

**Owner:** Security Engineer  
**Timeline:** 45 dias  

---

### RISK-005: Over-privileged Users
**Estratégia:** MITIGAR

**Actions:**
1. Audit admin users
2. Implement least privilege
3. Use Just-In-Time (JIT) access
4. MFA mandatory for admins

**Owner:** IAM Architect  
**Timeline:** 30 dias  

---

### RISK-006: Compromised Tokens
**Estratégia:** MITIGAR

**Actions:**
1. Token rotation policy
2. Monitor leaked credentials
3. Force password reset
4. Conditional access

**Owner:** Security Operations  
**Timeline:** 14 dias  

---

### RISK-007: MFA Disabled
**Estratégia:** MITIGAR

**Actions:**
1. Make MFA mandatory
2. Remove weak 2FA
3. Enforce authenticators
4. Monitor MFA status

**Owner:** Authentication Lead  
**Timeline:** 21 dias  

---

### RISK-008: IdP Downtime
**Estratégia:** EVITAR

**Actions:**
1. Implement IdP redundancy
2. Cache authentication data
3. Failover automation
4. Recovery procedures

**Owner:** Infrastructure Lead  
**Timeline:** 90 dias  
**Investment:** \  

---

### RISK-009: Incorrect Provisioning
**Estratégia:** MITIGAR

**Actions:**
1. Approval workflow
2. Validation process
3. Automated testing
4. Audit trails

**Owner:** Access Manager  
**Timeline:** 30 dias  

---

### RISK-010 a RISK-020
**Estratégia:** MITIGAR (maioria)

(Detalhes específicos em risk-register.md)

---

## 3. Matriz de Resposta

| Risk ID | Estratégia | Timeline | Budget | Owner |
|---------|-----------|----------|--------|-------|
| RISK-001 | Mitigar | 30d | \ | Identity Mgr |
| RISK-002 | Mitigar | 45d | \ | HR & IT |
| RISK-003 | Mitigar | 60d | \ | Compliance |
| RISK-004 | Mitigar | 45d | \ | Security Eng |
| RISK-005 | Mitigar | 30d | \ | IAM Arch |
| RISK-006 | Mitigar | 14d | \ | SecOps |
| RISK-007 | Mitigar | 21d | \ | Auth Lead |
| RISK-008 | Evitar | 90d | \ | Infrastructure |
| RISK-009 | Mitigar | 30d | \ | Access Mgr |
| RISK-010+ | Mitigar | Var | Var | Various |

**Total Budget (P1+P2):** \  
**Timeline (Critical):** 30-60 dias  

---

## 4. Justificativa PMBOK

### Razão das Estratégias Escolhidas

**EVITAR é ideal quando:**
- ✅ Risco pode ser completamente eliminado
- ✅ Solução é viável e custo-efetiva
- ✅ Não compromete objetivos do projeto

**MITIGAR é ideal quando:**
- ✅ Risco não pode ser evitado completamente
- ✅ Redução de probabilidade/impacto é possível
- ✅ Benefício > custo de mitigação

**TRANSFERIR é ideal quando:**
- ✅ Terceiro pode gerenciar melhor
- ✅ Contrato com SLA viável
- ✅ Custo de transferência < impacto

**ACEITAR é ideal quando:**
- ✅ Probabilidade é muito baixa
- ✅ Impacto é aceitável
- ✅ Custo de resposta > impacto

---

## 5. Monitoramento de Riscos

**Cadência:**
- Críticos (P1): Diária
- Altos (P2): Semanal
- Médios (P3): Bi-semanal
- Baixos (P4): Mensal

**Trigger de Escalação:**
- Nova exposição detectada
- Probabilidade aumenta > 20%
- Impacto aumenta > 2 níveis
- Timeline de remediação em risco

---

**Versão:** 1.0.0 | **Aprovação:** Security Committee
