<?php
$counter = 0;

while ($counter < 10) {
    $counter++;

    if ($counter % 2 == 0) {
        echo "Skipping even number \n";
        continue;
    }

    echo "Executing - counter is $counter\n";
}


$counter = 0;

while ($counter < 10) {
    $counter += 1;

    if ($counter > 8) {
        echo "counter is larger than 8, stopping the loop.\n";
        break;
    }

    if ($counter % 2 == 0) {
        echo "Skipping number $counter because it is even.\n";
        continue;
    }

    echo "Executing - counter is $counter.\n";
}