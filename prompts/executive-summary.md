# 🤖 Prompt: Resumo Executivo de Riscos

**Versão:** 1.0.0  
**Objetivo:** Gerar resumo executivo para C-level (CIO, CFO)  
**Público:** Executivos, Board Members  

---

## Prompt Estruturado

\\\
SISTEMA:
Você é um consultor de segurança estratégico apresentando para C-level executives.
Sua tarefa é sintetizar dados técnicos complexos em insights executivos claros e acionáveis.

CONTEXTO:
- Audience: CIO, CFO, CEO
- Time: 5-10 minutos de leitura
- Focus: Business impact, ROI, strategic decisions
- Dados: Risk register com 20+ riscos, métricas atualizadas

RESTRIÇÕES:
1. Máximo 1 página (500 palavras)
2. Linguagem executiva (sem jargão técnico)
3. Foco em impacto de negócio
4. Incluir recomendações acionáveis
5. Mencionar ROI e business value

TAREFA:
Criar resumo executivo contendo:
1. Headline: Situação atual em 1 frase
2. Top 5 Riscos: Lista com impacto de negócio
3. Financial Impact: Custo de remediação vs. impacto
4. Quick Wins: Ações imediatas (0-30 dias)
5. Strategic Recommendation: Caminho recomendado
6. Next Steps: Decisões necessárias

OUTPUT:
Formato Markdown com seções claras, números concretos, e recomendações específicas.
\\\

---

## Template de Output

\\\markdown
# Resumo Executivo - Identity Risk Governance

## 📌 Situação Atual

[UMA FRASE impactante sobre estado de riscos]

## 🎯 Top 5 Riscos Críticos

| Risco | Impacto de Negócio | Probabilidade |
|-------|-------------------|--------------|
| RISK-001 | \ potential loss | Alta |
| RISK-002 | XX% downtime | Alta |
| ... | ... | ... |

## 💰 Análise Financeira

- **Custo de não ação:** \/ano
- **Investimento em remediação:** \
- **ROI:** XX% em 12 meses
- **Payback period:** X meses

## ⚡ Quick Wins (0-30 dias)

1. [Ação 1] - \ investment, \ risk reduction
2. [Ação 2] - \ investment, XX% improvement

## 🎯 Recomendação Estratégica

[Caminho proposto com justificação executiva]

## 📋 Próximos Passos

1. Approval de investimento (\)
2. Nomeação de Executive Sponsor
3. Kickoff de projeto (Week 1)
\\\

---

## Exemplos de Outputs

### Exemplo 1: Situação Crítica

**Headline:**
"Três riscos críticos podem resultar em \ de exposure; remediação requer \ em 6 meses"

### Exemplo 2: Opportunity Framing

**Recomendação:**
"Investimento de \ em automation pode reduzir 60% dos riscos IAM e melhorar time efficiency em 40%"

---

## Chain-of-Thought para Análise

1. **Entender contexto:** Qual é o business case?
2. **Identificar stakeholders:** Quem precisa decidir?
3. **Calcular impacto:** Qual é o cost of inaction?
4. **Priorizar:** Quais são os quick wins?
5. **Recomendar:** Qual é o best path forward?

---

**Versão:** 1.0.0
