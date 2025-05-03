import json
import re
import pandas as pd

def analisar_titulo(titulo):
    """Analisa o título e retorna um dicionário com as colunas booleanas."""
    analista = re.search(r'analista de dados|data analyst', titulo, re.IGNORECASE) is not None
    arquiteto = re.search(r'arquiteto de dados|data architect', titulo, re.IGNORECASE) is not None
    engenheiro = re.search(r'engenheiro de dados|engenheira de dados|data engineer', titulo, re.IGNORECASE) is not None
    junior = re.search(r'junior|júnior|jr\.|jovior', titulo, re.IGNORECASE) is not None
    pleno = re.search(r'pleno', titulo, re.IGNORECASE) is not None
    senior = re.search(r'senior|sênior|sr\.', titulo, re.IGNORECASE) is not None
    estagiario = re.search(r'estagiario|estágio|intern', titulo, re.IGNORECASE) is not None
    cientista = re.search(r'cientista de dados|data scientist', titulo, re.IGNORECASE) is not None
    return {
        "Analista de Dados": analista,
        "Arquiteto de Dados": arquiteto,
        "Engenheiro de Dados": engenheiro,
        "Júnior": junior,
        "Pleno": pleno,
        "Senior": senior,
        "Estagiário": estagiario,
        "Cientista de Dados": cientista
    }

def analisar_texto(texto):
    """Analisa o texto e retorna um dicionário com as colunas de tecnologias booleanas."""
    sql = re.search(r'\bSQL\b', texto, re.IGNORECASE) is not None
    power_bi = re.search(r'\bPower BI\b', texto, re.IGNORECASE) is not None
    python = re.search(r'\bPython\b', texto, re.IGNORECASE) is not None
    etl = re.search(r'\bETL\b', texto, re.IGNORECASE) is not None
    r_lang = re.search(r'\bR\b(?!\w)', texto, re.IGNORECASE) is not None
    estatistica = re.search(r'\bestatística\b', texto, re.IGNORECASE) is not None
    excel = re.search(r'\bExcel\b', texto, re.IGNORECASE) is not None
    qlik = re.search(r'\bQlik\b', texto, re.IGNORECASE) is not None
    tableau = re.search(r'\bTableau\b', texto, re.IGNORECASE) is not None
    looker = re.search(r'\bLooker\b', texto, re.IGNORECASE) is not None
    kpis = re.search(r'\bKPIs?\b', texto, re.IGNORECASE) is not None
    spark = re.search(r'\bSpark\b', texto, re.IGNORECASE) is not None
    azure = re.search(r'\bAzure\b', texto, re.IGNORECASE) is not None
    aws = re.search(r'\bAWS\b', texto, re.IGNORECASE) is not None
    cloud = re.search(r'\bCloud\b', texto, re.IGNORECASE) is not None
    bigdata = re.search(r'\bBig Data\b', texto, re.IGNORECASE) is not None
    powerapps = re.search(r'\bPowerApps\b', texto, re.IGNORECASE) is not None
    llms = re.search(r'\bLLMs?\b', texto, re.IGNORECASE) is not None
    databricks = re.search(r'\bDatabricks\b', texto, re.IGNORECASE) is not None
    nosql = re.search(r'\bNoSQL\b', texto, re.IGNORECASE) is not None
    data_lakes = re.search(r'\bData Lakes?\b', texto, re.IGNORECASE) is not None
    data_warehouse = re.search(r'\bData Warehouse\b', texto, re.IGNORECASE) is not None
    return {
        "SQL": sql,
        "Power BI": power_bi,
        "Python": python,
        "ETL": etl,
        "R": r_lang,
        "Estatística": estatistica,
        "Excel": excel,
        "Qlik": qlik,
        "Tableau": tableau,
        "Looker": looker,
        "KPIs": kpis,
        "Spark": spark,
        "Azure": azure,
        "AWS": aws,
        "Cloud": cloud,
        "BigData": bigdata,
        "PowerApps": powerapps,
        "LLMs": llms,
        "Databricks": databricks,
        "NoSQL": nosql,
        "Data Lakes": data_lakes,
        "Data warehouse": data_warehouse
    }

def processar_arquivo_json(nome_arquivo="resultado.json", nome_excel="tabela_combinada.xlsx"):
    """Lê o arquivo JSON, analisa títulos e textos, e salva os resultados em um arquivo XLSX."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados_json = json.load(arquivo)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo JSON em '{nome_arquivo}'. Verifique a formatação.")
        return

    tabela_resultados = []
    for item in dados_json:
        titulo_analise = {}
        texto_analise = {}
        if "Titulo" in item:
            titulo_analise = analisar_titulo(item["Titulo"])
        else:
            print("Aviso: Item encontrado sem o campo 'Titulo'.")

        if "Texto" in item:
            texto_analise = analisar_texto(item["Texto"])
        else:
            print("Aviso: Item encontrado sem o campo 'Texto'.")

        # Combina os resultados das análises em um único dicionário
        resultado_combinado = {**titulo_analise, **texto_analise}
        tabela_resultados.append(resultado_combinado)

    if tabela_resultados:
        df = pd.DataFrame(tabela_resultados)
        try:
            df.to_excel(nome_excel, index=False)
            print(f"Tabela combinada salva com sucesso em '{nome_excel}'")
        except Exception as e:
            print(f"Erro ao salvar o arquivo Excel: {e}")
    else:
        print("Nenhum dado processado para criar a tabela.")

if __name__ == "__main__":
    processar_arquivo_json()