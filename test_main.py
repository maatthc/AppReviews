def capital_case(x):
    return x.capitalize()

def capital_case_wrong(x):
    return x

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'
