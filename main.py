import pandas
class StudyGuide():
    def __init__(self):
        #Activities: Training, Networking, Company knowledge,Current Events, General
        self.activity=""
        #Description:
        self.description=""
        #Brief:Goals, people met, introduced to
        self.goal=""
        #Dependency:
        self.dependency=""
        #Anything blocking to achieve this goal
        self.blockers=""
        self.LisAct= {}
        #Loads Activities
        try:
            FileAct=open("activities.txt")
        except expression as identifier:
            print(identifier)
        Acts=FileAct.read()
        FileAct.close()
        Acts=Acts.split(",")
        i=0
        for act in Acts:
            self.LisAct[str(i)]=act.strip()
            i=i+1
    def AddInfo(self):
        for key,item in self.LisAct.items():
            print(key+". "+item)
        self.activity=self.LisAct[input("Enter  Activity: ")]
        self.description=input("Description: ")
        self.goal=input("Goal: ")
        self.blockers=input("Blockers: ")
        self.dependency=input("Dependency: " )
        Infostr=self.activity+"$"+self.description+"$"+self.goal+"$"+self.blockers+"$"+self.dependency+"\n"
        try: 
            f=open("myinfo.txt","a")
            f.write(Infostr)
            print("Your Information has been saved succesfully!")
            f.close()
        except:
            print("There was an error saving your information")
    def SeeInfo(self):
        MyListInfo=[]
        try:
            f=open("myinfo.txt","r")
            print("Opening File.")
        except:
            print("Could not open file myinfo.txt for reading!")
        #dumping data on list
        print("Pulling data")
        # for line in f:
        #     data=line.split("$")
        #     MyListInfo.append(data)
        print("%-15s %-20s %-15s %-15s %-25s "%("Activity","Decription","Goal", "Blockers","Dependency"))
        for line in f:
            data=line.split("$")
            print("----------------------------------------------------------------------------------")
            print("%-15s %-20s %-15s %-15s %-25s "%(data[0],data[1],data[2],data[3], data[4]))
        

            


def main():
    MyStudy=StudyGuide()
    cont=True
    
   
    MyInfo=open('myinfo.txt',"a")
    while cont==True:
        print('''What Do you want to do?
1. Add Info.
2. See Info.
3. Generate Report.
4. Generate PDF ''')
        answer=input()
        print("=================================")
        if answer=="1":
            MyStudy.AddInfo()
        elif answer=="2":
            MyStudy.SeeInfo()  

    

        
main()