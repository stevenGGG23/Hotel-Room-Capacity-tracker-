def main():
    training_name = input().strip()
    print("Room  MaxCapac  Enrolled  Seats  Empty  Availability")
    print("***************************************************")

    rooms, total_capacity, total_enrollment, available_rooms, over_enrolled_rooms = process_training_data()

    for room in rooms:
        print(f"{room[0]:<8}{room[1]:<12}{room[2]:<12}{room[3]:<12}{room[4]}")

    print("***************************************************")
    final_summary(training_name, len(rooms), total_capacity, total_enrollment, available_rooms, over_enrolled_rooms)


def get_classroom_info():
    room = int(input().strip())
    if room < 0:
        return room, 0, 0
    max_capacity = int(input().strip())
    enrolled = int(input().strip())
    return room, max_capacity, enrolled


def process_training_data():
    rooms = []
    total_capacity = 0
    total_enrollment = 0
    available_rooms = 0
    over_enrolled_rooms = 0

    while True:
        room, max_capacity, enrolled = get_classroom_info()
        if room < 0:
            break

        empty_seats = max_capacity - enrolled

        if empty_seats == 0:
            availability = "FULL"
        elif empty_seats < 0:
            availability = "OVER"
        else:
            availability = "OPEN"
        
        if availability == "OPEN":
            available_rooms += 1
        elif availability == "OVER":
            over_enrolled_rooms += 1

        rooms.append((room, max_capacity, enrolled, empty_seats, availability))
        total_capacity += max_capacity
        total_enrollment += enrolled

    return rooms, total_capacity, total_enrollment, available_rooms, over_enrolled_rooms


def final_summary(training_name, room_count, total_capacity, total_enrollment, available_rooms, over_enrolled_rooms):
    print(training_name)
    print()
    print(f"Training Rooms: {room_count}")
    print(f"Training Capacity: {total_capacity}")
    print(f"Training Enrollment: {total_enrollment}")
    print(f"Available Training Rooms: {available_rooms}")
    print(f"Over Enrolled Training Rooms: {over_enrolled_rooms}")
    print("***************************************************")
    print("$")


if __name__ == "__main__":
    main()
