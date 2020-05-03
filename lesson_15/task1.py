# Task 1
#
# Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email
# , passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.
# Email validations:
#
# https://help.xmatters.com/ondemand/trial/valid_email_format.htm
#
# https://en.wikipedia.org/wiki/Email_address

# Задание 1 Создайте метод класса с именем `validate`, который должен вызываться из метода
# ` __init__` для проверки параметров электронной почты, передаваемой в конструктор. Логика внутри метода
# `validate` может заключаться в проверке, является ли переданный параметр электронной почты допустимой строкой электронной почты.
##############

from validate_email import validate_email
class A:
    def __init__(self, email:str, name:str):
        self.name = name
        self.email = email
    @staticmethod
    def validate_email(email:str) -> str:
        valid = validate_email(email)
        return valid
if __name__ == '__main__':
    if A.validate_email("my+address@mydomain.com"):
        print("Your e-mail is valid")
    else:
        raise "NotValid E-MAIL"
    assert A.validate_email("my+address@mydomain.com") == True





