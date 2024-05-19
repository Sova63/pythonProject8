class User:
	__name:str
	__second_name:str

	def __init__(self,name,second_name):
		self.__name = name
		self.__second_name = second_name

		def get_name(self):
			return self.__name
		def set_name(self,name):
			self.__name = name
		def get_second_name(self):
			return self.__name
		def set_second_name(self,second_name):
			self.__second_name = second_name