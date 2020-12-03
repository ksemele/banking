from random import randint


class Account:
	card_num = ''
	pin = ''
	balance = 0

	def __init__(self):
		pass

	def empty(self):
		self.card_num = ''
		self.pin = ''
		self. balance = 0

	def new_account(self):
		self.rand_card_number()
		self.rand_pin()

	def rand_card_number(self):
		# self.card_num = '400000' + ''.join(str(randint(0, 9)) for i in range(10))  # wow!
		self.card_num = '400000' + ''.join(str(randint(0, 9)) for i in range(9))  # wow!
		self.calc_luhn_last()

	def rand_pin(self):
		self.pin = ''.join(str(randint(0, 9)) for i in range(4))

	def calc_luhn_last(self):  # todo in work
		checksum = []
		odd = 1
		for each in self.card_num:
			if odd:
				checksum.append(int(each) * 2)
				odd = 0
			else:
				checksum.append(int(each))
				odd = 1
		for each in checksum:
			if int(each) > 9:
				checksum[checksum.index(each)] = each - 9
		res = 0
		for each in checksum:
			res = res + int(each)
		calc = res
		while calc % 10:
			calc += 1
		self.card_num = self.card_num + ''.join(str(calc - res))

	def print_balance(self):
		print(f'Balance: {self.balance}\n')

	def __str__(self):
		return 'Your card number:\n{}\nYour card PIN:\n{}\n'.format(self.card_num, self.pin)


def is_odd(num):
	if num % 2:
		return True  # Odd (нечетное)
	else:
		return False  # Even (четное)

class Storage:
	__instance__ = None
	cards = []
	cards_counter = 0
	login_in = Account()

	def __init__(self):
		if Storage.__instance__ is None:
			Storage.__instance__ = self
		else:
			raise Exception("Storage already created!")

	@staticmethod
	def get_instance():
		# Статический метод для того, чтобы вытащить текущий экземпляр
		# При извлечении объекта с помощью метода get_instance() мы проверяем,
		# доступен ли существующий экземпляр, и возвращаем его.
		# Если нет, то создаем его и опять возвращаем.
		if not Storage.__instance__:
			Storage()
		return Storage.__instance__

	def add_card(self, new_card):
		self.cards.append(new_card)

	def create_account(self):
		new_card = Account()
		new_card.new_account()
		if new_card.card_num in [x.card_num for x in self.cards]:
			new_card.rand_card_number()
		self.add_card(new_card)
		print(new_card)

	def search_card_pin(self, card_num):
		passbase = {c.card_num: c.pin for c in self.cards}
		if self.cards_counter > 0 and card_num in passbase:
			storage.login_in.card_num = card_num
			storage.login_in.pin = passbase[card_num]
			return passbase[card_num]
		else:
			return None


class MenuMain:
	elems = ['1. Create an account', '2. Log into account', '0. Exit']

	def __init__(self):
		pass

	def print(self):
		for each in self.elems:
			print(each)


def menu_main_choice_treat(choice):
	if choice == '0':  # exit
		print('Bye!')
	elif choice == '1':  # create account
		storage = Storage.get_instance()
		storage.create_account()
		storage.cards_counter += 1
	elif choice == '2':  # login
		menu_login_treat()
	else:
		print('Wrong choice\n')


class MenuLogin:
	elems = ['1. Balance', '2. Log out', '0. Exit']

	def __init__(self):
		pass

	def print(self):
		for each in self.elems:
			print(each)


def menu_login_treat():
	choice = ''
	if try_login():
		storage = Storage.get_instance()
		print('You have successfully logged in!\n')
		while choice != '0':
			menu_login.print()
			choice = input()
			if choice == '1':  # balance
				storage.login_in.print_balance()
			if choice == '2':  # Log out
				storage.login_in.empty()
				print('You have successfully logged out!\n')
				choice = '0'
			if choice == '0':
				exit()
	else:
		print('Wrong card number or PIN!\n')


def try_login():
	storage = Storage.get_instance()
	print('Enter your card number:')
	card_num = input()
	print('Enter your PIN:')
	pin = input()
	if storage.search_card_pin(card_num) is not None:
		storage.logged_in = card_num
		if storage.login_in.pin == pin:
			return True
	else:
		return False


storage = Storage()
menu = MenuMain()
menu_login = MenuLogin()
choice = ''
while choice != '0':
	menu.print()
	choice = input()
	menu_main_choice_treat(choice)