import pandas as pd
from django.shortcuts import render

def upload_csv(request):
    if request.method == "POST":
        arquivo = request.FILES['arquivo_csv']
        df = pd.read_csv(arquivo)

        # Análise simples
        total = df['valor'].sum()
        medias = df.groupby('produto')['valor'].mean().to_dict()

        context = {
            'total': total,
            'medias': medias
        }
        return render(request, 'vendas/resultado.html', context)
    
    return render(request, 'vendas/upload.html')