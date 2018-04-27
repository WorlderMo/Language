<!DOCTYPE html>
<html>
<body>
<?php
$db = new mysqli("localhost", "root", "root", "mydb");
$result = $db->query("SELECT * FROM employees");
echo "<table border=1>\n";
echo "<tr><td>姓名</td><td>职位</td></tr>\n";
while ($myrow = $result->fetch_row()) {
	printf("<tr><td>%s %s</td><td>%s</td></tr>\n", $myrow[1], $myrow[2], $myrow[3]);
}
echo "</table>\n";
?>
</body>
</html>


