# Pipeline de Dados - Hospital ODS-3 🏥

> Projeto de análise de dados desenvolvido como atividade para a disciplina de Tópicos Especiais em SI

![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

## Contexto

Você foi contratado como Analista de Dados para o Hospital Municipal ODS-3. O
sistema de prontuário eletrônico sofreu uma falha na exportação e gerou um arquivo "sujo" com
registros de 1.000 atendimentos. Sua missão é limpar esses dados para gerar o Relatório Mensal de
Eficiência Hospitalar.

**Tarefa:** Desenvolver um script em Python (Pandas) que realize o saneamento dos dados e, ao final,
entregar um Mini Relatório de Processamento, seguindo os passos abaixo:

1. Exploração Inicial: Identificar o volume de dados e tipos de erros.
2. Deduplicação: Remover registros repetidos (mesmo ID e Nome).
3. Integridade de Dados Vital: Remover linhas onde a informação de pressao_arterial está
nula (dado obrigatório).
4. Imputação Estratégica: Preencher idades nulas com a mediana e oxigenação nula com 95%
(valor base de segurança).
5. Casting e Limpeza de String: Converter a coluna oxigenacao de texto (ex: "98%") para
número decimal.
6. Tratamento de Outliers: Filtrar temperaturas menores que 30°C ou maiores que 45°C.
