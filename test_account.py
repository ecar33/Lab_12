from account import *

def main():
    test_account = Account("Steve Jobs")
    test_account.deposit(6.3333333)
    print(test_account.get_name())
    print(test_account.get_balance())




if __name__ == "__main__":
    main()