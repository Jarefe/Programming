<?php
// . is concatenator
$name = "John";
echo "Hello $name" . " . is the concatenator\n";

echo strlen($name) ."\n";

$filename = "image.png";

$extension = substr($filename, strlen($filename) - 3);
echo "The extension is $extension\n";

// join arrays to form strings or split strings to form arrays
$fruits = "apple,banana,orange";
$fruit_list = explode(",", $fruits);
echo "The second fruit in the list is $fruit_list[1]\n";

$joined = implode(",", $fruit_list);
echo "The fruits are $joined\n";