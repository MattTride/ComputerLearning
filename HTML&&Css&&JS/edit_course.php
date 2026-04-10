
<!-- 这里开始是带样式的表单 -->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>修改课程信息</title>
    <style>
        /* 全局样式 */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: "Microsoft YaHei";
        }

        /* 表单容器 */
        .form-box {
            width: 500px;
            margin: 80px auto;
            padding: 30px;
            border: 1px solid #ccc;
            border-radius: 10px;
            background: #f9f9f9;
        }

        /* 标题 */
        .form-box h2 {
            text-align: center;
            margin-bottom: 30px;
            color: #333;
        }

        /* 表单项 */
        .form-item {
            margin-bottom: 20px;
        }

        /* 标签 */
        .form-item label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
            color: #555;
        }

        /* 输入框 */
        .form-item input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
        }

        /* 按钮 */
        .btn {
            width: 100%;
            padding: 12px;
            background: #4CAF50;
            color: #fff;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }

        .btn:hover {
            background: #45a049;
        }
    </style>
</head>
<body>
    <div class="form-box">
        <h2>修改课程信息</h2>
        <form action="" method="post">
            <div class="form-item">
                <label>课程名称</label>
                <input type="text" name="course_name" value="<?php echo $row['course_name'] ?>">
            </div>

            <div class="form-item">
                <label>课程介绍</label>
                <input type="text" name="course_desc" value="<?php echo $row['course_desc'] ?>">
            </div>

            <div class="form-item">
                <label>课程时长</label>
                <input type="text" name="course_time" value="<?php echo $row['course_time'] ?>">
            </div>

            <div class="form-item">
                <label>学习进度</label>
                <input type="text" name="course_percent" value="<?php echo $row['course_percent'] ?>">
            </div>

            <button type="submit" name="submit" class="btn">保存修改</button>
        </form>
    </div>
</body>
</html>
