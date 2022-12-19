import mymodule


def work_with_db_xml_staff_shift():
    assert mymodule.NAME == "mymodule"


def test_empty_xml_shut_return_empty_dictionary():
    dict_empty = mymodule.work_with_db_xml_staff_shift("staff_empty_file.txt", 'key_name', 'val_name')
    assert dict_empty({}) == 0
    assert dict_empty


def test_xml_valid_shut_return_valid_dictionary():
    persons = mymodule.work_with_db_xml_staff_shift("staff_name_surname.xml", 'key_name', 'val_name')
    assert 2 == len(('persons', {"Denis", "Petrov"}))
    assert persons


def test_xml_shut_retur_valid_dictionary():
    valid_dictionary = mymodule.work_with_db_xml_staff_shift("staff_position.xml", 'key_name', 'val_name')
    assert len(('persons', {"Tomas", "web developer"}))
    assert valid_dictionary


def test_xml_root_should_return_dict():
    dict = mymodule.work_with_db_xml_staff_shift("staff_position.xml", 'key_name', 'val_name')
    assert len(('persons', {"Tomas", "web developer"}))
    assert dict


def test_3_line_xml_shut_retur_3_itiems():
    line_test = mymodule.work_with_db_xml_staff_shift("staff_name_surname.xml", 'key_name', 'val_name')
    assert len(('persons', 'name ', {"Denis",
                                     "Tania",
                                     "Lana", })) == 3
    assert line_test


def test_1_line_xml_shut_retur_1_itiems():
    test_line = mymodule.work_with_db_xml_staff_shift("staff_position.xml", 'key_name', 'val_name')
    assert len(({"web developer"})) == 1
    assert test_line
