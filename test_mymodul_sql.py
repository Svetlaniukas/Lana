import mymodule


def work_with_db_jsql_staff_shift():
    assert mymodule.NAME == "mymodule"


def test_empty_sql_shut_return_empty_dictionary():
    test_empty_sql = mymodule.work_with_sql_lite_db_files(
        "shift.db",
        'time_table'
        'day'
        'time'
    )
    assert len(test_empty_sql) == 7


def test_not_empty_sql_shut_retur_not_emthy_dictionary():
    staff_shift = mymodule. work_with_sql_lite_db_files(
        "staff_shift.db",
        'time_table',
        'User_id',
        'day'
    )
    assert staff_shift("SELECT * FROM time_table") == 7


def test_sql_valid_shut_return_valid_dictionary():
    persons = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db",
        'staff_name_surname',
        'Name',
        'Surname'
    )
    assert persons['Denis'] == 'Petrov'
    assert persons['Tania'] == 'Bal'
    assert persons['Lana'] == 'Mel'


def test_sql_shut_retur_valid_dictionary():
    staff = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db",
        'staff_position',
        'Name',
        'Position'
    )
    assert staff["Tomas"] == 'Web-Developer'


def test_sql_have_to_return_empty_dict():
    test_sql_have_to_return = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db",
        'time_table',
        'day',
        'time_shift'
        )
    assert len(test_sql_have_to_return) == 7


def test_3_line_in_sql_dict():
    test_3_line = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db",
        'staff_name_surname',
        'Name',
        'Surname'
        )
    assert len(test_3_line) == 3


def test_sql_have_to_return_1_key():
    test_sql = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db",
        'staff_position',
        'Name',
        'Position'
    )
    assert len(test_sql) == 1
