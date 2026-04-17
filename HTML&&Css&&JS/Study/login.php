<?php
    $user = $_POST['username'];
    $pass = $_POST['password'];
    echo "拦截到的账号是:" . $user . "<br>";

    if($user == "admin" && $pass == "admin"){
echo "<h2>登入成功!</h2>";}
else{echo "<h2>登入失败</h2>";}




?>