<!DOCTYPE html>
<html>
<body>
<?php
$db = new mysqli("localhost", "root", "root", "mydb");
$result = $db->query("SELECT * FROM employees");
if ($myrow = $result->fetch_array()) {
	echo "<table border=1>\n";
	echo "<tr><td>姓名</td><td>住址</td></tr>\n";
	do {
		printf("<tr><td>%s %s</td><td>%s</tr>\n", $myrow["first"],
			$myrow["last"], $myrow["address"]);
	} while ($myrow = $result->fetch_array());
	echo "</table>\n";
} else {
	echo "对不起，没有找到记录！";
}
?>
</body>
</html>


