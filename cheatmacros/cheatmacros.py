"""
Cheat code macros 
Date: 2016 Aug
Author: RollerSimmer
"""

import sims4.commands
import services
import bellrand
import sims.sim_info
import careers
from careers.career_tracker import CareerTracker

@sims4.commands.Command('cheatmacros', command_type=sims4.commands.CommandType.Live)
def pb_cheatmacros(_connection=None):
	output = sims4.commands.CheatOutput(_connection)
	output("\nCheat Macros | commands:\n\nsas|setallskills <level> - set every skill to the specified level\neqat|equipalltraits - traits.equip_trait *\nrmat|removealltraits - traits.remove_trait *\nsupro|superpromote <amtlevels> - promote career/school by number of levels\ncareertest|ct - ?")

skills = {'AdultMajor_Bartending', 
		'Major_Bartending','Major_Baking','Major_Charisma','Major_Comedy','Major_Fishing',
		'Major_Gardening','Major_GourmetCooking','Major_Guitar',
		'Major_Handiness','Major_HomestyleCooking','Major_Logic',
		'Major_Mischief','Major_Painting','Major_Photography',
		'Major_Piano','Major_Programming','Major_Reaping','Major_RocketScience',
		'Major_VideoGaming','Major_Violin','Major_Writing','Skill_Fitness',
		'Skill_Child_Creativity','Skill_Child_Mental','Skill_Child_Motor','Skill_Child_Social'}

@sims4.commands.Command('setallskills', 'sas', command_type=sims4.commands.CommandType.Live)
def pb_setallskills(level:int=None, _connection=None):		
	output = sims4.commands.CheatOutput(_connection)
	if level==None:
		output("setallskills - Setting skills to normally-distributed values with mean = 5")
	else:
		output("setallskills - Setting all skills to {}".format(level))
	for skl in skills:
		curlvl=0
		if level==None: curlvl=bellrand.minmax(bellrand.gen(-1,12,5),1,10)
		else:           curlvl=level
		command = "|stats.set_skill_level {} {}".format(skl, curlvl)
		sims4.commands.client_cheat(command, _connection)
		
traits={#store rewards
        'Savant','SuperGreenThumb','AlwaysWelcome',
		'FreeServices','Frugal','Marketable','SpeedReader','Observant',
		'Memorable','Connections','NightOwl','MorningPerson','CreativeVisionary',
		'Entrepreneurial','ProfessionalSlacker','Shameless',
		'NeverWeary','Independent','Antiseptic','HardlyHungry','SteelBladder','GymRat',
		'Carefree','Fertile','EternalBond','Beguiling','Mentor',
		'GreatKisser',
		#aspiration bonuses
		'Romantic','FamilySim','High_Metabolism','Business_Savvy','EssenceOfFlavor',		
		'Quick_Learner','Muser','Dastardly','Collector','Alluring','Gregarious',
		#aspiration rewards
		'EpicPoet','LivingVicariously','Outgoing','Patriarch','Matriarch'
		'Piper','Chronicler','WebMaster','Sincere',		
		'Longevity','Legendary','Player',
		'SpeedCleaner','PerfectHost','Hilarious','Mastermind','Bane','TheKnack',
		'AnglersTranquility',
		'PotionMaster','FreshChef','Appraiser',
		'OneWithNature','Expressionistic',
		#prodigy rewards
		'MentallyGifted','SociallyGifted','PhysicallyGifted','CreativelyGifted',
		#shore owner rewards?
		'ValuedCustomer','Invested'}
		
@sims4.commands.Command('equipalltraits', 'eqat', command_type=sims4.commands.CommandType.Live)
def pb_equipalltraits(_connection=None):
	output = sims4.commands.CheatOutput(_connection)
	output("equipalltraits - Equipping all known reward traits")
	for trait in traits:
		command = "|traits.equip_trait {}".format(trait)
		sims4.commands.client_cheat(command, _connection)
		
@sims4.commands.Command('removealltraits', 'rmat', command_type=sims4.commands.CommandType.Live)
def pb_removealltraits(_connection=None):
	output = sims4.commands.CheatOutput(_connection)
	output("removealltraits - Removing all known reward traits")
	for trait in traits:
		command = "|traits.remove_trait {}".format(trait)
		sims4.commands.client_cheat(command, _connection)	

careers={#adult careers
		'Astronaut','Athlete','Business','Criminal','Culinary',
		'Detective','Doctor','Entertainer','Painter','Scientist',
		'SecretAgent','TechGuru','Writer','Athletic',
		#teen careers
		'Manual','FastFood','Barista','Retail','Babysitter',
		#schooling
		'GradeSchool','HighSchool'}

@sims4.commands.Command('superpromote','supro', command_type=sims4.commands.CommandType.Live)
def pb_superpromote(amtlevels:int,_connection=None):
	output = sims4.commands.CheatOutput(_connection)
	if amtlevels==None: amtlevels=10
	output("superpromote - Promoting both school and work by {}".format(amtlevels))
	for career in careers:
		for i in range(0,amtlevels):
			command = "|careers.promote {}".format(career)
			#output(command)
			sims4.commands.client_cheat(command, _connection)	
		
@sims4.commands.Command('careertest','ct', command_type=sims4.commands.CommandType.Live)
def pb_careertest(_connection=None):
	output = sims4.commands.CheatOutput(_connection)
	output('At least I printed something.')
	sim_info = services.active_sim_info()
	i=0
	careers=[]
	for career in sim_info._career_tracker:
		careers[i]=career
		#career.promote()
		i+=1
	#career_name = career._current_track.career_name(sim_info)
	output('sim_info = {}'.format(sim_info))
	for career in careers:
		output('career = {}'.format(career))
	#output('career_name = {}'.format(career_name))

	
	
	
	
