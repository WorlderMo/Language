<?php
$title = "Hello World";
include "header.inc";
$db = new mysqli("localhost", "root", "root", "mydb");
$result = $db->query("SELECT * FROM employees");
echo "<table border=1>\n";
echo "<tr><td>名字</td><td>职位</tr>\n";
while ($myrow = $result->fetch_row()) {
	printf("<tr><td>%s %s</td><td>%s</tr>\n", $myrow[1], $myrow[2], $myrow[3]);
}
echo "</table>\n";
include "footer.inc";
?>


