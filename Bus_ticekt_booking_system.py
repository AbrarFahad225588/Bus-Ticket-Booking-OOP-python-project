from abc import ABC,abstractmethod
class Bus_Structure(ABC):
    def __init__(self,coach,driver,arrival,diparture,from_des,to_des) -> None:
        self.coach=coach
        self.driver=driver
        self.arrival=arrival
        self.diparture=diparture
        
        self.from_des=from_des
        self.to_des=to_des
        self.seats=['Empty' for _ in range(20)]
class Bus(Bus_Structure):
    pass
class BusCompany:
    def __init__(self) -> None:
        self.buses={}
    def install_bus(self,bus):
        print(f'Bus coach no {bus.coach} install succesfully!!')
        self.buses[bus.coach]=bus
    def dis_available_bus(self):
        if not  self.buses:
            print("No bus available")
        else:
            print(f"Coach\tDriver\tfrom \t to ")    
            for coach, bus in self.buses.items():
                
                print(f"{coach}\t{bus.driver}\t{bus.from_des}\t{bus.to_des}")
    def Book_Ticket(self,coach,seat):
        if coach in self.buses:
            if 1<=seat<=20:
                if self.buses[coach].seats[seat-1]=='Empty':
                    print(f'Bus coach no {coach} this bus {seat} no seat Booked Confirmed!! ')
                    self.buses[coach].seats[seat-1]='Booked'
                else:
                    print("Seat already booked")
            else:
                print("Invalid seat number")
        else:
            print("Invalid Coach number")
    def display_seat_status(self,coach):
        if coach in self.buses:
            print(self.buses[coach].seats)
        else:
            print("Invalid Coach number") 
            
            
            
            
fahad_paribahan=BusCompany()
while True:
   
    print("********Welcome To Bus Ticket Booking System !!*************")
    print("1.Install Bus")
    print("2.dis_available_bus")
    print("3.View_seat_status")
    print("4.Book_Ticket")
    print("5.Exit")
    op=int(input("Enter a Option : "))
    if op==1 :
        coach=int(input("Enter a Coach Number : "))
        driver=input("Enter a Driver name : ")
        arrival=input("Enter a Arrival time : ")
        diparture=input("Enter a Diparture Time : ")
        from_des=input("Enter a From Destination : ")
        to_des=input("Enter a To Destination : ")
        bus=Bus(coach,driver,arrival,diparture,from_des,to_des)
        fahad_paribahan.install_bus(bus)
    elif op==2:
        fahad_paribahan.dis_available_bus()
    elif op==3:
        coach=int(input("Enter a Coach Number : "))
        fahad_paribahan.display_seat_status(coach)
    elif op==4:
        coach=int(input("Enter a Coach Number : "))
        seat=int(input("Enter a seat Number : "))
        fahad_paribahan.Book_Ticket(coach,seat)
    elif op==5:
        print("Thanks Visiting Our Bus ticket Booking System !!")
        break
    else:
        print("Invalid Option !!")


            
                            
                
        