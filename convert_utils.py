def temperature(c):
    f = float(((9 / 5) * c) + 32)
    return str(f) + '°F'

def hours_seconds(hh):
    ss = hh * 60 * 60
    return str(ss) + ' секунд.'


def hours_minutes(hh):
    mm = hh * 60
    return str(mm) + ' минут.'


def hours_days(hh):
    dd = hh * 60
    return str(dd) + ' дней.'


def days_hours(dd):
    hh = dd / 60
    return str(hh) + ' часов.'


def days_minutes(dd):
    mm = dd * 24 * 60
    return str(mm) + ' минут.'