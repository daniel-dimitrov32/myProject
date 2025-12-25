def task_74():
    n = 0
    s = 0
    m = float('inf')
    
    print("Enter numbers one by one. Enter -1 to finish:")
    
    while (x := float(input())) != -1:
        n += 1
        s += x
        if x < m:
            m = x
            
    if n == 0:
        m = -1
        a = -1
    else:
        a = s / n
        
    print(f"n={n}, s={s}, m={m}, a={a}")
    
    
task_74()


# it looks like I learned how to use git today