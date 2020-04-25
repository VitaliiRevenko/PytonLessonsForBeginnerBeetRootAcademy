# Task 4
#
# def reverse(input_str: str) -> str:
#     """
#     Function returns reversed input string
#     reverse("hello") == "olleh"
#     True
#     reverse("o") == "o"
#     True

# def reverse(input_str: str) -> str:
#     if len(input_str) == 1:
#         return input_str
#     return input_str[-1] + reverse(input_str[:-1])
#
# if __name__ == '__main':
#     assert reverse("hello") == "olleh"
#     assert reverse("o") == "o"


def reverse1(input_str: str) -> str:
    if len(input_str) == 1:
        return "".join(reversed(input_str))
    return "".join(reversed(input_str[-1])) + reverse1(input_str[:-1])


if __name__ == '__main__':
    assert reverse1("hello") == "olleh"
    assert reverse1("o") == "o"

