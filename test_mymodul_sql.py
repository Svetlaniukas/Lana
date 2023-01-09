import mymodule


def work_with_db_jsql_staff_shift():
    assert mymodule.NAME == "mymodule"


def test_empty_sql_file_should_return_empty_dictionary():
    test_empty_sql = mymodule.work_with_sql_lite_db_files(
        "shift.db",
        'time_table',
        'day',
        'time'
    )
    assert len(test_empty_sql) == 0


def test_sql_file_retur_not_emthy_dictionary():
    test_sql_file = mymodule. work_with_sql_lite_db_files(
        "staff_shift.db",
        'User_id',
        'day',
        'time_table'
    )
    assert len(test_sql_file) == 7


def test_sql_valid_file_shut_return_valid_dictionary():
    test_sql_valid_file = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db",
        'Name',
        'Surname',
        'staff_name_surname'
    )
    assert test_sql_valid_file['Denis'] == 'Petrov'
    assert test_sql_valid_file['Tania'] == 'Bal'
    assert test_sql_valid_file['Lana'] == 'Mel'


def test_sql_shut_retur_valid_dictionary():
    staff = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db",
        'Name',
        'Position',
        'staff_position',
    )
    assert staff["Tomas"] == 'Web-Developer'


def test_sql_db_should_return_7_itiem():
    test_sql_db = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db",
        'user_id',
        'day',
        'time_table'
    )
    assert len(test_sql_db) == 7


def test_sql_db_file_should_return_3_items():
    test_sql_db = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db",
        'Name',
        'Surname',
        'staff_name_surname'
    )
    assert len(test_sql_db) == 3


def test_sql_db_should_return_1_itiem():
    test_sql_db = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db",
        'Name',
        'Position',
        'staff_position'
    )
    assert len(test_sql_db) == 1
