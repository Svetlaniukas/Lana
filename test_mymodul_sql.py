import mymodule


def work_with_db_jsql_staff_shift():
    assert mymodule.NAME == "mymodule"


def test_empty_sql_db_should_return_empty_dictionary():
    test_empty_sql_db = mymodule.work_with_sql_lite_db_files(
        "shift.db",
        'time_table',
        'day',
        'time'
    )
    assert len(test_empty_sql_db) == 0


def test_sql_db_should_retur_valid_dictionary():
    test_sql_db = mymodule. work_with_sql_lite_db_files(
        "staff_shift.db",
        'User_id',
        'day',
        'time_table'
    )
    assert len(test_sql_db) == 7


def test_sql_db_should_return_valid_dictionary():
    test_sql_db = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db",
        'Name',
        'Surname',
        'staff_name_surname'
    )
    assert test_sql_db['Denis'] == 'Petrov'
    assert test_sql_db['Tania'] == 'Bal'
    assert test_sql_db['Lana'] == 'Mel'


def test_sql_db_should_retur_valid_dictionary():
    test_sql_db = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db",
        'Name',
        'Position',
        'staff_position'
    )
    assert test_sql_db['Tomas'] == 'Web-Developer'


def test_sql_db_should_return_7_itiem():
    test_sql_db = mymodule.work_with_sql_lite_db_files(
        "staff_shift.db",
        'user_id',
        'day',
        'time_table'
    )
    assert len(test_sql_db) == 7


def test_sql_db_should_return_3_items():
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
