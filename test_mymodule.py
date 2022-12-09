import mymodule


def test_modul_name_is_valid():
    assert mymodule.NAME == "mymodule"


def test_emthy_file_shut_retur_emthy_dictionary():
    assert not mymodule.read_staff_from_file("test_file_week_day.txt", ':')


def test_not_emthy_file_shut_retur_not_emthy_dictionary():
    assert mymodule.read_staff_from_file("staff_week_day.txt", ':')


def test_delimiter_comma_shut_retur_valid_dictionary():
    assert mymodule.read_staff_from_file("staff_name_surname.txt", ',')


def test_delimiter_slash_shut_retur_valid_dictionary():
    assert mymodule.read_staff_from_file("staff_position.txt", '/')


def test_not_valid_delimiter_shud_trow_error():
    assert mymodule.read_staff_from_file("test_file_week_day.txt", '::')


def test_5_line_file_shut_retur_5_itiems():
    assert mymodule.read_staff_from_file("staff_week_day.txt", ':')
    return 'Monday : 10.am-4.pm', 'Tuesday : 9.am-3.pm', 'Wednesday : 10.am-5.pm',\
           'Thursday : 10am-4pm', 'Friday : ' '8am-4pm '


def test_1_line_file_shut_retur_1_itiems():
    assert mymodule.read_staff_from_file("staff_position.txt", '-')
    return 'Tomas :', 'web developer'
