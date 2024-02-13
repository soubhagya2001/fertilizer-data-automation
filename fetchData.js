
fetch('fetchData.php')
  .then(response => response.json())
  .then(data => {
  
    const sensorDataList = document.getElementById('sensorDataList');
    const table = document.createElement('table');
    const headers = ['Timestamp', 'Temp', 'Press', 'Humi', 'Sensor ID', 'Process ID'];

 
    const headerRow = document.createElement('tr');
    headers.forEach(headerText => {
      const th = document.createElement('th');
      th.textContent = headerText;
      headerRow.appendChild(th);
    });
    table.appendChild(headerRow);

   
    data.forEach(sensorData => {
      const row = document.createElement('tr');
      headers.forEach(header => {
        const cell = document.createElement('td');
        if (header === 'Timestamp') {
          cell.textContent = sensorData['timeStamp'];
        } else if (header === 'Sensor ID') {
          cell.textContent = sensorData['sensorId']; 
        } else if (header === 'Process ID') {
          cell.textContent = sensorData['processId']; 
        } else {
          cell.textContent = sensorData[header.toLowerCase()]; 
        }
        row.appendChild(cell);
      });
      table.appendChild(row);
    });

    sensorDataList.appendChild(table);

    




    const chartButton = document.getElementById('chartButton');
    chartButton.addEventListener('click', () => {
      window.location.href = 'graphs.html';
    });
  })
  .catch(error => console.error('Error fetching data:', error));
