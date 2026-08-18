# Ambiguidades e Lacunas - Identity Risk Governance

## 1. Objetivo

Este documento identifica pontos que ainda não estão suficientemente definidos no projeto para permitir uma especificação completa e inequívoca. A intenção é registrar lacunas, ambiguidades e dependências de stakeholder sem inventar respostas.

---

## 2. Lacunas e ambiguidades

### LAC-001 — Critério de privilégio excessivo não está formalizado
- Descrição: O projeto menciona permissões excessivas, privilege creep e acessos sem justificativa de negócio, mas não define um critério formal para classificar uma permissão como excessiva.
- Impacto: Pode haver interpretações diferentes entre analistas e stakeholders sobre quando uma autorização deve ser considerada problemática.
- Pergunta de esclarecimento: Qual regra de negócio, política ou referência deve ser usada para definir “privilegio excessivo” em termos concretos?
- Stakeholder responsável: IAM Manager / Security Architect
- Status: Aberta

### LAC-002 — Regras de SoD ainda dependem de validação de negócio
- Descrição: O projeto menciona conflitos de Segregation of Duties, porém não detalha as regras de conflito específicas por processo, função ou sistema.
- Impacto: A detecção automática pode ser incompleta ou inconsistente se os conflitos não forem previamente mapeados.
- Pergunta de esclarecimento: Quais processos críticos e combinações de permissões são considerados conflitantes pela organização?
- Stakeholder responsável: Compliance Officer / Process Owner
- Status: Aberta

### LAC-003 — Critério para conta órfã não foi definido em profundidade
- Descrição: A ideia de conta órfã é clara, mas o projeto não define quando uma conta deve ser considerada órfã, nem quais condições de inatividade ou desligamento a desencadeiam.
- Impacto: Há risco de falso positivo ou falso negativo na identificação de contas sem responsável.
- Pergunta de esclarecimento: Qual é o critério mínimo de inatividade e de desvinculação funcional para considerar uma conta órfã?
- Stakeholder responsável: HR / IAM Manager / IT Operations
- Status: Aberta

### LAC-004 — Justificativa de negócio para acesso privilegiado não possui modelo formal
- Descrição: O projeto menciona acessos sem justificativa de negócio, mas não apresenta um fluxo ou template formal para justificar o acesso.
- Impacto: A classificação de risco e a decisão de aprovação podem depender da subjetividade do analista.
- Pergunta de esclarecimento: Quais campos e evidências devem compor a justificativa de negócio de um acesso privilegiado?
- Stakeholder responsável: Business Owner / Access Governance Lead
- Status: Aberta

### LAC-005 — Escopo do histórico de decisões ainda precisa ser definido
- Descrição: O projeto prevê histórico de decisões e auditoria, mas não especifica por quanto tempo o registro deve ser mantido ou quais campos ele deve conter.
- Impacto: Há risco de inconsistência entre requisitos de rastreabilidade, conformidade e retenção de dados.
- Pergunta de esclarecimento: Qual é a política de retenção de histórico e quais metadados devem ser preservados?
- Stakeholder responsável: Security Governance / Compliance
- Status: Aberta

### LAC-006 — Governança de dados sensíveis e anonimização da IA não foi completamente padronizada
- Descrição: O projeto menciona uso de IA e proteção de dados, mas não define a regra operacional de anonimização, mascaramento e uso de campos sensíveis em prompts ou relatórios.
- Impacto: A utilização de IA pode expor informação sensível se não houver padronização clara.
- Pergunta de esclarecimento: Quais campos devem ser removidos ou anonimizados antes de envio à IA e quais dados podem permanecer em contexto interno?
- Stakeholder responsável: Data Protection Officer / Security Lead
- Status: Aberta

### LAC-007 — Não há critério instituído para revisão periódica de acessos
- Descrição: O projeto menciona falhas na revisão periódica de acessos, mas não define periodicidade, proprietário, evidência ou processo de revisão.
- Impacto: O processo pode não ser consistente entre áreas e sistemas.
- Pergunta de esclarecimento: Qual é a periodicidade mínima e quem é responsável pela revisão periódica de acessos por função e por sistema?
- Stakeholder responsável: IAM Manager / Control Owner
- Status: Aberta

### LAC-008 — Falta definição de exception handling para situações de risco alto
- Descrição: Não está explícito como o sistema ou a organização deve agir quando a recomendação da IA indicar risco alto com informação insuficiente para decidir.
- Impacto: A resposta a cenários ambíguos pode variar entre usuários e áreas.
- Pergunta de esclarecimento: Em caso de risco alto e informação insuficiente, qual é o procedimento correto de escalonamento e de pausa da decisão?
- Stakeholder responsável: Security Operations / CISO
- Status: Aberta

### LAC-009 — O papel exato de “aprovador” não foi detalhado
- Descrição: O projeto exige aprovação humana, mas não indica claramente qual perfil profissional ou função atua como aprovador em cada tipo de recomendação.
- Impacto: Pode haver conflito de autoridade e ausência de responsabilidade explícita.
- Pergunta de esclarecimento: Quem deve aprovar acessos privilegiados, acessos de suporte e remoções com impacto crítico?
- Stakeholder responsável: IAM Governance Board / Manager
- Status: Aberta

### LAC-010 — Não há regra definida para IA sem informação suficiente
- Descrição: O projeto menciona que a IA deve analisar riscos e recomendar, mas não especifica o comportamento do sistema quando os dados forem insuficientes ou inconsistentes.
- Impacto: A IA pode produzir interpretação indevida ou recomendação sem base adequada.
- Pergunta de esclarecimento: A IA deve rejeitar a análise, pedir dados complementares ou indicar nível de incerteza?
- Stakeholder responsável: AI Governance / Security Lead
- Status: Aberta

---

## 3. Observações finais

As lacunas acima não representam falhas do projeto, mas evidências de que a atividade acadêmica ainda depende de validação com stakeholders de negócio, segurança e governança. A metodologia correta foi registrar tais pontos sem inventar regras que o projeto ainda não confirmou.
