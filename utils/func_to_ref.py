from inspect import getmodule


def func_ref_to_import(func):
    """
    Function to convert function reference/object to the import syntax.
    Ex: from vsuite.test import test_func
    func_ref_to_import(test_func) -> 'test.test.test_func'



    Args:
        func: print_result

    Returns (str):
        A string similar to "test.test.test_external_django.print_result"

    """
    return f"{getmodule(func).__name__}.{func.__name__}"