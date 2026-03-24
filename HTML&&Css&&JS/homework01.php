<?php
echo"<table border = '0px'>";
for ($i = 1; $i < 100; $i++) {
    echo"<tr>";
    for( $j = 1; $j < $i; $j++ ) {
    $k = $i + $j;
    echo"<td bgcolor='blue'> $j*$i = $k</td>";
    }
    echo "</tr>";
}
?>