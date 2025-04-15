<?php
// for global variables, either define as global or refer to with syntax

$x = 75;

function test(){
    echo $GLOBALS['x'];
}

test();
echo $x;