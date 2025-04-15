<?php
$myfile = fopen("testfile.txt","w") or die("Unable to open file");
$txt = "John Doe\n";
fwrite($myfile, $txt);
$txt= "Jane Doe\n";
fwrite($myfile,$txt);
fclose($myfile);

// opening and writing to existing file overwrites all data
$myfile = fopen("testfile.txt","w") or die("Unable to open file");
$txt = "Mickey";
fwrite($myfile,$txt);
$txt = "Minnie";
fwrite($myfile,$txt);
fclose($myfile);


// to append to existing file, open with "a"
$myfile = fopen("testfile.txt","a") or die("Unable to open file");
fwrite($myfile,"Donald");
fwrite($myfile,"Goofy");
fclose($myfile);
