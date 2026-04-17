<?php
    $raw_user = $_POST['username'];
    $raw_pass = $_POST['password'];

    $clean_user = htmlspecialchars(trim($raw_user));
    $clean_pass = trim($raw_pass);

    if(strlen($clean_pass) < 6){
        die("<h2>密码长度不足！</h2>>");
    }
    echo "后端安全拦截到的账号是" .$clean_user ."<br>";

    if($clean_user == "admin" && $clean_pass == "admin666666"){
        echo "<h2>登入成功，欢迎进入系统</h2>";
    }else{
        echo "<h2>账号密码错误！</h2>";
    }
?>
