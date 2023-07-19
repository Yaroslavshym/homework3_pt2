def check_some_list(some_list: list) -> list:
    filtered_list = list(filter(check_some_object, some_list))
    return filtered_list


def check_some_object(some_object: any) -> bool:
    if check_if_object_is_evaluable(some_object):
        if eval(str(some_object)) >= 500:
            return True
    return False


def check_if_object_is_evaluable(some_object: any):
    try:
        eval(str(some_object))
        return True
    except NameError:
        return False
