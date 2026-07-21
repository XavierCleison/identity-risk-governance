# 📋 Registro de Riscos IAM - Identity Risk Governance

**Data de Criação:** 2026-07-21  
**Última Atualização:** 2026-07-21  
**Versão:** 1.0.0  
**Status:** Active

---

## 📊 Resumo Executivo de Riscos

- **Total de Riscos:** 20+
- **Riscos Críticos:** 3
- **Riscos Altos:** 6
- **Riscos Médios:** 8
- **Riscos Baixos:** 3+

---

## 🔴 RISCOS CRÍTICOS (Impacto + Probabilidade = MÁXIMA)

### RISK-001: Privilege Creep / Privilege Escalation

| Campo | Valor |
|-------|-------|
| **ID** | RISK-001 |
| **Categoria** | Access Control |
| **Descrição** | Usuários acumulam permissões ao longo do tempo sem remoção, levando a privilégios excessivos |
| **Probabilidade** | 🔴 ALTA (80%) |
| **Impacto** | 🔴 CRÍTICO (9/10) |
| **Prioridade** | 🔴 P1 - CRÍTICO |
| **Score de Risco** | 9.2/10 |
| **Detecção** | Análise de permissões acumuladas, anomalia behavioral |
| **Estratégia** | **Mitigar** |
| **Plano de Ação** | 1. Implementar periodic access reviews (quarterly) 2. Automation para revogar unused permissions 3. Real-time privilege monitoring 4. SoD enforcement |
| **Responsável** | Identity Manager |
| **Prazo** | 30 dias |
| **Status** | In Progress |

---

### RISK-002: Contas Órfãs (Abandoned/Orphaned Accounts)

| Campo | Valor |
|-------|-------|
| **ID** | RISK-002 |
| **Categoria** | Account Lifecycle |
| **Descrição** | Contas de ex-funcionários, contractors, ou systems não são desabilitadas, permanecendo com acesso ativo |
| **Probabilidade** | 🔴 ALTA (75%) |
| **Impacto** | 🔴 CRÍTICO (9/10) |
| **Prioridade** | 🔴 P1 - CRÍTICO |
| **Score de Risco** | 8.9/10 |
| **Detecção** | HR integration, Access logs analysis, No login > 90 dias |
| **Estratégia** | **Mitigar** |
| **Plano de Ação** | 1. Integrar com HR system para auto-detection 2. Disable contas inativas > 90 dias 3. Quarterly cleanup process 4. Alert para contas suspeitas |
| **Responsável** | HR & IT Lead |
| **Prazo** | 45 dias |
| **Status** | Planned |

---

### RISK-003: Segregation of Duties Violations (SoD)

| Campo | Valor |
|-------|-------|
| **ID** | RISK-003 |
| **Categoria** | Compliance |
| **Descrição** | Usuário possui permissões conflitantes (ex: criar e aprovar ordens), violando SoD |
| **Probabilidade** | 🔴 ALTA (70%) |
| **Impacto** | 🔴 CRÍTICO (9/10) |
| **Prioridade** | 🔴 P1 - CRÍTICO |
| **Score de Risco** | 8.7/10 |
| **Detecção** | Automated SoD rules, Periodic audits |
| **Estratégia** | **Mitigar** |
| **Plano de Ação** | 1. Map SoD rules por processo crítico 2. Implement automated SoD enforcement 3. Remediate existing violations 4. Real-time monitoring |
| **Responsável** | Compliance Officer |
| **Prazo** | 60 dias |
| **Status** | In Progress |

---

## 🟠 RISCOS ALTOS

### RISK-004: Shadow Identities (Unmanaged Accounts)

| Campo | Valor |
|-------|-------|
| **ID** | RISK-004 |
| **Categoria** | Access Management |
| **Descrição** | Contas criadas fora do processo formal (ex: service accounts não-documentados) |
| **Probabilidade** | 🟠 MÉDIA-ALTA (65%) |
| **Impacto** | 🟠 ALTO (8/10) |
| **Prioridade** | 🟠 P2 - ALTO |
| **Score de Risco** | 7.8/10 |
| **Estratégia** | **Mitigar** |
| **Plano de Ação** | 1. Discovery de shadow accounts 2. Centralize service account management 3. Implement provisioning governance 4. Regular audit trails |
| **Responsável** | Security Engineer |
| **Prazo** | 45 dias |

---

### RISK-005: Excesso de Privilégios (Over-privileged Users)

| Campo | Valor |
|-------|-------|
| **ID** | RISK-005 |
| **Categoria** | Access Control |
| **Descrição** | Usuários com privilégios administrative sem justificativa de negócio |
| **Probabilidade** | 🟠 ALTA (72%) |
| **Impacto** | 🟠 ALTO (8/10) |
| **Prioridade** | 🟠 P2 - ALTO |
| **Score de Risco** | 7.6/10 |
| **Estratégia** | **Mitigar** |
| **Plano de Ação** | 1. Audit de admin users 2. Implement least privilege principle 3. Use Just-In-Time (JIT) access 4. MFA mandatory for admins |
| **Responsável** | IAM Architect |
| **Prazo** | 30 dias |

---

### RISK-006: Tokens Comprometidos (Compromised Credentials)

| Campo | Valor |
|-------|-------|
| **ID** | RISK-006 |
| **Categoria** | Authentication |
| **Descrição** | Tokens JWT, session keys ou passwords expostos ou stolen |
| **Probabilidade** | 🟠 MÉDIA (55%) |
| **Impacto** | 🟠 ALTO (8/10) |
| **Prioridade** | 🟠 P2 - ALTO |
| **Score de Risco** | 7.2/10 |
| **Estratégia** | **Mitigar** |
| **Plano de Ação** | 1. Implement token rotation policy 2. Monitor for leaked credentials 3. Force password reset if compromised 4. Enable conditional access |
| **Responsável** | Security Operations |
| **Prazo** | 14 dias |

---

### RISK-007: MFA Desabilitado (Multi-Factor Auth Disabled)

| Campo | Valor |
|-------|-------|
| **ID** | RISK-007 |
| **Categoria** | Authentication |
| **Descrição** | Usuários desabilitam MFA ou usam métodos fracos de 2FA |
| **Probabilidade** | 🟠 MÉDIA (60%) |
| **Impacto** | 🟠 ALTO (8/10) |
| **Prioridade** | 🟠 P2 - ALTO |
| **Score de Risco** | 7.0/10 |
| **Estratégia** | **Mitigar** |
| **Plano de Ação** | 1. Make MFA mandatory (policy) 2. Remove weak 2FA methods 3. Enforce authenticators 4. Monitor MFA status |
| **Responsável** | Authentication Lead |
| **Prazo** | 21 dias |

---

### RISK-008: Identity Provider Indisponível (IdP Downtime)

| Campo | Valor |
|-------|-------|
| **ID** | RISK-008 |
| **Categoria** | Availability |
| **Descrição** | IdP (Active Directory, Azure AD) fica offline, impactando toda autenticação |
| **Probabilidade** | 🟠 BAIXA-MÉDIA (30%) |
| **Impacto** | 🟠 ALTO (8/10) |
| **Prioridade** | 🟠 P2 - ALTO |
| **Score de Risco** | 6.0/10 |
| **Estratégia** | **Mitigar** |
| **Plano de Ação** | 1. Implement IdP redundancy 2. Cache authentication data 3. Failover automation 4. Recovery procedures |
| **Responsável** | Infrastructure Lead |
| **Prazo** | 90 dias |

---

### RISK-009: Provisionamento Incorreto (Incorrect Provisioning)

| Campo | Valor |
|-------|-------|
| **ID** | RISK-009 |
| **Categoria** | Access Management |
| **Descrição** | Erros na provisionamento dão acesso incorreto ou acesso de menos |
| **Probabilidade** | 🟠 MÉDIA (50%) |
| **Impacto** | 🟠 ALTO (7/10) |
| **Prioridade** | 🟠 P2 - ALTO |
| **Score de Risco** | 6.5/10 |
| **Estratégia** | **Mitigar** |
| **Plano de Ação** | 1. Implement approval workflow 2. Validation of provisioning 3. Automated testing 4. Audit trails |
| **Responsável** | Access Management Lead |
| **Prazo** | 30 dias |

---

## 🟡 RISCOS MÉDIOS

### RISK-010: Revogação Tardia (Late Revocation)

| Campo | Valor |
|-------|-------|
| **ID** | RISK-010 |
| **Categoria** | Lifecycle |
| **Descrição** | Acesso não é revogado rapidamente quando necessário |
| **Probabilidade** | 🟡 MÉDIA (60%) |
| **Impacto** | 🟡 MÉDIO (6/10) |
| **Prioridade** | 🟡 P3 - MÉDIO |
| **Score de Risco** | 5.4/10 |
| **Estratégia** | **Mitigar** |
| **Plano de Ação** | 1. Automate revocation process 2. Reduce approval cycle 3. Real-time revocation API 4. Escalation procedures |
| **Responsável** | Operations Lead |
| **Prazo** | 45 dias |

---

### RISK-011: Recomendações Incorretas da IA

| Campo | Valor |
|-------|-------|
| **ID** | RISK-011 |
| **Categoria** | AI/ML |
| **Descrição** | LLM fornece recomendações incorretas ou prejudiciais |
| **Probabilidade** | 🟡 MÉDIA (45%) |
| **Impacto** | 🟡 MÉDIO (7/10) |
| **Prioridade** | 🟡 P3 - MÉDIO |
| **Score de Risco** | 5.6/10 |
| **Estratégia** | **Mitigar** |
| **Plano de Ação** | 1. Implement output validation 2. Human approval gates 3. Confidence thresholds 4. Feedback loops |
| **Responsável** | AI Lead |
| **Prazo:** | 30 dias |

---

### RISK-012: Prompt Injection Attacks

| Campo | Valor |
|-------|-------|
| **ID** | RISK-012 |
| **Categoria** | AI/Security |
| **Descrição** | Attacker injeta malicious prompts para manipular LLM |
| **Probabilidade** | 🟡 BAIXA-MÉDIA (35%) |
| **Impacto** | 🟡 MÉDIO (7/10) |
| **Prioridade** | 🟡 P3 - MÉDIO |
| **Score de Risco** | 4.9/10 |
| **Estratégia** | **Mitigar** |
| **Plano de Ação** | 1. Input sanitization 2. Prompt escaping 3. Context boundaries 4. Output validation |
| **Responsável** | Security Engineer |
| **Prazo:** | 21 dias |

---

### RISK-013: Vazamento de Logs (Log Leakage)

| Campo | Valor |
|-------|-------|
| **ID** | RISK-013 |
| **Categoria** | Data Protection |
| **Descrição** | Logs contém dados sensíveis e são expostos |
| **Probabilidade** | 🟡 BAIXA-MÉDIA (40%) |
| **Impacto** | 🟡 MÉDIO (6/10) |
| **Prioridade** | 🟡 P3 - MÉDIO |
| **Score de Risco** | 4.8/10 |
| **Estratégia** | **Mitigar** |
| **Plano de Ação** | 1. Log redaction rules 2. Encryption at rest 3. Access controls on logs 4. Regular audit |
| **Responsável** | Security Operations |
| **Prazo:** | 30 dias |

---

### RISK-014: Erro na Classificação de Criticidade

| Campo | Valor |
|-------|-------|
| **ID** | RISK-014 |
| **Categoria** | Risk Management |
| **Descrição** | Riscos são classificados com severidade incorreta |
| **Probabilidade** | 🟡 MÉDIA (50%) |
| **Impacto** | 🟡 MÉDIO (5/10) |
| **Prioridade** | 🟡 P3 - MÉDIO |
| **Score de Risco** | 4.5/10 |
| **Estratégia** | **Mitigar** |
| **Plano de Ação** | 1. Define clear classification criteria 2. Automated scoring 3. Expert review gate 4. Continuous refinement |
| **Responsável** | Risk Manager |
| **Prazo:** | 14 dias |

---

### RISK-015: Acesso Administrativo Indevido

| Campo | Valor |
|-------|-------|
| **ID** | RISK-015 |
| **Categoria** | Access Control |
| **Descrição** | Acesso administrative concedido sem aprovação adequada |
| **Probabilidade** | 🟡 BAIXA-MÉDIA (35%) |
| **Impacto** | 🟡 MÉDIO (7/10) |
| **Prioridade** | 🟡 P3 - MÉDIO |
| **Score de Risco** | 4.9/10 |
| **Estratégia** | **Mitigar** |
| **Plano de Ação** | 1. Implement approval workflow 2. Manager review required 3. Audit all admin access 4. Regular reviews |
| **Responsável** | Access Manager |
| **Prazo:** | 30 dias |

---

### RISK-016: Dependência do IdP Externo

| Campo | Valor |
|-------|-------|
| **ID** | RISK-016 |
| **Categoria** | Vendor Management |
| **Descrição** | Dependência crítica de fornecedor externo (Azure AD, Okta) |
| **Probabilidade** | 🟡 BAIXA (25%) |
| **Impacto** | 🟡 MÉDIO (6/10) |
| **Prioridade** | 🟡 P3 - MÉDIO |
| **Score de Risco** | 3.8/10 |
| **Estratégia** | **Aceitar + Mitigar** |
| **Plano de Ação** | 1. Maintain SLA contracts 2. Have fallback IdP 3. Regular testing 4. Vendor management |
| **Responsável** | Vendor Manager |
| **Prazo:** | 90 dias |

---

### RISK-017: Falha na Auditoria (Audit Failure)

| Campo | Valor |
|-------|-------|
| **ID** | RISK-017 |
| **Categoria** | Compliance |
| **Descrição** | Auditoria não consegue rastrear todas as ações |
| **Probabilidade** | 🟡 BAIXA-MÉDIA (30%) |
| **Impacto** | 🟡 MÉDIO (6/10) |
| **Prioridade** | 🟡 P3 - MÉDIO |
| **Score de Risco** | 3.6/10 |
| **Estratégia** | **Mitigar** |
| **Plano de Ação** | 1. Implement comprehensive logging 2. Immutable audit trail 3. Real-time monitoring 4. Regular testing |
| **Responsável** | Compliance Lead |
| **Prazo:** | 60 dias |

---

## 🟢 RISCOS BAIXOS

### RISK-018: Não Conformidade com ISO 27001

| Campo | Valor |
|-------|-------|
| **ID** | RISK-018 |
| **Categoria** | Compliance |
| **Descrição** | Processos não estão alinhados com ISO 27001 |
| **Probabilidade** | 🟢 BAIXA (20%) |
| **Impacto** | 🟢 BAIXO (4/10) |
| **Prioridade** | 🟢 P4 - BAIXO |
| **Score de Risco** | 2.4/10 |
| **Estratégia** | **Mitigar** |

---

### RISK-019: Não Conformidade com LGPD

| Campo | Valor |
|-------|-------|
| **ID** | RISK-019 |
| **Categoria** | Compliance |
| **Descrição** | Processamento de dados não segue LGPD |
| **Probabilidade** | 🟢 BAIXA (15%) |
| **Impacto** | 🟢 BAIXO (4/10) |
| **Prioridade** | 🟢 P4 - BAIXO |
| **Score de Risco** | 2.0/10 |
| **Estratégia** | **Mitigar** |

---

### RISK-020: Quebra de Trilha de Auditoria

| Campo | Valor |
|-------|-------|
| **ID** | RISK-020 |
| **Categoria** | Compliance |
| **Descrição** | Trilha de auditoria tem gaps ou inconsistências |
| **Probabilidade** | 🟢 BAIXA (25%) |
| **Impacto** | 🟢 BAIXO (3/10) |
| **Prioridade** | 🟢 P4 - BAIXO |
| **Score de Risco** | 1.9/10 |
| **Estratégia** | **Aceitar** |

---

## 📊 Estatísticas de Riscos

\\\
Distribuição por Severidade:
- Crítico:  3 riscos (15%)
- Alto:     6 riscos (30%)
- Médio:    8 riscos (40%)
- Baixo:    3 riscos (15%)

Distribuição por Probabilidade:
- Muito Alta (70-80%): 3 riscos
- Alta (50-69%): 6 riscos
- Média (30-49%): 8 riscos
- Baixa (<30%): 3 riscos

Distribuição por Estratégia:
- Mitigar: 16 riscos (80%)
- Aceitar: 2 riscos (10%)
- Evitar: 2 riscos (10%)
\\\

---

**Versão:** 1.0.0 | **Data:** 2026-07-21 | **Status:** ACTIVE
