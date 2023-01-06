import mymodule


def work_with_db_jsql_staff_shift():
    assert mymodule.NAME == "mymodule"


def test_empty_sql_shut_return_empty_dictionary():
    dict_empty = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db",
        'time_table',
        'day',
        'time_shift'
    )
    assert len(dict_empty) == 0


def test_not_empty_sql_shut_retur_not_emthy_dictionary():
    staff_shift = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db",
        'time_table',
        'day',
        'time_shift'
    )
    assert len(staff_shift) == 7


def test_sql_valid_shut_return_valid_dictionary():
    persons = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db",
        'staff_name_surname',
        'name',
        "surname"
    )
    assert persons['Denis'] == 'Petrov'
    assert persons['Tania'] == 'Bal'
    assert persons['Lana'] == 'Mel'


def test_sql_shut_retur_valid_dictionary():
    valid_dictionary = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db",
        'staff_position',
        'name'
        'position'
        )
    assert len(valid_dictionary) == 1


def test_sql_not_root__should_return_empty_dict():
    dict = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db",
        'time_table',
        'day',
        'time_shift'
    )
    assert len(dict) == 7


def test_3_line_sql_shut_retur_3_itiems():
    line_test = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db",
        'time_table',
        'day',
        'time_shift'
    )
    assert len(line_test) == 3


def test_1_line_sql_shut_retur_1_itiems():
    test_1_line = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db",
        'time_table',
        'day',
        'time_shift'
    )
    assert len(test_1_line) == 1
