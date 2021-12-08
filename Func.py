import random
from datetime import datetime

def lookFor(a,b):
    return (lambda a, b : any(i in b for i in a))(a, b)

def message_responses(input_text, user_name):
    user_message = str(input_text).lower()
    resp = []
    print(str(user_name) + ": " + str(input_text))

    if(lookFor(["влад","сер"], user_message)):
        resp.append(random.choice(["Ээ брат","Нетрогаи Влада","Ща пизды палучиш"]))
        resp.append(random.choice(["За Влада и дывор стреляйу вупор","Паясьни за Влада","Я за ниго гарой"]))
        
    elif(lookFor(["леш","лёх","лёш"], user_message)):
        resp.append(random.choice(["Я нэ понил","ээээ"]))
        resp.append(random.choice(["за лёху тоби пизида","ево не трогой ато наиду"]))

    elif(lookFor(["иди ","пош","нах"], user_message)):
        resp.append(random.choice(["куда","эээ сам иди","а ты неахуел"]))
        resp.append(random.choice(["К маме тваей пайду",""]))

    elif(lookFor(["лох","пид","придур","баран","идио","сук","дурак","мраз","дубин","уёб","уебан","даун","ебанут","оёб"], user_message)):
        resp.append(random.choice(["Ээээ","Слыш мудила","Ты че баран","Слыш агрызак капусты","Ты че"]))
        resp.append(random.choice(["Я тибя найду", "А ты ни ахуэл","Овца тупая","Я тибя вычеслю уебак","ديك مص"]))
        resp.append(random.choice(["Атветиш за слава","Рот патом не актроеж","Капсда тебе","",""]))

    elif(lookFor(["прив","добр","здра","сал","йо","даро","хай","ку"], user_message)):
        resp.append(random.choice(["И еcчо рас здравстуйти", "Да здастуйте", "Салам","Привет","Салам алейкум"]))
        resp.append(random.choice(["Са мной редка сдароваюса","","","","","",""]))

    elif(lookFor(["че","чо","ээ","непон","чё"], user_message)):
        resp.append(random.choice(["ты чо борзый","слыш ты че","харэ дрожнить","Ээ",""]))
        resp.append(random.choice(["Я не всекда такоц добрый","Атхватить так можеж","",""]))

    elif (lookFor(["зовут","звать","назыв","имя","кто"], user_message)):
        resp.append(random.choice(["Я абдула","Абдула мама звола",""]))
        resp.append(random.choice(["Друзья завут Дюдя как член каня",""]))
        
    elif("?" in user_message):
        resp.append(random.choice(["Да","Нет","Наверна","Я не знаьу","Ага","Нее","Канешна"])) 
        resp.append(random.choice(["А ты","хатя может быть","А сам","","","",""])) 

    elif user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        resp.append(str(date_time))

    if (len(resp)==0):
        resp = [random.choice(["Непонел","Чо","Гавари нармальна","Эээээ","Я плоха панимаю","Эээ","Говари нармальна пажалуста","Я не панимаю","Че","А","Паруски скажы"])]
        resp.append(random.choice(["Павтари пажуста","Што эта значит","Павтари пажалуста","","","","",""]))

    for i in resp:
        if(i==""):
        	continue
        print("Bot: " + i)
    return resp

def message_edited():
    resp = []
    resp.append(random.choice(["Ты че","Ты это","Нену харэ",""]))
    resp.append(random.choice(["Чо редактируэш","Соабшение не миняй"]))
    resp.append(random.choice(["Заибал ужэ","Не нажо так","",""]))
    return resp




