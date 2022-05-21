IDno = 1  # ID number of the user
L = []    # MultiDimensional list for storing user data of Borrower Requests
L1 = []   # MultiDimensional list for storing user data of Approved borrower requests with Loan offer by Lender 

class UserInfo:   #Parent class to store user object data    
    
    def __init__(self,name,age,address,mobile,role):
        self.name = name
        self.age = age
        self.address = address
        self.mobile = mobile
        self.role = role
        

    def Role(self):
        if (self.role == "Lender"):
            print("Your data is recorded, now you can add your details and requirments in Lenders class")

        elif(self.role == "Borrower"):
            print("Your data is recorded, now you can add your details and requirments in Borrowers class")
        
        else:
            print("Undefined Role(Select either 'Lender' or 'Borrower')")

        
class Borrowers(UserInfo):        # child class for borrower inheriting from UserInfo class
    def __init__(self,name,age,address,mobile,role):
        super().__init__(name,age,address,mobile,role)      
        global IDno
        self.a = [IDno,self.name,self.age,self.address,self.mobile,self.role]
        IDno += 1

    def Loandetails(self):     # to get loan requirment details
        self.amt = int(input('Enter the Amount(in Rupees)'))
        self.time = int(input('Enter the the time duration(in months)'))
        self.a.append(self.amt)
        self.a.append(self.time)
        global L
        L.append(self.a)
        for i in range(len(L)):
            if (L[i][1]==self.name):
                print(L[i])
                print("You Loan request is registered, your ID number is ",L[i][0],". You can check approval status in services")



class Lenders(UserInfo):       # child class for Lender inheriting from UserInfo class
    def __init__(self,name,age,address,mobile,role):
        super().__init__(name,age,address,mobile,role) 



class Service(Lenders,Borrowers):   # child class for main service providing central authority with multiple inheritance from lender and borrower class
    def __init__(self,name,age,address,mobile,role):
        Lenders.__init__(self,name,age,address,mobile,role)
        Borrowers.__init__(self,name,age,address,mobile,role)

        if(self.role=="Borrower"):
            print("Your Identity is approved. You can check your request approval status")

        elif(self.role=="Lender") :
            print("Your Identity is approved. You can check lending requests and offer money")
            

    def LoanRequests(self):     # for lenders to see current borrower requests
        print("Following are the loan requests")
        for i in range(len(L)):
            for j in range(8):
                print(L[i][j],' ')
            print("\n\n")


    def RequestOffer(self):  # for lender to providing offer to a certain borrow request
        BID = int(input('Enter ID number of whom you are lending loan to: '))
        interest = input("Enter the monthly rate of interest offered: ")
        i = BID - 1
        L[i].append(self.name)
        L[i].append(interest)
        L1.append(L[i])
        del L[i]
        
        
        

    def OfferStatus(self):  # for borrower to check offer status of there request
        BID = int(input('What is your IDno: '))
        for i in range(len(L1)):
            if (L1[i][0] == BID):
                print("Your Loan Request has got an offer !")
                print(L1[i])
                print("Loan is provided by",L1[i][8]," at ",L1[i][9],"% rate of Interest(monthly)")
                appr = input('Do you accept(Y/N): ')
                if (appr == 'Y'):
                    print("Loan approved!")
                    L1[i].append("Approved")
                elif (appr == 'N'):
                    print("Offer rejected")
                    del L1[i][8]
                    del L1[1][9]
                

            else :
                print("Your request hasn't got an offer yet.")
                print("Request made is given below: ")
                for i in range(len(L)):
                    if(L[i][0]== BID):
                        print(L[i])

    def OfferApproval(self):      #for lenders to check if loan offer has been accepted by borrower and approved
        BID = int(input('What is the  IDno of borrower: '))
        for i in range(len(L1)):
            if (L1[i][0] == BID):
                print(L1[i])
            if (len(L1[i])==11):
                print("Offer approved")

            elif(len(L1[i])==10):
                print("Offer response awaited")

            elif(len(L1[i])<10):
                print("Offer rejected")
                
                
                
# This program dosen't have all the technical and feature requirments of a complete loan service(Like database connection for storing data)
# But in the limited time I have tried to cover maximum OOP concepts in the program.

           
        
           


        
