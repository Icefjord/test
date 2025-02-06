type Person(name:string, add:string, phone: int) = 
    member val name = name with get, set
    member val address = add with get, set
    member val phone = phone with get, set


type Customer(a,b,c,num:int, mail:bool) = 
    inherit Person (a,b,c)
    member val Number = num with get, set
    member val x = 45

let dave = Customer("Fred", "57 Ave", 23764422, 12, false)

printf "
%A
%A
%A
%A
%A
" dave.name dave.address dave.phone dave.Number dave.mail


Spiller
Kort
Deck
Delt
Viser
Vinder
Vundne kort
stak
vinder hånden


Kort()
Value
