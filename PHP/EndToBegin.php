<?php
    /**
     * Say Goodbye to 2017
     */
    class GoodbyeTo2107
    {
        function sayGoodbyeTo2017()
        {
            echo " Goodbye, 2017 ";
        }
    }
    /**
     * Say Hello to 2018
     */
    class HelloTo2018 extends GoodbyeTo2107
    {
        function sayHelloTo2018()
        {
            echo " Hello, 2018 ";
        }
    }
    $mohailang_old = new GoodbyeTo2107();
    $mohailang_new = new HelloTo2018();
    $mohailang_old->sayGoodbyeTo2017();
    $mohailang_new->sayHelloTo2018();
?>
