class Multifunctions():
    def oddEven():
        num=int(input("Enter the number:"))
        if(num%2==0):
            print("even number")
            message="even number"
        else:
            print("ODD number")
            message="ODD number"
        return message 
    def BMI():
        bmi=int(input("Enter the BMI Index:"))
        if(bmi<18.5):
            print("Underweight")
            message="Underweight"
        elif(bmi<24.9):  
            print("Normal")
            message="Normal"
        elif(bmi<29.9):
            print("Overweight")
            message="Overweight"
        elif(bmi<30):
            print("Obese")
            message="Obese"
        else:
            print("Very Overweight")
            message="Very Overweight"
        return message
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gender=="Male" and age==21):
            print("ELIGIBLE")
        elif(gender=="Female" and age==18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
    def percentage():
        sub1=float(input("Subject1="))
        sub2=float(input("Subject2="))
        sub3=float(input("Subject3="))
        sub4=float(input("Subject4="))
        sub5=float(input("Subject5="))
        add=sub1+sub2+sub3+sub4+sub5
        print("Total:", add)
        percentage = (add / 500.0) * 100
        print("Percentage :", percentage)
        
    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        AF=(Height*Breadth)/2
        print("Area of Triangle:", AF)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        PF=Height1+Height2+Breadth
        print("Perimeter of Triangle:",PF)    