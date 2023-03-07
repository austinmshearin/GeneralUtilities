"""
Unit testing of the sql utility package

Notes
-----
The database should be initialized with a test dataset before running pytest  
Table name: ATable  
ATable_PK | INTColumn | STRColumn | BLOBColumn  
----------|-----------|-----------|-----------
1         |1          |"A"        |b"abc"
----------|-----------|-----------|-----------
2         |2          |"B"        |b"def"
----------|-----------|-----------|-----------
3         |3          |"C"        |b"ghi"
----------|-----------|-----------|-----------
"""
# Standard Imports
import pytest

# Local Imports
import App.utils.sql as sql

# Establish SQL client
db = sql.SQL_Client(
    {
        "host": "emu-db.camn5msy5ch2.us-west-2.rds.amazonaws.com",
        "database": "TestDB",
        "user": "admin",
        "password": "8en3TnfBWuVpbtVYGCMF"
    }
)

def test_connection():
    db.connect()
    assert db.connection.open

def test_close_connection():
    db.connect()
    db.disconnect()
    assert not db.connection.open

@pytest.fixture
def query_all():
    return db.query("SELECT * FROM `ATable`")

def test_num_query_all(query_all):
    assert len(query_all) == 3

def test_type_query_all(query_all):
    assert type(query_all[0]) == dict

def test_int_query_all(query_all):
    assert type(query_all[0]["INTColumn"]) == int

def test_str_query_all(query_all):
    assert type(query_all[0]["STRColumn"]) == str

def test_blob_query_all(query_all):
    assert type(query_all[0]["BLOBColumn"]) == bytes

@pytest.fixture
def query_row_one():
    return db.query("SELECT * FROM `ATable` WHERE `ATable_PK` = %s", [1])

def test_row_one_int(query_row_one):
    assert query_row_one[0]["INTColumn"] == 1

def test_row_one_int(query_row_one):
    assert query_row_one[0]["STRColumn"] == "A"

def test_row_one_int(query_row_one):
    assert query_row_one[0]["BLOBColumn"].decode() == "abc"

def test_max_value_int():
    assert db.get_max_value("ATable", "INTColumn") == 3

def test_max_value_str():
    assert db.get_max_value("ATable", "STRColumn") == "C"

def test_get_value_one_where():
    assert db.get_value("ATable", "STRColumn", ["INTColumn"], [2]) == "B"

def test_get_value_two_where():
    assert db.get_value("ATable", "INTColumn", ["ATable_PK", "STRColumn"], [3, "C"]) == 3

def test_upload_one_record():
    db.upload_record(
        "ATable",
        ["INTColumn", "STRColumn", "BLOBColumn"], 
        [[4, "D", "jkl".encode()]]
    )
    assert db.get_value("ATable", "INTColumn", ["STRColumn"], ["D"]) == 4

def test_upload_two_records():
    db.upload_record(
        "ATable",
        ["INTColumn", "STRColumn", "BLOBColumn"], 
        [
            [5, "E", "mno".encode()],
            [6, "F", "pqr".encode()]
        ]
    )
    assert db.query(
        "SELECT `STRColumn` FROM `ATable` WHERE `INTColumn` IN (%s,%s)",
        [5,6]
    ) == [{"STRColumn": "E"}, {"STRColumn": "F"}]

def test_alter_one_record_one_where():
    db.alter_value("ATable", ["INTColumn"], [[4]], ["STRColumn"], [["Z"]])
    assert db.get_value("ATable", "STRColumn", ["INTColumn"], [4]) == "Z"

def test_alter_one_record_two_wheres():
    db.alter_value("ATable", ["INTColumn", "STRColumn"], [[4, "Z"]], ["BLOBColumn"], [["zyx".encode()]])
    assert db.get_value("ATable", "BLOBColumn", ["INTColumn", "STRColumn"], [4, "Z"]).decode() == "zyx"

def test_alter_two_records_one_where():
    db.alter_value("ATable", ["INTColumn"], [[5],[6]], ["STRColumn"], [["Y"], ["X"]])
    assert db.query(
        "SELECT `STRColumn` FROM `ATable` WHERE `INTColumn` IN (%s,%s)",
        [5,6]
    ) == [{"STRColumn": "Y"}, {"STRColumn": "X"}]

def test_alter_two_records_two_wheres():
    db.alter_value("ATable", ["INTColumn", "BLOBColumn"], [[5, "mno".encode()], [6, "pqr".encode()]], ["STRColumn"], [["G"], ["H"]])
    assert db.query(
        "SELECT `STRColumn` FROM `ATable` WHERE `INTColumn` IN (%s,%s)",
        [5,6]
    ) == [{"STRColumn": "G"}, {"STRColumn": "H"}]

def test_exists_one_where():
    assert db.exists("ATable", ["INTColumn"], [4])

def test_exists_two_wheres():
    assert db.exists("ATable", ["INTColumn", "STRColumn"], [5, "G"])

def test_not_exists_one_where():
    assert not db.exists("ATable", ["INTColumn"], [100])

def test_not_exists_two_wheres():
    assert not db.exists("ATable", ["INTColumn", "STRColumn"], [100, "AA"])

def test_delete_one_where():
    db.delete_record("ATable", ["INTColumn"], [4])
    assert len(db.query("SELECT * FROM `ATable`")) == 5

def test_delete_two_wheres():
    db.delete_record("ATable", ["INTColumn", "STRColumn"], [5, "G"])
    db.delete_record("ATable", ["INTColumn", "STRColumn"], [6, "H"])
    assert len(db.query("SELECT * FROM `ATable`")) == 3

def test_connect_then_query():
    db.connect()
    result = db.query("SELECT * FROM `ATable`")
    db.disconnect()
    result2 = db.query("SELECT * FROM `ATable`")
    assert (len(result) == 3) and (len(result2) == 3)
