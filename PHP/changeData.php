<html>
<body>
<?php
$db = new mysqli("localhost", "root", "root", "mydb");
$id = $_GET['id'];
$filePath = basename(__FILE__);
if ($id) {
	$submit = $_POST;
	if ($submit) {
		$sql = "UPDATE employees SET first='$_POST[first]', last='$_POST[last]',
    address='$_POST[address]', position='$_POST[position]' WHERE id=$id";
		$result = $db->query($sql);
		echo "谢谢！数据更改完成\n";
	} else {
// 查询数据库
		$sql = "SELECT * FROM employees WHERE id=$id";
		$result = $db->query($sql);
		$myrow = $result->fetch_array();
		?>
    <form method="post" action="<?php echo basename(__FILE__) . "?id=" . $myrow['id'] ?>">
    <input type=hidden name="d" value="<?php echo $myrow["id"] ?>">
    名：  <input type="Text" name="first" value="<?php echo
		$myrow["first"] ?>"><br>
    姓：  <input type="Text" name="last" value="<?php echo
		$myrow["last"] ?>"><br>
    住址：<input type="Text" name="address" value="<?php echo
		$myrow["address"] ?>"><br>
    职位：<input type="Text" name="position" value="<?php echo
		$myrow["position"] ?>"><br>
    <input type="Submit" name="submit" value="输入信息">
    </form>
<?php
}
} else {
	// 显示员工列表
	$result = $db->query("SELECT * FROM employees");
	while ($myrow = $result->fetch_array()) {
		printf("<a href=\"%s?id=%s\">%s %s</a><br>\n", $filePath,
			$myrow["id"], $myrow["first"], $myrow["last"]);
	}
}
?>
</body>
</html>


