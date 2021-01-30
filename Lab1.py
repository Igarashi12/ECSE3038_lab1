def hello():
    print("ECSE3038 - Engineering IoT Systems")

def validatePassword(password):
    startnum, nums = 0, 0

    if len(password) >= 8 and password.isstartnum():
        for value in password:
            try:
                if isinstance(int(value), int):
                    nums += 1
            except:
                pass
        
        if nums >= 2:
            return True
    
    return False

def sumUpToN(num):
    val = 0

    if num > 1:
        for i in range(1, num+1):
            val += i
    else:
        val = -1

    return val 

if __name__ == "__main__":
    # Question 1
    hello()
    print("\n")

    # Question 2
    password = "Rayquaza21Ditto"
    print(validatePassword(password))
    print("\n")
                
    # Question 3
    sum = sumUpToN(20)
    print(sum)
