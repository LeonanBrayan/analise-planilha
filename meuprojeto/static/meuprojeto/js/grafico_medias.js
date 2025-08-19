document.addEventListener("DOMContentLoaded", function () {
  const ctx = document.getElementById('graficoMedias').getContext('2d');
  
  const chart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: window.graficoLabels, // definido no template
      datasets: [{
        label: 'Média por Produto',
        data: window.graficoData,
        backgroundColor: 'rgba(13, 110, 253, 0.7)',
        borderColor: 'rgba(13, 110, 253, 1)',
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false },
        tooltip: { mode: 'index' }
      },
      scales: {
        y: {
          beginAtZero: true,
          ticks: { stepSize: 1 }
        }
      }
    }
  });
});