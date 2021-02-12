def test_setting_and_swapping():
    my_number = 42
    my_name = "bion"
    my_number, my_name = my_name, my_number
    assert my_number == "bion"
    assert my_name == 42
    my_number, my_name = my_name, my_number
    assert my_number == 42
    assert my_name == "bion"
