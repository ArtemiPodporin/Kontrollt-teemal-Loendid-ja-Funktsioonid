def remove_person_and_height(person, people_list, heights_list):
    if person in people_list:
        index_to_remove = people_list.index(person)
        del people_list[index_to_remove]
        del heights_list[index_to_remove]
        print("Teave isiku {} kohta eemaldati".format(person))
    else:
        print("Isik nimega {} pole loendis".format(person))


def print_sorted_people_and_heights(people_list, heights_list):
    sorted_people = sorted(people_list)
    for person in sorted

