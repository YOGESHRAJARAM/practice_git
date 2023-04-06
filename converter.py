print(" this program is used to find the number of laber required ")
def find_persion():
   import math

   P1=int(input("Enter the number of person required for the day one : "))
   H1=int(input("Number of hours in day one : "))
   D1=int(input("Number of days required for day one : "))
   W1=int(input("Number of work done : "))
   print(" Thank you for your Inputs and please give some detailes about  day two requirement")
   H2=int(input("Number of working hours : "))
   D2=int(input("number of days  : "))
   W2=int(input("number of work : "))
   pro1=(P1*H1*D1)/(H2*D2)
   pro2=W1/W2
   pro3=pro1/pro2
   result=pro3
   print("the number of person required is :",result)
find_persion()


   
   
