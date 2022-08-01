# Ciasteczko z wróżbą

from random import randint

input("Witaj w programie imitującym ciasteczko z wróżbą. Aby poznać przepowiednie dla siebie kliknij Enter.")

los = randint(1, 5)

print("Twoja wróżba na dziś to:")

los

if los == 1:
    print("Dzień może przynieść pomyślne wydarzenia dotyczące Twych finansów lub kariery. Możesz spodziewać się wkrótce awansu lub zadowolenia z wcześniejszych lokat.")
elif los == 2:
    print("Szef będzie Ci dokładał obowiązków, a Ciebie aż rozboli głowa. Nie pozwalaj sobie na płacz, bo wtedy z niczym się nie wyrobisz.")
elif los == 3:
    print("Pamiętajcie, jeśli przesadzisz z miłosnymi ekscesami, dość szybko nastąpi wyczerpanie, które może wprawić cię w dezorientację. Jednym słowem, co za dużo, to nie zdrowo.")
elif los == 4:
    print("Nie odsuwaj dzisiaj na bok i nie zamiataj pod dywan problemów. Jeśli tak zrobisz, wrócą wkrótce do ciebie ze zdwojoną siłą.")
elif los == 5:
    print("Dzięki pozytywnemu podejściu będziesz mógł dokończyć pewne przedsięwzięcie. Jesteś w lepszej formie i czujesz się na siłach, aby stawić czoła temu, co nieuniknione")
else:
    print("Coś poszło nie tak! Przepraszam!")

print("Mam nadzieję, że wróżba Ci się spełni :)")
