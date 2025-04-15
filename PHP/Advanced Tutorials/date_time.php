<?php
echo"Today is " . date("Y/m/d") ."<br>";
echo"Today is " . date("Y.m.d") ."<br>";
echo"Today is " . date("Y-m-d") ."<br>";
echo"Today is " . date("l") ."<br>";

echo "The time is " . date("h:i:sa") ."<br>";

date_default_timezone_set("America/Chicago");
echo "The time is " . date("h:i:sa") ."<br>";

$d = mktime(11, 14, 54, 8, 12, 2014);
echo "Created date is " . date("Y-m-d h:i:sa", $d) ."<br>";

$d = strtotime("10:30pm April 15 2014");
echo "Created date is " . date("Y-m-d h:i:sa", $d) ."<br>";

$d=strtotime("tomorrow");
echo date("Y-m-d h:i:sa", $d) . "<br>";

$d=strtotime("next Saturday");
echo date("Y-m-d h:i:sa", $d) . "<br>";

$d=strtotime("+3 Months");
echo date("Y-m-d h:i:sa", $d) . "<br>";

$startDate = strtotime("Saturday");
$endDate = strtotime("+6 weeks", $startDate);

while ($startDate < $endDate) {
    echo date("M d", $startDate) . "<br>";
    $startDate = strtotime("+1 week", $startDate);
}