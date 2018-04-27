<html>
<body>
<?php
$submit = $_POST["submit"];
if ($submit) {
	// 处理表格输入
	$db = new mysqli("localhost", "root", "root", "mydb");
	$sql = "INSERT INTO employees(first,last,address,position) VALUES ('$_POST[first]','$_POST[last]', '$_POST[address]', '$_POST[position]')";
	$result = $db->query($sql);
	echo "Thank you! Information entered.\n";
} else {
	// 显示表格
	?>
  <form method="post" action="<?php echo basename(__FILE__) ?>">
  名：<input type="Text" name="first"><br>
  姓：<input type="Text" name="last"><br>
  住址：<input type="Text" name="address"><br>
  职位：<input type="Text" name="position"><br>
  <input type="Submit" name="submit" value="输入信息">
  </form>
  <?php
} // end if，if结束
?>
</body>
</html>


