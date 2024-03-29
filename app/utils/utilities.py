from datetime import datetime, timedelta


class SimpleDict(dict):
    """dot.notation access to dictionary attributes"""
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __getattr__(*args):
        val = dict.get(*args)
        return SimpleDict(val) if type(val) is dict else val


def get_interval_by_string(timeframe):
    # timeframes = ['1M', '1w', '3d', '1d', '12h', '8h', '6h', '4h', '2h', '1h', '30m', '15m', '5m', '3m', '1m']
    interval_digit = timeframe[0: len(timeframe) - 1]
    interval_period = timeframe[len(timeframe) - 1: len(timeframe)]

    periods = {
        'm': 60,
        'h': 3600,  # 60 * 60
        'd': 86400,  # 24 * 60 * 60
        'w': 604800,  # 7 * 24 * 60 * 60,
        'M': 2592000,  # 30 * 24 * 60 * 60,
    }
    time_multiplier = periods[interval_period]
    return int(interval_digit) * time_multiplier


def get_interval(timeframe, end_time=None):
    if end_time is None:
        end_time = datetime.now()
    interval = get_interval_by_string(timeframe)
    start_time = end_time - timedelta(seconds=interval)
    return start_time, end_time
