let ctx = document.getElementById('myChart').getContext('2d');
let labels = ['2 kali vaksin', '1 kali vaksin', 'belum vaksin'];
let colorHex = ['#5255a3', '#8688CE', '#c1c2eb'];

var vaksin2 = 76191677
var vaksin1 = 122464119-vaksin2;
var vaksin1 = 208265720 - (vaksin1+vaksin2)

let myChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    datasets: [{
      
      data: [vaksin2, vaksin1, vaksin1],
      backgroundColor: colorHex
    }],
    labels: labels
  },
  options: {
    responsive: true,
    legend: {
      position: 'bottom'
    },
    plugins: {
      datalabels: {
        color: '#fff',
        anchor: 'end',
        align: 'start',
        offset: -10,
        borderWidth: 2,
        borderColor: '#fff',
        borderRadius: 25,
        backgroundColor: (context) => {
          return context.dataset.backgroundColor;
        },
        font: {
          weight: 'bold',
          size: '10'
        },
        formatter: (value) => {
          return value + ' %';
        }
      }
    }
  }
})