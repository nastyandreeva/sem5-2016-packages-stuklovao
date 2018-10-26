class GuestBook:
    def __init__(self):
        self.guests = list()

    def add(self, name, surname):
        self.guests.append({"Guest name": name})
        self.guests.append({"Guest surname": surname})

    def remove(self, name, surname):
        for guest in self.guests:
            if (guest.get("Guest name") == name) and (guest.get("Guest surname") == surname):
                self.guests.remove(guest)

    def write_file(self):
        import json
        with open("./book.json", 'a') as file:
            data = { "Guests": self.guests }
            file.write(json.dumps(data,file))
            
            
if __name__ == "__main__":
	guestBook = GuestBook()
	guestBook.add("Olya","Stuklova")
       guestBook.add("Anya","Ivanova")
	guestBook.remove("Anya","Ivanova")
	guestBook.write_file()
