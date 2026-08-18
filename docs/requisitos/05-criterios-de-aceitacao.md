# Critérios de Aceitação - Identity Risk Governance

## 1. Visão geral

Os critérios abaixo orientam a validação do comportamento esperado da plataforma conceitual de governança de identidade e acesso.

---

## 2. Critérios de Aceitação

### CA-001 — Identificação de risco
- DADO que uma identidade possui permissões, histórico e contexto de acesso disponíveis
- QUANDO o sistema analisa o perfil e os acessos da identidade
- ENTÃO deve identificar possíveis riscos e registrar a evidência associada

### CA-002 — Risco de alta criticidade
- DADO que a análise indica risco crítico ou muito alto
- QUANDO o caso for submetido à governança
- ENTÃO a recomendação deve ser escalada para revisão humana formal e registrar a elevação do nível de criticidade

### CA-003 — Recomendação gerada pela IA
- DADO que há uma evidência de risco validada no contexto do caso
- QUANDO a IA gera uma recomendação
- ENTÃO a recomendação deve mencionar o contexto do risco, as evidências e a justificativa de forma compreensível para revisão humana

### CA-004 — Recomendação aprovada
- DADO que uma recomendação foi revisada por um responsável autorizado
- QUANDO o responsável aprova a recomendação
- ENTÃO o sistema deve registrar a aprovação, o responsável, a data e a justificativa da decisão

### CA-005 — Recomendação rejeitada
- DADO que uma recomendação não possui base suficiente ou não é adequada ao contexto
- QUANDO o responsável rejeita a recomendação
- ENTÃO o sistema deve registrar a rejeição, a justificativa e o status atualizado da recomendação

### CA-006 — IA sem informação suficiente
- DADO que a IA não possui dados suficientes para analisar o caso de forma confiável
- QUANDO tenta gerar uma recomendação
- ENTÃO deve indicar que a análise não pode ser concluída com segurança e não deve sugerir ação automatizada de acesso

### CA-007 — Falha na geração da recomendação
- DADO que ocorre falha técnica ou falta de contexto para a geração da recomendação
- QUANDO o sistema tenta criar a sugestão
- ENTÃO deve informar a falha, preservar o registro da análise e permitir reprocessamento ou revisão humana

### CA-008 — Tentativa de alteração sem aprovação
- DADO que uma operação de alteração de acesso seja solicitada sem aprovação humana
- QUANDO a regra de governança for verificada
- ENTÃO o sistema deve bloquear ou rejeitar a alteração e registrar a tentativa como evento de governança

### CA-009 — Registro da decisão
- DADO que uma recomendação foi aprovada ou rejeitada
- QUANDO o sistema persistir a decisão
- ENTÃO deve manter rastreabilidade suficiente para auditoria, incluindo responsável, data, contexto e status

### CA-010 — Consulta ao histórico
- DADO que um usuário autorizado consulta o histórico de decisões
- QUANDO a consulta for executada
- ENTÃO o sistema deve apresentar o histórico com evidências e status das decisões em ordem adequada para revisão

---

## 3. Cenários negativos e de exceção

### CA-011 — Risco identificado sem recomendação
- DADO que há evidência de risco, mas a IA não pode gerar recomendação
- QUANDO o caso for revisado
- ENTÃO o sistema deve registrar a limitação em vez de assumir uma ação sem base

### CA-012 — Recomendação contraditória
- DADO que a recomendação gerada conﬂita com o contexto de negócio ou com a regra de governança
- QUANDO o responsável avalia o caso
- ENTÃO a decisão deve ser recusada e registrada como revisão manual

### CA-013 — Acesso privilegiado sem justificativa
- DADO que uma identidade possui acesso privilegiado sem justificativa válida
- QUANDO a análise detectar o cenário
- ENTÃO deve registrar o risco e recomendar revisão humana, sem execução automática de remoção ou alteração

---

## 4. Critério de aceitação geral

O conjunto de artefatos será aceito quando:

- os riscos relevantes forem identificados com evidência;
- a IA for usada apenas como apoio analítico;
- a decisão humana for registrada e rastreada;
- as recomendações forem entregues com contexto e sem automação de acesso;
- a consulta ao histórico e a auditoria forem possíveis e consistentes.
