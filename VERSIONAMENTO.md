# Sistema de Versionamento - OLY Planejamento Estratégico

## 📋 Visão Geral

Este repositório utiliza um sistema de versionamento automatizado que cria uma nova branch para cada alteração no site, seguindo o padrão solicitado pelo usuário.

## 🚀 Como Usar

### Método Automatizado (Recomendado)

1. **Faça suas alterações** nos arquivos do site (HTML, CSS, JS, etc.)

2. **Execute o script de versionamento**:
   ```bash
   ./version_manager.sh v1.1 "Descrição da alteração"
   ```

3. **O script automaticamente**:
   - Cria uma nova branch com o nome da versão (ex: v1.1)
   - Faz commit das alterações
   - Envia a branch para o GitHub
   - Faz merge na branch main
   - Atualiza a branch main no GitHub

### Método Manual

Se preferir fazer manualmente:

```bash
# 1. Criar nova branch
git checkout -b v1.1

# 2. Adicionar alterações
git add .

# 3. Fazer commit
git commit -m "v1.1: Descrição da alteração"

# 4. Enviar branch para GitHub
git push -u origin v1.1

# 5. Voltar para main e fazer merge
git checkout main
git merge v1.1
git push origin main
```

## 📝 Padrão de Nomenclatura

- **Branches**: `v1.0`, `v1.1`, `v1.2`, `v2.0`, etc.
- **Commits**: `v1.1: Descrição clara da alteração`

## 🌿 Estrutura de Branches

- **main**: Branch principal com a versão mais atual
- **v1.0**: Versão inicial
- **v1.1**: Primeira atualização
- **v1.2**: Segunda atualização
- **v2.0**: Versão major com mudanças significativas

## 📁 Arquivos do Projeto

- `index.html` - Página principal do site
- `styles.css` - Estilos CSS
- `scripts.js` - Scripts JavaScript
- `*.md` - Documentos de planejamento estratégico
- `*.csv` - Dados e cronogramas
- `version_manager.sh` - Script de automação
- `VERSIONAMENTO.md` - Esta documentação

## 🔗 Links Úteis

- **Repositório**: https://github.com/EdmarJunior13/oly-planejamento-estrategico
- **Site**: Acesse através do GitHub Pages (se habilitado)

## ⚠️ Importante

- Sempre teste suas alterações localmente antes de fazer commit
- Use mensagens de commit descritivas
- Mantenha o padrão de versionamento consistente
- Cada alteração = nova branch com nova versão

