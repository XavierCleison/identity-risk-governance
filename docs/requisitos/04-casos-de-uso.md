# Casos de Uso - Identity Risk Governance

## 1. Convenção de responsabilidade

- IA → recomenda
- Humano → decide
- Sistema → registra a decisão

Essa separação é essencial para preservar a regra do projeto: a IA não executa alterações de acesso.

---

## 2. UC-001 — Analisar risco de identidade

### Objetivo
Analisar uma identidade, seu perfil e seus acessos para identificar riscos relacionados a permissões excessivas, contas órfãs, privilege creep e conflitos de Segregation of Duties.

### Atores
- Analista de segurança ou governança
- Sistema de análise de risco
- IA generativa (apoio analítico)

### Pré-condições
- A identidade e os acessos relevantes estão disponíveis para análise.
- Há dados de perfil, função, permissões e histórico de uso.

### Fluxo principal
1. O analista inicia a análise de risco da identidade.
2. O sistema coleta dados de perfil, permissões e histórico de acesso.
3. A IA analisa os dados e identifica possíveis evidências de risco.
4. O sistema classifica os riscos por severidade e contexto.
5. O analista revisa a evidência e o contexto apresentado.
6. O sistema registra a análise e os resultados levantados.

### Fluxos alternativos
- Se houver dados incompletos, o sistema sinaliza a necessidade de complementação.
- Se houver sinal de risco crítico, a análise é escalada para revisão humana formal.

### Exceções
- Dados ausentes ou inconsistentes.
- Identidade sem histórico suficiente para comparação.
- Conflito de dados entre sistemas de origem.

### Pós-condições
- O risco foi identificado e contextualizado.
- O sistema registra a evidência e a classificação inicial.
- A próxima etapa pode ser a geração de recomendação.

### Requisitos relacionados
RF-001, RF-002, RF-003, RF-004, RF-005, RF-006, RF-007, RF-011

---

## 3. UC-002 — Gerar recomendação de tratamento

### Objetivo
Gerar uma recomendação de tratamento de risco com base na análise realizada, explicitando a ação sugerida, o contexto e os impactos esperados.

### Atores
- IA generativa
- Sistema
- Analista de governança ou responsável pelo risco

### Pré-condições
- Existe pelo menos uma evidência de risco identificada.
- Há contexto suficiente para contextualizar a recomendação.

### Fluxo principal
1. O sistema identifica um risco priorizado.
2. A IA gera uma recomendação de tratamento com base na evidência e no contexto.
3. O sistema apresenta a recomendação, as evidências e os impactos possíveis.
4. O analista revisa a recomendação.
5. O sistema registra a recomendação gerada e sua origem.

### Fluxos alternativos
- Se a IA não tiver dados suficientes, ela indica incerteza e não recomenda ação automatizada.
- Se a recomendação for ambígua, o analista solicita revisão ou complementação.

### Exceções
- Falha na geração da recomendação.
- Evidência insuficiente para sustentar a ação.
- Recomendação contraditória com políticas internas ou contexto de negócio.

### Pós-condições
- A recomendação fica disponível para aprovação, rejeição ou ajuste.
- O sistema registra a recomendação e sua base de evidência.

### Requisitos relacionados
RF-007, RF-008, RF-011, RF-012, RNF-003

---

## 4. UC-003 — Aprovar ou rejeitar recomendação

### Objetivo
Permitir que um responsável humano decida sobre a recomendação gerada, registrando aprovação, rejeição ou pedido de revisão.

### Atores
- Responsável pela decisão
- Sistema
- IA (como suporte analítico)

### Pré-condições
- Existe uma recomendação pendente de decisão.
- O responsável possui papel autorizado para aprovar ou rejeitar a recomendação.

### Fluxo principal
1. O responsável acessa a recomendação e o contexto associado.
2. O sistema exibe risco, evidências, recomendação e impactação esperada.
3. O responsável decide entre aprovar, rejeitar ou solicitar revisão.
4. O sistema registra a decisão, o responsável, a data e a justificativa.
5. O sistema atualiza o status da recomendação.

### Fluxos alternativos
- A recomendação pode ser rejeitada por falta de evidência ou de alinhamento com o negócio.
- A recomendação pode ser reencaminhada para revisão por outra autoridade.

### Exceções
- Usuário sem autorização tenta aprovar decisão.
- Falha de persistência do registro.
- Recomendação de risco crítico sem justificativa formal.

### Pós-condições
- A decisão humana está registrada.
- A recomendação assume status explícito e rastreável.
- Nenhuma alteração de acesso ocorre sem aprovação humana.

### Requisitos relacionados
RF-009, RF-010, RF-012, RN-001, RN-002, RN-003, RN-005, RN-009

---

## 5. UC-004 — Consultar histórico de decisões

### Objetivo
Consultar o histórico de análises, recomendações e decisões registradas para auditoria, conformidade e revisão.

### Atores
- Analista
- Governança
- Auditor
- Responsável pela decisão

### Pré-condições
- Existem registros de decisões anteriores.
- O usuário possui permissão de consulta.

### Fluxo principal
1. O usuário acessa a funcionalidade de histórico.
2. O sistema lista recomendações, classificações e decisões associadas.
3. O usuário filtra por identidade, risco, responsável ou período.
4. O sistema exibe evidências, contexto e status da decisão.
5. O usuário utiliza as informações para auditoria, análise ou suporte à decisão.

### Fluxos alternativos
- Quando não houver registros, o sistema informa ausência de histórico.
- Quando houver erro de acesso, o sistema nega a consulta e registra a tentativa.

### Exceções
- Histórico inexistente.
- Falha de consulta.
- Usuário sem necessidade de acesso ou sem autorização.

### Pós-condições
- O histórico relevante foi consultado com rastreabilidade.
- O sistema mantém registro de acesso ao histórico quando necessário.

### Requisitos relacionados
RF-010, RF-011, RNF-004, RNF-007

---

## 6. Resumo da regra de governança

O fluxo de trabalho do projeto estabelece claramente:

- IA identifica e recomenda;
- Humano valida e decide;
- Sistema registra e mantém a prova da decisão.

Nenhuma alteração de acesso é executada automaticamente pela IA.
