import pendulum


def format_datetime(dt_str: str) -> str:
    dt = pendulum.parse(dt_str)
    return dt.format("DD MMMM YYYY, HH:mm", locale="ru")
