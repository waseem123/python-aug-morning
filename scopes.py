def printdata():
    global data
    global demo
    data = 140
    print(data)
    
    def demo():
        print('THIS IS A DEMO FUNCTION')

    demo()


printdata()
print(data)
demo()