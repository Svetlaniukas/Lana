

import mymodule


def work_with_db_json_staff_shift():
    assert mymodule.NAME == "mymodule"


def test_empty_json_shut_return_empty_dictionary():
    dict_empty = mymodule.work_with_db_xml_staff_shift("staff_empty_file.txt", ' child', 'key_name', 'val_name')
    assert len(dict_empty) == 0


def test_xml_valid_shut_return_valid_dictionary():
    persons = mymodule.work_with_db_xml_staff_shift("staff_name_surname.xml", 'val_name')
    assert persons['Denis'] == 'Petrov'
    assert persons['Tania'] == 'Bal'
    assert persons['Lana'] == 'Mel'


def test_xml_shut_retur_valid_dictionary():
    valid_dictionary = mymodule.work_with_db_xml_staff_shift("staff_position.xml", 'val_name')
    assert valid_dictionary['Tomas'] == 'web developer'


def test_xml_not_root__should_return_empty_dict():
    dict = mymodule.work_with_db_xml_staff_shift("staff_position.xml", 'val_name')
    assert dict


def test_3_line_xml_shut_retur_3_itiems():
    line_test = mymodule.work_with_db_xml_staff_shift("staff_name_surname.xml", 'val_name')
    assert len(line_test) == 3


def test_1_line_xml_shut_retur_1_itiems():
    test_line = mymodule.work_with_db_xml_staff_shift("staff_position.xml", 'val_name')
    assert len(test_line) == 1
