<?php
function divide($dividend, $divisor){
    if($divisor == 0){
        throw new Exception("Division by 0"); // exception thrown but not caught
    }
    return $dividend / $divisor;
}

// echo divide(5,0);   
try {
    echo divide(5,0);
} catch (Exception $e) {
    echo $e->getMessage()."\n";  
} finally {
    echo "Complete";
}


// try {
//     code that can throw exceptions
//   } catch(Exception $e) {
//     code that runs when an exception is caught
//   } finally {
//     code that always runs regardless of whether an exception was caught
//   }