from django.conf import settings

from main.models import Mailing, StatusMailing
from datetime import datetime, timedelta
import calendar
from django.core.mail import send_mail


list_Mailing = Mailing.objects.all()
list_StatusMailing = StatusMailing.objects.all()

Status_Create = list_StatusMailing[0]
Status_Finish = StatusMailing.objects.get(id=2)
Status_Work = list_StatusMailing[2]
def update_mailing_begin_date(mailing_id, new_begin_date):
    """Обновляем данные begin_date Mailing"""
    try:
        mailing = Mailing.objects.get(id=mailing_id)
        mailing.begin_date = new_begin_date
        mailing.begin_date = new_begin_date
        mailing.save()
        return True
    except Mailing.DoesNotExist:
        return False


def update_mailing_satus(mailing_id, new_satus):
    """Обновляем данные satus Mailing"""
    try:
        mailing = Mailing.objects.get(id=mailing_id)
        mailing.satus.name = "Finish"
        print("Меняем статус на Finish")
        mailing.save()
        return True
    except Mailing.DoesNotExist:
        print("Меняем статус не получилось")
        return False


def if_begin(time_):
    """Обработка времени начала рассылки"""
    try:
        date_time_begin = time_.strftime("%Y-%m-%d %H:%M:%S")
    except AttributeError:
        date_time_begin = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return date_time_begin
    else:
        return date_time_begin
def if_finish(time_):
    """Обработка времени завершения рассылки"""
    try:
        date_time_finish = time_.strftime("%Y-%m-%d %H:%M:%S")
    except AttributeError:
        date_time_finish = datetime.now() + timedelta(hours=1)
        date_time_finish = date_time_finish.strftime("%Y-%m-%d %H:%M:%S")
        return date_time_finish
    else:
        return date_time_finish

def time_rigth(mailing_id, time_now, time_obj):
    """
    Проверка временных границ
    """
    date_time_begin = if_begin(time_obj.begin_date) # Дата начала рассылки
    date_time_finish = if_finish(time_obj.close_date) # Дата окончания рассылки

    time_start = datetime.fromisoformat(date_time_begin).timestamp()
    date_time_now = time_now.timestamp()
    time_finish = datetime.fromisoformat(date_time_finish).timestamp()

    if time_start <= date_time_now <= time_finish:
        # print("Печатаем", date_time_begin, '<=', time_now.strftime("%Y-%m-%d %H:%M:%S"), '<=', date_time_finish)
        return True
    elif date_time_now > time_finish:
        update_mailing_satus(mailing_id, "Finish")
        return False
    else:
        # print("НЕ Печатаем", date_time_begin, '<=', time_now.strftime("%Y-%m-%d %H:%M:%S"), '<=', date_time_finish)
        return False



def update_time_Mailing(mailing_id, obj):
    """Вычисляем время begin_date + frequency в Mailing"""

    if str(obj.frequency) == "10S":
        new_datetime = obj.begin_date + timedelta(seconds=120)
    elif str(obj.frequency) == "H":
        new_datetime = obj.begin_date + timedelta(hours=1)
        # obj.begin_date = new_datetime
    elif str(obj.frequency) == "D":
        new_datetime = obj.begin_date + timedelta(days=1)
        # obj.begin_date = new_datetime
    elif str(obj.frequency) == "W":
        new_datetime = obj.begin_date + timedelta(days=7)
        # obj.begin_date = new_datetime
    elif str(obj.frequency) == "Y":
        next_month = obj.begin_date.month + 1
        year = obj.begin_date.year + next_month // 12
        month = next_month % 12

        if month == 0:  # Если следующий месяц январь следующего года
            month = 1
            year -= 1

        days_in_month = calendar.monthrange(year, month)[1]  # Количество дней в следующем месяце
        new_datetime = obj.begin_date + timedelta(days=days_in_month)
    print(f"{obj.begin_date} Изменена на - {new_datetime}")
    update_mailing_begin_date(mailing_id, new_datetime)
    update_mailing_satus(mailing_id, Status_Work)


def my_job():
    """
    Основное тело цикла
    """
    now = datetime.now()

    Stat = StatusMailing.objects.get(id=2)
    mailing = Stat.mailing_set.all()
    print(mailing)

    for i, element in enumerate(list_Mailing):
        id_element = Mailing.objects.values_list('id', flat=True)[i]

        print(element.name)

        if time_rigth(id_element, now, element):
            #Действия при ИСТИНЕ, когда scheduler попадает во временной диапазон

            # Обновляем время begin_date + frequency в Mailing
            update_time_Mailing(id_element, element)


            for client in element.clients.all():
                print(f"{element.name}, {client.email}-отправить письмо")
                send_mail(
                    subject=f"Тема рассылки{element.name}- {element.message.title}",
                    message=f"Сообщение рассылки {element.message.content}",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email]  # передача списка email в качестве получателей
                )

                print(f"{element.name}, {client.email}-Создаем отчет")

                #отправляем сообщение - получаем ответ отправилось или нет

            #Создаем Лог создаем эkземпляр класса Logs() с текущей датой

            #Обновляем Таймер

        # else:
        #     print("НЕЕЕЕЕЕЕ ----- Печатаем")
        # print(time_rigth(now,element))
        # print(element.begin_date, '<=', now.strftime("%Y-%m-%d %H:%M:%S"), '<=',element.close_date)

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


