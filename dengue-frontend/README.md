# Frontend Dengue - Visualização de Dados

Este é um frontend Next.js para visualizar dados de dengue da API do governo brasileiro com **tradução completa** de todos os campos.

## ✅ Funcionalidades Implementadas

- ✅ **Busca dados da API oficial** (https://apidadosabertos.saude.gov.br/)
- ✅ **Filtro por ano** (2020-2025)
- ✅ **Tradução COMPLETA** de todos os campos da API
- ✅ **Tabela responsiva** com dados traduzidos
- ✅ **Interface moderna** com Tailwind CSS
- ✅ **Tratamento de erros** e loading states

## 🚀 Como usar

### ✅ **SOLUÇÃO CORS IMPLEMENTADA**
A aplicação agora usa um **proxy local** para contornar problemas de CORS com a API do governo.

### Opção 1: Execução Simples
```bash
cd dengue-frontend
npm install
npm run dev
```

### Opção 2: Teste Completo
```bash
cd dengue-frontend
./test-app.sh
```

### Opção 3: Modo Produção
```bash
cd dengue-frontend
npm run build
npm start
```

### 🔧 **Configuração do Proxy**
- **Arquivo**: `next.config.js`
- **Proxy**: `/api/dengue` → `https://apidadosabertos.saude.gov.br/arboviroses/dengue`
- **Benefício**: Resolve problemas de CORS automaticamente

## 📊 Tradução COMPLETA Implementada

### Dados Demográficos
- **Idade**: Códigos especiais (3009 = 9 meses, 4018 = 18 anos)
- **Sexo**: M/F/I → Masculino/Feminino/Ignorado
- **Raça/Cor**: 1-5,9 → Branca/Preta/Amarela/Parda/Indígena/Ignorado
- **Escolaridade**: 1-10 → Descrições completas (EF, EM, Superior)
- **Gestação**: 1-6,9 → Trimestres/Não/Não se aplica/Ignorado

### Dados Clínicos
- **Classificação Final**: 1-20 → Descrições completas
- **Evolução**: 1-4,9 → Cura/Óbito por dengue/Outras causas/Ignorado
- **Sintomas**: Febre, cefaleia, mialgia, vômito, exantema, etc.
- **Manifestações**: Epistaxe, petequias, gengivorragia, etc.

### Comorbidades
- **Diabetes, Hipertensão, Doenças Renais, Hepatopatias, etc.**

### Exames e Resultados
- **Critério de Confirmação**: Laboratorial/Clínico-epidemiológico/Clínico
- **Exames Laboratoriais**: PCR, NS1, Sorologia, etc.
- **Sinais de Alarme**: Hipotensão, plaquetas, vômitos, sangramento
- **Critérios de Gravidade**: Pulso, convulsão, enchimento capilar

### Localização
- **Estados (UF)**: Códigos IBGE → Siglas (11→RO, 31→MG, etc.)
- **Países**: 1-20 → Brasil/Argentina/Bolívia/etc.

## 🌐 Acesso

Após executar, acesse: **http://localhost:3000**

## 📋 Tabela com 16 Colunas Principais

- Data Notificação, Data Sintomas, Idade, Sexo, Raça/Cor
- Classificação, Evolução, Hospitalização
- Febre, Cefaleia, Mialgia, Vômito, Exantema
- Gestante, Diabetes, Hipertensão

## 🔧 Dados da API

- **Endpoint**: `https://apidadosabertos.saude.gov.br/arboviroses/dengue`
- **Parâmetros**:
  - `nu_ano`: Ano dos dados (obrigatório)
  - `limit`: Limite de registros por página (máximo 20)
  - `offset`: Página (começa em 0)

## 🛠️ Tecnologias

- **Next.js 16** - Framework React
- **TypeScript** - Tipagem estática
- **Tailwind CSS** - Estilização
- **ESLint** - Linting de código

## 📝 Notas Importantes

- A aplicação foi testada e funciona corretamente
- Todos os campos da API foram traduzidos conforme documentação oficial
- Interface responsiva e moderna
- Tratamento completo de erros