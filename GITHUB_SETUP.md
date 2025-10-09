# Como Subir Este Projeto para o GitHub

## 📋 Pré-requisitos

1. Ter uma conta no GitHub: [https://github.com](https://github.com)
2. Git instalado localmente (já feito ✅)

## 🚀 Passos para Criar Repositório no GitHub

### Opção 1: Via Interface Web (Recomendado)

1. **Acesse o GitHub**: [https://github.com/new](https://github.com/new)

2. **Configurar o repositório:**
   - **Repository name**: `TCC1` ou `dengue-prediction`
   - **Description**: `Desenvolvimento de um Modelo de Previsão para Surtos de Dengue em Municípios Brasileiros utilizando Séries Temporais e Dados Climáticos`
   - **Visibility**: ✅ **Public** (Público)
   - ❌ **NÃO** marcar "Initialize this repository with a README" (já temos um)
   - ❌ **NÃO** adicionar .gitignore (já temos um)
   - ❌ **NÃO** adicionar License (já temos uma)

3. **Clique em "Create repository"**

4. **Na página que abrir, copie os comandos** que aparecem em "push an existing repository from the command line"

   Algo como:
   ```bash
   git remote add origin https://github.com/SEU_USUARIO/TCC1.git
   git branch -M main
   git push -u origin main
   ```

5. **Execute os comandos no terminal:**
   ```bash
   cd /Users/filippoferrari/Documents/UnB/TCC1
   
   # Adicionar remote (substitua SEU_USUARIO pelo seu usuário GitHub)
   git remote add origin https://github.com/SEU_USUARIO/TCC1.git
   
   # Renomear branch para main (se necessário)
   git branch -M main
   
   # Push inicial
   git push -u origin main
   ```

6. **Pronto! 🎉** Seu repositório está no GitHub!

---

### Opção 2: Via GitHub CLI (gh)

Se você tiver o GitHub CLI instalado:

```bash
cd /Users/filippoferrari/Documents/UnB/TCC1

# Criar repositório público
gh repo create TCC1 --public --source=. --remote=origin --push

# Ou com um nome mais descritivo
gh repo create dengue-prediction --public --source=. --remote=origin --push --description "Previsão de Surtos de Dengue usando Séries Temporais e Dados Climáticos"
```

---

## 🔧 Comandos Git Úteis

### Verificar status
```bash
git status
```

### Ver histórico de commits
```bash
git log --oneline
```

### Ver remote configurado
```bash
git remote -v
```

### Adicionar mudanças futuras
```bash
git add .
git commit -m "Descrição das mudanças"
git push
```

### Criar branch para feature
```bash
git checkout -b feature/nome-da-feature
# Fazer mudanças...
git add .
git commit -m "Implementar feature X"
git push -u origin feature/nome-da-feature
```

### Atualizar do remoto
```bash
git pull
```

---

## 📊 Adicionar Badges ao README (Opcional)

Após criar o repositório, você pode adicionar badges ao README.md:

```markdown
# TCC - Previsão de Surtos de Dengue no Brasil

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![GitHub issues](https://img.shields.io/github/issues/SEU_USUARIO/TCC1)](https://github.com/SEU_USUARIO/TCC1/issues)
[![GitHub stars](https://img.shields.io/github/stars/SEU_USUARIO/TCC1)](https://github.com/SEU_USUARIO/TCC1/stargazers)

...resto do README...
```

---

## 🌐 Configurar GitHub Pages (Opcional)

Para hospedar documentação online:

1. Vá em **Settings** → **Pages** no repositório
2. Selecione **Source**: Deploy from a branch
3. Selecione **Branch**: `main` e pasta `/docs`
4. Clique em **Save**

Sua documentação estará disponível em:
`https://SEU_USUARIO.github.io/TCC1/`

---

## 🔒 Proteger Branch Main (Recomendado)

1. Vá em **Settings** → **Branches**
2. Clique em **Add rule**
3. Configure:
   - **Branch name pattern**: `main`
   - ✅ Require a pull request before merging
   - ✅ Require status checks to pass
4. Clique em **Create**

Isso força que mudanças sejam feitas via Pull Request, melhorando qualidade.

---

## 📝 Adicionar Topics ao Repositório

No GitHub, clique em ⚙️ (Settings) ao lado de "About" e adicione topics:

- `machine-learning`
- `deep-learning`
- `time-series`
- `dengue`
- `epidemiology`
- `python`
- `tensorflow`
- `xgboost`
- `data-science`
- `public-health`

Isso ajuda outras pessoas a encontrarem seu projeto!

---

## 🤝 Adicionar Colaboradores (Opcional)

Se quiser adicionar colaboradores:

1. Vá em **Settings** → **Collaborators**
2. Clique em **Add people**
3. Digite o username do GitHub da pessoa

---

## 📢 Compartilhar o Projeto

Após publicar, você pode:

1. **Adicionar no LinkedIn**: Mostre seu projeto
2. **Compartilhar com orientador**: Facilita acompanhamento
3. **Submeter para showcases**: Dev.to, Kaggle, etc.
4. **Citar em artigos**: Repositório como material suplementar

---

## ✅ Checklist de Publicação

Antes de tornar público, verifique:

- [ ] README.md está completo e claro
- [ ] Não há dados sensíveis ou credenciais no código
- [ ] .gitignore está configurado corretamente
- [ ] LICENSE está incluída
- [ ] requirements.txt está atualizado
- [ ] Documentação em docs/ está completa
- [ ] Scripts têm comentários e docstrings
- [ ] Não há arquivos grandes (>100MB) commitados

---

## 🆘 Problemas Comuns

### "Repository not found" ao dar push
- Verifique se criou o repositório no GitHub
- Verifique se o remote está correto: `git remote -v`

### "Permission denied" ao dar push
- Configure suas credenciais do GitHub
- Considere usar SSH ao invés de HTTPS
- Ou use Personal Access Token

### Arquivo muito grande (>100MB)
- Adicione ao .gitignore
- Use Git LFS se realmente precisar versionar: `git lfs track "*.parquet"`

### Esqueci de adicionar .gitignore antes de commit
```bash
# Remover arquivos do histórico
git rm -r --cached data/raw/
git commit -m "Remove arquivos grandes do histórico"
```

---

## 📚 Recursos Úteis

- [Documentação Git](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com/)
- [Pro Git Book](https://git-scm.com/book/en/v2) (gratuito)
- [GitHub Skills](https://skills.github.com/) (tutoriais interativos)

---

**Boa sorte com seu TCC! 🚀**

Se tiver dúvidas, abra uma issue no repositório ou consulte a documentação oficial.

