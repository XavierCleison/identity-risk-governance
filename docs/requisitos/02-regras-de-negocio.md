# Regras de Negócio - Identity Risk Governance

## 1. Introdução

Este documento reúne as regras de negócio do projeto e reforça a exigência de governança humana sobre qualquer ação relacionada a acessos.

---

## 2. Regras de Negócio

### RN-001 — IA pode recomendar, mas não alterar acessos
- Descrição: A Inteligência Artificial pode analisar dados, identificar riscos, classificar riscos e sugerir ações de tratamento, mas não pode executar diretamente alterações de acesso.
- Evidência de origem: Regra fundamental do projeto e documento de contexto acadêmico
- Impacto: Garante que a IA permaneça como apoio analítico, sem assumir decisões operacionais de acesso

### RN-002 — Aprovação humana obrigatória
- Descrição: Alterações de acesso devem passar por aprovação humana antes de qualquer implementação, seja concessão, revogação, alteração ou reforço de permissões.
- Evidência de origem: Regra fundamental do projeto
- Impacto: Reduz riscos de automação indevida e assegura responsabilidade humanamente atribuída

### RN-003 — Decisões devem ter rastreabilidade
- Descrição: Toda decisão de aprovação, rejeição, solicitação de revisão ou manutenção de recomendação deve possuir rastreabilidade, incluindo responsável, data, evidências e justificativa.
- Evidência de origem: exigência de auditoria e governança do projeto
- Impacto: Permite revisão, auditoria e accountability

### RN-004 — Recomendações devem ser contextualizadas
- Descrição: Qualquer recomendação gerada pela IA deve ser baseada em evidências relevantes de identidade, permissão, negócio e histórico de acesso, e não em suposições isoladas.
- Impacto: Melhora qualidade da análise e reduz decisões inconsistentes

### RN-005 — Risco crítico exige revisão humana formal
- Descrição: Quando a análise indicar risco crítico, a recomendação deve ser submetida a revisão humana formal e registrada em histórico de decisão.
- Impacto: Garante atenção prioritária e disciplina de governança

### RN-006 — Recomendação sem justificativa de negócio deve ser questionada
- Descrição: Caso uma recomendação sugira remoção ou restrição de acesso sem justificativa de negócio clara, o responsável deve validar a necessidade antes da decisão final.
- Impacto: Evita remoções indevidas ou excesso de restrição

### RN-007 — Contas órfãs devem ser tratadas por processo formal de encerramento
- Descrição: Contas órfãs ou inativas devem ser avaliadas em processo formal de encerramento, desativação ou revisão, com registro da decisão.
- Impacto: Reduz risco de permanência de acessos sem responsável

### RN-008 — Conflitos de SoD devem ser tratados como risco de governança
- Descrição: Conflitos de Segregation of Duties não devem ser resolvidos automaticamente pela IA; devem ser evidenciados, avaliados e tratados por decisão humana compatível com o processo corporativo.
- Impacto: Preserva qualidade da governança de acesso e separação de responsabilidades

### RN-009 — O sistema deve registrar o status da decisão
- Descrição: Cada recomendação deve possuir status, como sugerida, em análise, aprovada, rejeitada, reaberta ou arquivada.
- Impacto: Garante transparência e rastreabilidade operacional

### RN-010 — A IA não substitui o papel do steward de acesso
- Descrição: O papel de responsável por aprovar, rejeitar ou ajustar acessos deve permanecer com a pessoa autorizada, não com a IA.
- Impacto: Mantém responsabilidade e governança claras sobre o controle de acesso

---

## 3. Regras derivadas do domínio IAM

- Identidades devem ter vínculo claro com a estrutura organizacional ou com a função de sistema quando aplicável.
- Permissões excessivas e acessos sem justificativa de negócio devem ser evidenciados e revisados por responsáveis.
- A análise de risco deve apoiar a tomada de decisão, e não substituir o julgamento humano.
- Qualquer ação sobre identidades, perfis e permissões deve respeitar políticas internas de governança, sem automatizar decisões sem aprovação humana.

---

## 4. Conclusão

As regras de negócio do projeto consolidam a abordagem correta para governança de identidade: a IA serve como suporte analítico, enquanto o ser humano retém a decisão final e a responsabilidade sobre alterações de acesso.
