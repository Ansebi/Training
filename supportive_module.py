def factorize(n):
    if n<0:
        print()
        print("error: works with positive input only!")
        print()
    global results
    i=0
    divisor=2
    results=[]
    while n>1:
        if n%divisor==0:
            results.append(divisor)            
            n=n/divisor
            divisor=2
        else:
            divisor+=1
    factorize.results=results

def crossout(a,b):
    if a==b:
        a,b=[1],[1]
    else:
        a_count=0
        while a_count in range(len(a)):
            switch=0
            b_count=0
            while b_count in range(len(b)):            
                if b[b_count]==a[a_count]:            
                    del b[b_count]
                    b_count=len(b)+1
                    del a[a_count]
                    switch=1
                else:
                    b_count+=1
            if switch==0:
                a_count+=1
            if a==[]:
                a=[1]
            if b==[]:
                b=[1]

    c=1
    for i in a:
        c=c*i
    a=c
    c=1
    for i in b:
        c=c*i
    b=c
    #for the external use    
    crossout.top,crossout.bottom=a,b
    #end for the external use

    

def fraction_simplifier(numerator,denominator):
    
    n=numerator
    factorize(n)
    factorized_numerator=results
    n=denominator
    factorize(n)
    factorized_denominator=results

    crossout(factorized_numerator,factorized_denominator)

    #for the external use
    if crossout.bottom==1:
        fraction_simplifier.output=str(crossout.top)
    else:
        fraction_simplifier.output=str(crossout.top)+"/"+str(crossout.bottom)
    #end for the external use 


def quadratics_composer():
    total_set=[]
    counter=0
    for a in range(-10,10):
        for b in range(-13,13):
            for c in range(-100,100):
                D=b**2-4*a*c
                if D>=0:
                    r2D=D**0.5
                    try:
                        x1=(-b+r2D)/(2*a)
                    except:
                        pass
                    if x1%1==0:
                        try:
                            x2=(-b-r2D)/(2*a)
                        except:
                            pass
                        if x2%1==0:
                            counter+=1
                            particular_set=[]
                            particular_set.append(a)
                            particular_set.append(b)
                            particular_set.append(c)
                            particular_set.append(int(x1))
                            particular_set.append(int(x2))
                            total_set.append(particular_set)

    quadratics_composer.total_set=total_set


                
                
