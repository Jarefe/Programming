<?php
// php arrays are actually ordered maps, with keys being the index starting at 0
$phone_numbers = [
    "Alex" => "415-235-8573",
    "Jessica" => "415-492-4856",
  ];

  print_r($phone_numbers);
  echo "Alex's phone number is " . $phone_numbers["Alex"] . "\n"; // . to concatenate string + variable
  echo "Jessica's phone number is " . $phone_numbers["Jessica"] . "\n";

  $phone_numbers["Michael"] = "415-955-3857"; // to add to array
  print_r($phone_numbers);

  if (array_key_exists("John", $phone_numbers)) {
    echo "John's phone number is " . $phone_numbers["John"] . "\n";
  } else {
    echo "John's phone number is not in the phone book";
  }

  // extract only keys (names) of array
  print_r(array_keys($phone_numbers));

  // extract only values (phone numbers)
  print_r(array_values($phone_numbers));