import argparse
import signal

from main import Cripto_change



# Объявляем параметр командной строки для определения нужной комманды
parser = argparse.ArgumentParser()
parser.add_argument(dest='command', type=str)
args = parser.parse_args()

bot = Cripto_change()

# Назначаем функцию, ответсвенную за обработку CTRL-C
signal.signal(signal.SIGINT, bot.sigint_handler)

if args.command == 'run':
    bot.run()
