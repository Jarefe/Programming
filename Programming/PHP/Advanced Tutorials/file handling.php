<?php
echo readfile("placeholder.txt"); // outputs file then char length

$myfile = fopen("placeholder.txt","r") or die("Unable to open file");
echo fread($myfile, filesize("placeholder.txt")); 
// fread reads from open file
fclose($myfile);

$myfile = fopen("placeholder.txt","r") or die("Unable to open file");
// fget reads single line
echo "\n" . fgets($myfile);
fclose($myfile);


$myfile = fopen("placeholder.txt","r") or die("Unable to open file");
// feof = end of file
while(!feof($myfile)) {
    echo fgets($myfile) . "<br>";
}
echo "\n";
fclose($myfile);

$myfile = fopen("placeholder.txt","r") or die("Unable to open file");
// fgetc gets 1 char
while(!feof($myfile)) {
    echo fgetc($myfile);
}
fclose($myfile);