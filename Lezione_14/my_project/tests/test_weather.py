from my_project.weather import check_weather
import pytest

'''#passed

def test_check_weater():
    assert check_weather(21.00) == "hot", 'temperatures greater than 20 degree \ must be considered as hot'



from my_project.weather import check_weather
# failed
def test_check_weather():
    assert check_weather(5.00) == "average", 'temperatures between 10 and 20 degree \
must be considered as average temperature'



from my_project.weather import check_weather
# failed
def test_check_weather():
    assert check_weather(5.00) == "average", 'temperatures between 10 and 20 degree \
must be considered as average temperature'
'''

'''from my_project.weather import check_weather

#passed
def test_chech_weather1():
    assert check_weather(21.00) == "hot", 'temperatures greater than 20 degree must be considered as hot'

#faild
def test_check_weather2():
    assert check_weather(5.00) == "average", 'temperatures between 10 and 20 degree must be considered as average temperature'

#passed
def test_check_weather3():
    assert check_weather(5.00) == "cold", 'temperatures lower than 10 degree must be considered as cold'

#passed
def test_check_weather4():
    assert check_weather(13.00) == "averege", 'temperatures beatween 10 and 20 degree must be considered as averege'''
'''
@pytest.mark.parametrize("temperature, expected", [
    (21.00, "hot"),
    (13.00, "average"),
    (0.00, "cold"),
    (15.00, "cold")
])
def test_check_weather(temperature, expected):
    assert check_weather(temperature) == expected'''



@pytest.mark.parametrize("temperature, expected", [
    (21.00, "hot"),
    (13.00, "average"),
    (0.00, "cold"),
    (15.00, "cold")
])
def test_check_weather(temperature, expected):
    assert check_weather(temperature) == expected
    ae: str = ""
    if temperature > 20:
        ae = 'temperatures greater than 20 degree must be considered as hot'
    elif 10 < temperature <= 20:
        ae = 'temperature within 10 and 20 defree must be considered as averege temperature'
    else:
        ae = 'temperature within 10 and 20 degree must be considered as averege temperature'
    assert check_weather(temperature) == expected, ae
