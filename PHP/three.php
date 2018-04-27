<html>
<body>
<?php
$submit = $_POST['submit'];
if ($submit) {
	$pattern = "/^([0-9A-Za-z\\-_\\.]+)@([0-9a-z]+\\.[a-z]{2,3}(\\.[a-z]{2})?)$/i";
	if (!preg_match($pattern, $_POST["last"])) {
		$error = "对不起，邮箱格式不正确！";
	} else {
// 处理表格输入内容
		echo "邮箱输入正确！";
	}
}
if (!$submit || $error) {
	echo $error;
	?>
<P>
<form method="post" action="<?php echo $PHP_SELF ?>">
邮箱: <input type="text" name="last" value="<?php echo $last ?>"><br>
<input type="Submit" name="submit" value="输入信息">
</form>
<?php
} // if结束
?>
</body>
</html>


