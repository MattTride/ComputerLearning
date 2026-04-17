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

// 1. 接收原始的脏数据
$raw_user = $_POST['username'];
$raw_pass = $_POST['password'];

// 我们连 trim 都不做了，把什么长度校验全删了，主打一个纯粹的漏洞环境！

// 2. 致命的拼接：直接把 $raw_user 和 $raw_pass 塞进 SQL 语句
$sql = "select * from users where username = '$raw_user' and password = '$raw_pass'";
$result = mysqli_query($conn, $sql);

// 3. 结果判断
if(mysqli_num_rows($result) > 0){
    echo "<h2>登入成功，欢迎进入系统</h2>";
} else{
    echo "<h2>账号密码错误</h2>";
}
mysqli_close($conn);
?>
