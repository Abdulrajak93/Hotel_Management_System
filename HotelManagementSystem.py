class hotelreception:

    def __init__(self,rt='',rent = 0,fun = 0,food = 0,wash = 0,gst = 1800,name='',address='',check_in_date='',check_out_date='',room_no=101):

        print ("\n\n*****WELCOME TO HEWING HOTEL*****\n")

        self.rt=rt

        self.food = food

        self.wash = wash 

        self.fun = fun

        self.rent = rent
        
        self.gst = gst
        
        self.name = name
        self.address = address
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.room_no = room_no
    def Reception_record(self):
        self.name=input("\nEnter your name:")
        self.address=input("\nEnter your address:")
        self.check_in_date=input("\nEnter your check in date:")
        self.check_out_date=input("\nEnter your checkout date:")
        
        
    def Room_rent(self):

        print ("We have the following rooms for you:-")

        print ("1.  type A---->rs 8000 PN\n")

        print ("2.  type B---->rs 6000 PN\n")

        print ("3.  type C---->rs 4000 PN\n")

        print ("4.  type D---->rs 3000 PN\n")

        type = int(input("Enter Your Choice Please->"))

        

        if(type == 1):

            print ("you have opted room type A")
            Nights = int(input("For How Many Nights Did You Stay:"))
            print(f"\nYour room no : {self.room_no}\n")

            self.rent = 8000 * Nights

        elif (type == 2):

            print ("you have opted room type B")
            Nights = int(input("For How Many Nights Did You Stay:"))
            print(f"\nYour room no : {self.room_no+1}\n")

            self.rent = 6000 * Nights

        elif (type == 3):

            print ("you have opted room type C")
            Nights = int(input("For How Many Nights Did You Stay:"))
            print(f"\nYour room no : {self.room_no+2}\n")

            self.rent = 4000 * Nights

        elif (type == 4):
            print ("you have opted room type D")
            Nights = int(input("For How Many Nights Did You Stay:"))
            print(f"\nYour room no : {self.room_no+3}\n")

            self.rent = 3000 * Nights

        else:

            print("please choose a room")

        print(f"your room rent is = {self.rent}\n")

    def Restaurant_food_bill(self):

        print("\n*****RESTAURANT MENU*****")

        print(" 1.water----->Rs20\n","2.tea----->Rs10\n","3.breakfast combo--->Rs90\n","4.lunch---->Rs110\n","5.dinner--->Rs150\n","6.Special Sweet----->Rs160\n","7.Exit\n")


        while (1):

            order=int(input("Enter your choice:"))


            if (order == 1):
                item = int(input("Enter the quantity:"))
                self.food += 20 * item

            elif (order == 2):
                 item = int(input("Enter the quantity:"))
                 self.food += 10 * item

            elif (order == 3):
                 item = int(input("Enter the quantity:"))
                 self.food += 90 * item

            elif (order == 4):
                 item = int(input("Enter the quantity:"))
                 self.food += 110 * item

            elif (order == 5):
                 item = int(input("Enter the quantity:"))
                 self.food += 150 * item

            elif (order == 6):
                 item = int(input("Enter the quantity:"))
                 self.food += 160 * item

            elif (order == 7):
                break;
            else:
                print("Invalid option")

        print (f"\nTotal food Cost=Rs {self.food}\n")

    def	Laundry_bill(self):
        print ("\n******LAUNDRY MENU******")

        print (" 1.Shorts----->Rs3\n","2.Trousers----->Rs4\n","3.Shirt--->Rs5\n","4.Jeans---->Rs6\n","5.Girlsuit--->Rs8\n","6.Exit\n")

        while (1):

            clothes_type = int(input("Enter your choice:"))

            if (clothes_type == 1):
                clothes_count = int(input("Enter the quantity:"))
                self.wash += 3 * clothes_count

            elif (clothes_type == 2):
                clothes_count = int(input("Enter the quantity:"))
                self.wash += 4 * clothes_count

            elif (clothes_type == 3):
                clothes_count = int(input("Enter the quantity:"))
                self.wash += 5 * clothes_count

            elif (clothes_type == 4):
                clothes_count = int(input("Enter the quantity:"))
                self.wash += 6 * clothes_count

            elif (clothes_type == 5):
                clothes_count = int(input("Enter the quantity:"))
                self.wash += 8 * clothes_count
            elif (clothes_type == 6):
                break;
            else:

                print ("Invalid option")


        print (f"\nTotal Laundary Cost=Rs {self.wash}\n")

    def Playtime_bill(self):
        print ("\n******GAME MENU*******")

        print (" 1.Table tennis----->Rs60\n","2.Bowling----->Rs80\n","3.Snooker--->Rs70\n","4.Video games---->Rs90\n","5.Pool--->Rs50\n","6.Exit\n")



        while (1):

            
            game=int(input("Enter your choice:"))


            if (game == 1):
                time = int(input("No. of hours:"))
                self.fun += 60 * time

            elif (game == 2):
                time = int(input("No. of hours:"))
                self.fun += 80 * time

            elif (game == 3):
                time = int(input("No. of hours:"))
                self.fun += 70 * time

            elif (game == 4):
                time = int(input("No. of hours:"))
                self.fun += 90 * time

            elif (game == 5):
                time = int(input("No. of hours:"))
                self.fun +=50 * time
            elif (game == 6):
                break;

            else:

                print ("Invalid option")



        print (f"\nTotal Game Bill=Rs {self.fun}\n")

    def display(self):
        print ("\n******HOTEL BILL******\n")
        print ("Customer details:")
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in date:",self.check_in_date)
        print ("Check out date",self.check_out_date)
        print ("Room no.",self.room_no)
        print ("Your Room rent is:",self.rent)
        print ("Your Food bill is:",self.food)
        print ("Your laundary bill is:",self.wash)
        print ("Your Game bill is:",self.fun)

        self.rt=self.rent+self.wash+self.fun+self.food

        print ("Your sub total bill is:",self.rt)
        print ("Additional Service Charges is",self.gst)
        print ("Your grandtotal bill is:",self.rt+self.gst,"\n")
        self.room_no += 1

            

        

        

def main():

    a=hotelreception()
    

    while (1):
        print("\n1.Enter Customer Data")
        
        print("2.Select your type of room & Calculate room rent")

        print("3.Calculate restaurant bill")

        print("4.Calculate laundry bill")

        print("5.Calculate gamebill")

        print("6.Show total cost")

        print("7.EXIT")

        val = int(input("\nEnter your choice:"))
        
        if (val == 1):
            a.Reception_record()

        if (val == 2):

            a.Room_rent()

        if (val == 3):

            a.Restaurant_food_bill()

        if (val == 4):

            a.Laundry_bill()

        if (val == 5):

            a.Playtime_bill()

        if (val == 6):

            a.display()

        if (val == 7):

            quit()



main()

