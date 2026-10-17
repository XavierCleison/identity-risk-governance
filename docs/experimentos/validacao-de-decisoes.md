# Experimento: validação de decisões de revisão de acessos

## Status e escopo

Este experimento implementa uma proposta de validação de entrada; não institui
uma regra oficial do produto nem altera os requisitos de governança existentes.
O código está em `identity_risk_governance/decision_validation.py` e os cenários
estão em `tests/test_decision_validation.py`.

## Regras usadas

| Decisão proposta | Validação experimental |
|---|---|
| `manter` | Aceita sem identificador de aprovador |
| `investigar` | Aceita sem identificador de aprovador |
| `revogar` | Exige identificador de aprovador humano não vazio |
| Valor desconhecido ou vazio | Rejeita com `ValueError` |

As opções e sua validação específica são propostas para este experimento e não
estão definidas como taxonomia oficial nos requisitos existentes. A exigência
de aprovação humana antes de uma alteração de acesso é compatível com RN-002,
RF-009 e CA-008. A tarefa solicitada limita-se à validação: a função não
registra nem executa concessões, revogações ou outras alterações.

## Limitações e lacunas

- LAC-009 e LAC-R-002 deixam em aberto o papel autorizado para aprovar cada tipo
  de decisão. O experimento apenas exige que seja informado um identificador
  textual não vazio; não verifica identidade, autorização ou aprovação real.
- Justificativa, evidências, data, registro de auditoria e persistência não são
  implementados; continuam relevantes para RF-009, RN-003 e RNF-004.
- A função não chama integrações de IAM e não realiza qualquer ação sobre
  permissões.

## Rastreabilidade dos testes

Os testes cobrem os cenários normal (`manter` e `investigar`), limite
(`revogar` com identificador), erro (`revogar` sem identificador) e entrada
inválida (decisão desconhecida ou vazia), alinhados ao escopo experimental e
relacionados a RF-009, RN-002 e CA-008.

Execute com Python 3.10 ou superior, sem dependências externas:

```text
python -m unittest discover -s tests -v
```
