"""
Shortcuts for TS4 | 2014-12-22

Written by pbox http://modthesims.info/members/plasticbox
Published under https://creativecommons.org/licenses/by-nc-sa/3.0/

Modified by RollerSimmer 2016 Aug
"""

import sims4.commands
	
@sims4.commands.Command('m', 'mo', 'moo', command_type=sims4.commands.CommandType.Live)
def pb_moveobj(_connection=None):
	command = 'bb.moveobjects'
	sims4.commands.client_cheat(command, _connection)

@sims4.commands.Command('casf', command_type=sims4.commands.CommandType.Live)
def pb_casfull(_connection=None):
	command = '|testingcheats on'
	sims4.commands.client_cheat(command, _connection)
	command = 'cas.fulleditmode'
	sims4.commands.client_cheat(command, _connection)

	
@sims4.commands.Command('u', 'unlock', command_type=sims4.commands.CommandType.Live)
def pb_unlock(_connection=None):
	command = 'bb.showhiddenobjects'
	sims4.commands.client_cheat(command, _connection)
	command = 'bb.ignoregameplayunlocksentitlement'
	sims4.commands.client_cheat(command, _connection)

@sims4.commands.Command('shortcuts', command_type=sims4.commands.CommandType.Live)
def pb_shortcuts(_connection=None):
	output = sims4.commands.CheatOutput(_connection)
	output("\nShortcuts | aliases:\n\ncasf – testingcheats on + cas.fulleditmode\nd | t | debug [on/off] – testingcheats\nh [on/off] – headlineeffects\nm | mo | moo – bb.moveobjects\nsetskill | ssk <skill> <level> – stats.set_skill_level <skill> <level>; for skill name shortcuts type ssk or setskill\nshortcuts – list shortcuts\nu | unlock – bb.showhiddenobjects + bb.ignoregameplayunlocksentitlement")
	
@sims4.commands.Command('t', 'd', 'debug', command_type=sims4.commands.CommandType.Live)
def pb_testing(enable:bool=None, _connection=None):
	output = sims4.commands.CheatOutput(_connection)
	if enable is not None:
		if enable:
			command = '|testingcheats on'
			sims4.commands.client_cheat(command, _connection)
		else:
			command = '|testingcheats off'
			sims4.commands.client_cheat(command, _connection)
	else:
		output("You need to turn this on or off with 't', 'true', 'on', '1', 'yes', 'y', 'enable' or 'f', 'false', 'off', '0', 'no', 'n', 'disable'")

@sims4.commands.Command('h', command_type=sims4.commands.CommandType.Live)
def pb_headline(enable:bool=None, _connection=None):
	output = sims4.commands.CheatOutput(_connection)
	if enable is not None:
		if enable:
			command = 'headlineeffects on'
			sims4.commands.client_cheat(command, _connection)
		else:
			command = 'headlineeffects off'
			sims4.commands.client_cheat(command, _connection)
	else:
		output("You need to turn this on or off with 't', 'true', 'on', '1', 'yes', 'y', 'enable' or 'f', 'false', 'off', '0', 'no', 'n', 'disable'")

@sims4.commands.Command('setskill', 'ssk', command_type=sims4.commands.CommandType.Live)
def pb_setskill(skill:str=None, level:int=None, _connection=None):
	output = sims4.commands.CheatOutput(_connection)
	skills = {'bt': 'AdultMajor_Bartending', 'bartending': 'AdultMajor_Bartending', 'ch': 'AdultMajor_Charisma', 'charisma': 'AdultMajor_Charisma', 'char': 'AdultMajor_Charisma', 'comedy': 'AdultMajor_Comedy', 'cm': 'AdultMajor_Comedy', 'ck': 'AdultMajor_HomestyleCooking', 'cooking': 'AdultMajor_HomestyleCooking', 'homestylecooking': 'AdultMajor_HomestyleCooking', 'fs': 'AdultMajor_Fishing', 'fish': 'AdultMajor_Fishing', 'fishing': 'AdultMajor_Fishing', 'gd': 'AdultMajor_Gardening', 'gardening': 'AdultMajor_Gardening', 'gourmet': 'AdultMajor_GourmetCooking', 'gourmetcooking': 'AdultMajor_GourmetCooking', 'guitar': 'AdultMajor_Guitar', 'hd': 'AdultMajor_Handiness', 'handiness': 'AdultMajor_Handiness', 'lg': 'AdultMajor_Logic', 'logic': 'AdultMajor_Logic', 'ms': 'AdultMajor_Mischief', 'mischief': 'AdultMajor_Mischief', 'pt': 'AdultMajor_Painting', 'painting': 'AdultMajor_Painting', 'piano': 'AdultMajor_Piano', 'pg': 'AdultMajor_Programming', 'prog': 'AdultMajor_Programming', 'programming': 'AdultMajor_Programming', 'rocksci': 'AdultMajor_RocketScience', 'rocketscience': 'AdultMajor_RocketScience', 'rs': 'AdultMajor_RocketScience', 'gaming': 'AdultMajor_VideoGaming', 'violin': 'AdultMajor_Violin', 'writing': 'AdultMajor_Writing', 'creative': 'Skill_Child_Creativity', 'creativity': 'Skill_Child_Creativity', 'mental': 'Skill_Child_Mental', 'motor': 'Skill_Child_Motor', 'soc': 'Skill_Child_Social', 'social': 'Skill_Child_Social', 'ft': 'Skill_Fitness', 'fitness': 'Skill_Fitness'}

	if skill in skills:
		if level is not None:
			skill_verbose = skills[skill]
			command = "|stats.set_skill_level {} {}".format(skill_verbose, level)
			sims4.commands.client_cheat(command, _connection)
			output("{} skill set to {}".format(skill_verbose, level))
		else:
			output("You need to set a level 1–10!")
	else:
		output("You need to set a skill! Valid shortcuts are {}".format(sorted(skills.keys())))

