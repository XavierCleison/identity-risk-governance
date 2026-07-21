# 🤖 Guia de Uso de IA/LLM - Identity Risk Governance

## 1. Visão Geral

O **Identity Risk Governance** integra modelos de linguagem (LLMs) para análise contextual e recomendações inteligentes de remediação de riscos IAM.

### LLMs Suportados

| Modelo | Provider | Capacidade | Custo/1M tokens |
|--------|----------|-----------|-----------------|
| GPT-4o | OpenAI | Análise avançada | \ |
| Claude 3.5 | Anthropic | Análise profunda | \-15 |
| GPT-3.5 | OpenAI | Análise básica | \.50 |
| Llama 2 | Meta | Self-hosted | Variável |

---

## 2. Casos de Uso de IA

### 2.1 Identificação de Riscos
**Objetivo:** Análise contextual de padrões de acesso anormais

\\\
Input: User profile, access logs, peer group data
Process: LLM analyzes patterns and historical data
Output: Risk identification with context
\\\

**Exemplo:**
- Usuário alterou comportamento de acesso
- Login de nova localização geográfica
- Acesso a recursos não-típicos
- → Recomendação: Investigar possível comprometimento

### 2.2 Análise Qualitativa de Riscos
**Objetivo:** Avaliação contextual de probabilidade e impacto

**Input:**
- Risco identificado
- Contexto de negócio
- Dados históricos
- Métricas de impacto

**Output:**
- Probabilidade assesssment
- Impacto assessment  
- Prioridade recomendada
- Score de risco contextual

### 2.3 Geração de Recomendações
**Objetivo:** Planos de remediação personalizados

**Exemplo de Recomendação:**
`
Risco: Privilege Creep detectado para john.doe@company.com

Contexto:
- 45 permissões acumuladas em 18 meses
- Acesso a 3 sistemas críticos
- SoD violation: Pode criar e aprovar ordens de compra

Recomendação IA:
1. Revoke 20 permissions not used in 90 days (Confidence: 95%)
2. Implement SoD rule enforcement (Risk reduction: 80%)
3. Enable automated access reviews (Quarterly)
4. Escalate to manager for final approval (Required)

Plano de Ação:
- Imediato: Revoke unused permissions
- Semana 1: Implement SoD rules
- Semana 4: Setup access reviews
- Ongoing: Monitor access patterns
`

### 2.4 Geração de Resumos Executivos
**Objetivo:** Síntese de riscos em linguagem executiva

**Input:**
- Riscos da semana
- Padrões de remediação
- Métricas de sucesso
- Próximas ações

**Output:**
- Resumo executivo (1 página)
- Top risks
- Roadmap de ações
- Métricas de sucesso

### 2.5 Relatórios de Conformidade
**Objetivo:** Geração automática de relatórios regulatórios

**Output:**
- ISO 27001 compliance report
- LGPD compliance certificate
- GDPR data processing report
- SOC 2 readiness assessment

---

## 3. Arquitetura de Prompts

### 3.1 Estrutura de Prompt

\\\
SISTEMA: [Contexto e role do LLM]

CONTEXTO:
- Dados do usuário
- Histórico de acessos
- Políticas de segurança
- Padrões de risco

TAREFA: [Específica e clara]

RESTRIÇÕES:
- Não incluir dados pessoais
- Manter conformidade LGPD
- Validar outputs

FORMATO: [JSON/Markdown/Estruturado]

INPUT: [Dados específicos]

OUTPUT: [Esperado]
\\\

### 3.2 Técnicas de Prompting

**Chain-of-Thought:**
`
Passo 1: Analisar padrões de acesso
Passo 2: Comparar com grupo de pares
Passo 3: Avaliar probabilidade de risco
Passo 4: Calcular impacto potencial
Passo 5: Gerar recomendação
`

**Few-Shot Learning:**
`
Exemplo 1: Privilege creep → Risco CRÍTICO
Exemplo 2: Contas órfãs → Risco CRÍTICO
Exemplo 3: MFA desabilitado → Risco ALTO

Agora analise este caso: [novo caso]
`

---

## 4. Controles de Segurança

### 4.1 Prevenção de Prompt Injection

**Técnicas:**
- ✅ Input sanitization
- ✅ Semantic escaping
- ✅ Context boundaries
- ✅ Output validation

**Exemplo de Proteção:**
`python
# Sanitize user input
user_input = sanitize_prompt(user_input)

# Add context boundary
system_prompt = "You are a security analyst. You can only discuss..."

# Validate output
validated_output = validate_against_schema(llm_output)
`

### 4.2 Proteção de Dados Sensíveis

**Antes de enviar para LLM:**
- ✅ Remover PII (nomes, emails, CPF)
- ✅ Anonimizar IDs de usuário
- ✅ Criptografar dados sensíveis
- ✅ Usar synthetic examples

**Exemplo:**
`
ANTES: "john.doe@company.com acessou BD_CUSTOMERS"
DEPOIS: "USER_001 acessou DB_CUSTOMER_DATA"
`

### 4.3 Validação de Outputs

**Antes de usar recomendação da IA:**

1. ✅ **Schema Validation**: Output segue formato esperado
2. ✅ **Sanity Check**: Recomendação é razoável
3. ✅ **Confidence Score**: Confiança > threshold
4. ✅ **Expert Review**: Revisão humana para críticos
5. ✅ **Audit Trail**: Log completo de decisão

---

## 5. Prompts Utilizados

### Arquivo: prompts/identify-risks.md
Utilizado para identificar riscos de identidade

### Arquivo: prompts/executive-summary.md
Utilizado para resumir riscos para executivos

### Arquivo: prompts/stakeholder-report.md
Utilizado para comunicar riscos a stakeholders

---

## 6. Governança de IA

### 6.1 Políticas

| Política | Descrição |
|----------|-----------|
| **Usage Policy** | Quando e como usar IA |
| **Cost Policy** | Orçamento máximo por modelo |
| **Quality Policy** | Padrão de qualidade mínimo |
| **Audit Policy** | Logging e compliance |

### 6.2 Governança de Modelos

- ✅ Version pinning (sempre usar versão conhecida)
- ✅ Approval gate para novos modelos
- ✅ Quarterly performance reviews
- ✅ ROI tracking

### 6.3 Conformidade

- ✅ LGPD: Sem dados pessoais em prompts
- ✅ GDPR: Right to explanation
- ✅ ISO 27001: Auditoria completa
- ✅ SOC 2: Logging de todas as decisões

---

## 7. Métricas de IA

| Métrica | Alvo | Frequência |
|---------|------|-----------|
| Acurácia de detecção | > 95% | Semanal |
| Taxa de falsos positivos | < 5% | Semanal |
| Confiança média | > 0.85 | Semanal |
| Latência P95 | < 5s | Diária |
| Custo/requisição | < \.01 | Mensal |

---

## 8. Troubleshooting

### Problema: Recomendações inconsistentes
**Solução:** Aumentar temperature para determinismo

### Problema: Dados sensíveis no output
**Solução:** Adicionar validação de regex + manual review

### Problema: Latência alta
**Solução:** Usar modelo menor ou cache de resultados

---

**Versão:** 1.0.0 | **Data:** 2026-07-21
