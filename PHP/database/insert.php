<?php
$mysql = new mysqli("localhost", "root", "520123");
if ($mysql->connect_error) {
	die('连接失败<br>' . $mysql->connect_error);
} else {
	echo "连接成功<br>";
}
$db_name = "databaseThree";
if (!$mysql->select_db($db_name)) {
	$createdatabase = "CREATE DATABASE databaseThree";
	if ($mysql->query($createdatabase)) {
		echo "创建数据库成功<br>";
	} else {
		echo "创建数据库失败: <br>" . $mysql->error;
	}
}

$mysql->select_db($db_name);
$sql_select = "SELECT * from Students";
if (!$mysql->query($sql_select)) {
	$sql_create_table = "CREATE TABLE Students
        (
            name char(20),
            student_id int,
            math int,
            chinese int,
            english int
        )";
	$mysql->query($sql_create_table);
}
$sql_insert = "INSERT INTO Students (name, student_id, math, chinese, english)
    VALUES ('$_POST[name]','$_POST[student_id]', '$_POST[math]', '$_POST[chinese]', '$_POST[english]')";
if (!$mysql->query($sql_insert)) {
	die('插入数据失败 <br>' . $mysql->error);
}
echo "Congratulation<br>";
?>
