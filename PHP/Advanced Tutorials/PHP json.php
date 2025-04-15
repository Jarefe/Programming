<?php
$age = array("Peter"=>35, "Ben"=>37, "Joe"=>43);

echo json_encode($age) . "\n";

$cars = array("Volvo", "BMW", "Toyota");
echo json_encode($cars) . "\n";

$jsonobj = '{"Peter":35,"Ben":37,"Joe":43}';
var_dump(json_decode($jsonobj, true));

// access php object
$obj = json_decode($jsonobj);
echo $obj->Peter . "\n" ;
echo $obj->Ben . "\n";
echo $obj->Joe . "\n";

// access associative array
$arr = json_decode($jsonobj, true);
echo $arr["Peter"] . "\n";
echo $arr["Ben"] . "\n";
echo $arr["Joe"] . "\n";

// loop through php object
foreach($obj as $key => $value) {  
    echo $key . " => " . $value . "\n";
}

// loop through associative array
foreach($arr as $key => $value){
    echo $key . " => " . $value . "\n";
}