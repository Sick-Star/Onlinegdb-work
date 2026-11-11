#!/home/codespace/.python/current/bin/python

def main():
    print("Managing a text file".title())
    # finished = 0
    # while not finished:
    car_list = get_list()
    for car in car_list:
        print(f"make: ")

def get_list():
    car_list = []
    with open("cars.txt", "r") as file:
        for item in file:
            car = item.strip()
            car_info = item.split()
            car_list.append(car_info)



    return car_list



main()