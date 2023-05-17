from datetime import datetime, date


class FloatConverter:
    regex = r'-?\d+(?:\.\d+)?'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)

class DateConverter:
    regex = '\d{4}-\d{1,2}-\d{1,2}'
    format = '%Y-%m-%d'

    def to_python(self, value):
        return datetime.strptime(value, self.format).date()

    def to_url(self, value):
        return value.strftime(self.format)