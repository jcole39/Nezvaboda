import world
import logging
from actions import DevAction
from player import Player

LOG_FILENAME = "dev091916012.log"
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

logging.debug("Adventure Game Log File")
#===
#BEGIN DEFINE
#GLOBAL MAP
#CARGS -- CLIENT ARGUMENTS
#===
carg_opt1 = False #CLIENT ARGUMENT ONE: DEV OPTIONS DISPLAYED?

def endGame(player):
	print("\n\tYou died! Don't worry, it's not the end!")
	print("\tYou were level {} with {} exp before you bit the dust.".format(player.level,player.exp))
	print("\tThe best enemy you killed was the {}, and it had {} max health.".format(player.bestEnemyKilled.name, player.bestEnemyKilled.maxhp))
	print("\tYou really were the best shot we had.\n")
	logging.info("Player death.")
	
def winGame(player):
	print("\n\tYou won! Congratulations!")
	print("\tYou were level {} with {} exp before you left the Manor.".format(player.level,player.exp))
	print("\tThe best enemy you killed was the {}, and it had {} max health.".format(player.bestEnemyKilled.name, player.bestEnemyKilled.maxhp))
	print("\tThe faith placed in your success proved merit!.")

def play():
	logging.info("Game loaded.")
	world.load_tiles()
	player = Player()
	room = world.tile_exists(player.location_x, player.location_y)
	logging.info("Player exists! Their health is {}, their stats are {}/{}/{}/{}.".format(player.hp, player.strength, player.intellect, player.discipline, player.summoning))
	print(room.intro_text())
	while player.is_alive() and not player.victory:
		#Game Loop Begins Here
		room = world.tile_exists(player.location_x, player.location_y)
		logging.info("Player is in room {},{}.".format(player.location_x, player.location_y))
		room.modify_player(player)
		logging.info(room)
		logging.info("Player's last action was {}. They just moved {}.".format(player.lastAction, player.lastDirection))
		# Check again as the room may have changed player state
		if player.is_alive() and not player.victory:
			logging.info("======")
			logging.info("PLAYER STATS:")
			logging.info("LVL {} / EXP {} ||| STR {} INT {} DIS {} SUM {}".format(player.level, player.exp, player.strength, player.intellect, player.discipline, player.summoning))
			logging.info("PLAYER HP is {}".format(player.hp))
			logging.info("======\n")
			if player.lastDirection != '':
				print("You just went {}.\n".format(player.lastDirection))
			print("\nChoose an action:\n")
			available_actions = room.available_actions()
			for action in available_actions:
				#LOAD GLOBALS IN NAMESPACE
				global carg_opt1
				#EXCEPTION HANDLING FOR ACTIONS THAT INTERFACE WITH A GLOBAL
				if isinstance(action, DevAction) and carg_opt1 is False:
					continue
				else:
					print(action)
			action_input = input('>: ')
			for action in available_actions:
				if action_input == action.hotkey:
					player.do_action(action, **action.kwargs)
					logging.info("======")
					if action.name == "Give exp":
						logging.info("Player got Exp! They may have levelled!~~")
					elif action.name == "Attack":
						logging.info("Player attacked!")
					else:
						logging.info("Player performed: {}".format(action.name))
					break
	if player.victory:
		winGame(player)
	else:
		endGame(player)

if __name__ == "__main__":
	play()