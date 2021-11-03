const ctx = document.getElementById('myChart').getContext('2d');
const config = {
    type: 'pie',
    data: data,
  };

  const data = {
    labels: [
      'Sudah Vaksin 2x',
      'Sudah Vaksin 1x',
      'belum Vaksin'
    ],
    datasets: [{
      label: 'My First Dataset',
      data: [300, 50, 100],
      backgroundColor: [
        'rgb(255, 99, 132)',
        'rgb(54, 162, 235)',
        'rgb(255, 205, 86)'
      ],
      hoverOffset: 4
    }]
  };