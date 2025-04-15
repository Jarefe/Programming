<?php
session_start();
?>
<!DOCTYPE html>
<html>
<body>

<?php
// Echo session variables that were set on previous page
echo "Favorite color is " . $_SESSION["favcolor"] . ".<br>";

// session variables can be changed just by overwriting
$_SESSION['favcolor'] = 'none';
echo "Session variable changed to none" . "<br>";
print_r($_SESSION["favcolor"]);
echo "<br>";
echo "Running session unset; removing global variables" . "<br>";
session_unset();
echo "destroying session" . "<br>";
session_destroy();
?>



</body>
</html>