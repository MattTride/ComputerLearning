<<?php
echo '<table border="1" cellpadding="8" cellspacing="0" 
      style="border-collapse:collapse; margin:20px auto; font-family:Arial;">
      <tr>';

for ($i = 1; $i <= 100; $i++) {
    // 判断是否含7（倍数、个位是7、十位是7）
    if ($i % 7 == 0 || $i % 10 == 7 || intdiv($i, 10) == 7) {
        echo '<td bgcolor="blue" style="color:#fff; font-weight:bold; font-size:22px; 
              text-align:center; width:60px; height:60px;">过</td>';
    } else {
        echo '<td bgcolor="#f79646" style="color:#000; font-weight:bold; font-size:22px; 
              text-align:center; width:60px; height:60px;">' . $i . '</td>';
    }
    if ($i % 10 == 0) {
        echo '</tr>';
        if ($i < 100) {
            echo '<tr>';
        }
    }
}

echo '</table>';
?>


