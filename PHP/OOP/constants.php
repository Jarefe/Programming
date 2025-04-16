<?php
class Goodbye{
    const MESSAGE = "Goodbye";
    public function bye(){
        echo self::MESSAGE;
    }
}

// can access constant in 2 ways
echo Goodbye::MESSAGE;

$goodbye = new Goodbye();
$goodbye->bye();