from datetime import datetime


def convert_unix_dateformat_to_utc(unix_dateformat):
    return datetime.utcfromtimestamp(unix_dateformat).strftime('%Y-%m-%d')
