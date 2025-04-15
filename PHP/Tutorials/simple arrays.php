<?php
$odd_numbers = [1,3,5,7,9];
$first_odd_number = $odd_numbers[0];
$second_odd_number = $odd_numbers[1];

echo "The first odd number is $first_odd_number\n";
echo "The second odd number is $second_odd_number";

$odd_numbers[5] = 11;
print $odd_numbers; // outputs data type
print_r($odd_numbers); // outputs data type and value(s)

// delete from array
unset($odd_numbers[0]);
print_r($odd_numbers);


$num_items = count($odd_numbers);
echo "There are $num_items items in the array";
$first_item = reset($odd_numbers); // gets first member of array and reset internal iteration pointer
$second_item = $odd_numbers[1];
$last_item = end($odd_numbers);

// stack and queue functions
$numbers =  [1,2,3];
array_push($numbers, 4); // array is now 1 2 3 4

array_pop($numbers); // array is now 1 2 3

array_unshift($numbers,0); // array is now 0 1 2 3

array_shift($numbers); // array is now 1 2 3

// concatenate arrays
$odd_numbers = [1,3,5,7,9];
$even_numbers = [2,4,6,8,10];
$all_numbers = array_merge($odd_numbers, $even_numbers);
print_r($all_numbers);

// sort arrays
sort($all_numbers);
print_r($all_numbers);


// advanced array functions
$numbers = [1,2,3,4,5,6];
print_r(array_slice($numbers,3)); // skips first 3 of array
print_r(array_slice($numbers, 3, 2)); // takes chunk of 2 starting at index 3
print_r(array_splice($numbers, 3, 2)); // same as slice but edits original variable
print_r($numbers);

