<?php
$multiArray = [ 
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
];

print_r($multiArray[0]); // 1 2 3
print_r($multiArray[0][0]); // 1

$people = [
    "john_doe" => [
        "name" => "John",
        "surname" => "Doe",
        "age" => 25,
    ],
    "jane_doe" => [
        "name" => "Jane",
        "surname" => "Doe",
        "age" => 25,
    ]
];

print_r($people);