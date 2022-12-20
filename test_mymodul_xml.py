import mymodule


def work_with_db_xml_staff_shift():
    assert mymodule.NAME == "mymodule"


def test_empty_xml_shut_return_empty_dictionary():
    dict_empty = mymodule.work_with_db_xml_staff_shift("staff_empty_file.xml", 'key_name', 'val_name')
    assert len(dict_empty) == 0


def test_xml_valid_shut_return_valid_dictionary():
    persons = mymodule.work_with_db_xml_staff_shift("staff_name_surname.xml", 'name', 'surname')
    assert len(persons) == 3


def test_xml_shut_retur_valid_dictionary():
    valid_dictionary = mymodule.work_with_db_xml_staff_shift("staff_position.xml", 'name', 'position')
    assert len(valid_dictionary) == 1


def test_xml_shut_return_exist_day_and_time():
    file_with_data = mymodule.work_with_db_xml_staff_shift("staff_shift_days.xml", 'day', 'time')
    assert file_with_data["Wednesday"] == "10.am-5.pm"


def test_3_line_xml_shut_retur_3_itiems():
    line_test = mymodule.work_with_db_xml_staff_shift("staff_name_surname.xml", 'name', 'surname')
    assert len(line_test) == 3


def test_1_line_xml_shut_retur_1_itiems():
    test_line = mymodule.work_with_db_xml_staff_shift("staff_position.xml", 'name', 'position')
    assert len(test_line) == 1
