import datetime
import time

def break_or_continue():
    answer = str(input("Would you like to exit app?\n"
                       "Y : True\n"
                       "N : False\n"
                       "====================="))
    return answer

def load(date,name):
    return [date,name]

def main():
    id_count = 0
    current_date = str(datetime.datetime.now()).split()[0]
    all_people = []
    work = True
    while work:
        action = str(input("[❤️🌹] - Welcome what would you like to do?\n"
                           "A. Show me actual date! 📆\n"
                           "B. Load a new birthday! 💿\n"
                           "C. Show me how much time left for someone birthday! 🥳\n"
                           "D. Show me loaded birthdays! 🧟\n"
                           "====================================\n"))

        # RETURNS CURRENT DATE
        if action.upper() == "A":
            time.sleep(0.5)

            print((f'Today date is : {current_date}\n'
            f'Nice to see you again! 🤩\n'
            f'====================================\n'))

            time.sleep(0.5)

        # LOADS A NEW BIRTHDAY
        elif action.upper() == "B":
            time.sleep(0.5)

            birthday_info = load(str(input("1) Please input date FORMAT [RRRR-MM-DD] 🗓️\n")),
                                 str(input("2) Please input identification FORMAT [NAME-SURNAME] 🪪\n")))
            print(f'Congratulations 🥳! I loaded {birthday_info[1].upper()}\n'
                  f'Takes place at {birthday_info[0]}\n'
                  f'====================================\n')

            id_count += 1
            birthday_info.append(id_count)
            all_people.append(birthday_info)


            time.sleep(2)

        # CHECKS AGE AND DAYS LEFT TILL BIRTHDAY
        elif action.upper() == "C":
            # Wrong load check
            if len(all_people) == 0:

                time.sleep(0.5)

                print("====================================\n"
                      "Load someone birthday before checking!\n"
                      "====================================\n")

                time.sleep(2)
            # Proper load
            else:
                id = int(input(f"Which person ID shall i use? [1-{len(all_people)}]")) - 1

                birthday_date = all_people[id][0]
                birthday_name = all_people[id][1].split('-')[0]
                # Current RRRR-MM-DD

                current_year = int(current_date.split('-')[0])
                current_month = int(current_date.split('-')[1])
                current_day = int(current_date.split('-')[2])
                # Birthday RRRR-MM-DD

                birthday_year = int(birthday_date.split('-')[0])
                birthday_month = int(birthday_date.split('-')[1])
                birthday_day = int(birthday_date.split('-')[2])

                # Just the age function
                age = current_year - birthday_year

                # How many days left function
                days = None
                time.sleep(0.5)

                # Age answer
                time.sleep(0.5)
                print(f'{birthday_name.upper()} is celebrating his/her : {age + 1} birthday!\n')

                time.sleep(0.5)

                month_days = {
                    1: 31,
                    2: 59,
                    3: 90,
                    4: 120,
                    5: 151,
                    6: 181,
                    7: 212,
                    8: 243,
                    9: 273,
                    10: 304,
                    11: 334,
                    12: 365
                }
                current_year_days = month_days[current_month] + current_day
                birthday_year_days = month_days[birthday_month] + birthday_day

                if current_year_days < birthday_year_days:
                    result = birthday_year_days - current_year_days
                    print(f'{result} days left till birthday\n'
                          f'====================================\n')
                elif current_year_days == birthday_year_days:
                    print("TODAY IS YOUR BIRTHDAY!\n"
                          "====================================\n")
                else:
                    result = birthday_year_days - current_year_days + 365 + 1
                    print(f'{result} days left till birthday\n'
                          f'====================================\n')
                time.sleep(2)

        elif action.upper() == "D":
            if len(all_people) == 0:

                time.sleep(0.5)

                print("====================================\n"
                      "Load someone birthday before checking!\n"
                      "====================================\n")

                time.sleep(2)
            else:
                for person in all_people:
                    print(f'ID : {person[2]}; NAME : {person[1]}; DATE : {person[0]}')
                print('====================================\n')
        elif action.upper() not in ['A','B','C','D']:
            raise Exception('Please return proper answer')






if __name__ == '__main__':
    main()