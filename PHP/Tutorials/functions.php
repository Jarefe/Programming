<?php
function sum($numbers){
    $sum = 0;

    foreach ($numbers as $number) {
        $sum += $number;
    }
    return $sum;
}

echo sum(array(1,2,3,4,5,6,7,8,9,10));

// can be imported into another file with 
// include("sum.php")