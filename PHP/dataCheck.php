<html>
<body>
<?php
$submit = $_POST['submit'];
if ($submit) {
	if (strlen($_POST["first"]) < 6 || strlen($_POST["last"]) < 6) {
		$error = "对不起，您必须填写所有栏目！";
	} else {
// 处理表格输入内容
		echo "谢谢！";
	}
}
if (!$submit || $error) {
	echo $error;
	?>
<P>
<form method="post" action="<?php echo $PHP_SELF ?>">
第一栏: <input type="text" name="first" value="<?php echo $first ?>"><br>
第二栏: <input type="text" name="last" value="<?php echo $last ?>"><br>
<input type="Submit" name="submit" value="输入信息">
</form>
<?php
} // if结束
?>
</body>
</html>

