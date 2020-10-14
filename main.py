import eel

# Initializing GUI Library
eel.init('gui')

@eel.expose
def check_rfid():
	'''
	Function checks if an rfid is present
	'''
	pass

	# if (rfid):
	# 	# match with database
	# 	if (matched):
	# 		# move to next page and fetch user details
	# 	else:
	# 		# rfid invalid

@eel.expose
def check_pin(pin):
	'''
	Function checks if pin is correct or not
	'''
	pass

@eel.expose
def check_fingerprint(data):
	'''
	Functin checks if fingerprint matched or not
	'''
	pass

	# if (matched):
	# 	return True
	# else:
	# 	return False

@eel.expose
def cast_vote(cadidate_index):
	'''
	Function casts vote for the selected candidate
	'''
	pass
	

eel.start('index.html', size=(1000,600))