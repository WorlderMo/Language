<html>
<body>
<?php
$db = new mysqli("localhost", "root", "root", "mydb");
$filePath = basename(__FILE__);
$submit = $_POST;
$id = $_GET['id'];
$delete = $_GET['delete'];
$add = $_GET['add'];
if ($submit) {
	// 如果没有ID，则我们是在增加记录，否则我们是在修改记录
	if ($id) {
		$sql = "UPDATE employees SET first='$_POST[first]', last='$_POST[last]',
    address='$_POST[address]', position='$_POST[position]' WHERE id=$id";
	} else {
		$sql = "INSERT INTO employees (first,last,address,position)
    VALUES ('$_POST[first]','$_POST[last]', '$_POST[address]', '$_POST[position]')";
	}
	// 向数据库发出SQL命令
	$result = $db->query($sql);
	echo "记录修改成功！<p>";
} elseif ($delete) {
// 删除一条记录
	$sql = "DELETE FROM employees WHERE id=$id";
	$result = $db->query($sql);
	echo "记录删除成功！<p>";
} elseif ($add) {
	?>
    <form method="post" action="<?php echo $filePath ?>">
    <input type=hidden name="id">

    名：<input type="Text" name="first"><br>
    姓：<input type="Text" name="last"><br>
    住址：<input type="Text" name="address"><br>
    职位：<input type="Text" name="position"><br>
    <input type="Submit" name="submit" value="输入信息">
    </form>
<?php
} else {
	// 如果我们还没有按submit按钮，那么执行下面这部分程序
	if (!$id) {
		// 如果不是修改状态，则显示员工列表
		$result = $db->query("SELECT * FROM employees");
		while ($myrow = $result->fetch_array()) {
			printf("<a href=\"%s?id=%s\">%s %s</a> \n",
				$filePath, $myrow["id"], $myrow["first"], $myrow["last"]);
			printf("<a href=\"%s?id=%s&delete=yes\">(DELETE)</a><br>", $filePath, $myrow["id"]);
		}
	}
	?>
  <P>
    <a href="<?php echo $filePath . "?add=yes" ?>">ADD A RECORD</a>
  <p>
  <form method="post" action="<?php echo $filePath . "?id=" . $_GET["id"] ?>">
  <?php
if ($id) {
		// 我们是在编辑修改状态，因些选择一条记录
		$sql = "SELECT * FROM employees WHERE id=$id";
		$result = $db->query($sql);
		$myrow = $result->fetch_array();
		$id = $myrow["id"];
		$first = $myrow["first"];
		$last = $myrow["last"];
		$address = $myrow["address"];
		$position = $myrow["position"];
		// 显示id，供用户编辑修改
		?>
    <input type=hidden name="id" value="<?php echo $id ?>">

    名：<input type="Text" name="first" value="<?php echo $first ?>"><br>
    姓：<input type="Text" name="last" value="<?php echo $last ?>"><br>
    住址：<input type="Text" name="address" value="<?php echo $address ?>"><br>
    职位：<input type="Text" name="position" value="<?php echo $position ?>"><br>
    <input type="Submit" name="submit" value="输入信息">
    </form>
<?php
}
	?>
  <?php
}
?>
</body>
</html>



