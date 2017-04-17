import datetime
from django.utils import timezone


def get_datetime_django(date_tuple):
    date = date_tuple[:3][::-1]
    if all(date_tuple[3:]):
        date += date_tuple[3:5]  # append time
    return timezone.make_aware(datetime.datetime(*[int(d) for d in date]))
