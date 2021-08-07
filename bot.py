from vkwave.bots import SimpleLongPollBot, SimpleBotEvent
from vkwave.bots.utils.keyboards.keyboard import Keyboard
from vkwave.bots.utils.keyboards.keyboard import ButtonColor
from vkwave.bots.core.dispatching import filters

import vk_api

from config import *
from MyTextBot import *
from CheckFun import *

bot = SimpleLongPollBot(tokens=token, group_id=group_id)

session = vk_api.VkApi(token=access_token)


def keyboar(num=0):
    if num == 0:
        payload = {"button": "начать"}
        kb = Keyboard()
        kb.add_text_button("Начать", color=ButtonColor.PRIMARY, payload = {"button": "начать"})
        return kb

    if num == 1:
        kb= Keyboard()
        kb.add_text_button("Информация", color=ButtonColor.PRIMARY, payload = {"button": "инфо"})
        kb.add_row()
        kb.add_text_button("Донат", color=ButtonColor.POSITIVE, payload = {"button": "донат"})
        kb.add_text_button("Помощь", color=ButtonColor.NEGATIVE, payload = {"button": "помощь"})
        kb.add_row()
        kb.add_text_button("Как начать играть?", color=ButtonColor.SECONDARY, payload = {"button": "играть"})
        return kb

    if num == 2:
        kb= Keyboard()
        kb.add_text_button("Информация", color=ButtonColor.PRIMARY, payload = {"button": "хелп_помощь"})
        kb.add_row()
        kb.add_text_button("Жалоба", color=ButtonColor.NEGATIVE, payload = {"button": "жалоба"})
        kb.add_text_button("Сотрудничество", color=ButtonColor.POSITIVE, payload = {"button": "сотруд"})
        kb.add_row()
        kb.add_text_button("Как стать админом?", color=ButtonColor.NEGATIVE, payload={"button": "яадмин"})
        kb.add_text_button("Как стать лидером?", color=ButtonColor.POSITIVE, payload={"button": "ялидер"})
        kb.add_row()
        kb.add_text_button("Вернутся в главное меню", color=ButtonColor.SECONDARY, payload = {"button": "гменю"})
        return kb

    if num == 3:
        kb= Keyboard()
        kb.add_text_button("Жалоба на админа", color=ButtonColor.NEGATIVE, payload = {"button": "жадмин"})
        kb.add_text_button("Жалоба на игрока", color=ButtonColor.NEGATIVE, payload = {"button": "жигрок"})
        kb.add_row()
        kb.add_text_button("Вернутся назад", color=ButtonColor.SECONDARY, payload = {"button": "жназад"})
        return kb

    if num == 4:
        kb= Keyboard()
        kb.add_text_button("Информация", color=ButtonColor.PRIMARY, payload = {"button": "админинф"})
        kb.add_row()
        kb.add_text_button("Бот", color=ButtonColor.NEGATIVE, payload = {"button": "настройкибота"})
        kb.add_text_button("Последние обновления", color=ButtonColor.POSITIVE, payload = {"button": "db"})
        kb.add_row()
        kb.add_text_button("Вернутся в главное меню", color=ButtonColor.SECONDARY, payload = {"button": "гменю"})
        return kb


@bot.message_handler(filters.PayloadFilter({"button": "инфо"}))
async def start(event: SimpleBotEvent):
    await event.answer(glav_info, keyboard=keyboar(1).get_keyboard())

@bot.message_handler(filters.PayloadFilter({"button": "начать"}))
async def start(event: SimpleBotEvent):
    await event.answer("Вы вошли в главное меню бота!", keyboard=keyboar(1).get_keyboard())

@bot.message_handler(filters.PayloadFilter({"button": "играть"}))
async def start(event: SimpleBotEvent):
    await event.answer(bt_play, keyboard=keyboar(1).get_keyboard())

@bot.message_handler(filters.PayloadFilter({"button": "донат"}))
async def start(event: SimpleBotEvent):
    await event.answer(donate, keyboard=keyboar(1).get_keyboard())

@bot.message_handler(filters.TextFilter(greeting))
async def only_greetings_in_text(event: SimpleBotEvent):
    await event.answer("Привет! Чтобы активировать бота нажмите кнопку \"Начать\"", keyboard=keyboar().get_keyboard())

@bot.message_handler(filters.PayloadFilter({"button": "помощь"}))
async def helper(event: SimpleBotEvent):
    await event.answer("Вы перешли в раздел \"Помощь\"", keyboard=keyboar(2).get_keyboard())

@bot.message_handler(filters.PayloadFilter({"button": "гменю"}))
async def helper(event: SimpleBotEvent):
    await event.answer("Вы вернулись в главное меню", keyboard=keyboar(1).get_keyboard())

@bot.message_handler(filters.PayloadFilter({"button": "жалоба"}))
async def helper(event: SimpleBotEvent):
    await event.answer("Вы перешли в раздел \"Жалоба\"", keyboard=keyboar(3).get_keyboard())

@bot.message_handler(filters.PayloadFilter({"button": "сотруд"}))
async def helper(event: SimpleBotEvent):
    await event.answer(sot, keyboard=keyboar(2).get_keyboard())

@bot.message_handler(filters.PayloadFilter({"button": "яадмин"}))
async def helper(event: SimpleBotEvent):
    await event.answer(ds_admin, keyboard=keyboar(2).get_keyboard())

@bot.message_handler(filters.PayloadFilter({"button": "ялидер"}))
async def helper(event: SimpleBotEvent):
    await event.answer(ds_leader, keyboard=keyboar(2).get_keyboard())

@bot.message_handler(filters.PayloadFilter({"button": "хелп_помощь"}))
async def helper(event: SimpleBotEvent):
    await event.answer(info_serv, keyboard=keyboar(2).get_keyboard())

@bot.message_handler(filters.PayloadFilter({"button": "жадмин"}))
async def start(event: SimpleBotEvent):
    await event.answer(com_admin, keyboard=keyboar(3).get_keyboard())

@bot.message_handler(filters.PayloadFilter({"button": "жигрок"}))
async def start(event: SimpleBotEvent):
    await event.answer(com_player, keyboard=keyboar(3).get_keyboard())

@bot.message_handler(filters.PayloadFilter({"button": "жназад"}))
async def helper(event: SimpleBotEvent):
    await event.answer("Вы вернулись в раздел \"Помощь\"", keyboard=keyboar(2).get_keyboard())

@bot.message_handler(filters.CommandsFilter(["bot","бот","инфо","ище"], prefixes=("!")))
async def admin_panel(event: SimpleBotEvent):
    await event.answer("Справка о боте.", keyboard=keyboar(4).get_keyboard())

@bot.message_handler(filters.CommandsFilter("статус", prefixes=("!")))
async def admin_panel(event: SimpleBotEvent):

    def user_status(user_id):
        status = session.method(f"status.get", {'user_id': user_id})
        if status['text']:
            return status['text']

    text = event.text.split()
    user_id = event.from_id

    if len(text) == 1:
        await event.answer(user_status(user_id))

    if len(text) == 2:
        await event.answer(user_status(text[1]))

@bot.message_handler(filters.CommandsFilter('1', prefixes=">"))
async def id_user_groups(event: SimpleBotEvent):
    groups = session.method("groups.getMembers", {"group_id": 'streetrrp'} )
    items = groups['items']
    for i in range(len(items)):
        print(items[i])

    #group = session.method("groups.getById", tuple(items))
    #await event.answer(group)
    await event.answer(groups["items"][:50])
    await event.answer(groups["items"][50:100])


@bot.message_handler(filters.CommandsFilter('2', prefixes=">"))
async def send(event: SimpleBotEvent):
    text = " ".join(event.text.split()[1:])
    author = event.from_id

    par = {
        #'user_id': 656343676,
        'peer_id': 2000000000 + 40,
        'chat_id': 40,
        'random_id': 0,
        'message': text,
        'group_id': group_id
    }
    send_mes = session.method("messages.send", par)
    await event.answer(text)

@bot.message_handler(filters.CommandsFilter("donatstreet", prefixes=("#")))
async def admin_panel(event: SimpleBotEvent):
    text= event.text
    if ch_donate(text):
        link = "https://vk.com/id" + str(event.from_id)
        users = session.method('users.get', {'user_ids': event.from_id})
        name = users[0]['first_name']
        last_name = users[0]['last_name']
        info = f"Отправитель\nИмя: {name}\nФамилия: {last_name}\nСсылка на ВК: {link}"
        text = "#donate" + text[13:] + "\n\n\n" + info
        await event.answer("Сообщение отправлено!")
        par = {
            'user_id': 656343676,
            #'peer_id': 2000000000 + 40,
            #'peer_ids': 205463730,
            'chat_id': 1,
            'random_id': 0,
            'message': text,
            'group_id': group_id,
            'intent': "default"
        }
        session.method("messages.send", par)

    else:
        await event.answer("Вы заполнили форму с ошибками! Попробуйте снова")
    #await event.answer("Справка о боте.", keyboard=keyboar(1).get_keyboard())

@bot.message_handler(filters.CommandsFilter("comadmin", prefixes=("#")))
async def admin(event: SimpleBotEvent):
    print(event.from_id)
    text= event.text
    if ch_admin(text):
        link = "https://vk.com/id" + str(event.from_id)
        users = session.method('users.get', {'user_ids': event.from_id})
        name = users[0]['first_name']
        last_name = users[0]['last_name']
        info = f"Отправитель\nИмя: {name}\nФамилия: {last_name}\nСсылка на ВК: {link}"
        text = "#жал_на_админа" + text[9:] + "\n\n\n" + info
        await event.answer("Сообщение отправлено!")
        par = {
            'user_id': 656343676,
            #'peer_id': 2000000000 + 40,
            #'peer_ids': 205463730,
            'chat_id': 1,
            'random_id': 0,
            'message': text,
            'group_id': group_id,
        }
        session.method("messages.send", par)

    else:
        await event.answer("Вы заполнили форму с ошибками! Попробуйте снова")
    #await event.answer("Справка о боте.", keyboard=keyboar(1).get_keyboard())

@bot.message_handler(filters.CommandsFilter("complayer", prefixes=("#")))
async def player(event: SimpleBotEvent):
    print(event.from_id)
    text= event.text
    print(text)
    if ch_player(text):
        link = "https://vk.com/id" + str(event.from_id)
        users = session.method('users.get', {'user_ids': event.from_id})
        name = users[0]['first_name']
        last_name = users[0]['last_name']
        info = f"Отправитель\nИмя: {name}\nФамилия: {last_name}\nСсылка на ВК: {link}"
        text = "#жал_на_игрока" + text[10:] + "\n\n\n" + info
        await event.answer("Сообщение отправлено!")
        par = {
            'user_id': 656343676,
            #'peer_id': 2000000000 + 40,
            #'peer_ids': 205463730,
            'chat_id': 1,
            'random_id': 0,
            'message': text,
            'group_id': group_id,
        }
        session.method("messages.send", par)

    else:
        await event.answer("Вы заполнили форму с ошибками! Попробуйте снова")
    #await event.answer("Справка о боте.", keyboard=keyboar(1).get_keyboard())

@bot.message_handler(filters.CommandsFilter("com", prefixes=("#")))
async def player(event: SimpleBotEvent):
    print(event.from_id)

bot.run_forever()