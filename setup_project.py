import os

folders = [
    "config",
    "data/raw",
    "data/processed",
    "src/collectors",
    "src/nlp",
    "src/database",
    "src/api/routes",
    "dashboard/assets"
]

files = {
    "config/__init__.py": "",
    "config/settings.py": "# Configurações de ambiente e credenciais\n",
    "config/keywords.py": "# Dicionário de serviços, profissões e expressões de intenção\n",
    "src/__init__.py": "",
    "src/collectors/__init__.py": "",
    "src/collectors/base_collector.py": "# Classe abstrata para os coletores\n",
    "src/collectors/reddit_collector.py": "# Coletor de dados via API do Reddit (PRAW)\n",
    "src/collectors/twitter_collector.py": "# Coletor/Scraper de dados do Twitter (X)\n",
    "src/nlp/__init__.py": "",
    "src/nlp/normalizer.py": "# Funções de limpeza e tratamento de texto\n",
    "src/nlp/categorizer.py": "# Classificação de categorias, urgência e intenções\n",
    "src/database/__init__.py": "",
    "src/database/connection.py": "# Conexão com o banco de dados PostgreSQL\n",
    "src/database/models.py": "# Modelos das tabelas (SQLAlchemy / SQL)\n",
    "src/database/repository.py": "# Métodos de inserção e busca no banco\n",
    "src/api/__init__.py": "",
    "src/api/main.py": "# Ponto de entrada da API REST (FastAPI / Flask)\n",
    "src/api/routes/__init__.py": "",
    "src/api/routes/posts.py": "# Endpoints para listagem de posts\n",
    "src/api/routes/metrics.py": "# Endpoints para relatórios e dados do dashboard\n",
    "requirements.txt": "# Bibliotecas do projeto\n",
    "README.md": "# PI-Contrata - Análise de Dados de Contratação Informal e Indicações\n",
    ".gitignore": "# Ignorar arquivos de ambiente virtual, cache e dados sensíveis\n.env\n__pycache__/\n*.pyc\nvenv/\n.vscode/\ndata/raw/*\n!data/raw/.gitkeep\n"
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    gitkeep_path = os.path.join(folder, ".gitkeep")
    if not os.path.exists(gitkeep_path) and "data" in folder:
        with open(gitkeep_path, "w") as f:
            pass

for filepath, content in files.items():
    if not os.path.exists(filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

print("Estrutura do projeto PI-Contrata gerada com sucesso!")