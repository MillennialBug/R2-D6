# Attribute Dictionary. Key = Attribute Name, Value = Tuple
# Tuple values in order below with explanation of each field.
#
# name         - Name of the attribute
# short_name   - Shortened name of the attribute
# description  - Description of the attribute as per rulebook
attributes = {'Dexterity': (1, 'dexterity', 'dex',
                            "Dexterity is a measure of your character’s eye-hand coordination "
                            "and balance. Characters with a high Dexterity are good "
                            "shots, can dodge blaster bolts, can walk balance beams with "
                            "ease and even make good pick-pockets. Characters with a low "
                            "Dexterity are clumsy."),
              'Knowledge': (2, 'knowledge', 'know',
                            "Knowledge skills generally reflect how much a character "
                            "knows about a given subject, whether it’s aliens, languages or laws. "
                            "Knowledge is a measure of your character’s “common sense” "
                            "and academic knowledge. Characters with a high Knowledge "
                            "have a good memory for details, and have learned a lot about "
                            "different aliens and planets. They often have a flair for languages, "
                            "and they know how to get things done in bureaucracies. "
                            "Knowledge is used whenever a player wants to find out how "
                            "much his character knows about a certain field. The difficulty "
                            "depends upon how obscure the information is and how much "
                            "the character knows about the general subject."),
              'Mechanical': (3, 'mechanical', 'mech',
                             "Mechanical stands for “mechanical aptitude” and represents "
                             "how well a character can pilot vehicles and starships and operate "
                             "the various systems on board. It also reflects how well the "
                             "character handles live mounts, like banthas and tauntauns. A "
                             "character with a high Mechanical attribute is going to take naturally "
                             "to driving landspeeders, flying cloud cars and piloting Xwings "
                             "and ships like the Millennium Falcon. A character with a "
                             "low Mechanical attribute has a lot of minor accidents."),
              'Perception': (4, 'perception', 'per',
                             "Perception is the character’s ability to notice things about his "
                             "surroundings and other characters. Those with a high Perception "
                             "are quick to spot concealed objects or people hiding behind a "
                             "corner. They’re also good at convincing other people to do "
                             "favors for them, tricking or conning others, and bargaining to "
                             "get a good price for goods or services. Characters with a low "
                             "Perception get lost a lot."),
              'Strength': (5, 'strength', 'str',
                           "Strength represents a character’s physical strength, "
                           "endurance and health. Characters with a high Strength can lift "
                           "heavy objects, push themselves for days without rest and are "
                           "good at resisting disease and injury. A character with a low "
                           "Strength gets winded very easily."),
              'Technical': (6, 'technical', 'tech',
                            "Technical stands for “technical aptitude” and represents a "
                            "character’s innate knowledge of how to take apart, repair and "
                            "modify things. A character with a high Technical attribute can "
                            "take apart a droid to repair a malfunction, fix a busted drive "
                            "system on a landspeeder, and modify a blaster to have a longer "
                            "range. Technical also reflects a character’s knowledge of healing "
                            "and medicine, skill setting explosives, and ability to figure out "
                            "electronic security systems. Characters with a low Technical have "
                            "trouble changing a power pack in a blaster.")}
# Skill Dictionary. Key = Skill Name, Value = Tuple
# Tuple values in order below with explanation of each field.
#
#  name        - Name of the skill
#  short_name  - Shortened name of the skill
#  attribute   - Attribute that the skill belongs to. This will be translated to an ID for the db insert
#  time        - Time it takes to perform the skill
#  short_time  - Shortened time above
#  specialise  - Can a character specialise in this skill? (True) 1 / (False) 0 value.
#  description - Description of the skill as per rulebook
skills = {
    'Acrobatics': ("acrobatics", "acr", "dexterity", "1 Round", "1rnd", 1,
                   "Characters with this skill can tumble, "
                   "leap, and roll to avoid falling damage, to entertain "
                   "an audience, or to surprise an opponent in combat."),
    'Astrogation': ("astrogation", "astro", "mechanical", "various", "var", 1,
                    "Starship pilots use astrogation to plot "
                    "a course from one star system to another.")}
