<?php
// Connect to MySQL database
$servername = "localhost";
$username = "root"; // Replace with your MySQL username
$password = ""; // Replace with your MySQL password
$dbname = "fertilizer"; // Replace with your MySQL database name

$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Fetch data from MySQL database
$sql = "SELECT * FROM sensorsData";
$result = $conn->query($sql);

$data = array();

if ($result->num_rows > 0) {
  while ($row = $result->fetch_assoc()) {
    // Append each row to the data array
    $data[] = $row;
  }
}

// Return data as JSON
echo json_encode($data);

// Close connection
$conn->close();
?>
