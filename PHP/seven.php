<html>
<body>
<?php
function db_connect($host = "localhost", $user = "root", $pass = "root") {
	$db = mysql_connect($host, $username, $password);
	return $db;
}
$old_db = db_connect();
$new_host = "site.com";
$new_db = db_connect($new_host);
?>
</body>
</html>


