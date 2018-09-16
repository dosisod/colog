from colorama import Fore, Back

class colog:
	def __init__(self, inv=False):
		self.inv=inv   #if True, invert color of message
		self.char=": " #character(s) to display between "warning lvl" and "msg"

		self.FG=0 #used to get var from color pairs
		self.BG=1 #eg: self.BLUE[self.FG]

		self.BLACK=[Fore.BLACK, Back.BLACK] #putting foreground and background into a single obj
		self.BLUE=[Fore.BLUE, Back.BLUE]
		self.CYAN=[Fore.CYAN, Back.CYAN]
		self.GREEN=[Fore.GREEN, Back.GREEN]
		self.LIGHTBLACK=[Fore.LIGHTBLACK_EX, Back.LIGHTBLACK_EX]
		self.LIGHTBLUE=[Fore.LIGHTBLUE_EX, Back.LIGHTBLUE_EX]
		self.LIGHTCYAN=[Fore.LIGHTCYAN_EX, Back.LIGHTCYAN_EX]
		self.LIGHTGREEN=[Fore.LIGHTGREEN_EX, Back.LIGHTGREEN_EX]
		self.LIGHTMAGENTA=[Fore.LIGHTMAGENTA_EX, Back.LIGHTMAGENTA_EX]
		self.LIGHTRED=[Fore.LIGHTRED_EX, Back.LIGHTRED_EX]
		self.LIGHTWHITE=[Fore.LIGHTWHITE_EX, Back.LIGHTWHITE_EX]
		self.LIGHTYELLOW=[Fore.LIGHTYELLOW_EX, Back.LIGHTYELLOW_EX]
		self.MAGENTA=[Fore.MAGENTA, Back.MAGENTA]
		self.RED=[Fore.RED, Back.RED]
		self.RESET=[Fore.RESET, Back.RESET]
		self.WHITE=[Fore.WHITE, Back.WHITE]
		self.YELLOW=[Fore.YELLOW, Back.YELLOW]

	def display(self, msg, lvl, color, black=True): #pass log message, color obj, and black/white FG
		if self.inv:
			s=color[self.BG]      #if inverted use color as BG
			if black:             #if inverted and black is set, display black FG
				s+=Fore.BLACK #
			else:                 #else, display a whiite FG
				s+=Fore.WHITE
		else:
			s=color[self.FG] #if not inverted, simply display color
		print(s + lvl + self.char + msg + Fore.RESET + Back.RESET) #display error lvl and message

	def gold(self, string): #very important output data
		self.display(string, "GOLD", self.YELLOW)

	def fatal(self, string): #fatal error
		self.display(string, "FATAL", self.RED, False)

	def info(self, string): #noteable info/other info
		self.display(string, "INFO", self.LIGHTBLUE)

	def good(self, string): #passes check or other
		self.display(string, "GOOD", self.LIGHTGREEN)

	def warn(self, string): #warning/fail
		self.display(string, "WARN", self.LIGHTRED)

	def dep(self, string): #deprecated error
		self.display(string, "DEPRECATED", self.MAGENTA, False)
