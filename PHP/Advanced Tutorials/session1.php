<?php
// start session
session_start();
?>

<!DOCTYPE html>
<html>
    <body>
        <?php
        // set session variables
        $_SESSION['favcolor'] = 'red';
        echo 'session variables are set';
        ?>
    </body>
</html>