#!/usr/bin/python3
'''


caveat emptor: This was code we wrote together in class; it is definitely not working. There will be syntax and other logic errors.
Use at your own risk



'''




import sys

assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

def show_location(current_location):
	''' Displays the description, displays a list of options, accepts and returns user input '''
	description = current_location["description"]
	options = current_location["options"]
	results = current_location["results"]
	print(description)
	count = 1
	for o in options:
		print('[' + str(count) + '] ' + o)
		count = count + 1
	print('[q] to quit')
	choice = input("What do you choose? ")
	if choice.lower() == 'q':
		return "quit"
	new_location = results[int(choice)-1]
	return new_location

#This code is missing an underground option, and therefore crashes whenever it comes up. Same with anything happening in the city.


world = {
	"start":{
		"description":"You are in a forest"
		,"options":["You can leave?","You can stay?","You can climb a tree?"]
		,"results":["city","bear","tree"]
	}
	,"bear":{
        "description":"A large brown bear walks in front of you with her cub and stares at you."
        ,"options":["Back away slowly with your eyes on the bears?","Stand there in shock?","RUN FOR YOUR LIFE?"]
        ,"results":["car","death","chased"]
    }
    ,"car":{
        "description":"You make it back safetly. When checking your rear view mirror, you notice the bears actually followed!"
        ,"options":["At this point, just drive to the city."]
        ,"results":["city"]
    }
    ,"death":{
        "description":"Despite the mother walking in to you, she becomes territorial and slashes you to death."
        ,"options":["Respawn back in front of the bear?","Respawn in the forest?"]
        ,"results":["bear","start"]
    }
    ,"chased":{
        "description":"You fool! Now they're chasing you!"
        ,"options":["Run to your car?","Climb a tree freakishly fast?"]
        ,"results":["car2","tree2"]
    }
    ,"car2":{
        "description":"You make it to your car but you didn't make it there alone. The bears are now shaking your car while you scream in horror."
        ,"options":["Wait it out? Maybe they'll go away.","Start your car leaving with scratches all over it?"]
        ,"results":["sheriff","city2"]
    }
    ,"sheriff":{
        "description":"An on patrol sheriff who heard the screams comes and fires shots in the air scaring the bears off."
        ,"options":["Thank the sheriff and head home?","Head to the city?"]
        ,"results":["home","city"]
    }
    ,"tree2":{
        "description":"Did you honestly forget bears could climb too? -_-"
        ,"options":["Jump off the tree","Accept fate"]
        ,"results":["tumble","life"]
    }
    ,"tumble":{
        "description":"When trying to jump, the bear smacks you into a branch and you hit the ground fatally"
        ,"options":["Respawn in front of the bears?","Respawn in the forest?"]
        ,"results":["bear","start"]
    }
    ,"life":{
        "description":"You've accepted your fate young one. I'll see you in the force"
        ,"options":["Repsawn in front of the bears?","Respawn in the forest?"]
        ,"results":["bear","start"]
    }
    ,"tree":{
        "description":"When climbing the tree, it just so happened to be the tallest. You see a beautiful sunset"
        ,"options":["Climb down to head home?","Climb down to head to the city?","Jump down like a savage?"]
        ,"results":["home","city","yolo"]
    }
    ,"yolo":{
        "description":"Well, I mean, hey! You only live once :)"
        ,"options":["Respawn in the forest?"]
        ,"results":["start"]
    }
    ,"home":{
        "description":"You return home finally after a long exhausting day."
        ,"options":["Cook dinner?","Watch t.v?","Go to bed?"]
        ,"results":["dinner","t.v","bed"]
    }
	,"city":{
		"description":"You are in a city"
		,"options":["You can explore","You can go underground","You can go back to the forest"]
		,"results":["explore","underground","start"]
	}

}
current = "start"

while current != "quit":
	current = show_location(world[current])


