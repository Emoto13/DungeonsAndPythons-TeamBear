class VerificationMixin:

    def verify_string_value(self, string: str):
        if not string:
            raise ValueError("Value cannot be an empty string")

    def verify_number_value(self, value: int):
        if value < 0:
            raise ValueError("Value should not be negative")

    def verify_health(self, health: int):
        if health <= 0:
            raise ValueError("Health should be above 0")

    def verify_if_more_than_max(self, value: int, max_value: int):
        if value > max_value:
            value = max_value
        return value

    def verify_attributes(self, *attributes):
        dicts = {int: self.verify_number_value,
                 str: self.verify_string_value
                 }

        for attribute in attributes:
            dicts[type(attribute)](attribute)

    @staticmethod
    def verify_command(dicts: dict, command: str):
        if command not in dicts.keys():
            raise ValueError("No such command. Try again")
