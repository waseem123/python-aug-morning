def demo(n):
    if n>0:
        print(f'helloWorld - {n}')
        demo(n-1)
    
demo(5)