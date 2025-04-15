<?php

// sanitize string and remove html tags
$str = "<h1>Hello World!</h1>";
$newstr = strip_tags($str);
echo $newstr;

// validate integer; filter will consider 0 invalid
$int = 100;
if (filter_var($int, FILTER_VALIDATE_INT) || 
filter_var($int, FILTER_VALIDATE_INT) == 0) {
    echo"integer is valid";
} else {
    echo "Integer is not valid";
}

// validate IP address
$ip = "127.0.0.1";

if (filter_var($ip, FILTER_VALIDATE_IP)){
    echo "$ip is a valid IP address";
} else {
    echo "$ip is not a valid IP address";
}

// sanitize and validate email address
$email = "john.doe@example.com";

// remove illegal characters
$email = filter_var($email, FILTER_VALIDATE_EMAIL);

//validate email
if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo "$email is a valid email address";
} else {
    echo "$email is not a valid email address";
}

// sanitize and validate url
$url = "https://www.w3schools.com";

// remove illegal characters
$url = filter_var($url, FILTER_VALIDATE_URL);

// validate url
if (filter_var($url, FILTER_VALIDATE_URL)) {
    echo "$url is a valid url";
} else {
    echo "$url is not a valid url";
}
