import datetime
import time


def horloge():
    reponse_1 = str(input("Quel format voulez vous ? \n 1) HH:MM:SS \n 2) AM PM \n "))
    reponse_2 = str(input("Voulez vous configurer une alarme ? \n 1) Oui \n 2) Non \n "))
    if reponse_2 == "1":
        a, b, c = input("Entrez l'alarme avec ce format HH:MM:SS \n ").split(":")
        alarm = datetime.datetime.now().replace(hour=int(a), minute=int(b), second=int(c))
        if reponse_1 == "1":
            temps(1, alarm)
        elif reponse_1 == "2":
            temps(2, alarm)
        else:
            print("Erreur")
            horloge()
    elif reponse_2 == "2":
        if reponse_1 == "1":
            temps(1,'none')
        elif reponse_1 == "2":
            temps(2,'none')
        else:
            print("Erreur")
            horloge()
    else:
        horloge()
    print("fin")


def temps(nb, alarm):
    a, b, c = input("Entrez l'heure avec ce format HH:MM:SS \n ").split(":")
    now = datetime.datetime.now().replace(hour=int(a), minute=int(b), second=int(c))
    temps = datetime.timedelta(seconds=1)
    while True:
        if nb == 1:
            alarm_time = alarm.strftime('%H:%M:%S') if alarm != 'none' else None
            now_time = now.strftime('%H:%M:%S')
            updated_now = now + temps
            now = updated_now
            re_updated_now = updated_now.strftime('%H:%M:%S')
            if alarm_time and now_time == alarm_time:
                print("Dring Dring")
                break
            print("\n\n         +~~~~~~~~~~~~~~~~~~~+")
            print(f"         |      {re_updated_now}     |")
            print("         +~~~~~~~~~~~~~~~~~~~+\n\n")
            time.sleep(1)
        elif nb == 2:
            alarm_time = alarm.strftime('%I:%M:%S %p') if alarm != 'none' else None
            now_time = now.strftime('%I:%M:%S %p')
            updated_now = now + temps
            now = updated_now
            re_updated_now = updated_now.strftime('%I:%M:%S %p')
            if alarm_time and now_time == alarm_time:
                print("Dring Dring")
                break
            print("\n\n         +~~~~~~~~~~~~~~~~~~~+")
            print(f"         |    {re_updated_now}    |")
            print("         +~~~~~~~~~~~~~~~~~~~+\n\n")
            time.sleep(1)

horloge()
