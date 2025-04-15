<?php
function my_callback($item){
    return strlen($item);
}

$strings = ["apple", "orange", "banana", "coconut"];
$lengths = array_map("my_callback", $strings);
print_r($lengths);

// anonymous functions can be passed as callbacks
$lengths = array_map(function($item){return strlen($item);}, $lengths);
print_r($lengths);


// callbacks from user defined functions
function exclaim($str){return $str . "!";}

function ask($str){return $str . "?";}

function printFormatted($str, $format){
    // call $format callback function
    echo $format($str);
}

// pass exclaim and ask as callback functions to printformatted
printFormatted("Hello world", "exclaim");
printFormatted("Hello World","ask");