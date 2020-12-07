import telebot
from telebot import types





rayon_spisok = ["район 1","район 2","район 3","район 4",
				"район 5","район 6","район 7","район 8","район 9","район 10"]
#Указываем полный список районов



what_spisok = ["наркотик 1","наркотик 2","наркотик 3","наркотик 4","наркотик 5",
                "наркотик 6","наркотик 7","наркотик 8","наркотик 9","наркотик 10"]
#Указываем полный список товара


keyboard = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="Проверить оплату", callback_data="Проверить оплату")
keyboard.row(but_1)



what = types.ReplyKeyboardMarkup(True, False)
cocamq1 = types.KeyboardButton("наркотик 1")
cocamq2 = types.KeyboardButton("наркотик 2")
cocahq03 = types.KeyboardButton("наркотик 3")
cocahq05 = types.KeyboardButton("наркотик 4")
cocahq1 = types.KeyboardButton("наркотик 5")
cocahq15 = types.KeyboardButton("наркотик 6")
back = types.KeyboardButton("Назад")
what.row(cocamq1)
what.row(cocamq2)
what.row(cocahq03)
what.row(cocahq05)
what.row(cocahq1)
what.row(cocahq15)
what.row(back)




start = telebot.types.ReplyKeyboardMarkup(True, False)
start.row('Информация')
start.row('Покупки', 'Мой кабинет')
start.row('Доступный ассортимент')


start2 = telebot.types.ReplyKeyboardMarkup(True, False)
start2.row('Информация')
start2.row('Покупки', 'Мой кабинет')
start2.row('Доступный ассортимент')
start2.row('Админ-Панель')


city = telebot.types.ReplyKeyboardMarkup(True, False)
city.row('Москва', 'Санкт-Петербург', 'Екатеринбург')
city.row('Домодедово', 'Мытищи', 'Зеленоград')
city.row('Подольск', 'Челябинск', 'Нижний Новгород')
city.row('Иркутск', 'Оренбург', 'Пенза')
city.row('Омск', 'Пермь', 'Рязань')
city.row('Назад')



admin = telebot.types.ReplyKeyboardMarkup(True, False)
admin.row('Рассылка', 'Баланс')
admin.row('Назад')


krekin = telebot.types.ReplyKeyboardMarkup(True, False)
krekin.row('Отправить новое сообщение')
krekin.row('Назад')



rayon_msk = types.ReplyKeyboardMarkup(True, False)
msk_cao = types.KeyboardButton("район 1")
msk_sao = types.KeyboardButton("район 2")
msk_vao = types.KeyboardButton("район 3")
msk_svao = types.KeyboardButton("район 4")
msk_uvao = types.KeyboardButton("район 5")
msk_zao = types.KeyboardButton("район 6")
msk_yao = types.KeyboardButton("район 7")
back = types.KeyboardButton("Назад")
rayon_msk.row(msk_cao, msk_sao, msk_zao, msk_yao)
rayon_msk.row(msk_svao, msk_uvao)
rayon_msk.row(back)


rayon_spb = types.ReplyKeyboardMarkup(True, False)
spb_vib = types.KeyboardButton("район 1")
spb_msk = types.KeyboardButton("район 2")
spb_petrodvor = types.KeyboardButton("район 3")
spb_kuror = types.KeyboardButton("район 4")
spb_prim = types.KeyboardButton("район 5")
spb_push = types.KeyboardButton("район 6")
spb_petrograd = types.KeyboardButton("район 7")
spb_vas = types.KeyboardButton("район 8")
spb_krasn = types.KeyboardButton("район 9")
spb_nevsk = types.KeyboardButton("район 10")
back = types.KeyboardButton("Назад")
rayon_spb.row(spb_vib, spb_msk)
rayon_spb.row(spb_petrodvor, spb_kuror)
rayon_spb.row(spb_prim, spb_push)
rayon_spb.row(spb_petrograd, spb_vas)
rayon_spb.row(spb_krasn, spb_nevsk)
rayon_spb.row(back)


rayon_ekb = types.ReplyKeyboardMarkup(True, False)
spb_verh = types.KeyboardButton("район 1")
spb_zhele = types.KeyboardButton("район 2")
spb_ordzh = types.KeyboardButton("район 3")
spb_oktyabr = types.KeyboardButton("район 4")
spb_chkal = types.KeyboardButton("район 5")
spb_lenin = types.KeyboardButton("район 6")
spb_kirov = types.KeyboardButton("район 7")
back = types.KeyboardButton("Назад")
rayon_ekb.row(spb_verh, spb_zhele)
rayon_ekb.row(spb_ordzh, spb_oktyabr)
rayon_ekb.row(spb_chkal, spb_lenin)
rayon_ekb.row(spb_kirov)
rayon_ekb.row(back)


rayon_voronezh = types.ReplyKeyboardMarkup(True, False)
voronezh_zhele = types.KeyboardButton("район 1")
voronezh_centr = types.KeyboardButton("район 2")
voronezh_komin = types.KeyboardButton("район 3")
voronezh_lenin = types.KeyboardButton("район 4")
voronezh_sovet = types.KeyboardButton("район 5")
voronezh_levober = types.KeyboardButton("район 6")
back = types.KeyboardButton("Назад")
rayon_voronezh.row(voronezh_zhele, voronezh_centr)
rayon_voronezh.row(voronezh_komin, voronezh_lenin)
rayon_voronezh.row(voronezh_sovet, voronezh_levober)
rayon_voronezh.row(back)


rayon_novosib = types.ReplyKeyboardMarkup(True, False)
navosib_zhele = types.KeyboardButton("район 1")
navosib_zael = types.KeyboardButton("район 2")
navosib_kalin = types.KeyboardButton("район 3")
navosib_kirov = types.KeyboardButton("район 4")
navosib_oktyab = types.KeyboardButton("район 5")
navosib_lenin = types.KeyboardButton("район 6")
navosib_pervo = types.KeyboardButton("район 7")
navosib_sovet = types.KeyboardButton("район 8")
back = types.KeyboardButton("Назад")
rayon_novosib.row(navosib_zhele, navosib_zael)
rayon_novosib.row(navosib_kalin, navosib_kirov)
rayon_novosib.row(navosib_oktyab, navosib_lenin)
rayon_novosib.row(navosib_pervo, navosib_sovet)
rayon_novosib.row(back)


rayon_perm = types.ReplyKeyboardMarkup(True, False)
perm_dzer = types.KeyboardButton("район 1")
perm_indu = types.KeyboardButton("район 2")
perm_kirov = types.KeyboardButton("район 3")
perm_lenin = types.KeyboardButton("район 4")
perm_motov = types.KeyboardButton("район 5")
back = types.KeyboardButton("Назад")
rayon_perm.row(perm_dzer, perm_indu)
rayon_perm.row(perm_kirov, perm_lenin)
rayon_perm.row(perm_motov)
rayon_perm.row(back)





operator = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="Тех.Поддержка", url="ССЫЛКА")
operator.row(but_1)
