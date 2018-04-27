<!DOCTYPE html>
<html>
<body>
<?php
$db = new mysqli("localhost", "root", "root", "mydb");
// if ($mysql->connect_error) {
// 	die('连接失败<br>' . $mysql->connect_error);
// } else {
// 	echo "连接成功<br>";
// }
$result = $db->query("SELECT * FROM employees");
$row = $result->fetch_array();
printf("First Name: %s<br>\n", $row["first"]);
printf("Last Name: %s<br>\n", $row["last"]);
printf("Address: %s<br>\n", $row["address"]);
printf("Position: %s<br>\n", $row["position"]);
?>
</body>
</html>
