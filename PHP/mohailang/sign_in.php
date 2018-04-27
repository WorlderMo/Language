<?php

/**
 * Created by PhpStorm.
 * User: mohailang
 * Date: 2017/12/5
 * Time: 9:45
 */

    $mail = $_REQUEST['mail'];
    $psd = $_REQUEST['psd'];

    # connect to the sql
    $datafile = "mohailang.sqlite";
    $query = "select * from user where mail='".$mail."' and psd='".$psd."'";
    $db = new SQLite3($datafile);
    $result = $db->query($query);
    if(!$result)
        echo "<script>location.href=\"index.php\"</script>";
    else{
        while($row = $result->fetchArray()){
            //
            $position = $row['position'];
            if($position==0)
                echo "<script>location.href=\"admin_index.php?id=".$row['id']."\"</script>";
            else
                echo "<script>location.href=\"salesman_index.php?id=".$row['id']."\"</script>";
            setcookie("current_user", $mail);
            exit;
        }
        echo "<script>location.href=\"index.php\"</script>";

    }

?>