from googletrans import Translator

def translate(matn)
translator = Translator()
til = translator . detect(matn).lang
if til=='eng' :
	return translator . translate(matn , dest= 'uz' ) . text
	else:
		return translator . translate(matn,dest='en' ) . text
		from translate import translate 
		import telebot
		TOKEN = "5066752655:AAFvHx_u2OdCMOr3guT-CLfmljBvFyr3lWk"
		tarjimonbot = telebot.TeleBot(token=TOKEN)
		@Tarjimonbot.message_handler(commands=['start'])
		def salom(message) :
			xabar = "Assalomu alaykum , tarjimon botga xush kelibsiz ."
			xabar += ' \n Matningizni yuboring. '
			tarjimonbot.reply_to( message , xabar )
			tarjimonbot.polling()
