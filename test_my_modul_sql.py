import mymodule


def work_with_db_sql_lite_staff_shift():
    assert mymodule.NAME == "mymodule"


def test_empty_sql_lite_shut_return_empty_dictionary():
    dict_empty = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db", 'day', 'time_shift')
    assert len(dict_empty) == 0


def test_sql_lite_valid_shut_return_valid_dictionary():
    persons = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db", 'day', 'time_shift')
    assert len(persons) == 6


def test_sql_lite_shut_retur_valid_dictionary():
    valid_dictionary = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db", 'time', 'time_shift')
    assert valid_dictionary(
        'Saturday', '10.am-5.pm') == 'Saturday', '10.am-5.pm'


def test_sql_lite_shut_return_exist_day_and_time():
    file_with_data = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db", 'day', 'time_shift')
    assert file_with_data[0] == 'Monday', '10.am-4.pm'


def test_7_line_sql_lite_shut_retur_7_itiems():
    line_test = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db", 'day', 'time')
    assert len(line_test) == 3


def test_1_line_sql_lite_shut_retur_1_itiems():
    line_test = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db", 'day', 'time_shift'
    )
    assert len(line_test) == 
