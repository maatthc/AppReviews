expected = 'Semaphore'

def capital_case(x):
    return x.capitalize()

def capital_case_wrong(x):
    return x

def test_capital_case():
    assert capital_case('semaphore') == expected

def test_capital_case_wrong():
    assert capital_case_wrong('semaphore') != expected

