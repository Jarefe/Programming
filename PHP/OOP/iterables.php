<?php

// iterable keyword can be used as a data type of a function argument
// or as the return type of a function

function printIterable1(iterable $myIterable) { // function argument
    foreach($myIterable as $item) {
      echo $item;
    }
  }
  
  $arr = ["a", "b", "c"];
  printIterable1($arr);

function getIterable():iterable {
    return ["a", "b", "c"]; 
}

$myIterable = getIterable();
foreach($myIterable as $item) {
echo $item;
}

// any object that implements Iterator interface can be used as an argument 
// for a function that requires an iterable

// iterator must have following methods:
// current(), key(), next(), rewind(), valid()

// Create an Iterator
class MyIterator implements Iterator
{
    private array $items = [];
    private int $pointer = 0;

    public function __construct(array $items){
        // array_values() ensures numeric keys for predictable iteration
        $this->items = array_values($items);
    }

    public function current(): mixed{
        return $this->items[$this->pointer];
    }

    public function key(): int{
        return $this->pointer;
    }

    public function next(): void{
        $this->pointer++;
    }

    public function rewind(): void{
        $this->pointer = 0;
    }

    public function valid(): bool{
        return isset($this->items[$this->pointer]);
    }
}

  
  // A function that uses iterables
  function printIterable(iterable $myIterable) {
    foreach($myIterable as $item) {
      echo $item;
    }
  }
  
  // Use the iterator as an iterable
  $iterator = new MyIterator(["a", "b", "c"]);
  printIterable($iterator);