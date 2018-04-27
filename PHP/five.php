<html>
<body>
<?php
function do_error($error) {
	echo "噢，好象有点儿问题...<br>";
	echo "系统报告的错误是：$error.\n<br>";
	echo "最好是暂时关闭网站并通知系统管理员。";
	die;
}
$db = @mysqli_connect("localhost", "root", "wrong_pw","mydb");
if (!$db) {
	$db_error = "无法连接到MySQL数据库";
	do_error($db_error);
} else {
	echo "数据库连接成功";
}
?>
</body>
</html>

