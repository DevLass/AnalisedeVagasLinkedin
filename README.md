# Projeto de Análise de Vagas no LinkedIn

Este repositório contém um conjunto de scripts e arquivos para coleta e análise de dados de vagas de emprego no LinkedIn, identificando tópicos de interesse (por exemplo, SQL, Python e etc.) e gerando um dashboard a partir dos resultados.

---

## Estrutura de Arquivos

* **bot.js**
  Script em JavaScript que realiza a coleta dos dados diretamente no console do navegador. Deve ser executado na página de vagas do LinkedIn cujo título e descrição você deseja capturar. Ao rodar este script, ele extrai o conteúdo de cada vaga e salva em um arquivo `resultado.json`.

* **resultado.json**
  Arquivo gerado pelo `bot.js` contendo uma lista de objetos JSON, cada um representando uma vaga coletada, com os campos:

  * `titulo`: título da vaga
  * `texto`: descrição completa da vaga

* **dados.py**
  Script em Python responsável por:

  1. Ler o arquivo `resultado.json`.
  2. Analisar o campo `titulo` e `texto` de cada vaga.
  3. Detectar a presença de tópicos de interesse (palavras-chave definidas como SQL, Python, Power BI, etc.).
  4. Adicionar colunas indicando se cada tópico foi encontrado.
  5. Exportar um arquivo consolidado em formato Excel.

* **tabelacombinada.xlsx**
  Resultado final do processamento realizado pelo `dados.py`. Contém uma planilha com as seguintes colunas:

  * `SQL` (Sim/Não)
  * `Python` (Sim/Não)
  * `Power BI` (Sim/Não)
  * ... (outras palavras-chave de interesse)

---

## Pré-requisitos

* **Node.js** (v12 ou superior) para executar o `bot.js`.
* **Python 3.7+** com as bibliotecas:

  * `pandas`
  * `openpyxl`

---

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/analise-linkedin.git
   cd analise-linkedin
   ```

2. Instale as dependências em Python:

   ```bash
   pip install pandas openpyxl
   ```

---

## Uso

1. Abra o LinkedIn na página de vagas desejada.
2. No console do navegador, cole o código do arquivo `bot.js` e execute.
3. Guarde os Dados em um arquivo resultado.json
4. Execute o script Python para processar os dados:

   ```bash
   python dados.py
   ```
5. O arquivo `tabelacombinada.xlsx` será gerado na raiz do projeto.

---

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---


