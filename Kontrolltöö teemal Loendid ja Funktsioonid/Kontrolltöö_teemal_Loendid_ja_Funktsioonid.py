import helpers

def inimesed():
    people = []
    heights = []
    
    # запросить количество людей, если пользователь хочет определить его заранее
    n = int(input("Sisestage inimeste arv (või 0, kui see pole eelnevalt määratud): ")) if n != 0 else None
    
    # заполнить списки данных о людях и их росте
    while n is None or len(people) < n:
        person = input("Sisestage isiku nimi: ")
        height = float(input("Sisestage inimese pikkus cm: "))
        people.append(person)
        heights.append(height)
    while True:
        print("Valige toiming:")
        print("1. Eemaldage loendist inimene ja tema pikkus")
        print("2. Kuvage tähestikulises järjekorras inimeste loend ja nende pikkus")
        print("3. Leidke inimestest kõrgeim ja madalaim")
        print("4. Leidke loendist n inimese keskmine pikkus")
        print("5. Sinu variant")
        print("0. Välju")

        choice=int(input("Sisestage toimingu number: "))
        if choice==0:
            break
        elif choice==1:
            person_to_remove=input("Sisestage eemaldatava isiku nimi:")
            helpers.remove_person_and_height(person_to_remove, people, heights)
        elif choice==2:
            helpers.print_sorted_people_and_heights(people, heights)
        elif choice == 3:
            helpers.print_tallest_and_shortest_person(people, heights)
        elif choice == 4:
            n = int(input("Sisestage inimeste arv, kelle keskmise pikkuse soovite leida: "))
            selected_people = helpers.select_people(n, people)
            if len(selected_people) > 0:
                selected_heights = helpers.get_heights(selected_people, people, heights)
                average_height = helpers.get_average_height(selected_heights)
                print("Valitud inimeste keskmine pikkus: {} см".format(average_height))
            else:
                print("Valitud inimesi pole")
        
        elif choice == 5:
            # здесь можно добавить свой вариант действия
            pass
        
        else:
            print("Vale valik")



