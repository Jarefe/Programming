<?php
class Student{
    private $first_name;
    private $last_name;
    public function __construct($first_name, $last_name){
        $this->first_name = $first_name;
        $this->last_name = $last_name;
}

    public function get_name(){
        echo $this->first_name . " " . $this->last_name . "\n";
    }

    public function say_name(){
        echo "My name is " . $this->full_name();
    }

    private function full_name(){
        return $this->first_name ." ". $this->last_name . "\n";
    }
}

$john = new Student("John", "Doe");
$john->say_name();


// inheritance
class MathStudent extends Student{
    function sum_numbers($first_number, $second_number){
        $sum = $first_number + $second_number;
        echo $this->get_name() . " says that " . $first_number . " + " . $second_number . " is " . $sum;
    }
}

$eric = new MathStudent("Eric", "Chang");
$eric->say_name();
$eric->sum_numbers(3, 5);