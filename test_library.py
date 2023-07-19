import library as lib


def test_check_if_object_is_evaluable():
    object1 = '12+3344'
    object2 = 'lksadla'
    object3 = 123
    object4 = '2333'
    condition1 = lib.check_if_object_is_evaluable(object1)
    condition2 = not lib.check_if_object_is_evaluable(object2)
    condition3 = lib.check_if_object_is_evaluable(object3)
    condition4 = lib.check_if_object_is_evaluable(object4)
    list_of_conditions = [condition1, condition2, condition3, condition4]
    assert all(list_of_conditions)


def test_check_some_object():
    object1 = '12+3344'
    object2 = 'lksadla'
    object3 = 123
    object4 = '2333'
    condition1 = lib.check_some_object(object1)
    condition2 = not lib.check_some_object(object2)
    condition3 = not lib.check_some_object(object3)
    condition4 = lib.check_some_object(object4)
    list_of_conditions = [condition1, condition2, condition3, condition4]
    assert all(list_of_conditions)


def test_check_some_list():
    some_list_of_data = [501, 'fff', 50, 0, -50.5, 'bat', 600, 358]
    c = lib.check_some_list(some_list_of_data)
    condition = c == [501, 600]
    assert condition
