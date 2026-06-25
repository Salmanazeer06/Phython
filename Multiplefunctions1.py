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

    def Elegible():
        age=int(input("Your age:"))
        gender=input("Your gender:")
        if (gender=="male" and age>=21):
            print("Eligible")
        elif (gender=="female" and age>=18):
            print("Eligible")
        else:
            print("Not Eligible")

    def percentage():
        Subject1=int(input("subject 1="))
        Subject2=int(input("subject 2="))
        Subject3=int(input("subject 3="))
        Subject4=int(input("subject 4="))
        Subject5=int(input("subject 5="))
        Total=(Subject1 + Subject2 + Subject3 + Subject4 + Subject5)
        Percentage=((Total / 500)*100)
        print("Total :", Total)
        print("Percentage :", Percentage)

    def triangle():
        Height=int(input("height="))
        Breadth=int(input("breadth="))
        AreaOfTriangle=(Height*Breadth)/2
        Height1=int(input("height1="))
        Height2=int(input("height2="))
        Breadth=int(input("breadth="))
        PerimeterOfTriangle=Height1+Height2+Breadth
        print("Area Of Triangle:", AreaOfTriangle)
        print("Perimeter Of Triangle:", PerimeterOfTriangle)

        