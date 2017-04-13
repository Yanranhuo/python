try:
	inp = raw_input("Enter Score: ")
	score = float(inp)
	if (score > 1.0):
		Score = "error"
	elif (score >= 0.9):
		Score = "A"
	elif (score >= 0.8):
		Score = "B"
	elif (score >= 0.7):
		Score = "C"
	elif (score >= 0.6):
		Score = "D"
	elif (score < 0.6):
		Score = "F"
		print Score
except:
    print "please enter numercial numbers"
    