class SubfieldsInAI():
    def Subfields():
        lists = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for i in lists:
            print(i)
            
    def OddEven():
        num=int(input("Enter the number is:"))
        if ((num%2==0)):
            print(num, "is Even Number")
            
    age=int(input("Your age:"))
    gender=input("Your gender:")
    def Elegible(gender,age):
        if (gender=="male" and age>=21):
            print("Eligible")
        elif (gender=="female" and age>=18):
            print("Eligible")
        else:
            print("Not Eligible")
            
    Subject1 = 98
    Subject2 = 87
    Subject3 = 95
    Subject4 = 95
    Subject5 = 93
    sub=int(input("subject 1="))
    sub=int(input("subject 2="))
    sub=int(input("subject 3="))
    sub=int(input("subject 4="))
    sub=int(input("subject 5="))
    Total=(Subject1 + Subject2 + Subject3 + Subject4 + Subject5)
    Percentage=((Total / 500)*100)
    def percentage():
        print ("Total :", Total)
        print ("Percentage :", Percentage)
    Height=32
    Breadth=34
    AreaOfTriangle=(Height*Breadth)/2
    Height1=2
    Height2=4
    Breadth=4
    PerimeterOfTriangle=Height1+Height2+Breadth
    def triangle():
        print("Area Of Triangle:", AreaOfTriangle)
        print("Perimeter Of Triangle:", PerimeterOfTriangle)
