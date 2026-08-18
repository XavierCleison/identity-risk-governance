# Requisitos do Sistema - Identity Risk Governance

## 1. Contexto e regra de governança

Este documento especifica requisitos funcionais e não funcionais para a plataforma conceitual de governança de identidade e acesso do projeto Identity Risk Governance (IRG).

A regra central do projeto deve ser mantida em toda a especificação:

- IA identifica e recomenda
- Humano valida e decide
- Sistema registra a decisão
- Nenhuma alteração de acesso pode ser executada automaticamente pela IA
- Qualquer concessão, alteração ou revogação de acesso exige aprovação humana e rastreabilidade

---

## 2. Requisitos Funcionais

### RF-001 — Representar identidade e perfil
- Nome: Representar identidade e perfil
- Descrição: O sistema deve representar uma identidade corporativa com atributos relevantes para análise de risco, como função, unidade, status, histórico de acesso e nível de privilégio.
- Prioridade: Alta
- Origem: Projeto IRG e domínio IAM
- Dependências: Nenhuma

### RF-002 — Registrar e analisar permissões e acessos
- Nome: Registrar e analisar permissões e acessos
- Descrição: O sistema deve registrar permissões associadas a cada identidade e permitir a análise de acessos atuais, históricos e padrões de uso.
- Prioridade: Alta
- Origem: Projeto IRG e domínio IAM
- Dependências: RF-001

### RF-003 — Identificar privilege creep
- Nome: Identificar privilege creep
- Descrição: O sistema deve detectar quando uma identidade acumula permissões além do necessário para sua função, especialmente quando há crescimento de acesso sem justificativa de negócio documentada.
- Prioridade: Alta
- Origem: Requisitos e riscos do domínio IAM
- Dependências: RF-001, RF-002

### RF-004 — Identificar contas órfãs
- Nome: Identificar contas órfãs
- Descrição: O sistema deve identificar contas ativas que não possuem vínculo claro com a estrutura organizacional vigente ou que permanecem acessando recursos após a saída ou inativação de uma pessoa ou função.
- Prioridade: Alta
- Origem: Riscos do domínio IAM
- Dependências: RF-001

### RF-005 — Identificar conflitos de Segregation of Duties (SoD)
- Nome: Identificar conflitos de Segregation of Duties
- Descrição: O sistema deve detectar combinações de permissões que permitam conflitos de responsabilidade dentro de um mesmo processo, como criação e aprovação, ou escrita e validação.
- Prioridade: Alta
- Origem: Requisitos de governança e conformidade IAM
- Dependências: RF-002

### RF-006 — Identificar acessos privilegiados
- Nome: Identificar acessos privilegiados
- Descrição: O sistema deve sinalizar acessos com nível administrativo, de suporte, de auditoria ou de operação crítica, destacando os casos sem justificativa adequada.
- Prioridade: Alta
- Origem: Domínio IAM e riscos de acesso
- Dependências: RF-002

### RF-007 — Classificar risco por criticidade
- Nome: Classificar risco por criticidade
- Descrição: O sistema deve classificar o risco identificado em categorias que apoiem priorização e ação, considerando, quando disponível, severidade, probabilidade e impacto.
- Prioridade: Alta
- Origem: Projeto IRG e gestão de riscos
- Dependências: RF-003, RF-004, RF-005, RF-006

### RF-008 — Gerar recomendações de tratamento de risco
- Nome: Gerar recomendações de tratamento de risco
- Descrição: O sistema deve apoiar a geração de recomendações de mitigação, revisão, reforço de controles e documentação de justificativa de negócio, com foco em ações humanas e rastreáveis.
- Prioridade: Alta
- Origem: Uso de IA generativa e objetivo do projeto
- Dependências: RF-007

### RF-009 — Solicitar e registrar aprovação ou rejeição de recomendação
- Nome: Solicitar e registrar aprovação ou rejeição de recomendação
- Descrição: O sistema deve permitir que uma recomendação seja aprovada, rejeitada ou reavaliada por um responsável humano, registrando o resultado, a justificativa e o contexto da decisão.
- Prioridade: Crítica
- Origem: Regra fundamental do projeto
- Dependências: RF-008

### RF-010 — Manter histórico e auditoria de decisões
- Nome: Manter histórico e auditoria de decisões
- Descrição: O sistema deve manter histórico de análises, recomendações geradas, decisões humanas e evidências associadas, permitindo rastreabilidade e auditoria.
- Prioridade: Crítica
- Origem: Requisito de governança, conformidade e rastreabilidade
- Dependências: RF-008, RF-009

### RF-011 — Rastrear evidências e origem da recomendação
- Nome: Rastrear evidências e origem da recomendação
- Descrição: O sistema deve registrar a origem das informações que sustentaram uma recomendação, incluindo sinais de risco, evidências de acesso e contexto do caso analisado.
- Prioridade: Alta
- Origem: Requisito de explicabilidade e governança
- Dependências: RF-008, RF-010

### RF-012 — Exibir contexto para decisão humana
- Nome: Exibir contexto para decisão humana
- Descrição: O sistema deve apresentar ao responsável a descrição do risco, as evidências, a recomendação sugerida e os impactos potenciais, para apoiar a decisão sem automatizar a ação.
- Prioridade: Alta
- Origem: Regra de aprovação humana e governança da IA
- Dependências: RF-008, RF-009

---

## 3. Requisitos Não Funcionais

### RNF-001 — Segurança dos dados de identidade
- Nome: Segurança dos dados de identidade
- Descrição: Os dados de identidade e acesso devem ser tratados com controles adequados de confidencialidade, integridade e acesso restrito.
- Prioridade: Crítica
- Origem: Requisito de segurança da informação e domínio IAM
- Dependências: RF-001, RF-010

### RNF-002 — Privacidade e minimização de dados
- Nome: Privacidade e minimização de dados
- Descrição: A solução deve evitar coleta e exposição desnecessária de dados sensíveis; informações pessoais ou identificáveis devem ser tratadas conforme a necessidade de análise e governança.
- Prioridade: Alta
- Origem: Requisito do projeto e conformidade com legislação aplicável
- Dependências: RF-001, RF-010

### RNF-003 — Explicabilidade das recomendações da IA
- Nome: Explicabilidade das recomendações da IA
- Descrição: As recomendações produzidas pela IA devem ser acompanhadas de contexto, evidências e justificativas suficientes para permitir revisão humana e validação crítica.
- Prioridade: Crítica
- Origem: Governança de IA e exigência de análise crítica
- Dependências: RF-008, RF-011, RF-012

### RNF-004 — Auditoria, rastreabilidade e prova de decisão
- Nome: Auditoria, rastreabilidade e prova de decisão
- Descrição: O sistema deve registrar a sequência de eventos e decisões relacionadas ao risco, garantindo que toda aprovação ou rejeição seja rastreável.
- Prioridade: Crítica
- Origem: Regras de negócio e necessidade de governança
- Dependências: RF-009, RF-010, RF-011

### RNF-005 — Confiabilidade e disponibilidade do processo de análise
- Nome: Confiabilidade e disponibilidade do processo de análise
- Descrição: O processo de análise de riscos deve ser confiável e estar disponível para uso em momentos de revisão e governança, reduzindo falhas que comprometam a avaliação de riscos.
- Prioridade: Alta
- Origem: Necessidade operacional do domínio IAM
- Dependências: RF-002, RF-007, RF-010

### RNF-006 — Desempenho e capacidade de suporte ao volume operacional
- Nome: Desempenho e capacidade de suporte ao volume operacional
- Descrição: O sistema deve suportar o volume esperado de identidades, permissões e avaliações sem degradação significativa da experiência de análise ou da qualidade das recomendações.
- Prioridade: Média
- Origem: Requisito funcional e exigência de operação institucional
- Dependências: RF-002, RF-007, RF-008

### RNF-007 — Integridade dos registros de decisão
- Nome: Integridade dos registros de decisão
- Descrição: Os registros de análise e decisão devem manter integridade, evitando alteração indevida ou perda de evidência após a decisão do responsável.
- Prioridade: Crítica
- Origem: Auditabilidade e governança
- Dependências: RF-009, RF-010

### RNF-008 — Separação de responsabilidades e controle de acesso
- Nome: Separação de responsabilidades e controle de acesso
- Descrição: O acesso aos dados e às decisões deve respeitar papéis e responsabilidades, assegurando que apenas usuários autorizados possam revisar ou aprovar recomendações.
- Prioridade: Alta
- Origem: Governança IAM e boas práticas de controle interno
- Dependências: RF-009, RF-012

---

## 4. Observações de validação

- Os requisitos acima foram elaborados a partir do contexto e da documentação existente do projeto.
- A exigência de aprovação humana antes de qualquer alteração de acesso foi tratada como regra de negócio e também como requisito funcional crítico.
- Quando uma métrica quantitativa não foi definida no projeto, a necessidade de validação ficou explicitada como lacuna ou necessidade de confirmação por stakeholder.
