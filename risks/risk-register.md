# ⚠️ Risk Register - Identity Risk Governance

[![Version](https://img.shields.io/badge/registry-v1.0-blue.svg)]()
[![Update](https://img.shields.io/badge/last_update-2026--07--21-green.svg)]()
[![Risks](https://img.shields.io/badge/total_risks-23-red.svg)]()

## 📋 Resumo Executivo

Este registro contém todos os riscos identificados no programa de governança de identidade corporativa, com análise qualitativa, estratégias de resposta e planos de ação baseados em PMBOK.

---

## 📊 Distribuição de Riscos por Severidade

| Severidade | Quantidade | % | Trend |
|-----------|-----------|---|-------|
| 🔴 **CRÍTICO** | 5 | 22% | ↘️ |
| 🟠 **ALTO** | 9 | 39% | → |
| 🟡 **MÉDIO** | 7 | 30% | ↗️ |
| 🟢 **BAIXO** | 2 | 9% | → |
| **TOTAL** | **23** | 100% | |

---

## 🔴 RISCOS CRÍTICOS

### RISK-001: Violação de Segregação de Deveres (SoD)

| Campo | Valor |
|-------|-------|
| **Categoria** | Compliance & Governance |
| **Probabilidade** | MÉDIA (0.65) |
| **Impacto** | CRÍTICO (0.95) |
| **Prioridade** | 1 |
| **Status** | ATIVO |
| **Owner** | GRC Manager |
| **Data Identificação** | 2026-06-15 |

**Descrição**:
Usuários possuem combinações de permissões conflitantes que violam princípios de segregação de deveres, como acumular funções de autorização e auditoria na mesma conta.

**Cenário de Risco**:
Um usuário administrativo com permissão de "Aprovar Transferências" e "Auditar Transferências" na mesma conta pode encobrir fraudes.

**Impacto Potencial**:
- Fraude financeira não detectada
- Violação de conformidade ISO 27001
- Penalidades regulatórias (BACEN, CVM)
- Perda de reputação corporativa
- Potencial perda de R$ 10M+

**Controles Existentes**:
- ✅ Política de SoD documentada
- ❌ Enforcement automático (não implementado)
- ❌ Alertas em tempo real (não implementado)

**Estratégia**: **MITIGAR**

**Plano de Ação**:
1. **Fase 1** (0-30 dias): Auditoria de SoD atual
   - Varrimento completo de 8000 usuários
   - Identificação de violações
   - Mapeamento de conflitos
   - **Responsável**: GRC Team
   - **Esforço**: 160 horas
   
2. **Fase 2** (30-60 dias): Remediação
   - Separação de contas onde viável
   - Criação de roles balanceados
   - Aprovação de exceções
   - **Responsável**: IAM + GRC
   - **Esforço**: 240 horas
   
3. **Fase 3** (60-90 dias): Enforcement
   - Implementar regras automáticas
   - Configurar alertas
   - Validação de 100% de novos acessos
   - **Responsável**: Security Ops
   - **Esforço**: 80 horas

**Indicadores de Sucesso**:
- ✅ 100% de conformidade SoD
- ✅ Zero novos casos de violação
- ✅ Compliance audit passa
- ✅ Tempo de detecção < 1 min

**Custo Estimado**: R$ 120,000

---

### RISK-002: Privilege Creep em Contas Administrativas

| Campo | Valor |
|-------|-------|
| **Categoria** | Access Management |
| **Probabilidade** | MÉDIA (0.60) |
| **Impacto** | CRÍTICO (0.90) |
| **Prioridade** | 2 |
| **Status** | ATIVO |
| **Owner** | IAM Manager |
| **Data Identificação** | 2026-06-20 |

**Descrição**:
Acúmulo gradual de permissões em contas administrativas ao longo do tempo, sem revisão ou revogação periódica.

**Cenário de Risco**:
Um DBA tem 450+ permissões após 8 anos, incluindo acesso a dados financeiros, recursos de RH, sistemas críticos de produção e ambiente de testes.

**Impacto Potencial**:
- Insider threat aumentado
- Violação não intencional de princípio de least privilege
- Risco de comprometimento total da identidade
- Impossibilidade de auditoria

**Evidência**:
- 156 admins com média de 320 permissões cada
- 12 admins com > 500 permissões
- Aumento de 2.3% ao mês em média

**Estratégia**: **MITIGAR**

**Plano de Ação**:
1. Implementar access reviews trimestrais obrigatórias
2. Automação de detecção de privilege creep via IA
3. Dashboard de "permission trending" por usuário
4. Alertas quando ↑20% de permissões em 30 dias
5. Revogação automática de permissões não-utilizadas > 90 dias

**Responsável**: IAM Manager  
**Custo**: R$ 85,000  
**Timeline**: 60 dias

---

### RISK-003: Contas Órfãs em Sistemas Críticos

| Campo | Valor |
|-------|-------|
| **Categoria** | Access Control |
| **Probabilidade** | MÉDIA (0.55) |
| **Impacto** | CRÍTICO (0.95) |
| **Prioridade** | 3 |
| **Status** | DETECTADO |
| **Owner** | IAM Manager |
| **Data Identificação** | 2026-07-10 |

**Descrição**:
Contas de usuários sem proprietário designado, sem supervisor, ou órfãs após saída de funcionários.

**Cenário de Risco**:
Conta de ex-funcionário "carlos.silva" com acesso a 47 sistemas críticos permanece ativa 6 meses após demissão.

**Impacto Potencial**:
- Acesso não autorizado a sistemas críticos
- Fraude corporativa
- Vazamento de dados sensíveis
- Violação LGPD

**Evidência**:
- **47 contas órfãs identificadas** em scan recente
- 23 em sistemas de produção críticos
- 5 com acesso a dados sensíveis (PII)

**Estratégia**: **EVITAR + MITIGAR**

**Plano de Ação**:
1. **Imediato (24 horas)**: Desabilitar contas órfãs críticas
2. **48 horas**: Auditoria completa de todas as 47 contas
3. **1 semana**: Deprovisioning das contas confirmadas como órfãs
4. **30 dias**: Implementar processo de ownership assignment
5. **60 dias**: Implementar automated lifecycle management

**Responsável**: IAM Team  
**Custo**: R$ 45,000  
**Timeline**: 30 dias urgente

---

### RISK-004: Identity Provider Indisponível

| Campo | Valor |
|-------|-------|
| **Categoria** | Infrastructure & Resilience |
| **Probabilidade** | BAIXA (0.15) |
| **Impacto** | CRÍTICO (0.98) |
| **Prioridade** | 4 |
| **Status** | PREVENTIVO |
| **Owner** | Infrastructure Manager |
| **Data Identificação** | 2026-05-30 |

**Descrição**:
Falha total do Identity Provider (Okta/Azure AD) resultaria em negação de acesso para todos os 8000 usuários corporativos.

**Cenário de Risco**:
Outage de 3+ horas no IdP durante horário de negócio → Operações paralisa.

**Impacto Potencial**:
- 8000+ usuários sem acesso
- Negócio parado completamente
- SLA violado
- Prejuízo estimado: R$ 500K/hora
- Reputação afetada
- Clientes impactados

**Controles Existentes**:
- Single point of failure (Okta Production)
- RTO: N/A (sem DR)
- RPO: N/A (sem DR)

**Estratégia**: **MITIGAR + TRANSFERIR**

**Plano de Ação**:
1. Implementar redundância de IdP (dual-region)
2. Configurar failover automático (< 5 minutos)
3. Contrato de DR com provider (SLA 99.99%)
4. Cache local de tokens (emergency mode)
5. Testes de failover mensais
6. Seguro de cyber (risk transfer)

**Responsável**: Infrastructure Manager  
**Custo**: R$ 300,000 (anual)  
**Timeline**: 90 dias

---

### RISK-005: Recomendações Incorretas da IA

| Campo | Valor |
|-------|-------|
| **Categoria** | AI & Automation |
| **Probabilidade** | MÉDIA (0.50) |
| **Impacto** | CRÍTICO (0.85) |
| **Prioridade** | 5 |
| **Status** | MITIGANDO |
| **Owner** | Security Director |
| **Data Identificação** | 2026-07-01 |

**Descrição**:
O LLM gera recomendações de segurança inválidas, inaplicáveis ou potencialmente prejudiciais.

**Cenário de Risco**:
IA recomenda revogar permissão de "System Administrator" do DBA critical.db, causando falha em backup automatizado noturno.

**Impacto Potencial**:
- Serviço comprometido/interrompido
- Reputação em risco
- Confiança em AI reduzida
- Potencial SLA violation
- Incident investigation custoso

**Mitigação em Andamento**:
- ✅ Implementar validação humana obrigatória
- ✅ Confidence score thresholds (min 0.75)
- ✅ Testing em staging antes de produção
- ⏳ Feedback loop para treinar modelo

**Estratégia**: **MITIGAR**

**Plano de Ação**:
1. Validação humana de 100% de recomendações críticas/altas
2. Implementar confidence scoring (0.0-1.0)
3. Rejeitar automaticamente se confidence < 0.70
4. Testes de acurácia mensal
5. Feedback loop com histórico de validações
6. Fine-tuning com dados corporativos trimestral

**Responsável**: Security Director  
**Custo**: R$ 80,000  
**Timeline**: 45 dias

---

## 🟠 RISCOS ALTOS

### RISK-006: MFA Desabilitado em Contas Críticas

| Campo | Valor |
|-------|-------|
| **Categoria** | Authentication |
| **Probabilidade** | ALTA (0.75) |
| **Impacto** | ALTO (0.80) |
| **Prioridade** | 6 |
| **Status** | ATIVO |
| **Owner** | Security Manager |

**Descrição**: 156 contas administrativas sem MFA habilitado.

**Impacto**: Credential compromise risco = 5x maior

**Plano de Ação**: 
1. Enforce MFA obrigatória (30 dias)
2. Monitorar compliance (diário)
3. Escalação automática de exceções
4. Educação de usuários

**Custo**: R$ 15,000  
**Timeline**: 30 dias

---

### RISK-007: Prompt Injection em Sistema de IA

| Campo | Valor |
|-------|-------|
| **Categoria** | AI Security |
| **Probabilidade** | MÉDIA (0.45) |
| **Impacto** | ALTO (0.82) |
| **Prioridade** | 7 |
| **Status** | MONITORADO |
| **Owner** | Security Engineer |

**Descrição**: Usuário manipula prompts para bypass de regras de segurança.

**Cenário**: Input injection causa IA gerar recomendações maliciosas.

**Mitigação**:
- Input sanitization + validation
- Rate limiting por usuário
- Audit trail de todas as interações IA
- Anomaly detection

**Custo**: R$ 40,000  
**Timeline**: 60 dias

---

### RISK-008: Revogação Tardia de Permissões

| Campo | Valor |
|-------|-------|
| **Categoria** | Lifecycle Management |
| **Probabilidade** | ALTA (0.80) |
| **Impacto** | ALTO (0.75) |
| **Prioridade** | 8 |
| **Status** | ATIVO |

**Descrição**: Delay de dias a semanas na revogação de permissões após saída de funcionário.

**Impacto**: Ex-funcionários com acesso continuado.

**Plano de Ação**:
1. Automation de offboarding (< 1 hora)
2. APIs integradas com RH system
3. Alertas de contas ativas após término

**Custo**: R$ 60,000  
**Timeline**: 45 dias

---

### RISK-009: Tokens Comprometidos

| Campo | Valor |
|-------|-------|
| **Categoria** | Secrets Management |
| **Probabilidade** | MÉDIA (0.50) |
| **Impacto** | ALTO (0.88) |
| **Prioridade** | 9 |
| **Status** | MITIGANDO |

**Descrição**: API tokens ou sessão tokens vazados/expostos.

**Mitigação**:
- Token rotation policy (15 dias)
- Vault centralizado (HashiCorp)
- Encryption at-rest + in-transit
- Token invalidation on-demand

**Custo**: R$ 70,000  
**Timeline**: 60 dias

---

### RISK-010: Classificação Incorreta de Criticidade

| Campo | Valor |
|-------|-------|
| **Categoria** | Risk Management |
| **Probabilidade** | MÉDIA (0.55) |
| **Impacto** | ALTO (0.78) |
| **Prioridade** | 10 |
| **Status** | MITIGANDO |

**Descrição**: Riscos classificados com severidade incorreta.

**Exemplo**: CRÍTICO marcado como BAIXO → ações não tomadas.

**Mitigação**:
- Validation rules na classificação
- LLM double-check automático
- Manual review de edge cases
- Auditoria mensal

**Custo**: R$ 25,000  
**Timeline**: 30 dias

---

### RISK-011: Vazamento de Informações em Logs

| Campo | Valor |
|-------|-------|
| **Categoria** | Data Protection |
| **Probabilidade** | MÉDIA (0.50) |
| **Impacto** | ALTO (0.85) |
| **Prioridade** | 11 |
| **Status** | MITIGANDO |

**Descrição**: Logs contêm PII, senhas, tokens ou dados sensíveis.

**Mitigação**:
- Data masking automático
- Encryption de logs
- Access control restrito
- Purga automática

**Custo**: R$ 50,000

---

### RISK-012: Provisionamento Incorreto de Acesso

| Campo | Valor |
|-------|-------|
| **Categoria** | Identity Management |
| **Probabilidade** | MÉDIA (0.60) |
| **Impacto** | ALTO (0.72) |
| **Prioridade** | 12 |
| **Status** | ATIVO |

**Descrição**: Usuários recebem permissões incorretas ou excessivas durante onboarding.

**Impacto**: Privilege escalation inadvertida.

**Plano de Ação**:
- Approval workflow obrigatório
- Validação de JD vs. permissões
- IA checking para anomalias
- Auditoria de provisioning

**Custo**: R$ 35,000

---

---

## 🟡 RISCOS MÉDIOS

### RISK-013: Shadow Identities

| Campo | Valor |
|-------|-------|
| **Categoria** | Identity Governance |
| **Probabilidade** | MÉDIA (0.55) |
| **Impacto** | MÉDIO (0.65) |
| **Prioridade** | 13 |

**Descrição**: Contas paralelas/alternativas criadas para bypass de controles.

**Mitigação**: Scanning automático, alertas, políticas de contas únicas.

---

### RISK-014: Falha em Auditoria Contínua

| Campo | Valor |
|-------|-------|
| **Categoria** | Audit & Compliance |
| **Probabilidade** | BAIXA (0.30) |
| **Impacto** | CRÍTICO (0.92) |
| **Prioridade** | 14 |

**Descrição**: Trilha de auditoria incompleta, perdida ou não confiável.

---

### RISK-015: Não Conformidade com ISO 27001

| Campo | Valor |
|-------|-------|
| **Categoria** | Compliance |
| **Probabilidade** | BAIXA (0.25) |
| **Impacto** | ALTO (0.88) |
| **Prioridade** | 15 |

---

### RISK-016: Não Conformidade com LGPD

| Campo | Valor |
|-------|-------|
| **Categoria** | Regulatory |
| **Probabilidade** | MÉDIA (0.50) |
| **Impacto** | CRÍTICO (0.95) |
| **Prioridade** | 16 |

**Descrição**: Processamento de dados pessoais sem consentimento ou fora da política.

**Mitigação**: Privacy impact assessment, data minimization, encryption.

---

### RISK-017: Acesso Administrativo Indevido

| Campo | Valor |
|-------|-------|
| **Categoria** | Administration |
| **Probabilidade** | MÉDIA (0.50) |
| **Impacto** | CRÍTICO (0.90) |
| **Prioridade** | 17 |

---

### RISK-018: Dependência Crítica do IdP

| Campo | Valor |
|-------|-------|
| **Categoria** | Architecture |
| **Probabilidade** | BAIXA (0.25) |
| **Impacto** | CRÍTICO (0.98) |
| **Prioridade** | 18 |

---

### RISK-019: Política de Retenção Inadequada

| Campo | Valor |
|-------|-------|
| **Categoria** | Records Management |
| **Probabilidade** | MÉDIA (0.55) |
| **Impacto** | MÉDIO (0.68) |
| **Prioridade** | 19 |

---

## 🟢 RISCOS BAIXOS

### RISK-020: Falta de Documentação de Políticas

| Campo | Valor |
|-------|-------|
| **Categoria** | Governance |
| **Probabilidade** | BAIXA (0.20) |
| **Impacto** | BAIXO (0.45) |
| **Prioridade** | 20 |

---

### RISK-021: Comunicação Deficiente com Stakeholders

| Campo | Valor |
|-------|-------|
| **Categoria** | Communication |
| **Probabilidade** | BAIXA (0.30) |
| **Impacto** | BAIXO (0.50) |
| **Prioridade** | 21 |

---

### RISK-022: Excesso de Privilégios em Grupos

| Campo | Valor |
|-------|-------|
| **Categoria** | Access Control |
| **Probabilidade** | MÉDIA (0.60) |
| **Impacto** | MÉDIO (0.70) |
| **Prioridade** | 22 |

---

### RISK-023: Falta de Monitoramento 24/7

| Campo | Valor |
|-------|-------|
| **Categoria** | Security Operations |
| **Probabilidade** | BAIXA (0.35) |
| **Impacto** | MÉDIO (0.75) |
| **Prioridade** | 23 |

---

## 📈 Resumo por Status

| Status | Quantidade | % | Ação |
|--------|-----------|---|------|
| 🔴 **ATIVO** | 8 | 35% | Remediação em curso |
| 🟠 **DETECTADO** | 3 | 13% | Aguardando aprovação |
| 🟡 **MITIGANDO** | 7 | 30% | Controles em implementação |
| 🟢 **PREVENTIVO** | 5 | 22% | Monitorando para evitar |

---

## 📞 Gerenciamento de Riscos

**Próxima Revisão**: 21 de Agosto de 2026  
**Proprietário do Registro**: GRC Manager  
**Aprovação**: CIO / CISO  
**Frequência de Atualização**: Semanal  

**Contato**:
- governance@company.com
- +55 (XX) XXXXX-XXXX

