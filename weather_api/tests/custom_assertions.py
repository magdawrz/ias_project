def assert_current_weather(current_weather):
    assert 'temperature' in current_weather
    assert 'win_speed' in current_weather
    assert 'pressure' in current_weather
    assert 'humidity' in current_weather
    assert 'time' in current_weather
