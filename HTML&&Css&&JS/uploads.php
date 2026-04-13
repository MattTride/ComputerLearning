<?php
header("Content_type:text/html;charset=utf-8");
if(!empty($_FILES["upfile"]["name"])){
    $file = $_FILES["upfile"];

    if($file["size"] >0 && $file["size"]< 20000000){
    $path = "".$_FILES["upfile"]["name"];

    move_uploaded_file($_FILES["upfile"]["tmp_name"],$path);

    echo"上传成功！";
}else{
    echo "文件大小不符合要求";
}

}else{
    echo "请上传文件";
}



?>


