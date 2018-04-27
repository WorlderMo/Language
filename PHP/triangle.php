<?php
$a = @$_POST['a'];
$b = @$_POST['b'];
$c = @$_POST['c'];
if ($a + $b > $c && $a + $c > $b && $b + $c > $a) {
	echo "三角形";
} else {
	echo "不是三角形";
}
?>
