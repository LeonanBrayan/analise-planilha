Django CSV Analyzer

:

📊 Um projeto Django que permite fazer upload de arquivos CSV com dados de vendas e analisa os dados usando Pandas, exibindo o total de vendas e a média de valor por produto diretamente no navegador.

🚀 Funcionalidades

Upload de arquivos .csv com colunas: produto, quantidade, valor

Leitura e processamento com Pandas

Cálculo de:

Total geral de vendas

Média de valor por produto

Exibição dos resultados em uma página HTML

(Opcional) Fácil de expandir com exportações, gráficos ou autenticação

🛠️ Tecnologias utilizadas

Python 3.x

Django

Pandas

📁 Estrutura básica do projeto
meuprojeto/
├── vendas/
│   ├── templates/
│   │   └── vendas/
│   │       ├── upload.html
│   │       └── resultado.html
│   ├── views.py
│   ├── urls.py
├── meuprojeto/
│   ├── settings.py
│   ├── urls.py

📄 Exemplo de CSV para upload
produto,quantidade,valor
Arroz,2,10.5
Feijão,1,8.0
Arroz,1,5.0
Macarrão,3,12.0
Feijão,2,16.0
Macarrão,1,4.0

▶️ Como rodar o projeto localmente

Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio


Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


Instale as dependências:

pip install -r requirements.txt


Execute as migrações e inicie o servidor:

python manage.py migrate
python manage.py runserver


Acesse em: http://localhost:8000


💡 Possíveis melhorias

Adicionar gráficos com Plotly ou Chart.js

Exportar relatórios em PDF ou Excel

Adicionar autenticação de usuários

Salvar histórico das análises no banco de dados