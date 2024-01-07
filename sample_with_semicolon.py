import math;

def fibo(i){
    global fibo_pre, fibo_after;
    if i == 0{
        return 0;
}
    elif i == 1{
        return 1;
}
    else{
        result = fibo_pre + fibo_after;
        fibo_pre, fibo_after = fibo_after, fibo_after + fibo_pre;
        return result;
    }
}

def facto(i){
    global factorial;
    if i == 0:
        return 1;
    else:
        factorial = factorial * i;
        return factorial;
}

def calculate_gcd(a, b){
    return gcd(a, b);
}


num = 20;
fibo_pre = 0;
fibo_after = 1;
factorial = 1;

with open('data.txt', 'a') as file{
    for i in range(0, num + 1){
        fibo_i = fibo(i);
        facto_i = facto(i);
        #gcd_i = calculate_gcd(fibo_i, facto_i);
        row = str(i) + " " + str(fibo_i) + " " + str(facto_i) + '\n';
        print(row);
        file.write(row);
    }
}


