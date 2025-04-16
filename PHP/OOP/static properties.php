<?php

// like static methods, static properties can be called directly
// class can have both static and non static properties
// can be accessed by method in same class by using self
class pi1 {
    public static $value=3.14159;
    public function staticValue() {
      return self::$value;
    }
  }
  
  $pi = new pi1();
  echo $pi->staticValue();


// to call static property thats in parent class, use parent keyword in child class

class pi {
    public static $value=3.14159;
  }
  
  class x extends pi {
    public function xStatic() {
      return parent::$value;
    }
  }
  
  // Get value of static property directly via child class
  echo x::$value;
  
  // or get value of static property via xStatic() method
  $x = new x();
  echo $x->xStatic();
