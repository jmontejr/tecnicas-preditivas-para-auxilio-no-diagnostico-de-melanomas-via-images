"""Module providing helper datetime functions."""

from datetime import datetime, timedelta, timezone


def get_current_datetime_with_timezone(timezone_hours=0) -> datetime:
    """
        Get the current datetime with timezone

        :param int timezone_hours: the timezone hours
        :return: the current datetime with the timezone
        :rtype: datetime
    """
    define_timezone = timezone(timedelta(hours=timezone_hours))
    current_datetime = datetime.now().astimezone(define_timezone)
    return current_datetime

def get_formatted_datetime(custom_format=None, timezone_hours=0):
    """
        Get datetime with a custom format

        :param custom_format: the custom format to apply in datetime
        :type custom_format: str or None
        :param int timezone_hours: the timezone hours
        :returns: the datetime with timezone formatted
        :rtype: str
    """
    current_datetime = get_current_datetime_with_timezone(timezone_hours)
    if custom_format:
        return current_datetime.strftime(custom_format)
    return current_datetime.strftime("%Y-%m-%d %H:%M:%S.%f %Z")

def get_formatted_total_runtime(date_start, date_end):
    """
        Get total formatted runtime from difference between two datetimes


        :param float date_start: the datetime start in float seconds
        :param float date_end: the datetime end in float seconds
        :returns: the total runtime obtained from difference between date_start and date_end
        :rtype: str
    """
    return str(timedelta(seconds=date_end - date_start))
