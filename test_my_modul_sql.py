

import mymodule
from my_sql_lite_db import time_table


def work_with_db_sql_lite_staff_shift():
    assert mymodule.NAME == "mymodule"


def test_empty_sql_lite_shut_return_empty_dictionary():
    dict_empty = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db", 'day', 'time_table')
    assert len(dict_empty) == 0


def test_sql_lite_valid_shut_return_valid_dictionary():
    persons = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db", 'day', 'time')
    assert persons(time_table) == len(7)


def test_sql_lite_shut_retur_valid_dictionary():
    valid_dictionary = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db", 'time', 'date')
    assert len(valid_dictionary) == 1


def test_sql_lite_shut_return_exist_day_and_time():
    file_with_data = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db", 'day', 'time')
    assert type(file_with_data) == time_table


def test_7_line_sql_lite_shut_retur_7_itiems():
    line_test = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db", 'day', 'time')
    assert line_test['Monday'] == "10.am-4.pm"


def test_1_line_sql_lite_shut_retur_1_itiems():
    line_test = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db", 'day', 'time'
    )
    assert line_test(time_table) == 7
