import random
import time
operators=["+","-","*"]
min_operator=3
max_operator=12
total_problems=10
def generate_problem():
    left=random.randint(min_operator,max_operator)
    right=random.randint(min_operator,max_operator)
    Operator=random.choice(operators)
    expr=str(left)+" "+Operator+" "+str(right)
    answer=eval(expr)
    return expr,answer
wrong=0 
input("press enter and start")
start_time=time.time()
for i in range(total_problems):
    expr,answer=generate_problem()
    while True:
         guess=input("problem #" + str(i+1)+ ":"+expr+"=")
         if guess==str(answer):
             break
         wrong+=1
end_time=time.time()
total_time=end_time-start_time
print("nice work! you finished in", total_time,"seconds")





