import pytest

import mymodule


def test_modul_name_is_valid():
    assert mymodule.NAME == "mymodule"


def test_emthy_file_shut_retur_emthy_dictionary():
    assert not mymodule.open_staff_file("staff_emty_file.txt", ':') == 0


def test_not_emthy_file_shut_retur_not_emthy_dictionary():
    file_with_data = mymodule.open_staff_file("staff_week_day.txt", ':')
    assert file_with_data['Wednesday'] == '10.am-5.pm\n'


def test_delimiter_comma_shut_retur_valid_dictionary():
    persons = mymodule.open_staff_file("staff_name_surname.txt", ',')
    assert persons.get("Denis") == "Petrov\n"
    assert persons.get("Tania") == "Bal\n"
    assert persons.get("Lana") == "Mel"
    print(persons)


def test_delimiter_slash_shut_retur_valid_dictionary():
    valid_dictionary = mymodule.open_staff_file("staff_position.txt", '/')
    assert valid_dictionary['Tomas'] == 'web developer'
    print(valid_dictionary)


def test_not_valid_delimiter_shud_trow_error():
    with pytest.raises(AssertionError):
        assert mymodule.open_staff_file("staff_position.txt", ':::')


def test_3_line_file_shut_retur_3_itiems():
    staff = mymodule.open_staff_file("staff_name_surname.txt", ',')
    assert staff["Denis"] == "Petrov"
    assert len('Denis,Petrov') == 3


def test_1_line_file_shut_retur_1_itiems():
    assert mymodule.open_staff_file("staff_position.txt", '/')
    return 'Tomas :', 'web developer'
