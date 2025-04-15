<?php

try{
    2 / 0;
} catch (Exception $e) {
    echo $e->getMessage();
} finally {
    echo "This output will happen even if an exception is caught";
}