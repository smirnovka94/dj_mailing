from main.models import Mailing
from datetime import datetime, timedelta

def send_mail(email: str)-> bool:
    """
    Отрпавляет email на указаный адрес с текстом и возвращает результат отправки
    """
    print(f'email send to {email}')
    return True

list_Mailing = Mailing.objects.all()

def if_begin(time_):
    try:
        date_time_begin = time_.strftime("%Y-%m-%d %H:%M:%S")
    except AttributeError:
        date_time_begin = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return date_time_begin
    else:
        return date_time_begin
def if_finish(time_):
    try:
        date_time_finish = time_.strftime("%Y-%m-%d %H:%M:%S")
    except AttributeError:
        date_time_finish = datetime.now() + timedelta(hours=1)
        date_time_finish = date_time_finish.strftime("%Y-%m-%d %H:%M:%S")
        return date_time_finish
    else:
        return date_time_finish
def time_rigth(time_now, time_obj):
    """
    Проверка временных границ
    """
    date_time_begin = if_begin(time_obj.begin_date) # Дата начала рассылки
    date_time_finish = if_finish(time_obj.close_date) # Дата окончания рассылки

    time_start = datetime.fromisoformat(date_time_begin).timestamp()
    date_time_now = time_now.timestamp()
    time_finish = datetime.fromisoformat(date_time_finish).timestamp()

    if time_start <= date_time_now <= time_finish:
        return True#("Печатаем", date_time_begin, '<=', time_now.strftime("%Y-%m-%d %H:%M:%S"), '<=', date_time_finish)
    else:
        return False#("НЕ Печатаем", date_time_begin, '<=', time_now.strftime("%Y-%m-%d %H:%M:%S"), '<=', date_time_finish)

def my_job():
    """
    Основное тело цикла
    """
    now = datetime.now()

    for element in list_Mailing:
        if time_rigth(now,element):
            #Действия при ИСТИНЕ когда scheduler попадает во временной диапазон
        else:
            print("НЕЕЕЕЕЕЕ ----- Печатаем")
        print(time_rigth(now,element))
        print(element.begin_date, '<=', now.strftime("%Y-%m-%d %H:%M:%S"), '<=',element.close_date)
        for c in element.clients.all():
            print(f"{element.name}, {c.email}-{element.message}")
    return True


""" 
def send_order_email(order_item: Order):
    send_mail(
        subject='Смена пароля',
        message=f'Новый пароль: {_key}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
"""

# class CDB():
#     send_mail()
#
# def periodic_task():
#     pass


