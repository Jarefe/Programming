<?php
$int = 100;
$min = 1;
$max = 200;

if (filter_var($int, FILTER_VALIDATE_INT, array("options" => array(
    "min_range" => $min, "max_range" => $max
))) == false) {
    echo"Variable value is not within legal range";
} else {
    echo "Variable is within legal range";
}

// easier way to check
if (is_int($int) && $int >= $min && $int <= $max) {
    echo"Variable value is not within legal range";
} else {
    echo "Variable is within legal range";
}

// validate ipv6 address
$ip = "2001:0db8:85a3:08d3:1319:8a2e:0370:7334";
if (filter_var($ip, FILTER_VALIDATE_IP)){
    echo "$ip is a valid IPv6 address";
} else {
    echo "$ip is not a valid IPv6 address";
}

// validate url with query string
$url = "https://www.w3schools.com";

if (filter_var($url, FILTER_VALIDATE_URL, FILTER_FLAG_QUERY_REQUIRED)){
    echo "$url is a valid URL with a query string";
} else{
    echo "$url is not a valid URL with a query string";
}

// remove chars with ascii value > 127
$str = "<h1>Hello WorldÆØÅ!</h1>";
$stripped = strip_tags($str);
$newstr = preg_replace('/[\x80-\xFF]/', '', $stripped);
echo $newstr;

