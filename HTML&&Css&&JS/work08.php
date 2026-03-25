<?php 
$student_infos = array(
    array(
        "student_id"=> "2019003001",
        "student_name"=> "赵佳",
        "student_age"=> "20",
        "student_tel"=> "6666",
    ),

    array(
        "student_if"=> "2019003002",
        "student_name"=> "兰",
        "studnet_age"=> "20",
        "student_tel"=> "1111",
    ),

    array(
        "student_id"=> "2019003003",
        "studnet_name"=> "林",
        "student_age"=> "20",
        "student_tel"=> "2222",
    ),

    array(
        "student_id"=> "2019003004",
        "student_name"=> "马",
        "student_age"=> "20",
        "student_tel"=> "3333",
    ),
);
?>

<table border ="1" cellpadding = "8" cellspacing = "0" style = "margin: 20px auto;">
    <caption>学生信息表</caption>
    <tr>
        <th>学生学号</th>
        <th>学生姓名</th>
        <th>学生年龄</th>
        <th>电话号码</th>
        <th>操作1</th>
        <th>操作2</th>
    </tr>
    <?php
    foreach ($student_infos as $student_info) {
        echo '<tr>';
        
        foreach($student_info as $value){
            echo '<td>'.$value.'</td>';
        }
        echo '<td><a href = "" >修改</a></td>';
        echo '<td><a href = "" >修改</a></td>';
        echo '</tr>';
    } 