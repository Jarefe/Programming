<?php
// static methods can be called directly without creating a class instance

class ClassName {
    public static function staticMethod() {
        echo "This function can be called without creating a class instance";
    }
}

className::staticMethod();


// static methods can be accessed by a method from same class with self
// can also be called from methods in other classes; must be public

class greeting {
    public static function welcome() {
      echo "Hello World!";
    }
  
    public function __construct() {
      self::welcome();
    }
  }
  
  new greeting();


  class A {
    public static function welcome() {
      echo "Hello World!";
    }
  }
  
  class B {
    public function message() {
      A::welcome();
    }
  }
  
  $obj = new B();
  echo $obj -> message();


  // for child class to access static method from parent, use parent keyword
  // static method can be public or protected

  class domain {
    protected static function getWebsiteName() {
      return "W3Schools.com";
    }
  }
  
  class domainW3 extends domain {
    public $websiteName;
    public function __construct() {
      $this->websiteName = parent::getWebsiteName();
    }
  }
  
  $domainW3 = new domainW3;
  echo $domainW3 -> websiteName;