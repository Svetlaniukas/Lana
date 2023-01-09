import mymodule


def work_with_db_json_staff_shift():
    assert mymodule.NAME == "mymodule"


def test_empty_json_shut_return_empty_dictionary():
    dict_empty = mymodule.work_with_db_json_staff_shift(
        "staff_empty_file.json", ''
    )
    assert len(dict_empty) == 0


def test_not_empty_json_shut_retur_not_emthy_dictionary():
    file_with_data = mymodule.work_with_db_json_staff_shift(
        "staff.json", 'weekday'
    )
    assert len(file_with_data) == 5


def test_json_valid_shut_return_valid_dictionary():
    pass
    persons = mymodule.work_with_db_json_staff_shift(
        "staff_name_surname.json", 'person'
    )
    assert persons['Denis'] == 'Petrov'
    assert persons['Tania'] == 'Bal'
    assert persons['Lana'] == 'Mel'


def test_json_shut_retur_valid_dictionary():
    valid_dictionary = mymodule.work_with_db_json_staff_shift(
        "staff_position.json", 'person'
    )
    assert len(valid_dictionary) == 1


def test_json_not_root__should_return_empty_dict():
    pass
    dict = mymodule.work_with_db_json_staff_shift(
        "staff_position.json", ':::'
    )
    assert len(dict) == 0


def test_3_line_json_shut_retur_3_itiems():
    line_test = mymodule.work_with_db_json_staff_shift(
        "staff_name_surname.json", 'person'
    )
    
    assert len(line_test) == 3


def test_1_line_json_shut_retur_1_itiems():
    test_1_line = mymodule.work_with_db_json_staff_shift(
        "staff_position.json", 'person'
    )
    assert len(test_1_line) == 1
