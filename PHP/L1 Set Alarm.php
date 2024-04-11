//https://www.codewars.com/kata/568dcc3c7f12767a62000038
<?php
    function setAlarm(bool $employed, bool $vacation): bool {
         if ($employed == true and $vacation == false) {
            return true;
    }
    return false;
    }
    