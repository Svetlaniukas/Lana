import pytest

import mymodule


def test_modul_name_is_valid():
    assert mymodule.NAME == "mymodule"


def test_emthy_file_shut_retur_emthy_dictionary():
    assert not mymodule.open_staff_file("staff_emty_file.txt", ':')


def test_not_emthy_file_shut_retur_not_emthy_dictionary():
    week_day = mymodule.open_staff_file("staff_week_day.txt", ':')

    for first_name, last_name in week_day.items():
        print(last_name + " : " + last_name)

        assert week_day["Wednesday"] == "10.am-5.pm\n"


def test_delimiter_comma_shut_retur_valid_dictionary():
        persons = mymodule.open_staff_file("staff_name_surname.txt", ',')
        assert persons.get("Denis") == "Petrov"
        assert persons.get("Tania") == "Bal"
        assert persons.get("Lana") == "Mel"


def test_delimiter_slash_shut_retur_valid_dictionary():
    assert mymodule.open_staff_file("staff_position.txt", '/')


def test_not_valid_delimiter_shud_trow_error():
    with pytest.raises(AssertionError):
        assert not mymodule.open_staff_file("staff_week_day.txt", '::')


def test_5_line_file_shut_retur_5_itiems():
    staff = mymodule.open_staff_file("staff_name_surname.txt", ',')

    for first_name, last_name in staff():
        print([first_name + "," + last_name])

        assert staff("Denis") == "Petrov"


def test_1_line_file_shut_retur_1_itiems():
    assert mymodule.open_staff_file("staff_position.txt", '/')
    return 'Tomas :', 'web developer'
