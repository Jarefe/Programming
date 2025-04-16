<?php

// interfaces cant have properties while abstract classes can

// all interface methods must be public, while abstract class methods 
// are public or protected

// all methods in an interface are abstract; cannot be implemented in 
// code and abstract keyword is not necessary

// classes can implement an interface and inherit from another class 
//simultaneously

// to implement interface, class must use implements keyword

interface Animal {
    public function makeSound(); // each class that implements the function will do the same thing but in its own way
}

class Cat implements Animal {
    public function makeSound() {
        echo "Meow";
    }
}

class Dog implements Animal {
    public function makeSound() {
        echo "Bark";
    }
}

class Mouse implements Animal {
    public function makeSound() {
        echo "Squeak";
    }
}

$cat = new Cat();
$dog = new Dog();
$mouse = new Mouse();
$animals = array($cat, $dog, $mouse);

foreach ($animals as $animal) {
    $animal->makeSound();
}

