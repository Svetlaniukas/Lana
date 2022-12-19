

import mymodule


def work_with_db_xml_staff_shift():
    assert mymodule.NAME == "mymodule"


def test_empty_xml_shut_return_empty_dictionary():
    dict_empty = mymodule.work_with_db_xml_staff_shift("staff_empty_file.txt", 'key_name', 'val_name', 'child')
    assert dict_empty.__iter__('persons', {}) == 0


def test_xml_valid_shut_return_valid_dictionary():
    persons = mymodule.work_with_db_xml_staff_shift("staff_name_surname.xml", 'key_name', 'val_name', 'child')
    assert 2 == len(('persons', {}))


def test_xml_shut_retur_valid_dictionary():
    valid_dictionary = mymodule.work_with_db_xml_staff_shift("staff_position.xml", 'key_name', 'val_name', 'child')
    assert len(('persons', {}))


def test_xml_not_root__should_return_empty_dict():
    dict = mymodule.work_with_db_xml_staff_shift("staff_position.xml", 'key_name', 'val_name', 'child')
    assert dict


def test_3_line_xml_shut_retur_3_itiems():
    line_test = mymodule.work_with_db_xml_staff_shift("staff_name_surname.xml", 'key_name', 'val_name', 'child')
    assert len(('persons', {})) == 2


def test_1_line_xml_shut_retur_1_itiems():
    test_line = mymodule.work_with_db_xml_staff_shift("staff_position.xml", 'key_name', 'val_name', 'child')
    assert test_line.__iter__('persons', {}) == 0
