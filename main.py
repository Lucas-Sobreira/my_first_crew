import os 
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
import pdfkit
import markdown

def criar_agentes(setor): 
    pesquisador = Agent(
        role="Pesquisador de Mercado",
        goal=f"Coletar e organizar informações relevantes sobre {setor}",
        backstory=f"""
            Você é um pesquisador experiente que analisa tendências de mercado e coleta dados 
            relevantes sobre {setor}. Seu trabalho é garantir que todas as informações 
            estejam atualizadas e bem documentadas.
        """,
        allow_delegation=False,
        verbose=True
    )

    analista = Agent(
        role="Analista de Tendências", 
        goal=f"Analisar os dados do setor {setor} e identificar padrões, oportunidades e ameaças",
        backstory=f"""
            Você é um analista de mercado que examina os dados coletados para identificar tendências
            emergentes, oportunidades e ameaças no setor {setor}.
        """,
        allow_delegation=False,
        verbose=True
    )

    redator = Agent(
        role="Redator de Relatórios", 
        goal=f"Elaborar um relatório consolidado sobre a análise de mercado do setor {setor}",
        backstory=f"""
            Você é um redator profissional que transforma análises de mercado em um relatório estruturado
            e compreensível para tomadores de decisão.
        """,
        allow_delegation=False,
        verbose=True
    )

    return pesquisador, analista, redator

def criar_tarefas(setor, pesquisador, analista, redator): 
    coleta_dados = Task(
        description=(
            f"1. Pesquisar e coletar informações atualizadas sobre {setor}.\n"
            f"2. Identificar os principais players, tendências e estatísticas do setor.\n"
            f"3. Organizar os dados de forma clara para análise."
        ),
        expected_output=f"Documento estruturado contendo dados de mercado sobre {setor}.",
        agent=pesquisador
    )

    analise_tendencias = Task(
        description=(
            f"1. Examinar os dados coletados pelo Pesquisador de Mercado.\n"
            f"2. Identificar padrões, tendências emergentes e oportunidades no setor {setor}.\n"
            f"3. Elaborar uma análise detalhada destacando os principais pontos."
        ),
        expected_output=f"Relatório com insights e tendências baseados nos dados do setor {setor}.",
        agent=analista
    )

    redacao_relatorio = Task(
        description=(
            f"1. Usar a análise de tendências para criar um relatório detalhado sobre {setor}.\n"
            f"2. Garantir que o relatório seja bem estruturado e compreensível.\n"
            f"3. Apresentar um resumo executivo e recomendações finais."
        ),
        expected_output="Relatório de análise de mercado em formato Markdown, pronto para leitura e apresentação.",
        agent=redator
    )

    return coleta_dados, analise_tendencias, redacao_relatorio

def criar_crew(agentes, tarefas): 
    return Crew(
        agents=agentes,
        tasks=tarefas,
        process=Process.sequential,
        verbose=False
    )

def salvar_pdf(texto, path):
    # Remove markdown extra se vier com blocos ```markdown
    if texto.startswith("```markdown"):
        texto = texto.replace("```markdown", "").replace("```", "").strip()

    html = f"""
    <html>
    <head><meta charset="utf-8"></head>
    <body>
    {markdown.markdown(texto)}
    </body>
    </html>
    """

    options = {'encoding': 'UTF-8'}
    config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")  # Ajuste o caminho
    pdfkit.from_string(html, path, configuration=config, options=options)
    print(f"Relatório salvo em: {path}")

def main():
    load_dotenv()
    openai_key = os.getenv("OPENAI_API_KEY")

    setor = input("Qual é o setor desejado para realizar a pesquisa?\nSetor: ").strip()
    nome_arquivo = str(input("Com qual nome deseja salvar o arquivo? \nArquivo: "))

    pesquisador, analista, redator = criar_agentes(setor)
    tarefas = criar_tarefas(setor, pesquisador, analista, redator)
    crew = criar_crew([pesquisador, analista, redator], tarefas)

    resultado = crew.kickoff(inputs={"sector": setor})

    texto = resultado.result if hasattr(resultado, "result") else str(resultado)
    path = "./relatorios/" + nome_arquivo + ".pdf"
    salvar_pdf(texto, path)

if __name__ == "__main__":
    main()