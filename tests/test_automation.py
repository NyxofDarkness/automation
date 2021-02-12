from automation.automation import clean_it_up


def test_phone_clean():

    assert clean_it_up("123-1234") == "206-123-1234"
    assert clean_it_up("(305)206-3456") == "305-206-3456"
    assert clean_it_up("206.456.4567") == "206-456-4567"
    assert clean_it_up(123-2345) == "206-123-2345"
