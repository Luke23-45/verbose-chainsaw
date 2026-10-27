from data_extract.config import fiscal_year_map, reporting_institution


def test_fy_mapping_covers_six_years():
    assert len(fiscal_year_map()) == 6
    assert fiscal_year_map()["FY2079-80"]["ad"] == "2022/23"


def test_merger_transition_flag():
    name, transition = reporting_institution("GBIME", "FY2079-80")
    assert transition is True
    assert reporting_institution("NMB", "FY2079-80")[1] is False
    assert reporting_institution("NIMB", "FY2076-77")[0] == (
        "Nepal Investment Bank Limited"
    )
    assert reporting_institution("NIMB", "FY2081-82")[0] == (
        "Nepal Investment Mega Bank Limited"
    )
