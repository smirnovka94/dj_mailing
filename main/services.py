from django.conf import settings

from main.models import Mailing, Logs
from datetime import datetime, timedelta
import calendar
from django.core.mail import send_mail


list_Mailing = Mailing.objects.all()

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
        mailing.satus = "Finish"
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

        mailing = Mailing.objects.get(id=mailing_id)
        mailing.satus = "Finish"
        print("Меняем статус на Finish")
        mailing.save()

        # update_mailing_satus(mailing_id, "Finish")
        return False
    else:
        # print("НЕ Печатаем", date_time_begin, '<=', time_now.strftime("%Y-%m-%d %H:%M:%S"), '<=', date_time_finish)
        return False



def update_time_Mailing(obj):
    """Вычисляем время begin_date + frequency в Mailing"""

    if str(obj.frequency) == "10S":
        new_datetime = obj.begin_date + timedelta(seconds=120)
    elif str(obj.frequency) == "Daily":
        new_datetime = obj.begin_date + timedelta(days=1)
        # obj.begin_date = new_datetime
    elif str(obj.frequency) == "Weekly":
        new_datetime = obj.begin_date + timedelta(days=7)
        # obj.begin_date = new_datetime
    else:# str(obj.frequency) == "Monthly":
        new_datetime = obj.begin_date + timedelta(days=30)
        # obj.begin_date = new_datetime
    return new_datetime
    # print(f"{obj.begin_date} Изменена на - {new_datetime}")
    # update_mailing_begin_date(mailing_id, new_datetime)


def my_job():
    """
    Основное тело цикла
    """

    now = datetime.now()

#
    # Stat = StatusMailing.objects.get(id=2)
    # mailing = Stat.mailing_set.all()
    # print(mailing)

    for i, element in enumerate(list_Mailing):
        id_element = Mailing.objects.values_list('id', flat=True)[i]#pk рассылки
        date_time_begin = if_begin(element.begin_date)  # Дата начала рассылки
        date_time_finish = if_finish(element.close_date)  # Дата окончания рассылк

        time_start = datetime.fromisoformat(date_time_begin).timestamp()
        date_time_now = now.timestamp()
        time_finish = datetime.fromisoformat(date_time_finish).timestamp()

        # mailing = element.objects.get(id=mailing_id)

        print(element.name)
        if time_start <= date_time_now <= time_finish:
            element.satus = "Work"

            # Обновляем время begin_date + frequency в Mailing
            new_date_time = update_time_Mailing(element)
            element.begin_date = new_date_time

            for client in element.clients.all():
                print(f"{element.name}, {client.email}-отправить письмо")
                # отправляем сообщение - получаем ответ отправилось или нет
                send_mail(
                    subject=f"Тема рассылки{element.name}- {element.message.title}",
                    message=f"Сообщение рассылки {element.message.content}",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email]  # передача списка email в качестве получателей
                )

                print(f"{element.name}, {client.email}, {element.satus}-Создаем отчет")

                # Создаем Лог создаем эkземпляр класса Logs() с текущей датой
                Logs.objects.create(status=element.satus, answer="Отправлено")
            element.save()
            print(f"{element.name}, {client.email}, {element.satus }-изм статус на Work")



        elif date_time_now > time_finish:

            element.satus = "Finish"
            element.save()
            print(f"{element.name}, {element.satus}-изм статус на Finish")
        else:
            print(f"{element.name}, {element.satus}-без изменнеий")
    return True


