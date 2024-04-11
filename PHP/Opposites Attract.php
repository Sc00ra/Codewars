//https://www.codewars.com/kata/555086d53eac039a2a000083
<?php
    function lovefunc($flower1, $flower2) {
        if ($flower1 % 2 != $flower2 % 2) {
            return true;
        }
        return false;
    }