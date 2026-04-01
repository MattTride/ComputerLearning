<?php
// 1. 启动会话，判断用户是否登录
session_start();
if (!isset($_SESSION['username'])) {
    header("Location: login.html");
    exit;
}
$currentUser = $_SESSION['username']; // 当前登录用户名

// 2. 连接数据库
$conn = mysqli_connect("localhost", "admin", "123456", "web");
if (!$conn) {
    die("数据库连接失败：" . mysqli_connect_error());
}
mysqli_set_charset($conn, "utf8");

// 3. 只查询当前用户的课程信息（核心：不同用户看到不同数据）
$sql = "SELECT * FROM tb_course WHERE username = '$currentUser'";
$result = mysqli_query($conn, $sql);
?>

<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>我的课程</title>
    <style>
        table {
            width: 90%;
            margin: 50px auto;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ccc;
            padding: 10px;
            text-align: center;
        }
        th {
            background-color: #f0f0f0;
        }
        h1 {
            text-align: center;
            margin-top: 30px;
        }
    </style>
</head>
<body>
    <h1>欢迎，<?php echo $currentUser; ?>！您的课程列表如下</h1>
    <table>
        <thead>
            <tr>
                <th>序号</th>
                <th>课程名称</th>
                <th>课程介绍</th>
                <th>课程时长</th>
                <th>学习进度</th>
                <th>用户姓名</th>
            </tr>
        </thead>
        <tbody>
            <?php
            $num = 1;
            while ($row = mysqli_fetch_assoc($result)) {
                echo "<tr>";
                echo "<td>" . $num++ . "</td>";
                echo "<td>" . $row['course_name'] . "</td>";
                echo "<td>" . $row['course_desc'] . "</td>";
                echo "<td>" . $row['course_time'] . "</td>";
                echo "<td>" . $row['course_percent'] . "</td>";
                echo "<td>" . $row['username'] . "</td>";
                echo "</tr>";
            }
            // 如果没有课程数据
            if (mysqli_num_rows($result) == 0) {
                echo "<tr><td colspan='6'>暂无课程信息</td></tr>";
            }
            ?>
        </tbody>
    </table>
</body>
</html>

<?php
// 4. 关闭数据库连接
mysqli_close($conn);
?>