# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    persons_dict = {}
    min_name = ""
    min_avg = float("inf")
    persons_list = [person1, person2, person3]

    for person in persons_list:
        sum_results = 0
        for key, value in person.items():
                if key == "name":
                    continue
                sum_results += value
        avg = sum_results/(len(person) - 1)
        if avg < min_avg:
            min_avg = avg
            min_name = person
    return min_name


