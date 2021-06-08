import telebot
from telebot import types 

bot = telebot.TeleBot('1863921054:AAGbD8-zLX5xDPfMno1d2JY8b-58a3-c1xk')

sum = []

@bot.message_handler(content_types=['text'])

def start(message):
	bot.send_message(message.from_user.id, 'Доброго времени суток! Чтобы начать работу, напиши "Привет".')
	bot.register_next_step_handler(message, get_weight)

def get_weight(message):
	if message.text == 'Привет':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		weight1 = types.KeyboardButton('25')
		weight2 = types.KeyboardButton('50')
		weight3 = types.KeyboardButton('100')
		weight4 = types.KeyboardButton('150')
		weight5 = types.KeyboardButton('200')
		markup.add(weight1, weight2, weight3, weight4, weight5)
		bot.send_message(message.chat.id, 'Выберите вес груза', reply_markup = markup)
		bot.register_next_step_handler(message, get_direct)
	else:
		bot.send_message(message.chat.id, 'Я тебя не понимаю, попробуй ещё раз.')


def get_direct(message):
	if message.text == '25':
		weight = 25
		sum.append(weight)
	elif message.text == '50':
		weight = 50
		sum.append(weight)
	elif message.text == '100':
		weight = 100
		sum.append(weight)
	elif message.text == '150':
		weight = 150
		sum.append(weight)
	else:
		weight = 200
		sum.append(weight)
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	direct1 = types.KeyboardButton('ВВЛ')
	direct2 = types.KeyboardButton('МВЛ')
	markup.add(direct1, direct2)
	bot.send_message(message.chat.id, 'Выберите направление', reply_markup = markup)
	bot.register_next_step_handler(message, get_cargo)

def get_cargo(message):
	if message.text == 'ВВЛ':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		cargoV1 = types.KeyboardButton('Генеральный груз ВВЛ')
		cargoV2 = types.KeyboardButton('Температурный груз ВВЛ')
		cargoV3 = types.KeyboardButton('Живые животные ВВЛ')
		cargoV4 = types.KeyboardButton('Человеческие останки ВВЛ')
		cargoV5 = types.KeyboardButton('Опасный груз ВВЛ')
		markup.add(cargoV1, cargoV2, cargoV3, cargoV4, cargoV5)
		bot.send_message(message.chat.id, 'Выберите тип груза', reply_markup = markup)
		bot.register_next_step_handler(message, get_save)
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		cargoM1 = types.KeyboardButton('Генеральный груз МВЛ')
		cargoM2 = types.KeyboardButton('Температурный груз МВЛ')
		cargoM3 = types.KeyboardButton('Живые животные МВЛ')
		cargoM4 = types.KeyboardButton('Человеческие останки МВЛ')
		cargoM5 = types.KeyboardButton('Опасный груз МВЛ')
		markup.add(cargoM1, cargoM2, cargoM3, cargoM4, cargoM5)
		bot.send_message(message.chat.id, 'Выберите тип груза', reply_markup = markup)
		bot.register_next_step_handler(message, get_save)

def get_save(message):
	if message.text == 'Генеральный груз ВВЛ':
		cargo = 7
		sum.append(cargo)
		save = 2
		sum.append(save)
	elif message.text == 'Температурный груз ВВЛ':
		cargo = 8
		sum.append(cargo)
		save = 3
		sum.append(save)
	elif message.text == 'Живые животные ВВЛ':
		cargo = 8
		sum.append(cargo)
		save = 20
		sum.append(save)
	elif message.text == 'Человеческие останки ВВЛ':
		cargo = 150
		sum.append(cargo)
		save = 13
		sum.append(save)
	elif message.text == 'Опасный груз ВВЛ':
		cargo = 8
		sum.append(cargo)
		save = 3
		sum.append(save)
	elif message.text == 'Генеральный груз МВЛ':
		cargo = 8
		sum.append(cargo)
		save = 3
		sum.append(save)
	elif message.text == 'Температурный груз МВЛ':
		cargo = 10
		sum.append(cargo)
		save = 6
		sum.append(save)
	elif message.text == 'Живые животные МВЛ':
		cargo = 10
		sum.append(cargo)
		save = 30
		sum.append(save)
	elif message.text == 'Человеческие останки МВЛ':
		cargo = 30
		sum.append(cargo)
		save = 16
		sum.append(save)
	else:
		cargo = 14
		sum.append(cargo)
		save = 4
		sum.append(save)
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	save1 = types.KeyboardButton('0')
	save2 = types.KeyboardButton('1')
	save3 = types.KeyboardButton('2')
	save4 = types.KeyboardButton('3')
	save5 = types.KeyboardButton('4')
	save6 = types.KeyboardButton('5')
	markup.add(save1, save2, save3, save4, save5, save6)
	bot.send_message(message.chat.id, 'Выберите срок хранения', reply_markup = markup)
	bot.register_next_step_handler(message, get_direction)

def get_direction(message):
	if message.text == '0':
		time = 0
		sum.append(time)
	elif message.text == '1':
		time = 1
		sum.append(time)
	elif message.text == '2':
		time = 2
		sum.append(time)
	elif message.text == '3':
		time = 3
		sum.append(time)
	elif message.text == '4':
		time = 4
		sum.append(time)
	else:
		time = 5
		sum.append(time)
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	direction1 = types.KeyboardButton('Получение')
	direction2 = types.KeyboardButton('Отправка')
	markup.add(direction1, direction2)
	bot.send_message(message.chat.id, 'Выберите направление операций с грузом', reply_markup = markup)
	bot.register_next_step_handler(message, get_service)

def get_service(message):
	if message.text == 'Получение':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		service1 = types.KeyboardButton('Добавить ускоренную выдачу')
		service2 = types.KeyboardButton('Не добавлять')
		markup.add(service1, service2)
		bot.send_message(message.chat.id, 'Добавить услугу ускоренной выдачи?', reply_markup = markup)
		bot.register_next_step_handler(message, get_service2)
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		service7 = types.KeyboardButton('Добавить консолидацию')
		service8 = types.KeyboardButton('Не добавлять')
		markup.add(service7, service8)
		bot.send_message(message.chat.id, 'Добавить консолидацию?', reply_markup = markup)
		bot.register_next_step_handler(message, get_service5)

def get_service2(message):
	if message.text == 'Добавить ускоренную выдачу':
		serv1 = 1500
		sum.append(serv1)
	else:
		serv1 = 0
		sum.append(serv1)
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	service3 = types.KeyboardButton('Добавить СМС-уведомление о прибытии')
	service4 = types.KeyboardButton('Не добавлять')
	markup.add(service3, service4)
	bot.send_message(message.chat.id, 'Добавить СМС-уведомление о прибытии?', reply_markup = markup)
	bot.register_next_step_handler(message, get_service3)

def get_service3(message):
	if message.text == 'Добавить СМС-уведомление о прибытии':
		serv2 = 100
		sum.append(serv2)
	else:
		serv2 = 0
		sum.append(serv2)
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	service5 = types.KeyboardButton('Добавить доставку')
	service6 = types.KeyboardButton('Не добавлять')
	markup.add(service5, service6)
	bot.send_message(message.chat.id, 'Добавить доставку?', reply_markup = markup)
	bot.register_next_step_handler(message, get_result1)

def get_service5(message):
	if message.text == 'Добавить консолидацию':
		serv4 = 1600
		sum.append(serv4)
	else:
		serv4 = 0
		sum.append(serv4)
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	service9 = types.KeyboardButton('Добавить упаковку груза')
	service10 = types.KeyboardButton('Не добавлять')
	markup.add(service9, service10)
	bot.send_message(message.chat.id, 'Добавить упаковку груза?', reply_markup = markup)
	bot.register_next_step_handler(message, get_service6)

def get_service6(message):
	if message.text == 'Добавить упаковку груза':
		serv5 = 600
		sum.append(serv5)
	else:
		serv5 = 0
		sum.append(serv5)
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	service11 = types.KeyboardButton('Добавить оформление грузоотправительных документов')
	service12 = types.KeyboardButton('Не добавлять')
	markup.add(service11, service12)
	bot.send_message(message.chat.id, 'Добавить оформление грузоотправительных документов?', reply_markup = markup)
	bot.register_next_step_handler(message, get_result2)

def get_result1(message):
	if message.text == 'Добавить доставку':
		serv3 = 800
		sum.append(serv3)
	else:
		serv3 = 0
		sum.append(serv3)
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	result = types.KeyboardButton('Рассчитать стоимость')
	markup.add(result)
	bot.send_message(message.chat.id, 'Нажмите на кнопку', reply_markup = markup)
	bot.register_next_step_handler(message, result1)

def get_result2(message):
	if message.text == 'Добавить оформление грузоотправительных документов':
		serv6 = 1500
		sum.append(serv6)
	else:
		serv6 = 0
		sum.append(serv6)
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	result = types.KeyboardButton('Рассчитать стоимость')
	markup.add(result)
	bot.send_message(message.chat.id, 'Нажмите на кнопку', reply_markup = markup)
	bot.register_next_step_handler(message, result2)

def result1(message):
	res1 = int((sum[0]*sum[1])+(sum[2]*sum[3]*sum[0])+sum[4]+sum[5]+sum[6])
	bot.send_message(message.chat.id, res1)

def result2(message):
	res2 = int((sum[0]*sum[1])+(sum[2]*sum[3]*sum[0])+sum[4]+sum[5]+sum[6])
	bot.send_message(message.chat.id, res2)

bot.polling()
