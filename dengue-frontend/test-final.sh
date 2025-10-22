#!/bin/bash

echo "🧪 TESTE FINAL - Aplicação de Dengue"
echo "======================================"

# Parar processos existentes
echo "🛑 Parando processos existentes..."
pkill -f "next" 2>/dev/null || true
sleep 3

# Limpar cache
echo "🧹 Limpando cache..."
rm -rf .next 2>/dev/null || true

# Testar build
echo "📦 Testando build..."
npm run build

if [ $? -eq 0 ]; then
    echo "✅ Build bem-sucedido!"
    
    # Iniciar servidor
    echo "🚀 Iniciando servidor..."
    npm start &
    SERVER_PID=$!
    
    # Aguardar inicialização
    echo "⏳ Aguardando servidor inicializar..."
    sleep 10
    
    # Testar aplicação
    echo "🔍 Testando aplicação..."
    if curl -s -I http://localhost:3000 | grep -q "200 OK"; then
        echo "✅ Aplicação funcionando!"
        
        # Testar proxy da API
        echo "🔍 Testando proxy da API..."
        API_RESPONSE=$(curl -s "http://localhost:3000/api/dengue?nu_ano=2025&limit=1&offset=0")
        
        if echo "$API_RESPONSE" | grep -q "parametros"; then
            echo "✅ Proxy da API funcionando!"
            echo "📊 Dados recebidos da API do governo"
            
            # Mostrar resumo dos dados
            echo "📋 Resumo dos dados:"
            echo "$API_RESPONSE" | jq -r '.parametros[0] | "Data: \(.dt_notific), Idade: \(.nu_idade_n), Sexo: \(.cs_sexo)"' 2>/dev/null || echo "Dados recebidos (formato JSON)"
            
            echo ""
            echo "🎉 SUCESSO! Aplicação funcionando perfeitamente!"
            echo "🌐 Acesse: http://localhost:3000"
            echo "📊 Digite o ano e clique em 'Buscar Dados'"
            echo ""
            echo "🛑 Para parar: kill $SERVER_PID"
        else
            echo "❌ Erro no proxy da API"
            echo "📋 Resposta: $API_RESPONSE"
        fi
    else
        echo "❌ Erro na aplicação"
    fi
else
    echo "❌ Erro no build"
fi
