<?php
    $host = "127.0.0.1";
    $port = 8889;
    $db_user = "root";
    $db_pass = "root";
    $db_name = "study_html";

    $conn = mysqli_connect($host, $db_user, $db_pass, $db_name, $port);

    if(!$conn){
        die("数据库连接失败，MAMP开启了吗？账号密码对了吗?" .mysqli_connect_error());
    }

    $raw_user = $_POST['username'];
    $raw_pass = $_POST['password'];

    $clean_user = htmlspecialchars(trim($raw_user));
    $clean_pass = trim($raw_pass);

    if(strlen($clean_pass) < 6){
        die("<h2>密码长度不足！</h2>");
    }


    $sql = "select * from users where username = '$clean_user' and password = '$clean_pass'";
    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result) > 0){
        echo "<h2>登入成功，欢迎进入系统</h2>";
    } else{
        echo "<h2>账号密码错误</h2>";
    }
    mysqli_close($conn);
?>
