<?php
error_reporting(E_ALL);

if(isset($_POST['Upload'])) {
    $fname = $_FILES['uploaded']['name'];
    $fsize = $_FILES['uploaded']['size'];
    $tmp_name = $_FILES['uploaded']['tmp_name'];
    $target = "uploads/" . basename($fname);

    $max_size = 2 * 1024;

    echo "文件临时路径: " . $tmp_name . "<br>";

    if ($fsize > $max_size) {
        echo "上传失败：文件大小为 " . round($fsize / 1024 , 2) . "MB，超过了 2KB 的限制。";
    } else {
        if(move_uploaded_file($tmp_name, $target)) {
            echo "上传成功！<br>";
            echo "<img src='$target' width='200'>";
        } else {
            echo "上传失败：服务器无法保存文件。";
        }
    }
}
?>