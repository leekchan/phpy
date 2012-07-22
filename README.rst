phPy
===============

phPy is a simple way to call legacy PHP functions from Python.


```php

    function LegacyPHPFunction($arg1, $arg2, $arg3) {
        //... original codes...

        $result = array(
            "foo" => $arg1,
            "bar" => $arg2,
        );

        echo json_encode($result);
    }
```

.. code-block:: python

    from phpy import PHP

    #php_file_path = the path of your legacy php file...
    php = PHP(php_file_path)
    result_raw = php.get_raw('LegacyPHPFunction', ['argument1',u'argument2', 3]) # get a return value as a raw string
    result_dict = php.get_dict('LegacyPHPFunction', ['argument1',u'argument2', 3]) # get return values as a python dictionary
    print result_dict['foo']