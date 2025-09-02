#!/bin/bash

# Script de Gerenciamento de Versões - OLY Planejamento Estratégico
# Uso: ./version_manager.sh <versao> "<mensagem_commit>"
# Exemplo: ./version_manager.sh v1.1 "Atualização do layout principal"

if [ $# -ne 2 ]; then
    echo "Uso: $0 <versao> \"<mensagem_commit>\""
    echo "Exemplo: $0 v1.1 \"Atualização do layout principal\""
    exit 1
fi

VERSION=$1
COMMIT_MESSAGE=$2

echo "🚀 Iniciando processo de versionamento..."
echo "📋 Versão: $VERSION"
echo "💬 Mensagem: $COMMIT_MESSAGE"

# Verificar se há mudanças para commit
if git diff --quiet && git diff --staged --quiet; then
    echo "❌ Nenhuma alteração detectada. Faça suas modificações antes de executar o script."
    exit 1
fi

# Criar nova branch
echo "🌿 Criando branch $VERSION..."
git checkout -b $VERSION

# Adicionar todas as alterações
echo "📦 Adicionando alterações..."
git add .

# Fazer commit
echo "💾 Fazendo commit..."
git commit -m "$VERSION: $COMMIT_MESSAGE"

# Push da nova branch
echo "☁️ Enviando branch para GitHub..."
git push -u origin $VERSION

# Voltar para main
echo "🔄 Retornando para branch main..."
git checkout main

# Fazer merge da nova versão na main
echo "🔗 Fazendo merge na branch main..."
git merge $VERSION

# Push da main atualizada
echo "☁️ Enviando main atualizada para GitHub..."
git push origin main

echo "✅ Processo concluído com sucesso!"
echo "🌐 Repositório: https://github.com/EdmarJunior13/oly-planejamento-estrategico"
echo "🌿 Branch criada: $VERSION"
echo "📋 Commit: $VERSION: $COMMIT_MESSAGE"

