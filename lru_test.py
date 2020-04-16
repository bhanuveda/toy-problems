from lru_cache import lru

class lru_testclass:

    def __init__(self,capacity,testcases):
        self.lru = lru(capacity)
        self.testcases = testcases
        self.passed = 0

    def test(self):
        print("Testcase : 1")
        string = self.lru.get_cache()
        print(string)
        assert string == "", "Testcase 1 Failed"
        if string == "":
            self.passed += 1
            print("Testcase passed")

        print("Testcase : 2")
        data = self.lru.get(22)
        print(data)
        assert data == None, "Testcase 2 Failed"
        if data == None:
            self.passed += 1
            print("Testcase passed")

        print("Testcase : 3")
        self.lru.put(11)
        self.lru.put(22)
        self.lru.put(33)
        self.lru.put(44)
        data = self.lru.get(33)
        print(data)
        assert data == 33, "Testcase 3 Failed"
        if data == 33:
            self.passed += 1
            print("Testcase passed")

        print("Testcase : 4")
        self.lru.put(55)
        string1 = self.lru.get_cache()
        print(string1)
        assert string1 == "55 33 44 22 11", "Testcase 4 Failed"
        if string1 == "55 33 44 22 11":
            self.passed += 1
            print("Testcase passed")

        print("Testcase : 5")
        self.lru.put(66)
        string1 = self.lru.get_cache()
        print(string1)
        assert string1 == "66 55 33 44 22", "Testcase 5 Failed"
        if string1 == "66 55 33 44 22":
            self.passed += 1
            print("Testcase passed")

        print("Testcase : 6")
        self.lru.put(44)
        string1 = self.lru.get_cache()
        print(string1)
        assert string1 == "44 66 55 33 22", "Testcase 6 Failed"
        if string1 == "44 66 55 33 22":
            self.passed += 1
            print("Testcase passed")

        print("Testcase : 7")
        self.lru.put(88)
        string1 = self.lru.get_cache()
        print(string1)
        assert string1 == "88 44 66 55 33", "Testcase 7 Failed"
        if string1 == "88 44 66 55 33":
            self.passed += 1
            print("Testcase passed")

        print("Test Case : 8")
        self.lru.put(66)
        string1 = self.lru.get_cache()
        print(string1)
        assert string1 == "66 88 44 55 33", "Test Case 8 Failed"
        if string1 == "66 88 44 55 33":
            self.passed += 1
            print("Test Case passed")


def main():
    t = lru_testclass(5, 8)
    print("one")
    t.test()
    print("Great!! All Testcases Passed!!")

if __name__== "__main__":
    main()