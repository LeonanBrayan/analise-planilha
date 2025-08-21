import pandas as pd
from django.shortcuts import render

def upload_csv(request):
    if request.method == "POST":
        arquivo = request.FILES['arquivo_csv']

        try:
            # Detecta a extensão e escolhe como abrir
            if arquivo.name.endswith('.csv'):
                df = pd.read_csv(arquivo)
            elif arquivo.name.endswith('.tsv'):
                df = pd.read_csv(arquivo, sep='\t')
            elif arquivo.name.endswith('.xlsx') or arquivo.name.endswith('.xls'):
                df = pd.read_excel(arquivo)
            else:
                return render(request, 'vendas/upload.html', {
                    'erro': 'Formato de arquivo não suportado. Envie CSV, TSV ou Excel.'
                })

            # Valida se as colunas necessárias existem
            if 'produto' not in df.columns or 'valor' not in df.columns:
                return render(request, 'vendas/upload.html', {
                    'erro': 'O arquivo deve conter as colunas "produto" e "valor".'
                })

            # Converte a coluna "valor" para número (caso venha como texto)
            df['valor'] = pd.to_numeric(df['valor'], errors='coerce')
            df = df.dropna(subset=['valor'])

            # Análise: soma total e média por produto
            total = df['valor'].sum()
            medias = df.groupby('produto')['valor'].mean().to_dict()

            context = {
                'total': total,
                'medias': medias
            }

            return render(request, 'vendas/resultado.html', context)

        except Exception as e:
            return render(request, 'vendas/upload.html', {
                'erro': f'Erro ao processar o arquivo: {str(e)}'
            })

    return render(request, 'vendas/upload.html')