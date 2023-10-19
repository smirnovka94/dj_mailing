from django.conf import settings

from main.models import Mailing, Logs
from datetime import datetime, timedelta

from django.core.mail import send_mail

list_Mailing = Mailing.objects.all()

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



def update_time_Mailing(obj):
    """Вычисляем время begin_date + frequency в Mailing"""
    if str(obj.frequency) == "10S":
        new_datetime = obj.begin_date + timedelta(seconds=120)
    elif str(obj.frequency) == "Daily":
        new_datetime = obj.begin_date + timedelta(days=1)
    elif str(obj.frequency) == "Weekly":
        new_datetime = obj.begin_date + timedelta(days=7)
    else:
        new_datetime = obj.begin_date + timedelta(days=30)
    return new_datetime



def my_job():
    """
    Основное тело цикла
    """
    now = datetime.now()


    for i, element in enumerate(list_Mailing):

        date_time_begin = if_begin(element.begin_date)  # Дата начала рассылки
        date_time_finish = if_finish(element.close_date)  # Дата окончания рассылок

        time_start = datetime.fromisoformat(date_time_begin).timestamp()
        date_time_now = now.timestamp()
        time_finish = datetime.fromisoformat(date_time_finish).timestamp()

        if time_start <= date_time_now <= time_finish:

            element.satus = "Work"
            # Обновляем время begin_date + frequency в Mailing
            new_date_time = update_time_Mailing(element)
            element.begin_date = new_date_time

            for client in element.clients.all():
                # отправляем сообщение
                send_mail(
                    subject=f"Тема рассылки{element.name}- {element.message.title}",
                    message=f"Сообщение рассылки {element.message.content}",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email]  # передача списка email в качестве получателей
                )
                # Создаем Лог создаем эkземпляр класса Logs() с текущей датой
                Logs.objects.create(status=element.satus, answer="Отправлено")
            element.save()
        elif date_time_now > time_finish:
            # изменяем статус неактуальной заявки на завершена
            element.satus = "Finish"
            element.save()

    return True


