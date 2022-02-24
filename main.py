import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("50_states.csv")
states_data2 = pd.read_csv("50_states.csv",index_col=0)
states_list = list(states_data["state"])
answered_list =[]

def get_input():
	return screen.textinput(title=f"{len(answered_list)}/50 States Correct", prompt="what's another state's name ?").title()

def get_coor(state):
	return tuple (states_data2.loc[state])

def write_to_map(state,coord):
	
	writer = turtle.Turtle()
	writer.hideturtle()
	writer.penup()
	writer.goto(coord)
	writer.write(state)

answered_list = []
def update_answered_list(state):
	if state not in answered_list:
		answered_list.append(state)
	

while len(answered_list) <50:
	#get user input
	guessed_state = get_input()
	
	if guessed_state == "Exit":
		break
		#Check the input and write on map
	elif guessed_state in states_list:
			#get coordinates
			coordinates = get_coor(guessed_state)
			#Write on the map
			write_to_map(guessed_state,coordinates)
			# Update correct list
			update_answered_list(guessed_state)
		
		
		
guessed_by_user = set(answered_list)
all_states = set(states_list)
states_not_guessed = all_states - guessed_by_user
states_to_learn = list(states_not_guessed)


answered_list_df = pd.DataFrame()
answered_list_df["States to Learn"] = states_to_learn
answered_list_df.to_csv("states_to_learn.csv")















## Three line below allows you to see the coordinates in console.
# def get_mouse_click_coor(x,y):
# 	print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()