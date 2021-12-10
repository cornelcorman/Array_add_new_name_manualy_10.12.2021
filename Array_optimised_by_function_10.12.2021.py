"""
clients                 = ["John", "Marry", "Kate"]
clients_High_priority   = ["Tob", "Pete"] 
clients_Low_priority    = ["Vicky", "Lessly", "Bob"]

print("##########################")
# ciclu care trece prin lista suplimentara 1 si adauga la lista de baza cate un index de al sau
for i in range(len(clients_High_priority)):
    clients.insert(0, clients_High_priority[i])
# ciclu care trece prin lista suplimentara 2 si adauga la lista de baza cate un index de al sau
for i in range(len(clients_Low_priority)):
    clients.append(clients_Low_priority[i])

# ciclu care afisseaza indexul+1 si valoarea indexului
for i in range(len(clients)):    
    print(i+1, clients[i]) 
"""
### ------------------------------------------------------------------------------
clients                 = ["John", "Marry", "Kate"]
clients_High_priority   = ["Tob", "Pete", "Clara"] 
clients_Low_priority    = ["Vicky", "Lessly", "Bob"]
print("Choise List where to add new clients :" "\n"
"1 List ----- > clients with ----> High Priority" "\n"
"2 List ----- > clients with ----> Ordinary Priority" "\n"
"3 List ----- > clients with ----> Low Priority")
list = int(input("List nr = "))
if list >=1 and list <=3:
    pass
    
    print("Add First Clients Name : ")
    new_clients_name = input("")
    if list == 1:
        clients_High_priority.append(new_clients_name)
        print("List of Clients_High_priority --> ", clients_High_priority)
    elif list == 2:
        clients.append(new_clients_name)
    elif list == 3:
        clients_Low_priority.append(new_clients_name)
    
    for i in range(len(clients_High_priority)):
            clients.insert(0, (clients_High_priority[i]))
    for i in range(len(clients_Low_priority)):
            clients.append(clients_Low_priority[i])
    # ----- FUNCTION ------------
    def showClients():
        p = clients
        for i in range(len(clients)):    
            print(i+1, clients[i]) 
        return(p)
    # ----- FUNCTION ------------
    print("############ New Clients List #################")
    showClients()
else:
    print("Such a list number does not exist. Try again !!! ")

