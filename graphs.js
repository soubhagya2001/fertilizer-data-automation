
fetch('fetchData.php')
  .then(response => response.json())
  .then(data => {
    console.log(data); 
    
    const timestamps = data.map(sensorData => sensorData.timeStamp);
    const temps = data.map(sensorData => sensorData.temp);
    const pressures = data.map(sensorData => sensorData.press);
    const humidities = data.map(sensorData => sensorData.humi);

    //  temperature chart
    const tempChartCanvas = document.getElementById('tempChart').getContext('2d');
    const tempChart = new Chart(tempChartCanvas, {
        type: 'line',
        data: {
            labels: timestamps,
            datasets: [{
                label: 'Temperature',
                data: temps,
                borderColor: 'red',
                borderWidth: 1,
                fill: false
            }]
        }
    });

    //  pressure chart
    const pressureChartCanvas = document.getElementById('pressureChart').getContext('2d');
    const pressureChart = new Chart(pressureChartCanvas, {
        type: 'line',
        data: {
            labels: timestamps,
            datasets: [{
                label: 'Pressure',
                data: pressures,
                borderColor: 'blue',
                borderWidth: 1,
                fill: false
            }]
        }
    });

    //  humidity chart
    const humidityChartCanvas = document.getElementById('humidityChart').getContext('2d');
    const humidityChart = new Chart(humidityChartCanvas, {
        type: 'line',
        data: {
            labels: timestamps,
            datasets: [{
                label: 'Humidity',
                data: humidities,
                borderColor: 'green',
                borderWidth: 1,
                fill: false
            }]
        }
    });
  })
  .catch(error => console.error('Error fetching data:', error));
