#!/bin/bash

echo "🚀 Testando aplicação de dengue..."

# Parar processos existentes
pkill -f "next" 2>/dev/null || true
sleep 2

# Limpar cache
rm -rf .next 2>/dev/null || true

echo "📦 Fazendo build..."
npm run build

if [ $? -eq 0 ]; then
    echo "✅ Build bem-sucedido!"
    echo "🚀 Iniciando servidor..."
    npm start &
    SERVER_PID=$!
    
    echo "⏳ Aguardando servidor inicializar..."
    sleep 10
    
    echo "🔍 Testando conexão..."
    if curl -s -I http://localhost:3000 | grep -q "200 OK"; then
        echo "✅ Aplicação funcionando em http://localhost:3000"
        echo "📊 Acesse o navegador e teste a funcionalidade!"
    else
        echo "❌ Erro ao conectar com a aplicação"
        echo "📋 Logs do servidor:"
        ps aux | grep next
    fi
    
    echo "🛑 Para parar o servidor, execute: kill $SERVER_PID"
else
    echo "❌ Erro no build"
fi
