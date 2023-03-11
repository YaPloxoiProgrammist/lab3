def bracket_check(test_string):
    if (len(test_string)) % 2 != 0 :
        return print("HET")
    if (len(test_string)) != 0:
        if test_string[len(test_string)-1] == "(":
            return print("НЕТ")
        else:
            tester = 0
            for i in range(len(test_string)):
                if test_string[i] == "(":
                    tester = tester + 1
                if test_string[i] == ")":
                    tester = tester - 1
                if tester < 0:
                    return print("НЕТ")
            a = test_string.count("(")
            b = test_string.count(")")
            test_string = test_string.replace("(", "", 1)
            test_string = test_string.replace(")", "", 1)
            print("( = ", a)
            print(") = ", b)
            if a == b:
                return print("Правильная последовательность")
            else:
                return print("HET")
    else:
        return print("HET")
ABSHDA = input()
bracket_check(ABSHDA)