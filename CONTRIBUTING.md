# Identity Risk Governance - Contribuindo

Obrigado por contribuir para o projeto Identity Risk Governance! 🙏

## Como Contribuir

### Antes de Começar

1. Faça fork do repositório
2. Clone seu fork localmente
3. Configure um remote upstream

```bash
git clone https://github.com/seu-usuario/identity-risk-governance.git
cd identity-risk-governance
git remote add upstream https://github.com/organization/identity-risk-governance.git
```

### Workflow de Contribuição

1. **Crie uma branch** para sua feature/fix
```bash
git checkout -b feature/minha-feature
```

2. **Faça seus commits** com mensagens descritivas
```bash
git commit -m "feat: adicionar novo controle de SoD

- Implementação de validação de segregação de deveres
- Testes unitários adicionados
- Documentação atualizada

Fixes #123"
```

3. **Push para seu fork**
```bash
git push origin feature/minha-feature
```

4. **Abra um Pull Request** com descrição clara

### Guias de Commit

#### Tipos de Commit (Conventional Commits)

- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Mudanças em documentação
- `style`: Formatação (sem mudança de código)
- `refactor`: Refatoração sem nova feature
- `test`: Adição de testes
- `chore`: Tarefas (dependências, build, etc)
- `ci`: Mudanças em CI/CD

#### Exemplos

```
feat: adicionar matriz de probabilidade x impacto
docs: atualizar README com novo diagrama
fix: corrigir cálculo de prioridade de risco
chore: atualizar dependências
```

### Padrões de Código

- **Markdown**: Use H1 (#), H2 (##), H3 (###) consistentemente
- **Tabelas**: Mantenha alinhamento com pipes
- **Listas**: Use - para bullets, números para ordenadas
- **Código**: Use blocos triple-backtick com linguagem especificada

### Processo de Review

1. Seu PR será revisado em até 2 dias úteis
2. Forneça feedback claro e construtivo
3. Atualize seu branch conforme comentários
4. Rebase before merge: `git rebase upstream/main`

### Convenção de Branches

```
main           # Production ready
develop        # Development branch
feature/*      # Novas funcionalidades
fix/*          # Bug fixes
docs/*         # Documentação
chore/*        # Tarefas
```

### Padrão de PR

```markdown
## Descrição
Brief description of changes

## Tipo de Mudança
- [ ] Feature nova
- [ ] Bug fix
- [ ] Breaking change
- [ ] Documentação

## Como Testar
Steps to reproduce...

## Checklist
- [ ] Código foi testado
- [ ] Documentação foi atualizada
- [ ] Sem warnings/errors
- [ ] Seguiu guias de estilo
```

---

## Código de Conduta

- Seja respeitoso
- Aceite crítica construtiva
- Foco no melhor para a comunidade
- Reportar abuso para: governance@company.com

---

## Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob Apache 2.0

---

## Perguntas?

Abra uma issue ou contacte: governance@company.com

**Obrigado por contribuir! 🎉**
