from Outdated import formatedText, checkPattern, datebyPattern1, datebyPattern2, datebyPattern3

def main():
    test_formatText()
    test_checkPattern()
    test_datebyPattern1()
    test_datebyPattern2()
    test_datebyPattern3()

def test_formatText():
    assert formatedText("January 15, 2015  ") == "january 15, 2015"
    assert formatedText("15 JANUARY 2015") == "15 january 2015"
    assert formatedText("  15.01.2015  ") == "15.01.2015"
    assert formatedText("  15/01/2015  ") == "15/01/2015"
    assert formatedText("  15-01-2015  ") == "15-01-2015"

def test_checkPattern():
    assert checkPattern("01.01.2025") == 1
    assert checkPattern("01/01/2025") == 1
    assert checkPattern("01-01-2025") == 1
    assert checkPattern("01.25.2025") == False
    assert checkPattern("1.1.2025") == 1
    assert checkPattern("15.1.2025") == 1
    assert checkPattern("15.12.2025") == 1
    assert checkPattern("december 12. 2025") == 2
    assert checkPattern("december 2, 2025") == 2
    assert checkPattern("2 dec 2025") == 3
    assert checkPattern("02 dec 2025") == 3
    assert checkPattern("02 december 2025") == 3

def test_datebyPattern1():
    assert datebyPattern1("01.01.2025") == "2025-01-01"
    assert datebyPattern1("01/01/2025") == "2025-01-01"
    assert datebyPattern1("01-01-2025") == "2025-01-01"
    assert datebyPattern1("1.1.2025") == "2025-01-01"
    assert datebyPattern1("15.1.2025") == "2025-01-15"
    assert datebyPattern1("15.12.2025") == "2025-12-15"

def test_datebyPattern2():
    assert datebyPattern2("january 1. 2025") == "2025-01-01"
    assert datebyPattern2("february 14, 1955") == "1955-02-14"
    assert datebyPattern2("march 05. 1988") == "1988-03-05"
    assert datebyPattern2("march 05  1988") == "1988-03-05"
    assert datebyPattern2("march 5 1988") == "1988-03-05"

def test_datebyPattern3():
    assert datebyPattern3("01.jan.2025") == "2025-01-01"
    assert datebyPattern3("01/january/2025") == "2025-01-01"
    assert datebyPattern3("01 january 2025") == "2025-01-01"
    assert datebyPattern3("1 jan 2025") == "2025-01-01"
    assert datebyPattern3("15-jan-2025") == "2025-01-15"
    assert datebyPattern3("15/december/2025") == "2025-12-15"

if __name__ == "__main__":
    main()
