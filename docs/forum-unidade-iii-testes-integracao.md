# Fórum - Unidade III: testes de integração para Identity Risk Governance

## 1. Contexto e cenário IAM

Este documento registra o experimento acadêmico realizado sobre o repositório Identity Risk Governance, com foco em análise de risco, decisão humana autorizada e auditoria de acesso.

O projeto documenta uma solução conceitual de governança de identidades e acessos corporativos, com apoio analítico da IA generativa. A regra central do projeto foi mantida em toda a documentação:

- IA identifica riscos e recomenda;
- responsável humano autorizado valida e decide;
- sistema registra a decisão;
- IA não executa concessões, revogações ou alterações de acesso diretamente.

O escopo documentado inclui riscos como:

- permissões excessivas;
- privilege creep;
- contas órfãs;
- conflitos de Segregation of Duties (SoD);
- acessos privilegiados;
- ausência de justificativa de negócio;
- falhas na revisão periódica de acessos;
- evidências de risco em perfis, papéis e histórico de acesso.

Fontes confirmadas no workspace:

- [README.md](../README.md)
- [docs/architecture.md](./architecture.md)
- [docs/requisitos/01-requisitos.md](./requisitos/01-requisitos.md)
- [docs/requisitos/02-regras-de-negocio.md](./requisitos/02-regras-de-negocio.md)
- [docs/requisitos/03-ambiguidades-e-lacunas.md](./requisitos/03-ambiguidades-e-lacunas.md)
- [docs/requisitos/04-casos-de-uso.md](./requisitos/04-casos-de-uso.md)
- [docs/requisitos/05-criterios-de-aceitacao.md](./requisitos/05-criterios-de-aceitacao.md)
- [docs/requisitos/06-rastreabilidade.md](./requisitos/06-rastreabilidade.md)
- [identity_risk_governance/decision_validation.py](../identity_risk_governance/decision_validation.py)

## 2. Objetivo

Documentar a evolução do raciocínio de QA e testes de integração aplicado ao projeto, preservando apenas o que está confirmado no workspace e evitando criação de contratos, infraestrutura ou regras que não existam no repositório.

Os objetivos específicos foram:

1. identificar o que está documentado e o que é apenas conceitual;
2. separar casos especificados de casos executáveis no estado atual;
3. propor cenários de risco, decisão humana e auditoria sem inventar endpoints, banco de dados ou API;
4. registrar lacunas que exigem decisão humana antes de qualquer implementação operacional.

## 3. Prompt V1 integral

> Analise o workspace do projeto Identity Risk Governance antes de propor testes de integração. Leia o README.md e os documentos relevantes em docs/requisitos, docs/ia e docs de arquitetura. Identifique quais componentes, contratos, regras de negócio e fluxos estão documentados e quais são apenas conceituais. Concentre-se no fluxo de análise de risco, decisão humana autorizada e registro de auditoria. Não invente endpoints, classes, banco de dados ou implementações que não existam. Liste: (1) evidências encontradas com caminhos dos arquivos; (2) componentes implementados versus conceituais; (3) regras confirmadas; (4) lacunas que exigem decisão humana; (5) qual tipo de teste de integração é realmente possível executar neste repositório. Não altere arquivos nesta etapa.

## 4. Resumo fiel da resposta V1

A resposta V1 concluiu que o repositório é um projeto de arquitetura e engenharia de requisitos de governança IAM, não uma aplicação operacional pronta. A documentação confirma que a regra central é:

- IA identifica riscos e recomenda;
- responsável humano autorizado valida e decide;
- sistema registra a decisão;
- nenhuma alteração de acesso é executada automaticamente pela IA.

A resposta listou as evidências documentais em README, docs/requisitos, docs/ia e docs/architecture, além da implementação real encontrada em [identity_risk_governance/decision_validation.py](../identity_risk_governance/decision_validation.py). Também apontou que os principais componentes do fluxo (IAM Platform, Risk Engine, IA Generativa, auditoria operacional, dashboard e integrações) são conceituais, não implementados.

A análise identificou regras confirmadas, como aprovação humana obrigatória, rastreabilidade, recomendação contextualizada e registro de decisões, e registrou lacunas importantes, como critérios de risco, políticas de aprovação e retenção de histórico.

Em relação aos testes, a resposta V1 concluiu que o único tipo de integração realmente possível neste workspace é um teste de integração de módulo Python local, sem API, banco ou infraestrutura operacional. A evidência real usada foi a execução do comando seguinte, que produziu sucesso:

```bash
python -m pytest -q
```

Saída observada:

```text
4 passed, 8 subtests passed in 0.02s
```

## 5. Prompt V2 integral

> Atue como engenheiro de QA especializado em IAM e testes de integração. Usando somente os contratos e requisitos confirmados no workspace, procure cenários negativos e de fronteira no fluxo de decisão humana e auditoria. Considere: responsável sem autorização adequada; justificativa obrigatória ausente, se definida; repetição da mesma solicitação; decisão baseada em evidência desatualizada; falha no registro de auditoria; e divergência entre a decisão apresentada e a persistida. Para cada cenário, descreva a sequência de interações, a invariante ou requisito que se pretende verificar e como confirmar o estado após o resultado. Não assuma que repetição deve ser aceita ou rejeitada sem regra documentada. Não invente endpoints ou infraestrutura. Se um cenário revelar uma lacuna de negócio, registre uma pergunta para o responsável e não escolha a regra por conta própria. Um teste que revela uma falha real deve permanecer como falha; não enfraqueça a asserção para obter resultado verde. Separe casos especificados de testes que podem ser executados hoje. Não altere arquivos ainda.

## 6. Resumo fiel da resposta V2

A resposta V2 focou em cenários negativos e de fronteira, diferenciando casos especificados de casos executáveis no código atual. A análise confirmou que a documentação exige:

- aprovação humana obrigatória;
- separação de responsabilidades e controle de acesso;
- rastreabilidade e prova de decisão;
- integridade dos registros e auditoria;
- justificativa de decisão e evidência contextualizada.

Entre os cenários discutidos, destacaram-se:

- responsável sem autorização adequada;
- justificativa obrigatória ausente;
- repetição da mesma solicitação;
- decisão baseada em evidência desatualizada;
- falha no registro de auditoria;
- divergência entre a decisão apresentada e a persistida.

A resposta V2 também destacou uma regra muito importante: para cenários sem contrato definido no workspace, não se deve inventar a regra. Quando a lacuna existe, ela foi registrada como pergunta para o responsável, como em:

- qual é o mínimo obrigatório de justificativa para aprovar, rejeitar ou solicitar revisão;
- quando os dados são insuficientes, a IA deve rejeitar, pedir complemento ou marcar apenas incerteza;
- a repetição da mesma solicitação deve ser tratada como idempotência, nova decisão ou conflito de auditoria;
- qual é a política de validade da evidência para decisão final.

A resposta V2 separou claramente:

- casos especificados pelo projeto;
- casos executáveis no código atual;
- lacunas que exigem decisão humana.

## 7. Tabela consolidada de casos

| ID | Origem do prompt | Cenário | Requisito ou invariante | Evidência esperada | Executável atualmente | Motivo | Classificação |
|---|---|---|---|---|---|---|---|
| IRG-TS-01 | V1 | Recomendação consultada e decisão aprovada | RF-008, RF-009, RF-010, RF-012; RN-002; RN-003; RN-009; CA-004; CA-009 | decisão humana registrada com responsável, data, justificativa e status | Não | O fluxo completo depende de IA + recomendação + decisão humana + auditoria, que são conceituais no workspace | proposta de teste |
| IRG-TS-02 | V1 | Recomendação consultada e decisão rejeitada | RF-009, RF-010; RN-002; RN-003; CA-005; CA-009 | rejeição registrada com justificativa e status atualizado | Não | O repositório não implementa a persistência nem a UI do fluxo de decisão e auditoria | proposta de teste |
| IRG-TS-03 | V1 | Recomendação sem justificativa de negócio | RN-006; RF-012; RF-009; CA-013 | a decisão não pode ser aceita sem justificativa clara; caso deve ser questionado ou rejeitado | Não | O projeto exige justificativa, mas não define o contrato formal da justificativa; isso é lacuna de negócio | lacuna que exige decisão humana |
| IRG-TS-04 | V1 | Verificação posterior do registro de auditoria | RF-010; RF-011; RNF-004; RNF-007; CA-009; CA-010 | histórico mostra evidência, decisão, responsável e status | Não | Não há persistence/auditoria implementada; apenas regra documental | proposta de teste |
| IRG-TS-05 | V1 | IA sem informação suficiente | RNF-003; CA-006; CA-011; LAC-010 | IA não gera ação automatizada; caso fica em limbo ou para revisão humana | Não | O comportamento exato da IA sem dados suficientes não foi definido como regra operacional | lacuna que exige decisão humana |
| IRG-TS-06 | V1 | Risco crítico elevado para revisão formal | RF-007; RN-005; CA-002 | risco crítico dispara revisão humana formal e rastreio do escalonamento | Não | O mecanismo de classificação/escala e auditoria do risco crítico não existe como implementação | proposta de teste |
| IRG-NEG-01 | V2 | Responsável sem autorização adequada | RN-002; RN-010; RNF-008; UC-003 | decisão não é aceita; recomendação continua pendente; tentativa pode ser registrada | Não | O projeto exige papel autorizado, mas não define o contrato de autorização nem a matriz de aprovador por risco | confirmada por documento |
| IRG-NEG-02 | V2 | Justificativa obrigatória ausente | RN-003; RF-009; RN-006; LAC-004 | decisão sem justificativa não é finalizada; deve ser rejeitada ou complementada | Não | O cenário é exigido por regra documental, mas a regra formal do campo mínimo de justificativa ainda não foi definida | lacuna que exige decisão humana |
| IRG-NEG-03 | V2 | Repetição da mesma solicitação | inexistente como regra documentada; RN-003, RNF-007 indirectamente | não deve haver duplicidade de decisão sem distinção clara; a repetição deve ser tratada de forma inequívoca | Não | O workspace não define idempotência, deduplicação ou política de reprocessamento; isso é uma lacuna de negócio | lacuna que exige decisão humana |
| IRG-NEG-04 | V2 | Decisão baseada em evidência desatualizada | RN-004; RF-011; RNF-007 | evidência precisa ser rastreada e atualizada antes da decisão final | Não | O projeto exige rastreabilidade, mas não define política de validade/freshness de evidência | lacuna que exige decisão humana |
| IRG-NEG-05 | V2 | Falha no registro de auditoria | RF-010; RNF-004; RNF-007; CA-009; CA-010 | não pode haver “decisão registrada” sem persistência de auditoria | Não | O fluxo de gravação/auditoria não existe como implementação real | confirmada por documento |
| IRG-NEG-06 | V2 | Divergência entre a decisão apresentada e a persistida | RNF-007; RNF-004; RF-010 | o histórico persistido deve refletir exatamente a decisão humana aceita | Não | Não há implementação de persistência nem mecanismo de integridade do histórico | confirmada por documento |
| IRG-EX-01 | V1/V2 | Decisão de revogar exige identificador de aprovador | regra implementada em [identity_risk_governance/decision_validation.py](../identity_risk_governance/decision_validation.py) | lança ValueError se approver_id ausente ou vazio para “revogar” | Sim | Existe implementação real e teste correspondente em [tests/test_decision_validation.py](../tests/test_decision_validation.py) | confirmada por documento |
| IRG-EX-02 | V1/V2 | Decisão inválida é rejeitada | regra implementada em [identity_risk_governance/decision_validation.py](../identity_risk_governance/decision_validation.py) | lança ValueError para valores fora do conjunto permitido | Sim | Existe implementação real e teste correspondente em [tests/test_decision_validation.py](../tests/test_decision_validation.py) | confirmada por documento |
| IRG-EX-03 | V1/V2 | “manter” ou “investigar” sem aprovador é aceito | regra implementada em [identity_risk_governance/decision_validation.py](../identity_risk_governance/decision_validation.py) | retorna sem erro quando decisão é “manter” ou “investigar” | Sim | Existe implementação real e teste correspondente em [tests/test_decision_validation.py](../tests/test_decision_validation.py) | confirmada por documento |

## 8. Ajustes de prompt e justificativa

### Ajuste entre V1 e V2

A V1 focou em análise do workspace e na confirmação do que existe de fato; a V2 foi uma etapa de aprofundamento orientada a QA, com foco em cenários negativos e fronteira.

Os ajustes relevantes foram:

1. V1 solicitou identificação de componentes, contratos, regras e tipos de teste possíveis.
2. V2 solicitou cenários de fronteira e negativa usando somente contratos e requisitos confirmados.
3. V2 introduziu a exigência explícita de separar:
   - casos especificados;
   - casos executáveis hoje;
   - lacunas que precisam de decisão humana.
4. V2 também reforçou a regra de não inventar infraestrutura, endpoints ou regras de negócio que o workspace não define.

### Justificativa do ajuste

Esse refinamento foi necessário porque a primeira versão identificou claramente o estado conceitual do projeto, mas não aprofundou a necessidade de separar as expectativas de negócio das evidências reais do código. A segunda versão corrigiu esse ponto ao distinguir a documentação de requisitos do que é efetivamente implementado.

## 9. Comandos de teste realmente executados e saídas

### Comando executado

```bash
python -m pytest -q
```

### Saída observada

```text
4 passed, 8 subtests passed in 0.02s
```

### Interpretação

Esta saída confirma que o código real presente no workspace passou na suíte atual em [tests/test_decision_validation.py](../tests/test_decision_validation.py). Não existe evidência de execução de testes de integração do fluxo completo de análise de risco, recomendação e auditoria, porque esses componentes não foram implementados como serviço ou infraestrutura real neste repositório.

## 10. Limitações

1. O projeto é conceitual e acadêmico, conforme documentação em [README.md](../README.md) e [docs/architecture.md](./architecture.md).
2. Não há evidência de implementação operacional de API, banco de dados, UI, IAM real, pipeline de risco ou armazenamento de auditoria.
3. O documento de requisitos registra lacunas que ainda dependem de decisão do stakeholder.
4. Não há contrato formal de payload, endpoint, persistência, cronograma de revisão ou política de retenção documentado em código.
5. Por isso, qualquer teste de integração end-to-end que dependa de entidades inexistentes seria uma hipótese e não uma evidência verificável do workspace.

## 11. Lacunas que exigem decisão humana

1. Critério formal de privilégio excessivo: conforme [docs/requisitos/03-ambiguidades-e-lacunas.md](./requisitos/03-ambiguidades-e-lacunas.md).
2. Regras específicas de SoD por processo, função e sistema.
3. Critério para conta órfã.
4. Modelo formal de justificativa de negócio para acesso privilegiado.
5. Política de retenção do histórico de decisões.
6. Governança de dados sensíveis e anonimização da IA.
7. Critério e periodicidade de revisão periódica de acessos.
8. Procedimento para risco alto com informação insuficiente.
9. Perfil exato do aprovador por tipo de risco e nível de privilégio.
10. Comportamento da IA quando os dados são insuficientes ou inconsistentes.
11. Regras para repetição da mesma solicitação.
12. Política de validade e atualização da evidência antes da decisão final.

### Perguntas objetivas para os responsáveis

- Qual é o mínimo obrigatório de justificativa para aprovar, rejeitar ou solicitar revisão em um caso de risco IAM?
- Quando os dados são insuficientes ou inconsistentes, a IA deve rejeitar a recomendação, pedir complemento ou apenas marcar incerteza?
- A repetição da mesma recomendação deve ser tratada como idempotência, nova decisão, conflito de auditoria ou reprocessamento?
- Qual é a regra de validade mínima da evidência para que uma decisão seja considerada atualizada e aceitável?
- Qual é a matriz definitiva de aprovadores por tipo de risco, nível de privilégio e área de negócio?

## 12. Resumo quantitativo

Os números a seguir são os que apareceram no histórico desta conversa e em evidências verificáveis do workspace:

- V1: 9 casos gerados
- V2: 9 casos gerados
- casos únicos após consolidação: 15
- casos executados: 3
- saídas verificadas: 4 passed, 8 subtests passed in 0.02s

Importante: a contagem de 15 casos únicos foi informada na consolidação da comparação entre V1 e V2. A contagem de 3 casos executados corresponde à regra implementada em [identity_risk_governance/decision_validation.py](../identity_risk_governance/decision_validation.py) e aos testes existentes em [tests/test_decision_validation.py](../tests/test_decision_validation.py). Não há evidência de execução dos casos conceituais de risco, recomendação e auditoria, porque esses componentes não existem como implementação operacional no repositório.

## 13. Classificação final

### Casos confirmados por documento

- IRG-NEG-01
- IRG-NEG-05
- IRG-NEG-06
- IRG-EX-01
- IRG-EX-02
- IRG-EX-03

### Casos propostos como teste

- IRG-TS-01
- IRG-TS-02
- IRG-TS-04
- IRG-TS-06

### Casos que exigem decisão humana

- IRG-TS-03
- IRG-TS-05
- IRG-NEG-02
- IRG-NEG-03
- IRG-NEG-04

## 14. Conclusão

O experimento demonstrou que o projeto é coerente como proposta acadêmica e de arquitetura conceitual, mas ainda não está em estado de implementação operacional. O que já existe no workspace é uma validação local de decisão de revisão, sem fluxo completo de IA, IAM, decisão humana autorizada e auditoria operacional.

Por isso, a prática correta de QA neste estado é separar claramente:

- o que foi documentado e se alinha ao domínio;
- o que foi implementado de fato;
- o que ainda exige decisão humana e validação com stakeholders.

Esse registro serve como evidência metodológica do experimento e como base para a próxima etapa de desenho de testes, quando houver implementação real ou contratos formais definidos.
