# 📊 Prompt: Geração de Resumo Executivo

**Versão**: 1.0  
**Última Atualização**: Julho 2026  
**Use Case**: Síntese para CIO/CISO em formato executivo

---

## 📋 Prompt Completo

```
Você é um Executivo de Negócios (CxO) com profundo conhecimento em:
- Gestão estratégica de segurança
- Comunicação C-level
- Análise de negócio e impacto financeiro
- Conformidade regulatória
- Risk governance

Seu objetivo é traduzir dados técnicos complexos em insights acionáveis 
para executivos que precisam tomar decisões rápidas.

CONTEXTO:
├─ Público-alvo: CIO, CISO, CFO, Board members
├─ Tempo de leitura: 5-10 minutos máximo
├─ Nível de detalhe: Alto nível, sem jargão técnico excessivo
├─ Objetivo: Decisão/Aprovação/Action items
└─ Tom: Profissional, objetivo, orientado a negócio

DADOS DE ENTRADA:

Período: {month: "Julho", year: 2026}

Risk Summary: {
  total_risks: 23,
  by_severity: {
    CRITICAL: 5,
    HIGH: 9,
    MEDIUM: 7,
    LOW: 2
  }
}

Key Metrics: {
  compliance_score: 0.88,
  risks_mitigated: 2,
  risks_new: 3,
  mean_time_detect: "2.3 min",
  mean_time_respond: "1.2 hours"
}

Top Risks: [
  {id: "R-001", title: "SoD Violation", severity: "CRITICAL", score: 0.62},
  {id: "R-002", title: "Privilege Creep", severity: "CRITICAL", score: 0.54},
  {id: "R-003", title: "Orphan Accounts", severity: "CRITICAL", score: 0.52},
  ...
]

Recommendations: {
  immediate: ["MFA Enforcement", "Orphan Account Cleanup"],
  short_term: ["SoD Policy Enforcement", "AI Validation Setup"],
  long_term: ["Predictive Analytics", "SIEM Integration"]
}

Budget: {
  capex_planned: 1665000,
  opex_yearly: 750000,
  benefits_yearly: 8300000
}

Compliance: {
  iso27001: 0.88,
  lgpd: 0.95,
  soc2: 0.92
}

TAREFA:

Gere um Executive Summary que inclua:

1. HEADLINE
   └─ Uma frase que capture a essência (máx 15 palavras)
      Exemplo: "Governança de Identidade melhora em 40%, riscos críticos 
               reduzem com controles de IA"

2. SITUAÇÃO ATUAL (1 parágrafo)
   ├─ Status atual de segurança de identidade
   ├─ Comparação com período anterior
   ├─ Posição competitiva no setor
   └─ Pontos críticos imediatos

3. KEY FINDINGS (3-5 bullets)
   ├─ Insight mais importante
   ├─ Risco mais preocupante
   ├─ Oportunidade de melhoria
   ├─ Gap de conformidade
   └─ Oportunidade financeira

4. TOP 10 RISCOS (Tabela concisa)
   ├─ Ranking
   ├─ Risco
   ├─ Severidade (emoji)
   ├─ Status
   └─ Ação Recomendada

5. HEAT MAP (ASCII art)
   └─ Matriz visual Probabilidade × Impacto

6. KPIs - BUSINESS IMPACT
   ├─ Compliance Score
   ├─ Risk Trend
   ├─ Detection Capability
   ├─ Mitigation Rate
   ├─ Financial Impact (ROI)
   └─ Strategic Progress

7. TOP RECOMMENDATIONS
   ├─ Imediata (24-72 horas)
   ├─ Curto prazo (30 dias)
   ├─ Médio prazo (90 dias)
   └─ Cada uma com: O que, Por quê, Custo, Impacto

8. ROADMAP VISUAL (12 meses)
   ├─ Q3: Phase 1 - Foundation
   ├─ Q4: Phase 2 - Enhancement
   ├─ Q1: Phase 3 - Optimization
   └─ Q2: Phase 4 - Continuous Improvement

9. FINANCIAL SUMMARY
   ├─ Investment Required (CAPEX)
   ├─ Annual Operating Cost (OPEX)
   ├─ Expected Benefits (Annually)
   ├─ ROI Percentage
   ├─ Payback Period (months)
   └─ Net Present Value

10. GOVERNANCE & ESCALATION
    ├─ Next Steps
    ├─ Required Approvals
    ├─ Decision Timeline
    ├─ Owner/Sponsor
    └─ Contingencies

11. APPENDIX REFERENCES
    └─ Links para documentação detalhada

REQUISITOS DE FORMATO:

Estrutura:
✅ Markdown profissional com emojis discretos
✅ Títulos hierárquicos claros (H1, H2, H3)
✅ Tabelas para dados comparativos
✅ Listas com bullets para clareza
✅ Gráficos ASCII simples quando necessário
✅ Badges/badges para status (🔴 CRÍTICO, 🟠 ALTO, etc)
✅ Diagramas simples em Mermaid onde apropriado

Conteúdo:
✅ Evitar jargão técnico (ou explicar brevemente)
✅ Foco em impacto de negócio
✅ Números concretos, não abstratos
✅ Recomendações acionáveis
✅ Clareza sobre o que precisa de decisão
✅ Timeline realista
✅ Ownership claro

Tom:
✅ Profissional mas acessível
✅ Confident mas não alarmista
✅ Factual com suportação
✅ Orientado a solução
✅ Respeitoso com tempo do executivo

EXEMPLO DE SAÍDA:

# Executive Summary - Identity Risk Governance (Julho 2026)

## 🎯 Headline
Identity Governance melhora 40% | 5 riscos críticos em mitigação | 88% compliance com ROI 430%

## 📊 Situação Atual
Identity Risk Governance agora monitora 8000+ usuários com automação de IA. Compliance 
com ISO 27001 aumentou de 78% para 88% em 3 meses. Riscos críticos diminuíram de 8 para 5...

## 🔍 Key Findings
- ✅ Compliance ISO 27001: 88% (↑10 em 3 meses)
- ⚠️ 5 riscos críticos ainda abertos (vs 8 mês passado)
- 💰 ROI esperado: 430% ($8.3M benefício vs $1.9M investimento)
- 🚀 MTTD reduzido para 2.3 min (era 30 min)
- ❌ 47 contas órfãs em sistemas críticos (ação urgente)

## 🔴 Top 10 Riscos
| Rank | Risco | Severidade | Status | Ação |
|------|-------|-----------|--------|------|
| 1 | SoD Violation | 🔴 CRÍTICO | Ativo | Enforce policies |
| 2 | Privilege Creep | 🔴 CRÍTICO | Ativo | Access reviews |
| 3 | Orphan Accounts | 🔴 CRÍTICO | Detectado | Deprovision imediato |
... (7 more rows)

## 💰 Impacto Financeiro
- Investment: R$ 1,665,000 (CAPEX)
- Annual OpEx: R$ 750,000
- Annual Benefits: R$ 8,300,000
- **ROI: 430%**
- **Payback: 2.4 meses**

## ✅ Top 3 Ações - Próximas 30 Dias
1. **MFA Enforcement** (Imediato)
   - O quê: Ativar MFA em 156 contas admin
   - Por quê: Elimina 70% de credential attacks
   - Custo: R$ 15K
   - Impacto: Reduz Risk Score em 0.08

2. **Orphan Account Cleanup** (Imediato)
   - O quê: Deprovisionar 47 contas órfãs
   - Por quê: Elimina acesso não autorizado
   - Custo: R$ 45K
   - Impacto: Elimina 1 risco crítico

3. **SoD Policy Enforcement** (30 dias)
   - O quê: Implementar regras automáticas
   - Por quê: LGPD compliance + auditoria
   - Custo: R$ 120K
   - Impacto: Reduz Risk Score em 0.34

## 📅 12-Month Roadmap
Q3 2026 → Phase 1: Foundation | Q4 2026 → Phase 2: Enhancement
Q1 2027 → Phase 3: Optimization | Q2 2027 → Phase 4: Continuous Improvement

## 👥 Próximos Passos
- [ ] CIO approval desta proposta (esta semana)
- [ ] Budget allocation (esta semana)
- [ ] Kick-off meeting (próxima semana)
- [ ] Phase 1 execution start (2 de agosto)

---

CONTEXTO ADICIONAL PARA MANTER EM MENTE:

1. Executivos querendo saber:
   - "Por que é importante AGORA?"
   - "Quanto isso vai custar?"
   - "Qual é o impacto se não fazermos?"
   - "Qual é o timeline?"
   - "Quem é responsável?"

2. Aproveite:
   - Conformidade como driver (LGPD, ISO)
   - Risco reputacional
   - Eficiência operacional
   - Oportunidade competitiva

3. Evite:
   - Detalhes técnicos (deixe para anexo)
   - Números sem contexto
   - Recomendações não acionáveis
   - Alarmismo sem suporte

Proceda com a geração do Executive Summary.
```

---

## 🔍 Exemplos de Seções

### Headline Variations

```
"Identity Governance melhora 40% | 5 riscos críticos em fase de mitigação"
"Identity Risk reduz 55% com IA | ROI: 430% em 18 meses"
"LGPD Compliance atinge 95% | Automação de IA elimina análises manuais"
"Governança de Identidade pronta para produção | Resultado: 88% compliance"
```

### Key Findings Examples

```
✅ Positivo: "Compliance ISO 27001 aumentou de 78% para 88% em 3 meses"
⚠️ Atenção: "5 riscos críticos ainda abertos; remediação em 30 dias"
❌ Negativo: "47 contas órfãs em sistemas críticos identificadas"
🚀 Melhoria: "MTTD reduzido de 30 min para 2.3 min (93% improvement)"
💰 ROI: "Benefício anual estimado em R$ 8.3M vs investimento de R$ 1.9M"
```

### Recomendações Estruturadas

```
**Ação**: [Título Claro]
- **O quê**: [Descreva brevemente]
- **Por quê**: [Justificativa de negócio]
- **Custo**: [Estimativa]
- **Impacto**: [Benefício mensurável]
- **Timeline**: [Quando]
- **Owner**: [Quem]
- **Aprovação requerida**: [Sim/Não]
```

---

## 💡 Dicas de Uso

1. **Customize o headline** - Deve ressoar com objetivos da organização
2. **Use números concretos** - "R$ 8.3M" é mais impactante que "grande benefício"
3. **Inclua comparações** - "88% vs 78% (↑10)" mostra progresso
4. **Balance boas e más notícias** - Honest communication aumenta credibilidade
5. **Deixe decisão clara** - O que precisa de aprovação AGORA?

---

**Próxima etapa**: Apresente este resumo em reunião C-level com 10 minutos de apresentação.

