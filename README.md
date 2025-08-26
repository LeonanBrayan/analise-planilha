Análise Planilha

📊 Um projeto Django que permite fazer upload de planilhas com dados de vendas (em formatos como .csv, .tsv e .xlsx) e analisa os dados usando Pandas, exibindo o total de vendas e a média de valor por produto diretamente no navegador.

🚀 Funcionalidades

Upload de arquivos .csv, .tsv ou .xlsx contendo colunas:

produto

valor

Leitura e processamento inteligente com Pandas

Cálculo de:

Total geral de vendas

Média de valor por produto

Exibição dos resultados em uma interface amigável com Bootstrap

✅ O sistema é extensível: pode facilmente ser adaptado para mais colunas, outros tipos de análise, autenticação ou gráficos.

🛠️ Tecnologias utilizadas

Python 3.x

Django

Pandas

Bootstrap 5

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
├── manage.py

📄 Exemplo de planilha aceita

A planilha (independente do formato) deve conter ao menos estas duas colunas:

produto,valor
Arroz,10.5
Feijão,8.0
Arroz,5.0
Macarrão,12.0
Feijão,16.0
Macarrão,4.0


Observação: Coluna quantidade pode existir, mas atualmente não é usada no cálculo.

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


Acesse no navegador:

http://localhost:8000

💡 Possíveis melhorias

📊 Adicionar gráficos interativos com Plotly ou Chart.js

📁 Permitir exportar relatórios em PDF ou Excel

🔐 Adicionar autenticação de usuários

🗂️ Salvar o histórico de análises no banco de dados

⚙️ Permitir que o usuário selecione quais colunas usar
