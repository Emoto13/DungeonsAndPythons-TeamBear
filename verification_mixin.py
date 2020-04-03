class VerificationMixin:

    def verify_string_value(self, string):
        if not string:
            raise ValueError("Value cannot be an empty string")

    def verify_number_value(self, value):
        if value < 0:
            raise ValueError("Value should not be negative")

    def verify_health(self, health):
        if health <= 0:
            raise ValueError("Health should be above 0")

    def verify_if_more_than_max(self, value, max_value):
        if value > max_value:
            value = max_value
        return value

    def verify_number_attributes(self, *attributes):
        for attribute in attributes:
            self.verify_number_value(attribute)

    def verify_string_values(self, *attributes):
        for attribute in attributes:
            self.verify_string_values(attribute)

    def verify_attributes(self, *attributes):
        dicts = {int: self.verify_number_value,
                 str: self.verify_string_value
                 }

        for attribute in attributes:
            dicts[type(attribute)](attribute)
