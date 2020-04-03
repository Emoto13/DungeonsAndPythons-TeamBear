class VerificationMixin:

    def verify_value(self, value):
        if value < 0:
            raise ValueError("Value should not be negative")

    def verify_health(self, health):
        if health <= 0:
            raise ValueError("Health should be above 0")

    def verify_if_more_than_max(self, value, max_value):
        if value > max_value:
            value = max_value
        return value
