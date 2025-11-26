import xlsxwriter

# --- Configuração do Cronograma no Estilo Tabela com Células Coloridas ---

# Definir os meses do cronograma (colunas)
meses = ['09/2025', '10/2025', '11/2025', '12/2025', '01/2026', '02/2026', '03/2026']

# Dados das tarefas organizadas por fase
# Formato: (Fase, Tarefa, mês_início, mês_fim, status)
# status: 'realizada' (verde escuro) ou 'a_realizar' (verde claro)
tarefas = [
    # TCC 1 - Planejamento da Pesquisa
    ('Planejamento da Pesquisa', '1. Background', 0, 0, 'realizada'),
    ('Planejamento da Pesquisa', '   Pesquisa bibliográfica', 0, 1, 'realizada'),
    ('Planejamento da Pesquisa', '   Definição do problema, objetivos e metodologia', 0, 1, 'realizada'),
    ('Planejamento da Pesquisa', '2. Design', 1, 1, 'realizada'),
    ('Planejamento da Pesquisa', '3. Seleção do caso', 1, 1, 'realizada'),
    ('Planejamento da Pesquisa', '   Pesquisa documental', 1, 2, 'realizada'),
    ('Planejamento da Pesquisa', '4. Procedimentos e papéis', 1, 2, 'realizada'),
    
    # TCC 1 - Coleta de Dados
    ('Coleta de Dados', '5. Coleta de dados', 1, 2, 'realizada'),
    ('Coleta de Dados', '   Download e processamento SINAN', 1, 2, 'realizada'),
    ('Coleta de Dados', '   Download e processamento INMET', 1, 2, 'realizada'),
    ('Coleta de Dados', '   Pipeline ETL e unificação', 2, 2, 'realizada'),
    
    # TCC 1 - Análise dos Dados
    ('Análise dos Dados', '6. Análise', 2, 3, 'realizada'),
    ('Análise dos Dados', '7. Validação do plano', 2, 2, 'realizada'),
    ('Análise dos Dados', '8. Limitações do estudo', 2, 3, 'realizada'),
    
    # TCC 1 - Relatório
    ('Relatório', '9. Relatório', 2, 3, 'realizada'),
    ('Relatório', '10. Cronograma', 2, 2, 'realizada'),
    ('Relatório', '11. Apêndices', 2, 3, 'realizada'),
    ('Relatório', 'Defesa do TCC1', 3, 3, 'realizada'),
    
    # TCC 2 - Modelagem
    ('Modelagem', 'Feature Engineering', 3, 3, 'a_realizar'),
    ('Modelagem', 'Implementação SARIMA', 3, 4, 'a_realizar'),
    ('Modelagem', 'Implementação XGBoost', 4, 4, 'a_realizar'),
    ('Modelagem', 'Implementação LSTM', 4, 5, 'a_realizar'),
    ('Modelagem', 'Comparação de Modelos', 5, 5, 'a_realizar'),
    
    # TCC 2 - Finalização
    ('Finalização', 'Escrita e submissão de artigos', 5, 6, 'a_realizar'),
    ('Finalização', 'Defesa do TCC2', 6, 6, 'a_realizar'),
]

# Criar o workbook
workbook = xlsxwriter.Workbook('Cronograma_TCC_2025.xlsx')
worksheet = workbook.add_worksheet('Cronograma')

# --- Definir formatos ---
title_format = workbook.add_format({
    'bold': True, 
    'font_size': 14, 
    'align': 'center', 
    'valign': 'vcenter',
    'border': 1
})

header_format = workbook.add_format({
    'bold': True, 
    'font_size': 10, 
    'align': 'center', 
    'valign': 'vcenter',
    'bg_color': '#375623',
    'font_color': 'white',
    'border': 1,
    'text_wrap': True
})

# Formato para os meses (com rotação)
header_meses_format = workbook.add_format({
    'bold': True, 
    'font_size': 10, 
    'align': 'center', 
    'valign': 'vcenter',
    'bg_color': '#375623',
    'font_color': 'white',
    'border': 1,
    'text_wrap': True,
    'rotation': 45
})

fase_format = workbook.add_format({
    'bold': True, 
    'font_size': 9, 
    'align': 'left', 
    'valign': 'vcenter',
    'bg_color': '#F2F2F2',
    'border': 1,
    'text_wrap': True
})

tarefa_format = workbook.add_format({
    'font_size': 9, 
    'align': 'left', 
    'valign': 'vcenter',
    'border': 1,
    'text_wrap': True
})

# Célula verde escura (atividade realizada)
verde_escuro = workbook.add_format({
    'bg_color': '#375623',
    'border': 1
})

# Célula cinza clara (atividade a realizar)
cinza_claro = workbook.add_format({
    'bg_color': '#D9D9D9',
    'border': 1
})

# Célula vazia com borda
vazio_format = workbook.add_format({
    'border': 1
})

# --- Configurar larguras das colunas ---
worksheet.set_column('A:A', 18)  # Fases
worksheet.set_column('B:B', 50)  # Etapas/Tarefas
worksheet.set_column('C:I', 8)   # Meses

# --- Escrever título ---
worksheet.merge_range('A1:I1', 'Cronograma do Projeto de Pesquisa - TCC 2025/2026', title_format)
worksheet.set_row(0, 25)

# --- Escrever cabeçalhos ---
worksheet.write('A2', 'Fases', header_format)
worksheet.write('B2', 'Etapas do Projeto', header_format)
worksheet.set_row(1, 30)

# Escrever os meses (com altura maior para texto diagonal)
worksheet.set_row(1, 60)
for col, mes in enumerate(meses):
    worksheet.write(1, col + 2, mes, header_meses_format)

# --- Escrever as tarefas ---
row = 2
fase_atual = None

for fase, tarefa, mes_inicio, mes_fim, status in tarefas:
    # Escrever a fase (apenas se mudou)
    if fase != fase_atual:
        worksheet.write(row, 0, fase, fase_format)
        fase_atual = fase
    else:
        worksheet.write(row, 0, '', fase_format)
    
    # Escrever a tarefa
    worksheet.write(row, 1, tarefa, tarefa_format)
    
    # Preencher as células dos meses
    for col in range(len(meses)):
        if mes_inicio <= col <= mes_fim:
            if status == 'realizada':
                worksheet.write(row, col + 2, '', verde_escuro)
            else:
                worksheet.write(row, col + 2, '', cinza_claro)
        else:
            worksheet.write(row, col + 2, '', vazio_format)
    
    row += 1

# --- Adicionar legenda ---
row += 1
worksheet.write(row, 0, 'Legenda:', workbook.add_format({'bold': True}))
row += 1
worksheet.write(row, 0, '', verde_escuro)
worksheet.write(row, 1, 'Atividades realizadas', tarefa_format)
row += 1
worksheet.write(row, 0, '', cinza_claro)
worksheet.write(row, 1, 'Atividades a serem realizadas', tarefa_format)

# Salvar o arquivo
workbook.close()

print("Arquivo 'Cronograma_TCC_2025.xlsx' criado com sucesso!")
print("O cronograma está no estilo de tabela com células coloridas, similar à imagem de referência.")
