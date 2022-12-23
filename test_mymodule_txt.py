import mymodule


def test_modul_name_is_valid():
    assert mymodule.NAME == "mymodule"


def test_empty_file_shut_return_empty_dictionary():
    dict_empty = mymodule.open_staff_file(
        "test_function/staff_empty_file.txt", ':')
    assert len(dict_empty) == 0


def test_not_emthy_file_shut_retur_not_emthy_dictionary():
    file_with_data = mymodule.open_staff_file("staff_week_day.txt", ':')
    assert file_with_data['Wednesday'] == '10.am-5.pm\n'


def test_delimiter_comma_shut_retur_valid_dictionary():
    persons = mymodule.open_staff_file(
        "test_function/staff_name_surname.txt", ','
        )
    assert persons.get("Denis") == "Petrov\n"
    assert persons.get("Tania") == "Bal\n"
    assert persons.get("Lana") == "Mel"


def test_delimiter_slash_shut_retur_valid_dictionary():
    valid_dictionary = mymodule.open_staff_file(
        "test_function/staff_position.txt", '/'
        )
    assert valid_dictionary['Tomas'] == 'web developer'


def test_not_valid_delimiter_shud_trow_error():
    dict = mymodule.open_staff_file("test_function/staff_position.txt", ':::')
    assert len(dict) == 0


def test_3_line_file_shut_retur_3_itiems():
    line_test = mymodule.open_staff_file(
        "test_function/staff_name_surname.txt", ',')
    assert len(line_test) == 3


def test_1_line_file_shut_retur_1_itiems():
    test_1_line = len(mymodule.open_staff_file(
        "test_function/staff_position.txt", '/')
                      )
    assert test_1_line == 1
