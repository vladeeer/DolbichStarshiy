import random
from Jokes import *
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
        
    elif(lookFor(["олег","олеж"], user_message)):
        resp.append(random.choice(["Я нэ понил","Ээээ"]))
        resp.append(random.choice(["За Алежу тоби пизида","Ево не трогой ато наиду","За Алежу и дывор стреляйу вупор"]))

    elif(lookFor(["шут","анекд","юмор"], user_message)):
        resp.append(random.choice(["Хочиш пасмиаца?","Разкажыу анегдот","Есть у миня шутка"]))
        resp = resp + random.choice(jokes)
        resp.append(random.choice(["Правда смишно?","Апаахпхз","Понел?!)))","Пахаха"]))
        resp.append(random.choice(["Маиа любимая","Абажаю эту шутыку","","","",""])) 

    elif(lookFor(["пасиб","спс","благод"], user_message)):
        resp.append(random.choice(["Незашта","Нестоет"]))
        resp.append(random.choice(["Рат был стараца","Всигда пажаласта"]))

    elif(lookFor(["иди ","пош","нах"], user_message)):
        resp.append(random.choice(["Куда","Эээ сам иди","А ты неахуел"]))
        resp.append(random.choice(["К маме тваей пайду",""]))

    elif(lookFor(["лох","пид","придур","баран","идио","сук","дурак","мраз","дубин","уёб","уебан","даун","ебанут","оёб","урод","суч"], user_message)):
        resp.append(random.choice(["Ээээ","Слыш мудила","Ты че баран","Слыш агрызак капусты","Ты че","Што ты сичас сказал"]))
        resp.append(random.choice(["Я тибя найду", "А ты ни ахуэл","Овца тупая","Я тибя вычеслю уебак","ديك مص"]))
        resp.append(random.choice(["Атветиш за слава","Рот патом не актроеж","Капсда тебе","",""]))
    
    elif(lookFor(["прив","добр","здра","сал","йо","даро","хай","ку"], user_message)):
        resp.append(random.choice(["И еcчо рас здравстуйти", "Да здастуйте", "Салам","Привет","Салам алейкум","Ассаля́му але́йкум","اَلسَّلَامُ عَلَيْكُمُ‏"]))
        resp.append(random.choice(["Са мной ретка сдароваюса","","","","","","",""]))

    elif(lookFor(["пока","проща","свид","счастливо"], user_message)):
        resp.append(random.choice(["Даваи","Сычаслива","Давай","Уадчи"]))

    elif(lookFor(["че","чо","ээ","непон","чё"], user_message)):
        resp.append(random.choice(["Ты чо борзый","Слыш ты че","Харэ дрожнить","Ээ",""]))
        resp.append(random.choice(["Я не всекда такоц добрый","Атхватить так можеж","",""]))

    elif (lookFor(["зовут","звать","назыв","имя","кто"], user_message)):
        resp.append(random.choice(["Я абдула","Абдула мама звола",""]))
        resp.append(random.choice(["Друзья завут Дюдя как член каня",""]))

    elif (lookFor(["врем","час"], user_message)):
        now = datetime.now()
        date_time = now.strftime("%H %M")
        resp.append(random.choice(["Сичас ","У миня на чисах ","Друк сказыал "])+str(date_time))
        
    elif("?" in user_message):
        resp.append(random.choice(["Да","Нет","Наверна","Я не знаьу","Ага","Нее","Канешна"])) 
        resp.append(random.choice(["А ты","хатя может быть","А сам","","","",""])) 

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




