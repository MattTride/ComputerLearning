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

    $sql = "select * from users where username = ? and password = ?";
    $stmt = mysqli_prepare($conn, $sql);

    if($stmt){
        mysqli_stmt_bind_param($stmt, "ss", $raw_user, $raw_pass);
        mysqli_stmt_execute($stmt);

        $result = mysqli_stmt_get_result($stmt);

        if(mysqli_num_rows($result) > 0){
            echo "<h2>登入成功，预处理生效中</h2>>";
        }else {
            echo "<h2>账号密码错误</h2>>";
        }
        mysqli_stmt_close($stmt);
    }else{
        echo "预处理失败";
    }
    mysqli_close($conn);
?>
