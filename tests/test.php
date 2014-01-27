<?php
    function mapping($foo, $bar, $baz) {
        $rv = array(
            "foo" => $foo,
            "bar" => $bar,
            "baz" => $baz
        );
        echo json_encode($rv);
    }
?>
