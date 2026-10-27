from data_extract.normalize import parse_number, to_npr
from data_extract.parsers.per_share import bvps, eps, roa_percent
from data_extract.validate import check_identity


def test_to_npr_thousands():
    assert to_npr(123, "NPR '000") == 123_000
    assert to_npr(123, "NPR") == 123


def test_parse_number_parentheses_and_dash():
    assert parse_number("(1,234)") == -1234
    assert parse_number("-") is None
    assert parse_number("") is None


def test_derived_variables():
    assert eps(1_000_000, 100_000) == 10
    assert bvps(2_000_000, 100_000) == 20
    assert roa_percent(100, 900, 1_100) == 10  # avg assets 1,000


def test_identity():
    # Toy numbers need zero tolerance; the default 1m NPR tolerance is
    # for rounding in real published statements, not for unit tests.
    assert check_identity(100, 60, 40, tolerance_npr=0) is None
    assert check_identity(100, 60, 30, tolerance_npr=0) is not None
