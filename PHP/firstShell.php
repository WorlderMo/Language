<!DOCTYPE html>
<html>
<body>
<?php
$db = new mysqli("localhost", "root", "root", "mydb");
$result = $db->query("SELECT * FROM employees");
if ($myrow = $result->fetch_array()) {
	do {
		printf("<a href=\"%s?id=%s\">%s %s</a><br>\n",
			$PATH_INFO, $myrow["id"], $myrow["first"], $myrow["last"]);
	} while ($myrow = $result->fetch_array());
} else {
	echo "对不起，没有找到记录！";
}
?>
</body>
</html>



