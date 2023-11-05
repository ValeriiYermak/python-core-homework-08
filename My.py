from datetime import datetime, timedelta, date


def get_birthdays_per_week(users):
    
    if not users:
        return {}
    
    now = date.today()
    current_week_day = now.weekday()
    weekdays = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday',
    }
    birthdays_per_week = {day: [] for day in weekdays.values()}
        
    for user in users:
        name = user['name']
        birthday = user['birthday']
        new_birthday = birthday.replace(year=now.year)
        
        if new_birthday < now:
            new_birthday = new_birthday.replace(year=now.year + 1)
        
        # Перевіряємо, чи дата народження потрапляє в наступний тиждень
        if now <= new_birthday <= now + timedelta(days=7):
            day_week = new_birthday.weekday()
            # Отримуємо назву дня тижня
            day_name = weekdays[day_week]

        else:
            return{}

            # Перевірка, чи день народження потрапляє на вихідний            
        if day_name in ['Saturday', 'Sunday']:
                # Переносимо на понеділок
                day_name = 'Monday'
                birthdays_per_week[day_name].append(name)
        print(birthdays_per_week)
        return birthdays_per_week


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": date(2023, 11, 1)}, # Wednesday
        {"name": "Angelina", "birthday": date(2023, 11, 2)}, # Thursday
        {"name": "Bill Jill", "birthday": date(2023, 11, 3)},# Friday
        {"name": "Kolya", "birthday": date(2023, 11, 4)},    # Saturday
        {"name": "Sophia", "birthday": date(2023, 11, 5)},   # Sunday
        {"name": "Solomia", "birthday": date(2023, 11, 6)},  # Monday
        {"name": "Sasha", "birthday": date(2023, 11, 7)},    # Tuesday
        {"name": "Pasha", "birthday": date(2023, 11, 8)},    # Wednesday
        {"name": "BiJi", "birthday": date(2023, 11, 9)},     # Thursday
        {"name": "Oksana", "birthday": date(2023, 11, 10)},  # Friday
        {"name": "Jill", "birthday": date(2023, 11, 11)},    # Saturday
        {"name": "Fill", "birthday": date(2023, 11, 12)},    # Sunday
        {"name": "NIll", "birthday": date(2023, 11, 13)},    # Monday
        {"name": "Luccy", "birthday": date(2023, 11, 14)},   # Tuesday
    ]
    result = get_birthdays_per_week(users)
    # Виведення результатів
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")