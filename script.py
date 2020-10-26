import random
import numpy as np

loop_counter = 0
no_of_user = 8

no_of_duty = [0 for i in range(no_of_user)]

duty = [
	#Mo	Ev Ni
	[0, 0, 0], #Sun
	[0, 0, 0], #Mon
	[0, 0, 0], #Tue
	[0, 0, 0], #Wed
	[0, 0, 0], #Thu
	[0, 0, 0], #Fri
	[0, 0, 0] #Sat
]

def get_per_head_duty():
	per_head_duty = (7 * 3)/no_of_user
	if per_head_duty > int(per_head_duty):
		per_head_duty =  int(per_head_duty) + 1
	else:
		per_head_duty =  int(per_head_duty)

	return per_head_duty


def possable(y, x, user): # row, col
	print(y, x, user, end=" => ")
	global duty


	for i in range(3):
		if duty[y][i] == user:
			print("False 	//Same Day")
			return False


	if no_of_duty[user -1] >= get_per_head_duty():
		print("False 	//More Duty")
		return False


	if y > 0 and duty[y-1][2] == user:
		print("False 	//Yesterday Night")
		return False


	if (y+1) < 7:
		for i in range(3):
			if duty[y+1][i] == user:
				print("False 	//Tomorrow Duty, No night today")
				return False


	###############   test ####################
	if x == 2 and user == 5:
		print("False 	//user 5 not took night")
		return False

	if x == 0 and user == 3:
		print("False 	//user 3 not took mornig")
		return False

	if y == 5 and user == 2:
		print("False 	//Special day off")
		return(False)

	# if user == 5:
	# 	print("False 	//Full off")
	# 	return(False)
	###############   test ####################
	print("True")
	return True


def evalute():
	global duty
	flag = 0
	for temp in range(1,no_of_user+1):
		counter = 0
		for y in range(7):
			for x in range(3):
				if duty[y][x] == temp:
					counter += 1
				if duty[y][x] == 0:
					flag = 1
		no_of_duty[temp - 1] = counter
		# print(temp, " => ", counter)
	return flag


def get_random(start, end):
	return random.randint(start,end)


def get_random_user(exp=[]):
	while True:
		usr = get_random(1,no_of_user)
		if usr not in exp:
			break
	return usr

# def calculate():
# 	global duty
# 	row = get_random(0,6)
# 	col = get_random(0,2)
# 	random_usr = get_random_user()
# 	if duty[row][col] == 0:
# 		if possable(row, col, random_usr):
# 			duty[row][col] = random_usr
# 			print(">>>>>",row,col,random_usr)
# 			print(np.matrix(duty))
# 			print("##########################################")
# 	if evalute():
# 		calculate()


# def calculate():
# 	global duty
# 	for row in range(7):
# 		for col in range(3):
# 			if duty[row][col] == 0:
# 				# for i in range(1,no_of_user):
# 				random_usr = get_random_user()
# 					# random_usr = i + 100
# 				if possable(row,col,random_usr):
# 					duty[row][col] = random_usr
# 					print(">>>>>",row,col,random_usr)
# 					print(np.matrix(duty))
# 					print("##########################################")
# 					evalute()
# 					calculate()



def calculate():
	global duty
	for y in range(7):
		for x in range(3):
			if duty[y][x] == 0:
				for i in range(no_of_user):
					print(i)
					random_usr = get_random_user()
					if possable(y,x,random_usr):
						duty[y][x] = random_usr
						print(">>>>>",y,x,random_usr)
						print(np.matrix(duty))
						print("##########################################")
						evalute()
						calculate()
				return


if __name__ == "__main__":

	calculate()
	print(np.matrix(duty))
	print(no_of_duty)
	print(get_per_head_duty())
