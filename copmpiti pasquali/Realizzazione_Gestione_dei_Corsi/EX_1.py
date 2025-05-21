class Room:
    def __init__(self, id: str, floor: int, seats: int, area: int):
        self.id: str = id
        self.floor: int = floor
        self.seats: int = seats
        self.area: int = area

    def get_id(self) -> str:
        return self.id
    def get_floor(self) -> int:
        return self.floor
    def get_seats(self) -> int:
        return self.seats
    def set_seats(self, new_seats: int):
        self.seats = new_seats
    def get_area(self) -> int:
        return self.area

    
class Building:
    def __init__(self, name: str, address: str, floors: int):
        self.name:str = name
        self.address:str = address
        self.floors:int = floors
        self.rooms: list = []
   
    def get_floors(self) -> int:
        return self.floors
    
    def get_rooms(self) -> list:
        return self.rooms
    
    def add_room(self, room):
        self.rooms.append(room)

    def get_total_area(self) -> int:
        total_area = 0
        for room in self.rooms:
            total_area += room.get_area()
        return total_area
    

if __name__ == "__main__":
    # Test della classe Room
    room1 = Room("Room1", 0, 15, 20)
    print(f"ID Stanza: {room1.get_id()}, Atteso: Room1")
    print(f"Piano stanza: {room1.get_floor()}, Atteso: 0")
    print(f"Posti stanza: {room1.get_seats()}, Atteso: 15")
    print(f"Area stanza: {room1.get_area()}, Atteso: 20")

    room2 = Room("Room2", 1, 25, 30)
    print(f"ID Stanza: {room2.get_id()}, Atteso: Room2")
    print(f"Piano stanza: {room2.get_floor()}, Atteso: 1")
    print(f"Posti stanza: {room2.get_seats()}, Atteso: 25")
    print(f"Area stanza: {room2.get_area()}, Atteso: 30")

    room3 = Room("Room3", -1, 5, 10) # Test con piano fuori range
    print(f"ID Stanza: {room3.get_id()}, Atteso: Room3")
    print(f"Piano stanza: {room3.get_floor()}, Atteso: -1")
    print(f"Posti stanza: {room3.get_seats()}, Atteso: 5")
    print(f"Area stanza: {room3.get_area()}, Atteso: 10")

     # Test della classe Building
    building = Building("Test Building", "123 Test St", 10)
    print(f"Nome edificio: {building.name}, Atteso: Test Building")
    print(f"Indirizzo edificio: {building.address}, Atteso: 123 Test St")
    print(f"Piani edificio: {building.get_floors()}, Atteso: 10")

    # Test aggiunta aule all'edificio
    building.add_room(room1)
    building.add_room(room2)
    print(f"Aule nell'edificio: {[room.get_id() for room in building.get_rooms()]}, Atteso: ['Room1', 'Room2']")

    # Test aggiunta di aule duplicate
    building.add_room(room1)
    print(f"Aule nell'edificio (dopo duplicato): {[room.get_id() for room in building.get_rooms()]}, Atteso: ['Room1', 'Room2', 'Room1']")

    # Test calcolo area totale edificio
    print(f"Area totale dell'edificio: {building.get_total_area()}, Atteso: 50") # 20 + 30

    
