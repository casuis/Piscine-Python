import sys


def main():
    user_input = ""
    buff = ",.!?:;()[]{}<>_-\"'`/\\@#$%^&*~+=|"
    try:
        if len(sys.argv) == 1:
            user_input = input("Please provide a string: > ")
            assert user_input
        else:
            user_input = sys.argv[1]
    except EOFError:
        return
    except Exception:
        raise AssertionError("TBD")
    upper_case = sum(1 for c in user_input if c.isupper())
    lower_case = sum(1 for c in user_input if c.islower())
    space = sum(1 for c in user_input if c.isspace())
    ponct = sum(1 for c in user_input if c in buff)
    digit = sum(1 for c in user_input if c.isdigit())
    print(upper_case, "upper letters")
    print(lower_case, "lower letters")
    print(ponct, "punctuation marks")
    print(space, "spaces")
    print(digit, "digits")
    return


if __name__ == "__main__":
    main()
