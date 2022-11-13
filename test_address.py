from address import extract_city, \
    extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("3505 Queen Ann Drive, Clayton, NC 27527") == "Clayton"
    assert extract_city("111 Parkway Rd, Dallas, TX 19284")


def test_extract_state():
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("3505 Queen Ann Drive, Clayton, NC 27527") == "NC"
    assert extract_state("111 Parkway Rd, Dallas, TX 19284") == "TX"


def test_extract_zipcode():
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
    assert extract_zipcode("3505 Queen Ann Drive, Clayton, NC 27527") == "27527"
    assert extract_zipcode("111 Parkway Rd, Dallas, TX 19284") == "19284"
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])