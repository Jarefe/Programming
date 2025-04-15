<?php
$servername = "localhost";
$username = "username";
$password = "password";

echo extension_loaded('mysqli') ? "mysqli is loaded ✅" : "mysqli is NOT loaded ❌";

// create connection
$conn = new mysqli($servername, $username, $password);

// check connection
if ($conn->connect_error) {
    die("Connection failed: ". $conn->connect_error);
}
echo "Connected successfully";

