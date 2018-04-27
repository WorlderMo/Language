<html>
<body>
<?php
$db = new mysqli("localhost", "root", "root", "mydb");
function db_query($sql) {
	global $db;
	$result = $db->query($sql);
	return $result;
}
$sql = "SELECT * FROM employees";
$result = db_query($sql);
?>
</body>
</html>

