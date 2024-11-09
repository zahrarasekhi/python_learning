def get_user_input():
    user_input_list = []
    while True:
        user_input = input("please enter a number or type ok: ")
        if user_input.lower() == "ok":
            break
        try:
            number = float(user_input)
            if number not in user_input_list:
                user_input_list.append(number)
        except ValueError:
            print("please enter a number")
    total_sum = sum(user_input_list)
    print(f"sum of numbers : {total_sum}")
    print(f"len of number: {len(user_input_list)}")
    return total_sum

get_user_input()
