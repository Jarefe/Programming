<?php

// PHP only supports single inheritance: a child class can only inherit from 1 parent

// traits used to declare methods that can be used in multiple classes

trait message1{
    public function msg1(){
        echo "This is message 1\n";
}
}

trait somethingElse{
    public function somethingElse(){
        echo "This is a different function that was inherited\n";
    }
}

class Welcome {
    use message1;
    use somethingElse;
}

$obj = new Welcome();
$obj->msg1();
$obj->somethingElse();