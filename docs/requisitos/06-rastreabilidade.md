# Matriz de Rastreabilidade - Identity Risk Governance

## 1. Objetivo

Este documento relaciona requisitos, regras de negócio, casos de uso e critérios de aceitação, permitindo acompanhar a consistência geral da especificação.

---

## 2. Matriz de rastreabilidade

| Requisito | Regra de negócio | Caso de uso | Critério de aceitação | Observações |
|---|---|---|---|---|
| RF-001 — Representar identidade e perfil | RN-004 | UC-001 | CA-001 | Mapeado |
| RF-002 — Registrar e analisar permissões e acessos | RN-004 | UC-001 | CA-001 | Mapeado |
| RF-003 — Identificar privilege creep | RN-004 | UC-001 | CA-001 | Mapeado |
| RF-004 — Identificar contas órfãs | RN-007 | UC-001 | CA-001 | Mapeado |
| RF-005 — Identificar conflitos de SoD | RN-008 | UC-001 | CA-001 | Mapeado |
| RF-006 — Identificar acessos privilegiados | RN-004 | UC-001 | CA-013 | Mapeado |
| RF-007 — Classificar risco por criticidade | RN-005 | UC-002 | CA-002 | Mapeado |
| RF-008 — Gerar recomendações de tratamento | RN-001, RN-004 | UC-002 | CA-003 | Mapeado |
| RF-009 — Solicitar e registrar aprovação ou rejeição | RN-002, RN-003, RN-009 | UC-003 | CA-004, CA-005, CA-009 | Mapeado |
| RF-010 — Manter histórico e auditoria | RN-003, RN-009 | UC-004 | CA-009, CA-010 | Mapeado |
| RF-011 — Rastrear evidências e origem da recomendação | RN-003, RN-004 | UC-002, UC-004 | CA-003, CA-009 | Mapeado |
| RF-012 — Exibir contexto para decisão humana | RN-002, RN-005 | UC-003 | CA-004, CA-005 | Mapeado |
| RNF-001 — Segurança dos dados de identidade | RN-010 | UC-001, UC-004 | CA-001, CA-010 | Mapeado |
| RNF-002 — Privacidade e minimização de dados | RN-004 | UC-001, UC-004 | CA-006, CA-010 | Mapeado |
| RNF-003 — Explicabilidade das recomendações da IA | RN-001, RN-004 | UC-002, UC-003 | CA-003, CA-004 | Mapeado |
| RNF-004 — Auditoria, rastreabilidade e prova de decisão | RN-003 | UC-003, UC-004 | CA-009, CA-010 | Mapeado |
| RNF-005 — Confiabilidade e disponibilidade do processo | RN-005 | UC-001, UC-002 | CA-002, CA-007 | Mapeado |
| RNF-006 — Desempenho e capacidade operacional | RN-004 | UC-001, UC-002 | CA-001, CA-003 | Mapeado |
| RNF-007 — Integridade dos registros de decisão | RN-003, RN-009 | UC-003, UC-004 | CA-009, CA-010 | Mapeado |
| RNF-008 — Separação de responsabilidades e controle de acesso | RN-002, RN-010 | UC-003 | CA-008, CA-009 | Mapeado |

---

## 3. Análise de consistência

### Requisitos sem caso de uso
- Nenhum requisito funcional identificado ficou sem caso de uso correspondente.
- Nenhum requisito não funcional identificado ficou sem associação direta a um caso de uso ou critério. 

### Regras sem requisito associado
- RN-001, RN-002 e RN-003 são fundamentais e também diretamente associados aos requisitos funcionais e não funcionais de governança.
- Nenhuma regra de negócio ficou isolada sem suporte de requisito.

### Casos de uso sem requisito associado
- UC-001, UC-002, UC-003 e UC-004 possuem associação direta com requisitos de análise, recomendação e decisão.
- Nenhum caso de uso ficou sem requisito associado.

### Critérios sem requisito correspondente
- CA-001 até CA-010 estão vinculados a requisitos ou eixos de governança claramente identificados.
- Nenhum critério ficou sem correspondência.

---

## 4. Lacunas de rastreabilidade

### LAC-R-001 — Política de retenção de histórico
- Situação: A política de retenção de registros ainda precisa ser validada por stakeholder.
- Impacto: Pode afetar a definição exata do histórico e da evidência rastreada.

### LAC-R-002 — Perfil de aprovador por tipo de risco
- Situação: O projeto exige aprovação humana, mas não definiu a matriz de aprovação por tipo de risco e nível de privilégio.
- Impacto: A responsabilidade operacional pode variar por área.

### LAC-R-003 — Critério formal de “acesso sem justificativa”
- Situação: Ainda depende de validação do processo de negócio.
- Impacto: Afeta a consistência da análise e da recomendação.

---

## 5. Conclusão

A rastreabilidade foi mantida com consistência entre requisitos, regras, casos de uso e critérios de aceitação. As lacunas restantes são de validação de negócio e governança, e não de inconsistência técnica da estrutura da documentação.
