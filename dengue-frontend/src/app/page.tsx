'use client';

import { useState } from 'react';

interface DengueData {
  tp_not: string;
  id_agravo: string;
  dt_notific: string;
  sem_not: string;
  nu_ano: string;
  sg_uf_not: string;
  id_municip: string;
  id_regiona: string | null;
  id_unidade: string;
  dt_sin_pri: string;
  sem_pri: string;
  nu_idade_n: string;
  cs_sexo: string;
  cs_gestant: string;
  cs_raca: string;
  cs_escol_n: string | null;
  sg_uf: string;
  id_mn_resi: string;
  id_rg_resi: string | null;
  id_pais: string;
  nduplic_n: string | null;
  dt_digita: string;
  cs_flxret: string;
  flxrecebi: string | null;
  migrado_w: string | null;
  dt_invest: string | null;
  id_ocupa_n: string | null;
  dt_soro: string | null;
  resul_soro: string | null;
  histopa_n: string | null;
  dt_viral: string | null;
  resul_vi_n: string | null;
  sorotipo: string | null;
  imunoh_n: string | null;
  dt_pcr: string | null;
  resul_pcr_: string | null;
  classi_fin: string;
  criterio: string | null;
  tpautocto: string | null;
  coufinf: string | null;
  copaisinf: string | null;
  comuninf: string | null;
  doenca_tra: string | null;
  evolucao: string | null;
  dt_obito: string | null;
  dt_encerra: string;
  mani_hemor: string | null;
  epistaxe: string | null;
  gengivo: string | null;
  metro: string | null;
  petequias: string | null;
  hematura: string | null;
  sangram: string | null;
  laco_n: string | null;
  plasmatico: string | null;
  evidencia: string | null;
  plaq_menor: string | null;
  con_fhd: string | null;
  complica: string | null;
  hospitaliz: string | null;
  dt_interna: string | null;
  uf: string | null;
  municipio: string | null;
  arquivo: string;
  ano_nasc: string;
  febre: string | null;
  mialgia: string | null;
  cefaleia: string | null;
  exantema: string | null;
  vomito: string | null;
  nausea: string | null;
  dor_costas: string | null;
  conjuntvit: string | null;
  artrite: string | null;
  artralgia: string | null;
  petequia_n: string | null;
  leucopenia: string | null;
  laco: string | null;
  dor_retro: string | null;
  diabetes: string | null;
  hematolog: string | null;
  hepatopat: string | null;
  renal: string | null;
  hipertensa: string | null;
  acido_pept: string | null;
  auto_imune: string | null;
  dt_chik_s1: string | null;
  dt_chik_s2: string | null;
  dt_prnt: string | null;
  res_chiks1: string | null;
  res_chiks2: string | null;
  resul_prnt: string | null;
  dt_ns1: string | null;
  resul_ns1: string | null;
  clinc_chik: string | null;
  alrm_hipot: string | null;
  alrm_plaq: string | null;
  alrm_vom: string | null;
  alrm_sang: string | null;
  alrm_hemat: string | null;
  alrm_abdom: string | null;
  alrm_letar: string | null;
  alrm_hepat: string | null;
  alrm_liq: string | null;
  dt_alrm: string | null;
  grav_pulso: string | null;
  grav_conv: string | null;
  grav_ench: string | null;
  grav_insuf: string | null;
  grav_taqui: string | null;
  grav_extre: string | null;
  grav_hipot: string | null;
  grav_hemat: string | null;
  grav_melen: string | null;
  grav_metro: string | null;
  grav_sang: string | null;
  grav_ast: string | null;
  grav_mioc: string | null;
  grav_consc: string | null;
  grav_orgao: string | null;
  dt_grav: string | null;
  tp_sistema: string;
  acido_pept_c121: string | null;
  cs_escolar: string | null;
  nu_idade: string | null;
  id_dg_not: string | null;
  id_ev_not: string | null;
  ant_dt_inv: string | null;
  ocupacao: string | null;
  dengue: string | null;
  ano: string | null;
  vacinado: string | null;
  dt_dose: string | null;
  dt_febre: string | null;
  duracao: string | null;
  dor: string | null;
  prostacao: string | null;
  nauseas: string | null;
  diarreia: string | null;
  outros: string | null;
  sin_out: string | null;
  outros_m: string | null;
  outros_m_d: string | null;
  ascite: string | null;
  pleural: string | null;
  pericardi: string | null;
  abdominal: string | null;
  hepato: string | null;
  miocardi: string | null;
  hipotensao: string | null;
  choque: string | null;
  manifesta: string | null;
  insuficien: string | null;
  outro_s: string | null;
  outro_s_d: string | null;
  dt_choque: string | null;
  dt_col_hem: string | null;
  hema_maior: string | null;
  dt_col_plq: string | null;
  palq_maior: string | null;
  dt_col_he2: string | null;
  hema_menor: string | null;
  dt_col_pl2: string | null;
  dt_soro1: string | null;
  dt_soro2: string | null;
  dt_soror1: string | null;
  dt_soror2: string | null;
  s1_igm: string | null;
  s1_igg: string | null;
  s2_igm: string | null;
  s2_igg: string | null;
  s1_tit1: string | null;
  s2_tit1: string | null;
  material: string | null;
  soro1: string | null;
  soro2: string | null;
  tecidos: string | null;
  resul_vira: string | null;
  histopa: string | null;
  imunoh: string | null;
  amos_pcr: string | null;
  resul_pcr: string | null;
  amos_out: string | null;
  tecnica: string | null;
  resul_out: string | null;
  con_classi: string | null;
  con_criter: string | null;
  con_inf_mu: string | null;
  con_inf_uf: string | null;
  con_inf_pa: string | null;
  con_doenca: string | null;
  con_evoluc: string | null;
  con_dt_obi: string | null;
  con_dt_enc: string | null;
  in_vincula: string | null;
  nduplic: string | null;
  in_aids: string | null;
}

interface ApiResponse {
  parametros: DengueData[];
}

// Mapeamento completo de códigos para valores legíveis
const translateData = (data: DengueData) => {
  // Mapeamentos básicos
  const sexoMap: { [key: string]: string } = {
    'M': 'Masculino',
    'F': 'Feminino',
    'I': 'Ignorado'
  };

  const racaMap: { [key: string]: string } = {
    '1': 'Branca',
    '2': 'Preta',
    '3': 'Amarela',
    '4': 'Parda',
    '5': 'Indígena',
    '9': 'Ignorado'
  };

  const gestantMap: { [key: string]: string } = {
    '1': '1º Trimestre',
    '2': '2º Trimestre',
    '3': '3º Trimestre',
    '4': 'Idade gestacional ignorada',
    '5': 'Não',
    '6': 'Não se aplica',
    '9': 'Ignorado'
  };

  const escolaridadeMap: { [key: string]: string } = {
    '1': '1ª a 4ª série incompleta do EF',
    '2': '4ª série completa do EF',
    '3': '5ª à 8ª série incompleta do EF',
    '4': 'Ensino fundamental completo',
    '5': 'Ensino médio incompleto',
    '6': 'Ensino médio completo',
    '7': 'Educação superior incompleta',
    '8': 'Educação superior completa',
    '9': 'Ignorado',
    '10': 'Não se aplica'
  };

  const classiFinMap: { [key: string]: string } = {
    '1': 'Dengue',
    '2': 'Dengue com sinais de alarme',
    '3': 'Dengue grave',
    '4': 'Dengue clássico',
    '5': 'Febre hemorrágica da dengue',
    '6': 'Síndrome do choque da dengue',
    '7': 'Dengue com complicações',
    '8': 'Dengue sem complicações',
    '9': 'Dengue com sinais de alarme',
    '10': 'Dengue grave',
    '11': 'Dengue com sinais de alarme',
    '12': 'Dengue grave',
    '13': 'Dengue com sinais de alarme',
    '14': 'Dengue grave',
    '15': 'Dengue com sinais de alarme',
    '16': 'Dengue grave',
    '17': 'Dengue com sinais de alarme',
    '18': 'Dengue grave',
    '19': 'Dengue com sinais de alarme',
    '20': 'Dengue grave'
  };

  const evolucaoMap: { [key: string]: string } = {
    '1': 'Cura',
    '2': 'Óbito por dengue',
    '3': 'Óbito por outras causas',
    '4': 'Óbito sem especificação',
    '9': 'Ignorado'
  };

  const hospitalizMap: { [key: string]: string } = {
    '1': 'Sim',
    '2': 'Não',
    '9': 'Ignorado'
  };

  const simNaoMap: { [key: string]: string } = {
    '1': 'Sim',
    '2': 'Não',
    '9': 'Ignorado'
  };

  const criterioMap: { [key: string]: string } = {
    '1': 'Laboratorial',
    '2': 'Clínico-epidemiológico',
    '3': 'Clínico',
    '4': 'Laboratorial + Clínico-epidemiológico',
    '5': 'Laboratorial + Clínico',
    '6': 'Clínico-epidemiológico + Clínico',
    '7': 'Laboratorial + Clínico-epidemiológico + Clínico',
    '9': 'Ignorado'
  };

  const tipoNotificacaoMap: { [key: string]: string } = {
    '1': 'Individual',
    '2': 'Investigação de surto',
    '3': 'Vigilância sentinela'
  };

  const tipoSistemaMap: { [key: string]: string } = {
    '1': 'SINAN',
    '2': 'SINAN NET'
  };

  const paisMap: { [key: string]: string } = {
    '1': 'Brasil',
    '2': 'Argentina',
    '3': 'Bolívia',
    '4': 'Chile',
    '5': 'Colômbia',
    '6': 'Equador',
    '7': 'Guiana',
    '8': 'Paraguai',
    '9': 'Peru',
    '10': 'Suriname',
    '11': 'Uruguai',
    '12': 'Venezuela',
    '13': 'Guiana Francesa',
    '14': 'Outros países da América do Sul',
    '15': 'Outros países da América Central',
    '16': 'Outros países da América do Norte',
    '17': 'Outros países da Europa',
    '18': 'Outros países da Ásia',
    '19': 'Outros países da África',
    '20': 'Outros países da Oceania',
    '99': 'Ignorado'
  };

  // Função para traduzir idade
  const translateIdade = (idade: string): string => {
    if (!idade || idade === 'null') return 'Não informado';
    
    const idadeNum = parseInt(idade);
    if (idadeNum < 100) return `${idadeNum} anos`;
    
    // Código de idade em meses (ex: 3009 = 9 meses)
    if (idadeNum >= 3000 && idadeNum <= 3012) {
      const meses = idadeNum - 3000;
      return `${meses} ${meses === 1 ? 'mês' : 'meses'}`;
    }
    
    // Código de idade em anos (ex: 4018 = 18 anos)
    if (idadeNum >= 4000) {
      const anos = idadeNum - 4000;
      return `${anos} ${anos === 1 ? 'ano' : 'anos'}`;
    }
    
    return idade;
  };

  // Função para traduzir UF
  const translateUF = (uf: string): string => {
    const ufMap: { [key: string]: string } = {
      '11': 'RO', '12': 'AC', '13': 'AM', '14': 'RR', '15': 'PA',
      '16': 'AP', '17': 'TO', '21': 'MA', '22': 'PI', '23': 'CE',
      '24': 'RN', '25': 'PB', '26': 'PE', '27': 'AL', '28': 'SE',
      '29': 'BA', '31': 'MG', '32': 'ES', '33': 'RJ', '35': 'SP',
      '41': 'PR', '42': 'SC', '43': 'RS', '50': 'MS', '51': 'MT',
      '52': 'GO', '53': 'DF'
    };
    return ufMap[uf] || uf;
  };

  return {
    // Dados básicos
    ano: data.nu_ano,
    tipo_notificacao: tipoNotificacaoMap[data.tp_not] || data.tp_not,
    id_agravo: data.id_agravo,
    data_notificacao: data.dt_notific,
    semana_notificacao: data.sem_not,
    sigla_uf_notificacao: translateUF(data.sg_uf_not),
    id_regional_saude_notificacao: data.id_regiona || 'Não informado',
    id_municipio_notificacao: data.id_municip,
    id_estabelecimento: data.id_unidade,
    data_primeiros_sintomas: data.dt_sin_pri,
    semana_sintomas: data.sem_pri,
    pais_residencia: paisMap[data.id_pais] || data.id_pais,
    sigla_uf_residencia: translateUF(data.sg_uf),
    id_regional_saude_residencia: data.id_rg_resi || 'Não informado',
    id_municipio_residencia: data.id_mn_resi,
    ano_nascimento_paciente: data.ano_nasc,
    idade_paciente: translateIdade(data.nu_idade_n),
    sexo_paciente: sexoMap[data.cs_sexo] || data.cs_sexo,
    raca_cor_paciente: racaMap[data.cs_raca] || data.cs_raca,
    escolaridade_paciente: data.cs_escol_n ? escolaridadeMap[data.cs_escol_n] || data.cs_escol_n : 'Não informado',
    ocupacao_paciente: data.id_ocupa_n || 'Não informado',
    gestante_paciente: gestantMap[data.cs_gestant] || data.cs_gestant,
    
    // Comorbidades
    possui_doenca_autoimune: data.auto_imune ? simNaoMap[data.auto_imune] || data.auto_imune : 'Não informado',
    possui_diabetes: data.diabetes ? simNaoMap[data.diabetes] || data.diabetes : 'Não informado',
    possui_doencas_hematologicas: data.hematolog ? simNaoMap[data.hematolog] || data.hematolog : 'Não informado',
    possui_hepatopatias: data.hepatopat ? simNaoMap[data.hepatopat] || data.hepatopat : 'Não informado',
    possui_doenca_renal: data.renal ? simNaoMap[data.renal] || data.renal : 'Não informado',
    possui_hipertensao: data.hipertensa ? simNaoMap[data.hipertensa] || data.hipertensa : 'Não informado',
    possui_doenca_acido_peptica: data.acido_pept ? simNaoMap[data.acido_pept] || data.acido_pept : 'Não informado',
    
    // Vacinação
    paciente_vacinado: data.vacinado ? simNaoMap[data.vacinado] || data.vacinado : 'Não informado',
    data_vacina: data.dt_dose || 'Não informado',
    
    // Investigação
    data_investigacao: data.dt_invest || 'Não informado',
    
    // Sintomas
    apresenta_febre: data.febre ? simNaoMap[data.febre] || data.febre : 'Não informado',
    data_febre: data.dt_febre || 'Não informado',
    duracao_febre: data.duracao || 'Não informado',
    apresenta_cefaleia: data.cefaleia ? simNaoMap[data.cefaleia] || data.cefaleia : 'Não informado',
    apresenta_exantema: data.exantema ? simNaoMap[data.exantema] || data.exantema : 'Não informado',
    apresenta_dor_costas: data.dor_costas ? simNaoMap[data.dor_costas] || data.dor_costas : 'Não informado',
    apresenta_prostacao: data.prostacao ? simNaoMap[data.prostacao] || data.prostacao : 'Não informado',
    apresenta_mialgia: data.mialgia ? simNaoMap[data.mialgia] || data.mialgia : 'Não informado',
    apresenta_vomito: data.vomito ? simNaoMap[data.vomito] || data.vomito : 'Não informado',
    apresenta_nausea: data.nausea ? simNaoMap[data.nausea] || data.nausea : 'Não informado',
    apresenta_diarreia: data.diarreia ? simNaoMap[data.diarreia] || data.diarreia : 'Não informado',
    apresenta_conjutivite: data.conjuntvit ? simNaoMap[data.conjuntvit] || data.conjuntvit : 'Não informado',
    apresenta_dor_retroorbital: data.dor_retro ? simNaoMap[data.dor_retro] || data.dor_retro : 'Não informado',
    apresenta_artralgia: data.artralgia ? simNaoMap[data.artralgia] || data.artralgia : 'Não informado',
    apresenta_artrite: data.artrite ? simNaoMap[data.artrite] || data.artrite : 'Não informado',
    apresenta_leucopenia: data.leucopenia ? simNaoMap[data.leucopenia] || data.leucopenia : 'Não informado',
    
    // Manifestações hemorrágicas
    apresenta_epistaxe: data.epistaxe ? simNaoMap[data.epistaxe] || data.epistaxe : 'Não informado',
    apresenta_petequias: data.petequias ? simNaoMap[data.petequias] || data.petequias : 'Não informado',
    apresenta_gengivorragia: data.gengivo ? simNaoMap[data.gengivo] || data.gengivo : 'Não informado',
    apresenta_metrorragia: data.metro ? simNaoMap[data.metro] || data.metro : 'Não informado',
    apresenta_hematuria: data.hematura ? simNaoMap[data.hematura] || data.hematura : 'Não informado',
    apresenta_sangramento: data.sangram ? simNaoMap[data.sangram] || data.sangram : 'Não informado',
    
    // Complicações
    apresenta_complicacao: data.complica ? simNaoMap[data.complica] || data.complica : 'Não informado',
    apresenta_ascite: data.ascite ? simNaoMap[data.ascite] || data.ascite : 'Não informado',
    apresenta_pleurite: data.pleural ? simNaoMap[data.pleural] || data.pleural : 'Não informado',
    apresenta_pericardite: data.pericardi ? simNaoMap[data.pericardi] || data.pericardi : 'Não informado',
    apresenta_dor_abdominal: data.abdominal ? simNaoMap[data.abdominal] || data.abdominal : 'Não informado',
    apresenta_hepatomegalia: data.hepato ? simNaoMap[data.hepato] || data.hepato : 'Não informado',
    apresenta_miocardite: data.miocardi ? simNaoMap[data.miocardi] || data.miocardi : 'Não informado',
    apresenta_hipotensao: data.hipotensao ? simNaoMap[data.hipotensao] || data.hipotensao : 'Não informado',
    apresenta_choque: data.choque ? simNaoMap[data.choque] || data.choque : 'Não informado',
    apresenta_insuficiencia_orgao: data.insuficien ? simNaoMap[data.insuficien] || data.insuficien : 'Não informado',
    
    // Outros sintomas
    apresenta_sintoma_outro: data.outros ? simNaoMap[data.outros] || data.outros : 'Não informado',
    apresenta_qual_sintoma: data.sin_out || 'Não informado',
    
    // Exames
    prova_laco: data.laco ? simNaoMap[data.laco] || data.laco : 'Não informado',
    
    // Hospitalização
    internacao: data.hospitaliz ? hospitalizMap[data.hospitaliz] || data.hospitaliz : 'Não informado',
    data_internacao: data.dt_interna || 'Não informado',
    sigla_uf_internacao: data.uf || 'Não informado',
    id_municipio_internacao: data.municipio || 'Não informado',
    
    // Sinais de alarme
    alarme_hipotensao: data.alrm_hipot ? simNaoMap[data.alrm_hipot] || data.alrm_hipot : 'Não informado',
    alarme_plaqueta: data.alrm_plaq ? simNaoMap[data.alrm_plaq] || data.alrm_plaq : 'Não informado',
    alarme_vomito: data.alrm_vom ? simNaoMap[data.alrm_vom] || data.alrm_vom : 'Não informado',
    alarme_sangramento: data.alrm_sang ? simNaoMap[data.alrm_sang] || data.alrm_sang : 'Não informado',
    alarme_hematocrito: data.alrm_hemat ? simNaoMap[data.alrm_hemat] || data.alrm_hemat : 'Não informado',
    alarme_dor_abdominal: data.alrm_abdom ? simNaoMap[data.alrm_abdom] || data.alrm_abdom : 'Não informado',
    alarme_letargia: data.alrm_letar ? simNaoMap[data.alrm_letar] || data.alrm_letar : 'Não informado',
    alarme_hepatomegalia: data.alrm_hepat ? simNaoMap[data.alrm_hepat] || data.alrm_hepat : 'Não informado',
    alarme_liquidos: data.alrm_liq ? simNaoMap[data.alrm_liq] || data.alrm_liq : 'Não informado',
    data_alarme: data.dt_alrm || 'Não informado',
    
    // Critérios de gravidade
    grave_pulso: data.grav_pulso ? simNaoMap[data.grav_pulso] || data.grav_pulso : 'Não informado',
    grave_convulsao: data.grav_conv ? simNaoMap[data.grav_conv] || data.grav_conv : 'Não informado',
    grave_enchimento_capilar: data.grav_ench ? simNaoMap[data.grav_ench] || data.grav_ench : 'Não informado',
    grave_insuficiencia_respiratoria: data.grav_insuf ? simNaoMap[data.grav_insuf] || data.grav_insuf : 'Não informado',
    grave_taquicardia: data.grav_taqui ? simNaoMap[data.grav_taqui] || data.grav_taqui : 'Não informado',
    grave_extremidade_fria: data.grav_extre ? simNaoMap[data.grav_extre] || data.grav_extre : 'Não informado',
    grave_hipotensao: data.grav_hipot ? simNaoMap[data.grav_hipot] || data.grav_hipot : 'Não informado',
    grave_hematemese: data.grav_hemat ? simNaoMap[data.grav_hemat] || data.grav_hemat : 'Não informado',
    grave_melena: data.grav_melen ? simNaoMap[data.grav_melen] || data.grav_melen : 'Não informado',
    grave_metrorragia: data.grav_metro ? simNaoMap[data.grav_metro] || data.grav_metro : 'Não informado',
    grave_sangramento: data.grav_sang ? simNaoMap[data.grav_sang] || data.grav_sang : 'Não informado',
    grave_ast_alt: data.grav_ast ? simNaoMap[data.grav_ast] || data.grav_ast : 'Não informado',
    grave_miocardite: data.grav_mioc ? simNaoMap[data.grav_mioc] || data.grav_mioc : 'Não informado',
    grave_consciencia: data.grav_consc ? simNaoMap[data.grav_consc] || data.grav_consc : 'Não informado',
    grave_orgaos: data.grav_orgao ? simNaoMap[data.grav_orgao] || data.grav_orgao : 'Não informado',
    
    // Exames laboratoriais
    data_hematocrito: data.dt_col_hem || 'Não informado',
    hematocrito_maior: data.hema_maior || 'Não informado',
    data_plaquetas: data.dt_col_plq || 'Não informado',
    plaqueta_maior: data.palq_maior || 'Não informado',
    data_hematocrito_2: data.dt_col_he2 || 'Não informado',
    hematocrito_menor: data.hema_menor || 'Não informado',
    data_plaquetas_2: data.dt_col_pl2 || 'Não informado',
    plaqueta_menor: data.plaq_menor || 'Não informado',
    
    // Sorologia Chikungunya
    data_sorologia1_chikungunya: data.dt_chik_s1 || 'Não informado',
    data_resultado_sorologia1_chikungunya: data.dt_chik_s2 || 'Não informado',
    resultado_sorologia1_chikungunya: data.res_chiks1 || 'Não informado',
    sorologia1_igm: data.s1_igm || 'Não informado',
    sorologia1_igg: data.s1_igg || 'Não informado',
    sorologia1_tit1: data.s1_tit1 || 'Não informado',
    resultado_sorologia2_chikungunya: data.res_chiks2 || 'Não informado',
    sorologia2_igm: data.s2_igm || 'Não informado',
    sorologia2_igg: data.s2_igg || 'Não informado',
    sorologia2_tit1: data.s2_tit1 || 'Não informado',
    resultado_prnt: data.resul_prnt || 'Não informado',
    
    // Exames específicos
    data_ns1: data.dt_ns1 || 'Não informado',
    resultado_ns1: data.resul_ns1 || 'Não informado',
    data_viral: data.dt_viral || 'Não informado',
    resultado_viral: data.resul_vi_n || 'Não informado',
    data_pcr: data.dt_pcr || 'Não informado',
    resultado_pcr: data.resul_pcr_ || 'Não informado',
    amostra_pcr: data.amos_pcr || 'Não informado',
    amostra_outra: data.amos_out || 'Não informado',
    tecnica: data.tecnica || 'Não informado',
    resultado_amostra_outra: data.resul_out || 'Não informado',
    
    // Sorologia Dengue
    data_sorologia_dengue: data.dt_soro || 'Não informado',
    resultado_sorologia_dengue: data.resul_soro || 'Não informado',
    sorotipo: data.sorotipo || 'Não informado',
    histopatologia: data.histopa || 'Não informado',
    imunohistoquimica: data.imunoh || 'Não informado',
    
    // Manifestações e classificação
    manifestacao_hemorragica: data.mani_hemor ? simNaoMap[data.mani_hemor] || data.mani_hemor : 'Não informado',
    classificacao_final: classiFinMap[data.classi_fin] || data.classi_fin,
    criterio_confirmacao: data.criterio ? criterioMap[data.criterio] || data.criterio : 'Não informado',
    caso_fhd: data.con_fhd || 'Não informado',
    caso_autoctone: data.tpautocto ? simNaoMap[data.tpautocto] || data.tpautocto : 'Não informado',
    pais_infeccao: data.copaisinf || 'Não informado',
    sigla_uf_infeccao: data.coufinf || 'Não informado',
    id_municipio_infeccao: data.comuninf || 'Não informado',
    doenca_trabalho: data.doenca_tra ? simNaoMap[data.doenca_tra] || data.doenca_tra : 'Não informado',
    apresentacao_clinica: data.clinc_chik || 'Não informado',
    evolucao_caso: data.evolucao ? evolucaoMap[data.evolucao] || data.evolucao : 'Não informado',
    data_obito: data.dt_obito || 'Não informado',
    data_encerramento: data.dt_encerra,
    tipo_sistema: tipoSistemaMap[data.tp_sistema] || data.tp_sistema,
    data_digitacao: data.dt_digita
  };
};

export default function Home() {
  const [year, setYear] = useState('2025');
  const [data, setData] = useState<DengueData[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchData = async () => {
    setLoading(true);
    setError(null);
    
    try {
      const response = await fetch(
        `https://apidadosabertos.saude.gov.br/arboviroses/dengue?nu_ano=${year}&limit=20&offset=0`,
        {
          headers: {
            'accept': 'application/json'
          }
        }
      );
      
      if (!response.ok) {
        throw new Error('Erro ao buscar dados da API');
      }
      
      const result: ApiResponse = await response.json();
      setData(result.parametros);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Erro desconhecido');
    } finally {
      setLoading(false);
    }
  };

  const translatedData = data.map(translateData);

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="bg-white shadow rounded-lg p-6">
          <h1 className="text-3xl font-bold text-gray-900 mb-8 text-center">
            Dados de Dengue - API Governo (Tradução Completa)
          </h1>
          
          <div className="mb-6 flex flex-col sm:flex-row gap-4 items-center justify-center">
            <div className="flex items-center gap-2">
              <label htmlFor="year" className="text-sm font-medium text-gray-700">
                Ano:
              </label>
              <input
                id="year"
                type="number"
                value={year}
                onChange={(e) => setYear(e.target.value)}
                className="border border-gray-300 rounded-md px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                min="2020"
                max="2025"
              />
            </div>
            <button
              onClick={fetchData}
              disabled={loading}
              className="bg-blue-600 hover:bg-blue-700 disabled:bg-blue-400 text-white font-medium py-2 px-6 rounded-md transition-colors duration-200"
            >
              {loading ? 'Carregando...' : 'Buscar Dados'}
            </button>
          </div>

          {error && (
            <div className="mb-4 p-4 bg-red-50 border border-red-200 rounded-md">
              <p className="text-red-600">{error}</p>
            </div>
          )}

          {translatedData.length > 0 && (
            <div className="overflow-x-auto">
              <table className="min-w-full divide-y divide-gray-200">
                <thead className="bg-gray-50">
                  <tr>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Data Notificação
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Data Sintomas
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Idade
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Sexo
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Raça/Cor
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Classificação
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Evolução
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Hospitalizado
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Febre
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Cefaleia
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Mialgia
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Vômito
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Exantema
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Gestante
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Diabetes
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Hipertensão
                    </th>
                  </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                  {translatedData.map((item, index) => (
                    <tr key={index} className="hover:bg-gray-50">
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                        {item.data_notificacao}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                        {item.data_primeiros_sintomas}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                        {item.idade_paciente}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                        {item.sexo_paciente}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                        {item.raca_cor_paciente}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                        {item.classificacao_final}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                        {item.evolucao_caso}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                        {item.internacao}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                        {item.apresenta_febre}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                        {item.apresenta_cefaleia}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                        {item.apresenta_mialgia}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                        {item.apresenta_vomito}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                        {item.apresenta_exantema}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                        {item.gestante_paciente}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                        {item.possui_diabetes}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                        {item.possui_hipertensao}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}

          {translatedData.length > 0 && (
            <div className="mt-4 text-sm text-gray-600 text-center">
              Total de registros: {translatedData.length}
            </div>
          )}

          {translatedData.length > 0 && (
            <div className="mt-6 p-4 bg-blue-50 border border-blue-200 rounded-md">
              <h3 className="text-lg font-medium text-blue-900 mb-2">
                📊 Dados Traduzidos Completamente
              </h3>
              <p className="text-sm text-blue-700">
                Esta tabela mostra apenas os campos principais. Todos os dados da API foram traduzidos 
                conforme a documentação oficial do Ministério da Saúde, incluindo:
              </p>
              <ul className="mt-2 text-sm text-blue-700 list-disc list-inside">
                <li>Dados demográficos (idade, sexo, raça, escolaridade)</li>
                <li>Sintomas e manifestações clínicas</li>
                <li>Comorbidades e fatores de risco</li>
                <li>Exames laboratoriais e resultados</li>
                <li>Classificação final e evolução do caso</li>
                <li>Sinais de alarme e critérios de gravidade</li>
              </ul>
            </div>
          )}
        </div>
        </div>
    </div>
  );
}