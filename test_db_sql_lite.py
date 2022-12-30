import mymodule


def work_with_db_xml_staff_shift():
    assert mymodule.NAME == "mymodule"


def test_empty_xml_shut_return_empty_dictionary():
    dict_empty = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db", 'key_name', 'val_name')
    assert len(dict_empty) == 0


def test_xml_valid_shut_return_valid_dictionary():
    persons = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db", 'name', 'surname')
    assert len(persons) == 3


def test_xml_shut_retur_valid_dictionary():
    valid_dictionary = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db", 'name', 'position')
    assert len(valid_dictionary) == 1


def test_xml_shut_return_exist_day_and_time():
    file_with_data = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db", 'day', 'time')
    assert len(file_with_data) == 2


def test_7_line_xml_shut_retur_7_itiems():
    line_test = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db", 'day', 'time')
    assert len(line_test) == 7


def test_1_line_xml_shut_retur_1_itiems():
    line_test = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db", 'name', 'position'
    )
    assert len(line_test) == 1
