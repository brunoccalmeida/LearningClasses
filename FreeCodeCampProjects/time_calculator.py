# Escreva uma função chamada add_time, que recebe dois parâmetros necessários e um parâmetro opcional:
#
#     uma hora de início no formato de relógio de 12 horas (terminando em AM ou PM)
#     um tempo de duração que indica o número de horas e minutos
#     (opcional) um dia de início na semana, sem distinção de maiúsculas ou minúsculas
#
# A função deve adicionar o tempo de duração ao horário inicial e retornar o resultado.
#
# Se o resultado for no dia seguinte, ele deve mostrar (next day) (dia seguinte) após o tempo.
# Se o resultado for mais de um dia depois, ele deve mostrar (n days later) (n dias depois) após o tempo,
# onde "n" é o número de dias depois.
#
# Se a função receber o parâmetro opcional do dia de início na semana, então o resultado deve exibir o
# dia da semana do resultado. O dia da semana no resultado deve aparecer após o tempo e antes do número de dias depois.
# Suponha que os horários de início são tempos válidos. Os minutos no tempo de duração serão um número inteiro menor
# que 60, mas a hora pode ser qualquer número inteiro.
# def round_up_number(n):
#     if n == int(n):
#         return n
#     return int(n + 1)


def time_flag_change(time_flag):
    if time_flag == 'PM':
        return 'AM'
    else:
        return 'PM'


def add_time(start, duration, day_of_week=None):

    start_time_str = start
    hour_start_int = int(start_time_str.split(":")[0])
    minutes_start_int = int(start_time_str.split(":")[1][:2])
    time_flag = start_time_str.split(":")[1][3:]  # Time flag can be "AM" or "PM"
    time_flag_start = time_flag

    duration_str = duration
    duration_hour_int = int(duration_str.split(":")[0])
    duration_min_int = int(duration_str.split(":")[1])
    time_flag_hour = hour_start_int + (duration_hour_int % 24)

    if duration_min_int + minutes_start_int > 60:
        # this is used to determine if time_flag, after adding the duration minutes, stays the same or changes
        time_flag_hour += 1

    if time_flag_hour >= 12:
        # this will determine if time_flag changes at the beginning with the sum
        # of the start minutes and duration minutes
        time_flag = time_flag_change(time_flag)

    hour_start_plus_duration = hour_start_int + duration_hour_int
    minutes_start_plus_duration = minutes_start_int + duration_min_int
    minutes_final = minutes_start_plus_duration
    hours_from_sum_of_minutes = 0

    if minutes_start_plus_duration >= 60:
        hours_from_sum_of_minutes += 1
        minutes_final = minutes_start_plus_duration - 60

    if minutes_final in range(0, 10):
        minutes_final = f'0{minutes_final}'

    days = (duration_hour_int + hours_from_sum_of_minutes) // 24
    if time_flag_start == 'PM' and time_flag == 'AM':
        days += 1

    hour_final = (hour_start_plus_duration + hours_from_sum_of_minutes) - ((days - 1) * 24)

    if hour_final == 0:
        hour_final = 12

    while hour_final > 12:
        hour_final -= 12

    if day_of_week:
        days_of_week_dict = {
                            "sunday": 1,
                            "monday": 2,
                            "tuesday": 3,
                            "wednesday": 4,
                            "thursday": 5,
                            "friday": 6,
                            "saturday": 7
                            }
        days_of_week_dict_invert = {}
        day_of_week = day_of_week.lower()
        day_of_week = days_of_week_dict.get(day_of_week)
        day_of_week += days

        while day_of_week > 7:
            day_of_week -= 7
        for k, v in days_of_week_dict.items():
            days_of_week_dict_invert[v] = k
        day_of_week = days_of_week_dict_invert[day_of_week]

        if days == 1:
            return f'{hour_final}:{minutes_final} {time_flag}, {day_of_week.capitalize()} (next day)'

        if days >= 2:
            return f'{hour_final}:{minutes_final} {time_flag}, {day_of_week.capitalize()} ({days} days later)'

        return f'{hour_final}:{minutes_final} {time_flag}, {day_of_week.capitalize()}'

    if days == 1:
        return f'{hour_final}:{minutes_final} {time_flag} (next day)'

    if days >= 2:
        return f'{hour_final}:{minutes_final} {time_flag} ({days} days later)'

    return f'{hour_final}:{minutes_final} {time_flag}'


if __name__ == '__main__':
    print(add_time("3:00 PM", "3:10"))
    print(add_time("11:30 AM", "2:32", "Monday"))
    print(add_time("11:43 AM", "00:20"))
    print(add_time("10:10 PM", "3:30"))
    print(add_time("11:43 PM", "24:20", "tueSday"))
    print(add_time("6:30 PM", "205:12"))
    print(add_time("8:16 PM", "466:02", 'tuesday'))

