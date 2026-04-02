<?php
    // 1. 数据库连接部分
    // 连接本地数据库，参数依次为：主机、用户名、密码、数据库名
    $conn = mysqli_connect("localhost","admin","123456","web");
    // 检查连接是否成功，如果失败则输出错误信息并终止脚本
    if (mysqli_connect_errno()){
        exit(mysqli_connect_error());
    }
    // 设置字符集为 utf8，防止中文乱码
    mysqli_set_charset($conn,"utf8");

    // 2. 数据查询与防重检查部分
    // 构造SQL查询语句，检查用户名是否已存在
    $result=mysqli_query($conn,"select *from studentinfo where username='".$_POST["username"]."'");
    // 获取查询结果的行数
    $num = mysqli_num_rows($result);

    // 3. 获取并处理表单数据
    // 从POST请求中获取用户提交的各个字段
    $name=$_POST['username'];
    $pwd=$_POST['password'];
    $gender=$_POST['gender'];
    $age=$_POST['age'];
    $birthday=$_POST['birthday'];
    $email=$_POST['email'];
    $address=$_POST['address'];
    // 将兴趣爱好数组转为字符串存储
    $hobby = isset($_POST['hobby']) ? implode(",", $_POST['hobby']) : '';
    
    // 4. 业务逻辑判断与数据插入
    // 如果查询到的行数大于0，说明用户已存在
    if ($num > 0){
        echo "<script>alert('用户信息已存在');history.back();</script>";
    }else{
        // 用户不存在，执行插入操作
        mysqli_query($conn,"insert into studentinfo values('$name','$pwd','$gender','$age','$birthday','$email','$address','$hobby')");
        echo "<script>alert('注册成功');location.href='login1.html'</script>";
    }