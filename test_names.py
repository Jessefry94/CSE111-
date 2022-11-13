from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    #call to chek if it makes a string
    full = make_full_name("upbeat", "upgrade")
    assert isinstance(full, str), "This should return a string"
    #testing to see if it formats the names correctly
    assert make_full_name("John", "Hatt") == "Hatt; John"
    assert make_full_name("Walter", "Nathanielelll") == "Nathanielelll; Walter"
    assert make_full_name("Lucy", "Kirger-James") == "Kirger-James; Lucy"

#Testing to see if the extract_family_name function works properly.
def test_extract_family_name():
    assert extract_family_name("Hatt; John") == "Hatt"
    assert extract_family_name("Nathanielelll; Walter") == "Nathanielelll"
    assert extract_family_name("Kirger-James; Lucy") == "Kirger-James"
    
#Testing first given name. Name is seperated by a ; 
def test_extract_given_name():
    assert extract_given_name("Hatt; John") == "John"
    assert extract_given_name("Nathanielelll; Walter") == "Walter"
    assert extract_given_name("Kirger-James; Lucy") == "Lucy"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])