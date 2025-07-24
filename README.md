# 📊 Análise de Mercado com CrewAI

Este projeto utiliza a biblioteca [CrewAI](https://docs.crewai.com/) para simular uma equipe de agentes inteligentes que realizam uma análise de mercado automatizada sobre um setor escolhido. Ao final do processo, é gerado um relatório em formato PDF com os insights da pesquisa.

---

## 🔍 Objetivo

Automatizar a coleta, análise e redação de relatórios sobre setores de mercado utilizando agentes de IA especializados, com possibilidade de exportação para PDF.

---

## 🧠 Estrutura dos Agentes

- **Pesquisador de Mercado**: coleta informações atualizadas sobre o setor.
- **Analista de Tendências**: interpreta os dados e identifica padrões e oportunidades.
- **Redator de Relatórios**: organiza os insights em um relatório bem estruturado.

---

## ⚙️ Tecnologias Utilizadas

- [CrewAI](https://docs.crewai.com/)
- Python 3.10+
- `pdfkit` + `wkhtmltopdf` (para gerar PDF)
- `markdown` (para renderização do relatório)

---

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/crewai-analise-mercado.git
   cd crewai-analise-mercado

2. Instale as dependências, com PIP ou outro gerenciador de pacotes Python da sua escolha:
    ```bash
    pip install -r requirements.txt

3. Caso deseje transformar o relatório para PDF. Instale o wkhtmltopdf e adicione ao PATH. <url>https://wkhtmltopdf.org/downloads.html</url>

4. Criar um arquivo ".env" para colocar API_KEY da OpenAI, exemplo: 
   - OPENAI_API_KEY = 'sua_chave_API'

5. Execute o script:
    ```bash
    python main.py

6. Informe o setor desejado e o nome do relatório no terminal. Aguarde a geração do relatório:
    ```bash
    Setor: energia renovável
    Arquivo: relatorio_setor

7. O arquivo PDF será salvo em:
    - relatorios/relatorio_setor.pdf