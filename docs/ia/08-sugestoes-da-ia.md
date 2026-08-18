# Sugestões da IA

## 1. Visão geral

Durante a atividade, a IA foi usada para gerar sugestões iniciais de organização, requisitos, regras e cenários. Algumas sugestões agregaram valor e foram mantidas com ajustes; outras precisaram ser adaptadas; outras foram descartadas por não estarem alinhadas ao contexto do projeto.

---

## 2. Sugestões aproveitadas

### 2.1 Estruturação em documentos por tema
- A IA sugeriu dividir a especificação em artefatos separados para requisitos, regras, casos de uso, critérios e rastreabilidade.
- Essa sugestão foi aproveitada porque melhora a legibilidade, a manutenção e a rastreabilidade acadêmica do trabalho.

### 2.2 Identificação de requisitos funcionais e não funcionais
- A IA contribuiu para identificar requisitos coerentes com IAM, como representação de identidade, análise de permissões, identificação de privilege creep, conflitos de SoD e rastreabilidade de decisões.
- A lista foi ajustada para refletir o projeto conceitual e evitar requisitos tecnicamente excessivos ou sem base documental.

### 2.3 Definição de regras de negócio centrais
- A IA sugeriu regras claras sobre recomendação da IA, aprovação humana e rastreabilidade.
- Essas regras foram aproveitadas e reforçadas como núcleo do trabalho, porque são consistentes com o domínio e com a regra fundamental do projeto.

### 2.4 Cenários de critérios de aceitação
- A IA ajudou a sugerir critérios de aceite para identificação de risco, recomendação, aprovação, rejeição, falhas técnicas e histórico.
- Os cenários foram mantidos após revisão crítica para remover ambiguidades e reforçar o foco de governança.

---

## 3. Sugestões modificadas

### 3.1 Ajuste da linguagem dos requisitos
- A IA produziu versões mais gerais e, em alguns pontos, excessivamente amplas.
- Essas redações foram modificadas para torná-las mais objetivas, verificáveis e alinhadas ao escopo do projeto.

### 3.2 Organização da rastreabilidade
- A IA sugeriu uma estrutura simples de mapeamento entre artefatos.
- A estrutura foi ajustada para refletir melhor a relação entre requisitos, objetivos de negócio, casos de uso e critérios de aceitação.

### 3.3 Uso de termos específicos do domínio IAM
- Algumas sugestões iniciais usavam expressões mais genéricas.
- Foi necessário adaptar para termos mais específicos, como privilege creep, contas órfãs, acessos privilegiados e conflitos de Segregation of Duties.

---

## 4. Sugestões descartadas

### 4.1 Automação direta de ações de tratamento
- A IA sugeriu automatizar determinadas ações de tratamento de risco, como revogação imediata de permissões e confirmação de policy enforcement sem revisão humana.
- Essa sugestão foi descartada porque o projeto exige aprovação humana antes de qualquer alteração de acesso.
- Do ponto de vista técnico, a automação direta de revogação ou concessão de acesso introduz risco de ação indevida, especialmente em cenários de privilege creep, contas órfãs e conflitos de SoD.
- Do ponto de vista de governança, a decisão sobre acesso deve ser atribuída a um responsável com autoridade e rastreabilidade. A IA pode identificar e recomendar, mas não substituir a decisão humana nem os controles de separação de responsabilidades.

### 4.2 Redução do papel humano em decisões críticas
- Sugestões que diminuíram a relevância do papel do responsável humano foram descartadas, porque contradizem a regra fundamental do projeto.

### 4.3 Excesso de automação em regras de conformidade
- Sugestões que apresentavam ação automática em conformidade sem revisão humana também foram descartadas, pois poderiam gerar erros operacionais e violar princípios de auditoria e accountability.

---

## 5. Conclusão

A IA foi útil como geradora de ideias, suporte à estruturação e auxiliar de organização. No entanto, a crítica humana foi decisiva para preservar a arquitetura correta de governança: a IA recomenda; o ser humano decide; o sistema registra.
