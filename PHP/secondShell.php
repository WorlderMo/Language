<!DOCTYPE html>
<html>
<body>
<?php
$db = new mysqli("localhost", "root", "root", "mydb");
// display individual record
// 显示单条记录内容
$id = $_GET["id"];
if ($id) {
	$result = $db->query("SELECT * FROM employees WHERE id=$id");
	$myrow = $result->fetch_array();
	printf("名: %s\n<br>", $myrow["first"]);
	printf("姓: %s\n<br>", $myrow["last"]);
	printf("住址: %s\n<br>", $myrow["address"]);
	printf("职位: %s\n<br>", $myrow["position"]);
} else {
	// show employee list
	// 显示员工列表
	$result = $db->query("SELECT * FROM employees");
	if ($myrow = $result->fetch_array()) {
		// display list if there are records to display
		// 如果有记录，则显示列表
		do {
			printf("<a href=\"%s?id=%s\">%s %s</a><br>\n", $PATH_INFO,
				$myrow["id"], $myrow["first"], $myrow["last"]);
		} while ($myrow = $result->fetch_array());
	} else {
		// no records to display
		// 没有记录可显示
		echo "对不起，没有找到记录！";
	}
}
?>
</body>
</html>


