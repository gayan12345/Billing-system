class MyClass:
    def __init__(self):
        self.tplan={"1":["Beginner",10.0],
                   "2": ["Intermediate ",2],
                   "3":["Elite ",35.00],
                   "4":["Private tuition ",9.50],

                    }
        self.keys= list(self.tplan.keys())
        self.values=list(self.tplan.values())


    def calculate(self):
           print("..............................................")
           self.competitionEnFee =22;
           self.cost=0;
           print(self.athlete_name1)
           print(f"{self.athlete_name1} selected catogory is: {self.selected1}")
           print("Your Monthly Bill as Below")

           self.yourcost= self.noofhourscoaching*9.50
           print(f"your cost for the caching this week :{self.yourcost}")
           if int(self.choice1)==3:
               self.cost=35*3

               print(f"your session cost is :{self.cost}")
               print(f"Your Competition Entry free is :{self.competitionEnFee}")
               self.total = self.competitionEnFee +self.cost+self.yourcost
               print(f"Total cos of {self.athlete_name1} is {self.total}")

           if int(self.choice1)==2:
               self.cost=30*5

               print(f"your session cost is :{self.cost}")
               print(f"Your Competition Entry free is :{self.competitionEnFee}")
               self.total = self.competitionEnFee +self.cost+self.yourcost
               print(f"Total cos of {self.athlete_name1} is {self.total}")

           if int(self.choice1)==1:
               self.cost=25*2

               print(f"your session cost is :{self.cost}")
               print(f"You can not go to Competition")
               self.total = self.cost+self.yourcost
               print(f"Total cos of {self.athlete_name1} is {self.total}")
           else:
               print("You cant particiate any session")


    def get_input(self):

        self.athlete_name="";
        self.current_weight_kg="";

        self.number_of_competitions="";


    def display_current_training_palan(self):
        print(".............. Training Plan..................")

        for self.key ,self.value in self.tplan.items() :
            print(f" {self.key}:{self.value}")

    def select_training_plan(self):
        while(self.tplan):
            try:
                self.choice1= input("Enter the traning plan :")
                # for x , self.tplan in enumerate(self.tplan,start=1):
                if self.choice1 in self.tplan:
                    selected =self.tplan[self.choice1]
                    self.selected1 =self.tplan[self.choice1][0]

                    # print(f"You have selected {selected}")
                    print(f"You have selected :{self.selected1}")
                    break
            except ValueError:
                print("invalid")

    # def select_weight_catory(self):
    #     while(self.category):
    #         try:
    #             self.choice2 =input("Select the weight catogory :")
    #             if self.choice2 in self.category:
    #                 self.weigh_catogory =self.category[self.choice2[0]]
    #                 print(f" you have selected weight catogory :{self.weigh_catogory}")
    #                 return  self.choice2[0]
    #                 break
    #         except ValueError:
    #             print("invalid weight")


    # def display_weight_category(self):
    #     print("....................................................")
    #     print("Enter the weight Category :")
    #     self.category={"1":["Heavyweight"],
    #                "2": ["Light-Heavyweight"],
    #                "3": ["Middleweight"],
    #                "4": ["Light-Middleweight"],
    #                "5":["Lightweight"],
    #                "6":["Flyweight"]
    #                      }

        # for i ,category in  enumerate(self.category,start=1) :
        #     print(f" {category}")
        #     return self.category
    def selection_selection_weight(self):
        self.x=0;
        self.weight =int(input("Enter the your current weight :"))
        if self.weight>100:
            print("Heavyweight")
            self.x=1
            return 1
        elif 100>self.weight>=90:
            print("Light-Heavyweight")
            return 2
        elif 90>self.weight>=80:
            print("Middleweight")
            return 3
        elif 80>self.weight>=73:
            print("Light-Middleweight")
            return 4
        elif 73>self.weight>=66:
             print("Lightweight")
             return 5

        elif 66>self.weight>=0:
             print("Flyweight")
             return 5
        else:
            print("Not permitted to join")


    # def desplat_weight_catgory(self):
    #          for self.key ,self.value in self.category.items() :
    #             print(f" {self.key}:{self.value}")
    def check_max_training_hours(self):
        # self.noofhourscoaching=int(input("Enter the number of hours private coaching :"))
        print(self.choice1)
        # print(self.noofhourscoaching)
        while True:
            try:
                self.noofhourscoaching=int(input("Enter the number of hours private coaching :"))

                # Check if the value is within the desired range
                if 0 <= self.noofhourscoaching <= 5:
                     return self.noofhourscoaching
                else:
                    print("Value is outside the range (0-10). Please re-enter.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")



    def get_inputs(self):


         # self.athlete_name =input("Enter the student name :")
         self.athlete_name1 =input("Enter the athlete name :")
         obj.display_current_training_palan()
         obj.select_training_plan()
         obj.check_max_training_hours()
         obj.selection_selection_weight()

         # obj.display_weight_category()
         # obj.desplat_weight_catgory()
         # obj.select_weight_catory()

         obj.calculate()







if __name__=="__main__":
    obj=MyClass()

    obj.get_inputs()







