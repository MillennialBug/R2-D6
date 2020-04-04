# Skill Dictionary. Key = Skill Name, Value = Tuple
# Tuple values in order below with explanation of each field.
#
#  skill_id        - Id for the skill - Incremental number
#  type            - attr or skill
#  name            - Name of the skill
#  sheet_name      - Shortened name of the skill as per the gsheet
#  attribute       - Attribute that the skill belongs to, if applicable.
#  time            - Time it takes to perform the skill
#  short_time      - Shortened time above
#  specialise      - Can a character specialise in this skill? (True) 1 / (False) 0 value.
#  description     - Description of the skill as per rulebook
#  specialisations - What, if any, are the specialisation options for the skill
skills = {
    'Dexterity': (1, 'attr', 'dexterity', 'dex', 1, 'various', 'var', 0,
                  "Dexterity is a measure of your character’s eye-hand coordination "
                  "and balance. Characters with a high Dexterity are good "
                  "shots, can dodge blaster bolts, can walk balance beams with "
                  "ease and even make good pick-pockets. Characters with a low "
                  "Dexterity are clumsy.", ""),
    'Knowledge': (2, 'attr', 'knowledge', 'know', 2, 'various', 'var', 0,
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
                  "the character knows about the general subject.", ""),
    'Mechanical': (3, 'attr', 'mechanical', 'mech', 3, 'various', 'var', 0,
                   "Mechanical stands for “mechanical aptitude” and represents "
                   "how well a character can pilot vehicles and starships and operate "
                   "the various systems on board. It also reflects how well the "
                   "character handles live mounts, like Banthas and Tauntauns. A "
                   "character with a high Mechanical attribute is going to take naturally "
                   "to driving landspeeders, flying cloud cars and piloting X-wings "
                   "and ships like the Millennium Falcon. A character with a "
                   "low Mechanical attribute has a lot of minor accidents.", ""),
    'Perception': (4, 'attr', 'perception', 'per', 4, 'various', 'var', 0,
                   "Perception is the character’s ability to notice things about his "
                   "surroundings and other characters. Those with a high Perception "
                   "are quick to spot concealed objects or people hiding behind a "
                   "corner. They’re also good at convincing other people to do "
                   "favors for them, tricking or conning others, and bargaining to "
                   "get a good price for goods or services. Characters with a low "
                   "Perception get lost a lot.", ""),
    'Strength': (5, 'attr', 'strength', 'str', 5, 'various', 'var', 0,
                 "Strength represents a character’s physical strength, "
                 "endurance and health. Characters with a high Strength can lift "
                 "heavy objects, push themselves for days without rest and are "
                 "good at resisting disease and injury. A character with a low "
                 "Strength gets winded very easily.", ""),
    'Technical': (6, 'attr', 'technical', 'tech', 6, 'various', 'var', 0,
                  "Technical stands for “technical aptitude” and represents a "
                  "character’s innate knowledge of how to take apart, repair and "
                  "modify things. A character with a high Technical attribute can "
                  "take apart a droid to repair a malfunction, fix a busted drive "
                  "system on a landspeeder, and modify a blaster to have a longer "
                  "range. Technical also reflects a character’s knowledge of healing "
                  "and medicine, skill setting explosives, and ability to figure out "
                  "electronic security systems. Characters with a low Technical have "
                  "trouble changing a power pack in a blaster.", ""),
    'Acrobatics': (7, 'skill', 'Acrobatics', 'Acrobatics', 1, '1 Round', '1rnd', 1,
                   "Characters with this skill can tumble, leap, and roll to avoid falling damage, to entertain an "
                   "audience, or to surprise an opponent in combat.",
                   "Type of acrobatics used, form or style — diving, trapeze, tumbling."),
    'Alien Species': (8, 'skill', 'Alien Species', 'Alien Species', 2, '1 Round+', '1rnd+', 1,
                      "Alien species involves knowledge of any species outside of the character’s. For human "
                      "characters, it covers all nonhumans; for Wookiees, the skill covers all non-Wookiees.\nAlien "
                      "species represents knowledge of customs, societies, physical appearance, attitudes, philosophy, "
                      "history, art, politics, special abilities, and other areas of reasonable knowledge.",
                      "Knowledge of a particular alien species — Wookiees, Gamorreans, Ewoks, Sullustans."),
    'Aquatic Vehicle Operation': (9, 'skill', 'Aquatic Vehicle Operation', 'Aquatic Vehicle Operation', 3, '1 Round+',
                                  '1rnd+', 1,
                                  "This skill allows characters to pilot naval ships and boats. While these"
                                  " vehicles are seldom used in the highertech worlds, many low-tech cultures "
                                  "use them for transporting personnel and freight over bodies of water."
                                  "\nNote that aquatic vehicles which employ the use of repulsorlift or hover "
                                  "technology may also require the use of different skills (namely "
                                  "repulsorlift operation and hover vehicle operation).\nAquatic vehicle "
                                  "operation can be used for a vehicle dodge — a “reaction skill” — to avoid "
                                  "enemy fire.",
                                  "Particular ship type or class — Oceanic transport, "
                                  "coastal runabout, skiff, sailboat."),
    'Aquatic Vehicle Repair': (10, 'skill', 'Aquatic Vehicle Repair', 'Aquatic Vehicle Repair', 6, 'Various', 'var', 1,
                               "This skill represents a character’s familiarity with the workings of aquatic vehicles, "
                               "and his ability to repair and modify them. Each roll may repair one damaged system "
                               "aboard a particular vessel. The cost and difficulty to repair a vessel depends on how "
                               "badly it is damaged, and what systems have been hit.",
                               "Particular ship type or class — Oceanic transport, coastal runabout, skiff. sailboat."),
    'Archaic Guns': (11, 'skill', 'Archaic Guns', 'Archaic Guns', 1, '1 Round', '1rnd', 1,
                     "Archaic guns is a 'ranged combat' skill used to fire any primitive gun, including black powder "
                     "pistols, flintlocks and muskets. Normally, only characters from primitive technology worlds will "
                     "know this skill.",
                     "Indicates a specific kind or model of archaic gun — black powder pistol, matchlock, musket, "
                     "wheelock."),
    'Archaic Starship Piloting': (
        12, 'skill', 'Archaic Starship Piloting', 'Archaic Starship Piloting', 3, '1 Round+', '1rnd+', 1,
        "This skill allows characters to pilot primitive starships and other basic archaic ship designs. While these "
        "vehicles are seldom used in settled areas, they can be encountered on frontier worlds or planets that have "
        "just developed space travel on their own.\nArchaic starship piloting can be used for a vehicle dodge — a "
        "“reaction skill” — to avoid enemy fire.",
        "Particular ship type or class — Delayaclass, Coruscant-class heavy courier."),
    'Armor Repair': (13, 'skill', 'Armor Repair', 'Armor Repair', 6, 'Various', 'var', 1,
                     "Armor repair reflects the character’s ability to fix and modify armor that has been damaged. "
                     "The cost and difficulty to repair armor depends upon how badly damaged it is.",
                     "Armor Type — Stormtrooper armor."),
    'Artillery': (14, 'skill', 'Artillery', 'Artillery', 1, '1 Round+', '1rnd+', 1,
                  "Artillery is the 'ranged combat' skill used to fire all non-energy projectile weapons, such as "
                  "cannons and field guns (excluding self-propelled projectiles or launched grenades, which are "
                  "covered under missile weapons).",
                  "The particular type or model of projectile artillery — cannons, Golan Arms M102 Fire Arc."),
    'Astrogation': (15, 'skill', 'Astrogation', 'Astrogation', 3, 'Various', 'var', 0,
                    "Starship pilots use astrogation to plot a course from one star system to another.", ""),
    'Bargain': (16, 'skill', 'Bargain', 'Bargain', 4, '1 Minute - 1 Hour', '1min-1hr', 1,
                "Characters use this skill to haggle over prices for goods they want to purchase or sell. The "
                "difficulty is often an opposed roll against the gamemaster character’s bargain skill.",
                "Kind of merchandise to be purchased or sold — spice, weapons, droids, datapads."),
    'Beast Riding': (17, 'skill', 'Beast Riding', 'Beast Riding', 3, '1 Round+', '1rnd+', 1,
                     "Beast riding represents a character’s ability to ride any live mount. Unlike vehicles, "
                     "animals sometimes resist orders from their riders. Each animal has an orneriness code. When a "
                     "character mounts a riding animal, the character makes an opposed roll against the animal’s "
                     "orneriness code. If the character rolls higher than the animal, it does as he wishes. If the "
                     "animal rolls higher, find the results on the chart below.",
                     "Particular riding animal — banthas, Cracian thumpers, dewbacks, tauntauns."),
    'Blaster Artillery': (18, 'skill', 'Blaster Artillery', 'Blaster Artillery', 1, '1 Round+', '1rnd+', 1,
                          "Blaster artillery is the 'ranged combat' skill that coversall fixed, multi-crew heavy "
                          "energy weapons, such as those used by the Rebel Alliance at the Battle of Hoth and the "
                          "fixed ion cannons fired from a planet’s surface.",
                          "The particular type or model of artillery — anti-infantry, anti-vehicle, Golan Arms DF.9, "
                          "surface-to-space, surface-to-surface."),
    'Blaster': (19, 'skill', 'Blaster', 'Blaster', 1, '1 Round', '1rnd', 1,
                "Blaster is the ranged combat skill used to shoot blaster weapons that can be held and carried by a "
                "character. Blaster covers everything from tiny holdout blasters to large repeating blasters (such as "
                "the EWEB heavy repeating blaster used by Imperial snowtroopers on Hoth in The Empire Strikes Back). "
                "Other blaster types include sporting blasters (Princess Leia uses a sporting blaster in Star Wars: A "
                "New Hope), blaster pistols, heavy blaster pistols (like Han Solo’s BlasTech DL-44), and the blaster "
                "rifles used by stormtroopers.",
                "A specific type or model of character-scale blaster weapon — blaster pistol, heavy blaster pistol, "
                "blaster rifle, BlasTech DL-44, hold-out blaster."),
    'Blaster Repair': (20, 'skill', 'Blaster Repair', 'Blaster Repair', 6, 'Various', 'var', 1,
                       "A character’s ability to fix and modify blaster weapons (character-, speeder- and walker-scale)"
                       " is represented by his blaster repair skill. The cost and difficulty to repair weapons depends "
                       "upon how badly it is damaged.\nNote vibroblades, slugthrowers, and other non-blaster weapons "
                       "are repaired and modified using the equipment repair skill.",
                       "Type or model blaster — blaster pistols, surface-to-surface blaster artillery, heavy blaster "
                       "cannon."),
    'Bowcaster': (21, 'skill', 'Bowcaster', 'Bowcaster', 1, '1 Round', '1rnd', 0,
                  "Bowcaster is a 'ranged combat' skill that reflects the user’s proficiency at firing the unusual "
                  "Wookiee bowcaster. This weapon requires great strength and is normally only used by Wookiees.", ""),
    'Bows': (22, 'skill', 'Bows', 'Bows', 1, '1 Round', '1rnd', 1,
             "Bows is a 'ranged combat' skill covering all bow-type weapons, including short bows, long bows and "
             "crossbows (excluding Wookiee bowcasters, which fall under the bowcaster skill). Bows are normally only "
             "found on lowtechnology worlds, so this skill is fairly unusual.",
             "Specific type or model bow — crossbow, long bow, short bow."),
    'Brawling Parry': (23, 'skill', 'Brawling Parry', 'Brawling Parry', 1, '1 Round', '1rnd', 1,
                       "Brawling parry is a “reaction skill” used to avoid being hit by a brawling or melee combat "
                       "attack if you’re unarmed. Brawling parry is used to hold one’s ground yet avoid or block a "
                       "hand-to-hand combat attack.",
                       "Style of brawling being parried when unarmed and avoiding a brawling or melee attack — boxing, "
                       "martial arts."),
    'Brawling': (24, 'skill', 'Brawling', 'Brawling', 5, '1 Round', '1rnd', 1,
                 "Brawling is the “melee combat” skill used for fighting hand-to-hand without any weapons. Most "
                 "creatures have a good brawling skill.\nThe base difficulty to make a brawling attack is Very Easy "
                 "unless the target makes a brawling parry roll.",
                 "Specific brawling style — boxing, martial arts."),
    'Bureaucracy': (25, 'skill', 'Bureaucracy', 'Bureaucracy', 2, '1 Round - Days', '1rnd-days', 1,
                    "This skill reflects a character’s familiarity with bureaucracies and their procedures. "
                    "Bureaucracy can be used in two ways:\nFirst, the character can use this skill to determine "
                    "whether or not he knows what to expect from a bureaucracy. For example, if a character needs "
                    "to get a permit for his blaster, a successful bureaucracy skill check means he knows what forms "
                    "and identification he needs, who he would have to talk to, how long the process might take and "
                    "some short cuts he might be able to use.\nSecond, bureaucracy can also be used to find out what "
                    "information a bureaucracy has on file.",
                    "Specific planetary or administrative government, or branch within it — Tatooine, Celanon, "
                    "Bureau of Commerce, Bureau of Ships and Services."),
    'Business': (26, 'skill', 'Business', 'Business', 2, '1 Round - Days', '1rnd-days', 1,
                 "The character has a working knowledge of businesses and business procedures. A character skilled "
                 "in business might want to run his own company, or knows how to convince a warehouse manager to "
                 "give him a tour of a facility or to allow him to 'borrow' a few things in an emergency.\nCharacters "
                 "with a high business skill know how much it costs companies to produce goods and will be able to "
                 "negotiate for good prices direct from a company or distributor. The character probably has several "
                 "contacts in the business world and can get special favors done for him if he is somewhere where the "
                 "company has a lot of power.",
                 "Field or organization (company, conglomerate, trade guild) — starships, weapons, droids, Sienar "
                 "Fleet Systems, Corporate Sector Authority, Golan Arms."),
    'Capital Ship Gunnery': (27, 'skill', 'Capital Ship Gunnery', 'Capital Ship Gunnery', 3, '1 Round', '1rnd', 1,
                             "Capital ship gunnery is the “ranged combat” skill that covers the operation of "
                             "capital-scale starship weapons, including turbolasers, ion cannons and tractor beams.",
                             "Weapon type or model — concussion missiles, gravity well projectors, ion cannons, "
                             "laser cannons, proton torpedoes, tractor beams, turbolasers."),
    'Capital Ship Piloting': (28, 'skill', 'Capital Ship Piloting', 'Capital Ship Piloting', 3, '1 Round+', '1rnd+', 1,
                              "Capital ship piloting covers the operation of large combat starships such as Imperial "
                              "Star Destroyers, Carrack- class cruisers, Corellian Corvettes and Mon Cal cruisers."
                              "\nCapital ships normally require huge crews for efficient operation, and thus the "
                              "skill emphasizes both quick reflexes and disciplined teamwork. The chapter on “Space "
                              "Travel and Combat” has more details about using capital ship piloting.\nCapital ship "
                              "piloting can be used for a starship dodge — a “reaction skill” — to avoid enemy fire.",
                              "Type or class of capital ship — Imperial Star Destroyer, Victory Star Destroyer, "
                              "Nebulon-B frigate, Trade Federation Battleship."),
    'Capital Ship Repair': (29, 'skill', 'Capital Ship Repair', 'Capital Ship Repair', 6, 'Various', 'var', 1,
                            "This skill represents a character’s familiarity with the workings of capital ships, "
                            "and his ability to repair them. Each roll may repair one damaged component aboard a "
                            "particular vessel. The cost and difficulty to repair a system depends on how badly it "
                            "is damaged, and what systems have been damaged.",
                            "Type or class of capital ship — Imperial Star Destroyer, Victory Star Destroyer, "
                            "Nebulon-B frigate."),
    'Capital Ship Shields': (30, 'skill', 'Capital Ship Shields', 'Capital Ship Shields', 3, '1 Round', '1rnd', 0,
                             "Characters use this skill when operating shields on capital-scale starships, both "
                             "military and civilian. These shields normally require large, coordinated crews for "
                             "efficient operation. You can find more information about capital ship shields in "
                             "the chapter “Space Travel and Combat.”\nCapital ship shields can be used to bring up "
                             "shields — a “reaction skill” — to block enemy fire.",
                             ""),
    'Capital Ship Weapon Repair': (
        31, 'skill', 'Capital Ship Weapon Repair', 'Capital Ship Weapon Repair', 6, 'Various', 'var', 1,
        "Capital ship weapon repair is used to repair capital-scale ship weapons. The cost and difficulty to repair "
        "a weapon depends upon how badly it is damaged.",
        "Weapon type or model — concussion missiles, gravity well projectors, ion cannons, laser cannon, proton "
        "torpedoes, tractor beams, turbolaser."),
    'Climbing/Jumping': (32, 'skill', 'Climbing/Jumping', 'Climbing/Jumping', 5, '1 Round', '1rnd', 1,
                         "Use this skill when a character attempts to climb a tree, wall or cliff, leap a wide gap, "
                         "or jump up and grab an outcropping.",
                         "Climbing, jumping."),
    'Command': (33, 'skill', 'Command', 'Command', 4, '1 Round', '1rnd', 1,
                "Command is a measure of a character’s ability to convince gamemaster characters and subordinates "
                "to do what they’re told. Command generally shouldn’t be used against other player characters to "
                "force them to do something against their will — these situations should be handled through "
                "roleplaying interaction.\nA high command roll can complement individual participants’ rolls in a "
                "group activity, while a low command roll can impose negative modifiers. It generally requires at "
                "least one round of planning to perform effectively.\nThe skill is often used in combat situations, "
                "such as a squad leader commanding his troops or a Star Destroyer captain telling his gunners which "
                "enemy ship to target.",
                "Leader’s unit — Rogue Squadron,Imperial stormtroopers."),
    'Communications': (34, 'skill', 'Communications', 'Communications', 3, '1 Round', '1rnd', 1,
                       "Communications represents a character’s ability to use subspace radios, comlinks and other "
                       "communications systems. While operating communications devices is generally a Very Easy "
                       "task, the difficulty numbers are higher when the skill is used to descramble enemy codes and "
                       "find particular enemy transmission frequencies.\nCharacters may also use communications to "
                       "send or receive a signal through natural hazards which disrupt communications, such as a "
                       "gas cloud, heavy magnetic fields or locations with a high metal content.",
                       "Type or model of communications unit — comlink, subspace radio."),
    'Computer Programming/Repair': (
        35, 'skill', 'Computer Programming/Repair', 'Computer Programming/Repair', 6, '1 Round - Days', '1rnd-days', 1,
        "Characters use this skill to repair, modify, and program computers — it also covers a character’s "
        "familiarity with computer security procedures, his ability to evade them, and the ability to get secure "
        "information.",
        "Type or model computer — portable computer, mainframe, datapad, YT1300- computer."),
    'Con': (36, 'skill', 'Con', 'Con', 4, '1 Round', '1rnd', 1,
            "Con is used to trick and deceive characters, or otherwise convince them to do something that isn’t in "
            "their best interest. (Con is another interaction skill, so you’ll often want to use roleplaying to "
            "resolve these situations.)",
            "Particular method of conning — disguise, fast-talk."),
    'Cultures': (37, 'skill', 'Cultures', 'Cultures', 2, '1 Round - Days', '1rnd-days', 1,
                 "This skill reflects knowledge of particular cultures and common cultural forms (primitive tribal "
                 "civilizations tend to be somewhat similar, for example). Cultures allows a character to determine "
                 "how he is expected to behave in a particular situation among a certain group of individuals. "
                 "The more obscure the information or culture, the higher the difficulty. Cultural knowledge "
                 "includes information about a certain group’s art, history, politics, customs, rites of passage, "
                 "and views on outsiders.\nFor instance, a visitor to Tatooine might make a cultures roll to better "
                 "understand the moisture farmers he’s dealing with. Depending on what the player asks about this "
                 "culture, he could learn the moisture farmers depend heavily on droids, they often trade with "
                 "roaming bands of Jawa scavengers, and their calendar revolves around planting and harvesting "
                 "seasons.\nThis skill can be used for cultures of one’s own species or for those of other species.",
                 "Planet or social group — Corellians, Alderaan royal family, Brentaal, Prexian pirates."),
    'Demolitions': (38, 'skill', 'Demolitions', 'Demolitions', 6, '1 Round - Minutes', '1rnd-mins', 1,
                    "Demolitions reflects a character’s ability to set explosives for both destructive purposes "
                    "and to accomplish specific special effects.",
                    "pecific target type — bridges, walls, vehicles."),
    'Dodge': (39, 'skill', 'Dodge', 'Dodge', 1, '1 Round', '1rnd', 1,
              "Dodge is a 'reaction skill' used to avoid any ranged attack, including blaster fire, grenades, "
              "bullets and arrows. Characters using this are doing whatever they can to dodge the attack — slipping "
              "around a corner for cover, diving behind cargo containers, dropping to the ground, or any other "
              "maneuvers to avoid getting hit.",
              "Kind of ranged attack to be dodged — energy weapons, grenades, missile weapons."),
    'Droid Programming': (40, 'skill', 'Droid Programming', 'Droid Programming', 6, 'Various', 'var', 1,
                          "Characters may use this skill to program a droid to learn a new skill or task. While "
                          "droids can “learn” through trial and error, or by drawing conclusions, it is often "
                          "easier and faster to program the activity into the droid’s memory.\nThe programmer must "
                          "have access to a computer or datapad, which must be jacked directly into the droid’s "
                          "memory for programming.",
                          "Type or model droid — astromech droid, protocol droid, probe droid."),
    'Droid Repair': (41, 'skill', 'Droid Repair', 'Droid Repair', 6, 'Various', 'var', 1,
                     "This skill represents a character’s talent to repair, modify, and maintain droids. The repair "
                     "difficulty depends on how badly damaged the droid is — the cost reflects the price of "
                     "replacement parts based on the droid’s original value.",
                     "Type or model droid — astromech droid, protocol droid, probe droid."),
    'Equipment Repair': (42, 'skill', 'Equipment Repair', 'Equipment Repair', 6, 'Various', 'var', 1,
                         "A character’s ability to fix and modify various character, speeder, and walker-scale "
                         "equipment items (including non-blaster, and non-energy beam weapons). The cost and "
                         "difficulty to repair equipment depends upon how badly it is damaged.\nNote blasters and "
                         "other energy weapons are repaired and modified using the blaster repair skill. Computers "
                         "and small sensors are repaired using the computer programming/repair skill.",
                         "Type or model equipment — breath mask, comlink, slugthrower, vibroblade."),
    'Firearms': (43, 'skill', 'Firearms', 'Firearms', 1, '1 Round', '1rnd', 1,
                 "Firearms is the 'ranged combat' skill used to for all guns which fire bullets, including pistols, "
                 "rifles, machine guns, assault rifles and any other firearms. (Firearms doesn’t include very "
                 "primitive guns, which are covered under archaic guns.)",
                 "Type or model firearm used — pistols, rifles, machineguns."),
    'First Aid': (44, 'skill', 'First Aid', 'First Aid', 6, '1 Round', '1rnd', 1,
                  "First aid reflects a character’s ability to perform emergency life saving procedures in the field.",
                  "Species of patient — humans, Ewoks, Wookiees."),
    'Flamethrower': (45, 'skill', 'Flamethrower', 'Flamethrower', 1, '1 Round+', '1rnd+', 1,
                     "Flamethrower is the 'ranged combat' skill used to fire all types of flame projectors, "
                     "including flame rifles, wrist mounted flame projectors, and flame carbines.",
                     "Type or model flamethrower — Merr-Sonn C-22, Wrist-Mounted Flame Projectors."),
    'Forgery': (46, 'skill', 'Forgery', 'Forgery', 4, '1 Round - Days', '1rnd-days', 1,
                "The character has the ability to falsify electronic documents to say what the character wishes. "
                "Characters might forge bank codes to get someone else’s credits out of an account, alter official "
                "Imperial cargo vouchers so they may appear to have the right permit to carry a certain type of "
                "restricted good, or create valid identification so they may impersonate New Republic inspectors."
                "\nA person inspecting a forged document may make an opposed forgery, search or Perception roll to "
                "spot the forgery. This is further modified by the difficulty in forging the document and "
                "familiarity with the type of document in question.",
                "Specific kind of documentation to be forged — security codes, datapad scandocs, starship permits."),
    'Gambling': (47, 'skill', 'Gambling', 'Gambling', 4, '1 Round - Minutes', '1rnd-mins', 1,
                 "Gambling reflects a character’s skill at various games of chance — it is used to increase his "
                 "odds of winning. This skill doesn’t affect games that are purely random, but does influence games "
                 "with an element of strategy, like sabacc or a similar game. When playing a skill game honestly, "
                 "all characters make opposed gambling rolls, and the highest roll wins.",
                 "Particular game of chance — sabacc, Trin sticks, warp-top."),
    'Grenade': (48, 'skill', 'Grenade', 'Grenade', 1, '1 Round', '1rnd', 1,
                "Grenade is the “ranged combat” skill to throw grenades. Success means the grenade hits the "
                "location it was thrown to. Failure means it lands somewhere else. This skill covers throwing "
                "other objects like rocks and balls.",
                "Kind or model of grenade — thermal detonator, anti-vehicle grenade."),
    'Ground Vehicle Operation': (
        49, 'skill', 'Ground Vehicle Operation', 'Ground Vehicle Operation', 3, '1 Round+', '1rnd+', 1,
        "Ground vehicle operation covers primitive wheeled and tracked land vehicles, including Jawa sandcrawlers, "
        "the Rebel personnel transports on Yavin IV, personal transportation cars and bikes, and cargo haulers. "
        "Some military vehicles — such as the Empire’s Juggernaut and PX-4 Mobile Command Base — also utilize wheel "
        "or track-technology.\nGround vehicle operation is seldom needed on modern worlds — where repulsorlift "
        "vehicles are very common — but this primitive technology is often used on low-tech worlds.\nGround vehicle "
        "operation can be used for a vehicle dodge — a “reaction skill” — to avoid enemy fire.",
        "Type or model ground vehicle — compact assault vehicle, Juggernaut."),
    'Ground Vehicle Repair': (50, 'skill', 'Ground Vehicle Repair', 'Ground Vehicle Repair', 6, 'Various', 'var', 1,
                              "This skill represents a character’s familiarity with the workings of ground vehicles, "
                              "and his ability to modify or repair them. Each roll may repair one damaged system "
                              "aboard a particular craft. The cost and difficulty to repair a vehicle depends on "
                              "how badly it is damaged, and what systems have been damaged.",
                              "Type or model ground vehicle — compact assault vehicle, Juggernaut."),
    'Hide': (51, 'skill', 'Hide', 'Hide', 4, '1 Round', '1rnd', 1,
             "Hide represents a character’s ability to conceal objects from view. The skill is used when trying to "
             "hide weapons on one’s person, conceal goods within luggage, plant objects to be left in a room and "
             "other similar tasks.\nWhen characters are attempting to spot hidden objects, they must make an "
             "opposed search or Perception check. Modifiers include how well the gamemaster thinks the character "
             "hid the object. Just rolling high to hide a lightsaber on a character’s belt won’t do any good in a "
             "pat-down search, but dumping one into a ventilator shaft will be much more effective (usually).\nHide "
             "can also be used to conceal large objects: camouflaging a grounded starfighter or covering up the "
             "cave entrance of a secret base.",
             "Camouflage."),
    'Hover Vehicle Operation': (
        52, 'skill', 'Hover Vehicle Operation', 'Hover Vehicle Operation', 3, '1 Round+', '1rnd+', 1,
        "Hover vehicles generate a cushion of air for travel — hover vehicle operation enables characters to pilot "
        "these vehicles. Hovercraft are generally unwieldy, but they are used on many primitive worlds and are "
        "sometimes used for specific military applications. They are also used on planets with unusual gravitational "
        "fluctuations or other quirks which interfere with repulsorlift operation.\nHover vehicle operation can be "
        "used for a vehicle dodge — a “reaction skill” — to avoid enemy fire.",
        "Type or model vehicle — hoverscout."),
    'Hover Vehicle Repair': (53, 'skill', 'Hover Vehicle Repair', 'Hover Vehicle Repair', 6, 'Various', 'var', 1,
                             "Characters use this skill when repairing or modifying hover vehicle systems. Each "
                             "roll may repair one damaged component aboard a particular craft. The cost and "
                             "difficulty to repair a hover vehicle depends on how badly it is hit, and what "
                             "systems have been damaged.",
                             "Type or model hover vehicle — hoverscout."),
    'Intimidation': (54, 'skill', 'Intimidation', 'Intimidation', 2, '1 Round - Hours', '1rnd-hrs', 1,
                     "Intimidation is a character’s ability to scare or frighten others to force them to obey "
                     "commands, reveal information they wish to keep hidden, or otherwise do the bidding of the "
                     "intimidating character.\nIntimidation is normally dependent upon a character’s physical "
                     "presence, body language or force of will to be successful. Some characters use the threat of "
                     "torture, pain or other unpleasantness to intimidate others.\nCharacters resist intimidation "
                     "with the willpower skill.",
                     "Interrogation, bullying."),
    'Investigation': (55, 'skill', 'Investigation', 'Investigation', 4, '1 Round - Days', '1rnd-days', 1,
                      "Investigation is a character’s ability to find and gather information regarding someone else’s "
                      "activities, and then draw a conclusion about what the target has done or where she has gone. "
                      "Investigation is useful for finding out about the target’s ship reservations and following her "
                      "to a specific planet, or figuring out what shady business dealings she has undertaken. Just as "
                      "with other skills, investigation is often more fun when you use roleplaying over skill rolls; "
                      "when   player makes a good investigation roll, gamemasters can provide additional hints and "
                      "clues rather than just giving the player the answer to a puzzle.",
                      "Locale or field of investigation — Mos Eisley, Imperial City, property estates, criminal "
                      "records."),
    'Jet Pack Operation': (56, 'skill', 'Jet Pack Operation', 'Jet Pack Operation', 3, '1 Round', '1rnd', 0,
                           "This skill represents a character’s skill at using jet packs. Since these back-mounted "
                           "packs rely on pulling in surrounding atmosphere and mixing it with regulated amounts of "
                           "fuel, they can only be operated within atmospheres.\nCharacters with jet pack operation "
                           "gain no bonuses when operating “rocket packs,” which use the rocket pack operation skill."
                           "\nJet pack operation can be used as a “reaction skill” to avoid enemy fire.",
                           ""),
    'Languages': (57, 'skill', 'Languages', 'Languages', 2, '1 Round', '1rnd', 1,
                  "The common language of the Known Galaxy is Basic. Most people speak it — if not as their main "
                  "language, they are at least fluent in it — and virtually everyone can understand it. However, "
                  "some areas of the galaxy are so isolated that Basic is rarely spoken. Some aliens can’t or "
                  "refuse to speak Basic. For example, Wookiees can under-stand Basic, but, because of the structure "
                  "of their mouths, usually cannot speak it. Ewoks do not normally understand Basic, but can learn "
                  "it fairly easily.\nThe languages skill is used to determine whether or not a character understands "
                  "something in another language.",
                  "Specific language known — Wookiee, Huttese, Bocce, Ewok."),
    'Law Enforcement': (58, 'skill', 'Law Enforcement', 'Law Enforcement', 2, '1 Round', '1rnd', 1,
                        "The character is familiar with law enforcement techniques and procedures. He knows how to "
                        "deal with the authorities — for example, he may be able to persuade a customs official not "
                        "to impound his ship or not arrest him for a minor offense.\nCharacters are also "
                        "knowledgeable about laws. By making a successful law enforcement skill check, the character "
                        "will know whether or not bribery, resistance or cooperation is advisable under particular "
                        "circumstances. This skill covers major laws — Old Republic, New Republic, or Imperial — "
                        "and their underlying principles. Some planets have very unusual legal systems and customs: "
                        "law enforcement difficulties on these worlds should be much higher.",
                        "Particular planet’s or organization’s laws and procedures — Alderaan, Tatooine, the Empire, "
                        "Rebel Alliance."),
    'Lifting': (59, 'skill', 'Lifting', 'Lifting', 5, '1 Round', '1rnd', 0,
                "Lifting is a character’s ability to lift heavy objects; it’s also the character’s ability to carry "
                "something for a long time. The difficulty depends on the weight of the object and how long it will "
                "be carried.",
                ""),
    'Lightsaber': (60, 'skill', 'Lightsaber', 'Lightsaber', 1, '1 Round', '1rnd', 1,
                   "Lightsaber is the 'melee combat' skill used for the lightsaber, the weapon of the famed Jedi "
                   "Knights. While a very powerful weapon, a lightsaber is dangerous to an unskilled user — if an "
                   "attacking character misses the attack difficulty number by 10 or more points, then the character "
                   "has injured himself with the weapon and rolls damage against his own Strength.\nLightsaber can "
                   "also be used as a 'reaction skill' to parry brawling, lightsaber and melee combat attacks. Jedi "
                   "Knights can parry blaster bolts with a lightsaber, but that’s only because they have the "
                   "lightsaber combat Force power; it’s very, very difficult for a character without the power to "
                   "parry blaster shots.",
                   "Specific type or model lightsaber — double-bladed lightsaber, light-whip."),
    'Lightsaber Repair/Engineering': (
        61, 'skill', 'Lightsaber Repair/Engineering', 'Lightsaber Repair/Engineering', 6, 'Various', 'var', 1,
        "Characters use this skill when repairing, modifying, or building a lightsaber, the weapon of the Jedi. This "
        "skill is generally restricted to Jedi Knights who learned it from their master. Lightsaber repair/engineering "
        "combines the repair and design skills into one, due to the special nature of the skill. The cost and "
        "difficulty to repair equipment depends upon how badly it is damaged.",
        "Specific type or model lightsaber — double-bladed lightsaber, light-whip."),
    'Melee Combat': (62, 'skill', 'Melee Combat', 'Melee Combat', 1, '1 Round', '1rnd', 1,
                     "Melee combat is the 'melee combat' skill used for all hand-to-hand weapons (except lightsabers, "
                     "which is covered under the lightsaber skill). Melee weapons include vibro-axes, force pikes, "
                     "lubs, bayonets and even impromptu weapons like chairs and blaster butts.",
                     "Specific type of melee weapon — swords, knives, axes, vibroblades, vibro-axes."),
    'Melee Parry': (63, 'skill', 'Melee Parry', 'Melee Parry', 1, '1 Round', '1rnd', 1,
                    "Melee parry is the 'reaction skill' used if a character has a melee weapon and is attacked by "
                    "someone with a melee combat, brawling or lightsaber attack. (Melee parry can’t be used to parry "
                    "blaster attacks — that’s dodge.)",
                    "Type of melee weapon used — lightsabers, knives, clubs, axes, vibroblades."),
    'Missile Weapons': (64, 'skill', 'Missile Weapons', 'Missile Weapons', 1, '1 Round+', '1rnd+', 1,
                        "Missile weapons is the 'ranged combat' skill used to fire all types of missile weapons, "
                        "including grappling hook launchers, grenade launchers, and personal proton torpedo launchers.",
                        "Type or model missile weapon — concussion missile, grenade launcher, Golan Arms FC1 "
                        "flechette launcher, power harpoon."),
    'Persuasion': (65, 'skill', 'Persuasion', 'Persuasion', 4, '1 Round+', '1rnd+', 1,
                   "Persuasion is similar to con and bargain — and is a little bit of both. A character using "
                   "persuasion is trying to convince someone to go along with them — but they aren’t tricking the "
                   "person (that would be con), and they aren’t paying them (as in a bargain).\nHowever, potential "
                   "rewards can be offered — talking someone into rescuing a princess from an Imperial holding cell "
                   "is definitely a persuasion attempt. And stating that the reward would be “bigger than anything "
                   "you can imagine” without going into details is not unusual.",
                   "Specific form of persuasion — debate, storytelling, flirt, oration."),
    'Pick Pocket': (66, 'skill', 'Pick Pocket', 'Pick Pocket', 1, '1 Round', '1rnd', 0,
                    "Characters use pick pocket to pick the pockets of others, or to palm objects without being "
                    "noticed. When a character makes a pick pocket attempt, the victim makes an opposed search or "
                    "Perception roll to notice it.",
                    ""),
    'Planetary Systems': (67, 'skill', 'Planetary Systems', 'Planetary Systems', 2, '1 Round', '1rnd', 1,
                          "This skill reflects a character’s general knowledge of geography, weather, life-forms, "
                          "trade products, settlements, technology, government and other general information about "
                          "different systems and planets. Much of this information is gained from personal experience, "
                          "computer records and hearsay from others who’ve visited various systems.\nCharacters "
                          "specializing in particular planets have a deeper knowledge of more subtle details — more "
                          "than the average general database would contain. Although someone with an improved planetary"
                          " systems skill would know that Tatooine’s deserts are home to Jawas and Tusken Raiders, "
                          "those with planetary systems: Tatooine would know the role the Jawa scavengers play in "
                          "supplying the moisture farmers with spare parts and droids.",
                          "Specific system or planet — Tatooine, Endor, Hoth, Kessel."),
    'Powersuit Operation': (68, 'skill', 'Powersuit Operation', 'Powersuit Operation', 3, '1 Round+', '1rnd+', 1,
                            "Powersuits are devices which enhance a person’s natural abilities through servo-mechanisms"
                            " and powered movement. These suits are often used for construction or cargo movement work "
                            "wherever industrial droids are neither practical nor desirable. This technology has also "
                            "been adapted to the zero-gee stormtrooper (spacetrooper) battle suits.\nPowersuit "
                            "operation can be used as a “reaction skill” to dodge enemy fire.",
                            "Particular kind or model powersuit — spacetrooper armor, servo-lifter."),
    'Repulsorlift Operation': (69, 'skill', 'Repulsorlift Operation', 'Repulsorlift Operation', 3, '1 Round+', '1rnd+',
                               1,
                               "The character knows how to operate common repulsorlift (or “antigrav”) craft, including"
                               " landspeeders, snowspeeders, T-16 skyhoppers, cloud cars, airspeeders, speeder bikes, "
                               "skiffs and sail barges.\nRepulsorlift operation can be used for a vehicle dodge — a "
                               "“reaction skill” — to avoid enemy fire.",
                               "Type or model repulsorlift vehicle — XP-38 landspeeder, Incom T-16 Skyhopper, Rebel "
                               "Alliance combat snowspeeder."),
    'Repulsorlift Repair': (70, 'skill', 'Repulsorlift Repair', 'Repulsorlift Repair', 6, 'Various', 'var', 1,
                            "Repulsorlift repair represents a character’s affinity for repairing and modifying "
                            "vehicles with repulsorlift generators. Each roll may repair one damaged system aboard a "
                            "particular vehicle. The cost and difficulty to repair a vehicle depends on how badly it "
                            "is damaged, and what systems have been hit.",
                            "Type or model repulsorlift vehicle — XP-38 landspeeder, Incom T-16 Skyhopper, Rebel "
                            "Alliance combat snowspeeder."),
    'Rocket Pack Operation': (71, 'skill', 'Rocket Pack Operation', 'Rocket Pack Operation', 3, '1 Round+', '1rnd+', 0,
                              "This skill reflects the character’s ability to use personal, self-contained rocket "
                              "packs. Since these backpack units contain all the chemical thrust components for "
                              "propulsion and maneuvering, they can be used in zero, low or high atmosphere conditions."
                              " Characters with rocket pack operation gain no bonuses when operating “jet packs,” which"
                              " use the jet pack operation skill.\nRocket pack operation can be used as a “reaction "
                              "skill” to dodge enemy fire.",
                              ""),
    'Running': (72, 'skill', 'Running', 'Running', 1, '1 Round+', '1rnd+', 1,
                "Running is the character’s ability to run and keep his balance, especially in dangerous terrain. The "
                "running difficulty is based on the kind of terrain being crossed and how fast the character moves.",
                "Long distance, short sprint."),
    'Scholar': (73, 'skill', 'Scholar', 'Scholar', 2, '1 Round - Days', '1rnd-days', 1,
                "This skill reflects formal academic training or dedicated research in a particular field. Scholar "
                "also reflects a character’s ability to find information through research. Characters often choose a "
                "specialization to reflect a specific area which they have studied. Specializations are subjects often "
                "taught at the great universities throughout the galaxy, including archaeology, botany, chemistry, "
                "geology, history, hyperspace theories, and physics. Specializationscan also be topics a character can "
                "research on his own.\nScholar represents “book-learning,” not information learned from practical "
                "experience. A character can know the various hyperspace theories inside and out, but this doesn’t "
                "qualify him to fly starships through hyperspace (that’s covered by the astrogation skill). He might "
                "know the physical principles which make a blaster fire, but that doesn’t make him a better shot.",
                "Particular field of study — archaeology, Jedi lore, history, geology, physics."),
    'Search': (74, 'skill', 'Search', 'Search', 4, '1 Round+', '1rnd+', 1,
               "This skill is used when the character is trying to spot hidden objects or individuals. If the subject "
               "of the search has been purposefully hidden, the searching character makes an opposed roll against the "
               "hiding character’s hide skill. If the object hasn’t been hidden, the character simply makes a roll "
               "against a difficulty.\nThis skill is also used to spot characters using the sneak skill, such as a "
               "group of rebels moving into position to prepare an ambush, or someone attempting to conceal themselves."
               " This is an opposed roll — the character sneaking around makes a roll, and anyone who might spot the "
               "character makes a search (or Perception) roll.",
               "Tracking."),
    'Security': (75, 'skill', 'Security', 'Security', 6, '1 Round - Minutes', '1rnd-mins', 1,
                 "This skill represents a character’s knowledge of physical security systems: locks, alarm systems "
                 "and other detection devices. It does not govern computer security procedures.",
                 "Type or model security device — magna lock, blast door, retinal lock."),
    'Sensors': (76, 'skill', 'Sensors', 'Sensors', 3, '1 Round+', '1rnd+', 1,
                "Characters with the this skill can operate various kinds of sensors, including those that detect "
                "lifeforms, identify vehicles, pick up energy readings, and make long-distance visual readings. Sensors"
                " covers everything from portable hand scanners (like the one used by Han Solo on Hoth) to the huge "
                "sensor arrays used on capital ships and in military bases.\nSome scanners have die code bonuses — "
                "these extra dice are added when characters roll their sensors skill.",
                "Type or model scanner — hand scanner, med diagnostic scanner, heat sensor."),
    'Sneak': (77, 'skill', 'Sneak', 'Sneak', 4, '1 Round', '1rnd', 1,
              "Sneak represents the character’s ability to move silently, hide from view, move in shadows and otherwise"
              " creep around without being noticed. This is an opposed roll — the character sneaking around makes a "
              "sneak roll, and anyone who might spot the character makes a search or Perception roll.\nThis skill "
              "allows characters to hide themselves only — to conceal objects, they must use the hide skill.",
              "Specific type of terrain — jungle, urban."),
    'Space Transports': (78, 'skill', 'Space Transports', 'Space Transports', 3, '1 Round+', '1rnd+', 1,
                         "Space transports is used to pilot all space transports: any non-combat starship, ranging "
                         "from small light freighters (the Millennium Falcon is a highly-modified YT-1300 light "
                         "freighter) and scout ships to passenger liners, huge container ships and super transports. "
                         "Transports may be starfighter- or capital-scale.\nSpace transports can be used for a "
                         "starship dodge — a “reaction skill” — to avoid enemy fire.",
                         "Type or model transport — YT-1300 transport, Gallofree medium transport, Corellian Action VI"
                         " transport."),
    'Space Transports Repair': (79, 'skill', 'Space Transports Repair', 'Space Transports Repair', 6, 'Various', 'var',
                                1,
                                "Characters with this skill can repair and modify space transports. Each roll may "
                                "repair one damaged component aboard a particular transport. The cost and difficulty "
                                "to repair a vessel depends on how badly it is damaged, and what systems have been "
                                "hit.",
                                "Type or model transport — YT-1300 transport, Gallofree medium transport, Corellian "
                                "Action VI transport."),
    'Stamina': (80, 'skill', 'Stamina', 'Stamina', 5, 'Various', 'var', 0,
                "Stamina checks reflect that a character is being pushed to his or her physical limits. They should "
                "be called for once in a while to show the strain on a character; only require them when a character "
                "does something out of the ordinary.\nWhenever a character fails a stamina roll, he is fatigued; all "
                "actions are at −1D for every stamina check failed until the character rests for as long as he exerted "
                "himself.",
                ""),
    'Starfighter Piloting': (81, 'skill', 'Starfighter Piloting', 'Starfighter Piloting', 3, '1 Round+', '1rnd+', 1,
                             "Starfighter piloting is used for all combat starfighters, including X-wings, Y-wings, "
                             "A-wings, and TIE fighters.\nStarfighter piloting can be used for a starship dodge — "
                             "a “reaction skill” — to avoid enemy fire.",
                             "Type or model starfighter — X-wing, TIE/In, TIE interceptor, Z-95 Headhunter."),
    'Starfighter Repair': (82, 'skill', 'Starfighter Repair', 'Starfighter Repair', 6, 'Various', 'var', 1,
                           "nent aboard a particular transport. The cost and difficulty to repair a vessel depends on "
                           "how badly it is damaged, and what systems have been hit.",
                           "Type or model starfighter — X-wing, TIE/In, TIE interceptor, Z-95 Headhunter."),
    'Starship Gunnery': (83, 'skill', 'Starship Gunnery', 'Starship Gunnery', 3, '1 Round', '1rnd', 1,
                         "Starship gunnery is the “ranged combat” skill that covers all starfighter-scale weapons, "
                         "including laser cannons, ion cannons, concussion missiles, and proton torpedoes."
                         "\nStarfighter-scale weapons may be mounted on both starfighter-scale ships and capital-scale "
                         "vessels.",
                         "Specific type or model weapon — concussion missiles, ion cannons, laser cannon, proton "
                         "torpedoes, turbolasers."),
    'Starship Shields': (84, 'skill', 'Starship Shields', 'Starship Shields', 3, '1 Round', '1rnd', 0,
                         "Starship shields is the skill used to operate shields on all starfighter-scale ships. The "
                         "difficulty of the roll is determined by how many fire arcs the character is trying to raise "
                         "shields over (front, left, right, back).\nStarship shields can be used to bring up shields "
                         "— a “reaction skill” — to block enemy fire.",
                         ""),
    'Starship Weapon Repair': (85, 'skill', 'Starship Weapon Repair', 'Starship Weapon Repair', 6, 'Various', 'var', 1,
                               "Starship weapon repair covers a character’s ability to fix and modify starfighter-scale"
                               " weapons. The cost and difficulty to repair weapons depends upon how badly it is "
                               "damaged",
                               "Specific type or model weapon — concussion missiles, ion cannons, laser cannon, proton "
                               "torpedoes, turbolasers."),
    'Streetwise': (86, 'skill', 'Streetwise', 'Streetwise', 2, '1 Round - Days', '1rnd-days', 1,
                   "Streetwise reflects a character’s familiarity with underworld organizations and their operation. "
                   "He can use streetwise to make a contact in the criminal underworld, purchase illegal goods or "
                   "services, or find someone to do something illegal.\nIllegal activities may include the usual "
                   "vices: gambling, fencing stolen goods, racketeering, blackmail, contract killing, and fraud. "
                   "Because Imperial laws are repressive, some actions deemed “criminal” may be perfectly moral: "
                   "freeing slaves, delivering medicine and food to refugees from Imperial aggression, and smuggling "
                   "wanted criminals (such as Alliance personnel) through Imperial blockades.\nThis skill also "
                   "reflects knowledge of specific criminal bosses, such as Jabba the Hutt or Talon Karrde, and "
                   "their organizations and activities.",
                   "Specific planet or criminal organization — Celanon, Corellia, Jabba the Halt’s organization, "
                   "Black Sun, Talon Karrde’s organization."),
    'Submersible Vehicle Operation': (
        87, 'skill', 'Submersible Vehicle Operation', 'Submersible Vehicle Operation', 3, '1 Round+', '1rnd+', 1,
        "This skill allows characters to pilot submersible ships and boats. While these vehicles are seldom used in "
        "the higher-tech worlds, many low-tech cultures use them for inspection, exploration and transportation."
        "\nNote that submersibles which employ the use of repulsorlift may also require the use of the repulsorlift "
        "operation skill.\nSubmersible vehicle operation can be used for a vehicle dodge — a “reaction skill” — to "
        "avoid enemy fire.",
        "Particular submersible type or class — Bongo, electric submarine."),
    'Submersible Vehicle Repair': (
        88, 'skill', 'Submersible Vehicle Repair', 'Submersible Vehicle Repair', 6, 'Various', 'var', 1,
        "This repair skill represents a character’s ability to fix and modify submersible vehicles. Each roll may "
        "repair one damaged system aboard a particular submersible. The cost and difficulty to repair depends on how "
        "badly it is damaged, and what systems have been hit.",
        "Particular submersible type or class — Bongo, electric submarine."),
    'Survival': (89, 'skill', 'Survival', 'Survival', 2, '1 Round - Hours', '1rnd-hrs', 1,
                 "This skill represents how much a character knows about surviving in hostile environments, "
                 "including deserts, jungles, ocean, forests, asteroid belts, volcanoes, poisonous atmosphere worlds, "
                 "mountains and other dangerous terrain.\nSurvival can be rolled to gain general information — "
                 "revealing what the character knows about this environment — and it can give clues as to how best "
                 "to deal with native dangers.\nIf the character is in a dangerous situation, the player may roll the "
                 "survival skill to see if the character knows how to handle the situation.",
                 "Type of environment — volcano, jungle, desert, poisonous atmosphere."),
    'Swimming': (90, 'skill', 'Swimming', 'Swimming', 5, '1 Round - Hours', '1rnd-hrs', 0,
                 "This skill represents the character’s ability to stay afloat in aquatic environments — lakes, "
                 "oceans, flooding rivers and luxury starliner swimming pools. Swimming difficulties are determined "
                 "by the water conditions: the starliner pool is Very Easy, while a roaring river might be Very "
                 "Difficult.\nWhen a character fails a swimming check, he begins to drown. Roll 2D at the beginning "
                 "of each round; if the total is less than the number of rounds that the character has been drowning, "
                 "the character drowns and dies. Characters can attempt other actions while drowning at a −3D penalty. "
                 "Characters who are drowning may attempt to save themselves once per round. They must make a swimming "
                 "total at one level of difficulty higher than the one in which they failed their swimming roll (the "
                 "character doesn’t suffer the −3D penalty when making this roll).",
                 ""),
    'Swoop Operation': (91, 'skill', 'Swoop Operation', 'Swoop Operation', 3, '1 Round+', '1rnd+', 1,
                        "Swoops are dangerously fast, difficult to pilot vehicles which combine a typical repulsorlift "
                        "engine with an ion engine afterburner for unbelievable performance. Swoop operation reflects "
                        "a character’s ability to successfully fly what is little more than a powerful engine with a "
                        "seat.\nSwoop operation can be used for a vehicle dodge — a “reaction skill” — to avoid enemy "
                        "fire.",
                        "Specific type or model swoop — TaggeCo Air-2, Ubrikkian Skybird."),
    'Tactics': (92, 'skill', 'Tactics', 'Tactics', 2, '1 Round - Minutes', '1rnd-mins', 1,
                "Tactics represents a character’s skill in deploying military forces and maneuvering them to his best "
                "advantage. It may be rolled to gain general knowledge of how best to stage certain military "
                "operations: blockading a planet with a fleet, invading an enemy installation, assaulting a fixed "
                "turbolaser bunker.\nThis skill may also be used to determine the best response to an opponent’s move "
                "in battle: for instance, what to do if the enemy entraps your ships in a pincer movement, how to "
                "proceed in the assault should reinforcements arrive, what to do if a unit becomes trapped behind "
                "enemy lines.\nAlthough tactics rolls might reveal how best to handle military situations, the final "
                "outcome of how well the character’s side does in a battle hinges on other skill rolls — command for "
                "the leader, and the combat rolls of both forces.",
                "Type of military unit — squads, fleets, capital ships, ground assault."),
    'Thrown Weapons': (93, 'skill', 'Thrown Weapons', 'Thrown Weapons', 1, '1 Round', '1rnd', 1,
                       "Thrown weapons is the 'ranged combat' skill used whenever a character employs a primitive "
                       "thrown weapon, including throwing knives, slings, throwing spears and javelins.",
                       "pecific kind of thrown weapon — knife, spear, sling."),
    'Value': (94, 'skill', 'Value', 'Value', 2, '1 Round', '1rnd', 1,
              "This skill reflects a character’s ability to gauge the fair market value of goods based on the local "
              "economy, the availability of merchandise, quality and other market factors. The character can also "
              "gauge specific capabilities of and modifications made to goods with regard to performance.\nUsing "
              "value often answers the question, “How much is it really worth?” Results often depend on the source of "
              "information about the item, and how much the character already knows about that kind of merchandise. "
              "A starship dealer rattling on about a particular used-freighter might be exaggerating — although "
              "characters can make some estimations based on the starship model. If the item can be examined in person,"
              " its value is much easier to determine.",
              "Type of goods or specific planet’s markets — starships, droids, Kessel, Coruscant."),
    'Vehicle Blasters': (95, 'skill', 'Vehicle Blasters', 'Vehicle Blasters', 1, '1 Round', '1rnd', 1,
                         "Vehicle blasters is the 'ranged combat' skill used to fire vehicle-mounted energy weapons, "
                         "especially those that are speeder- or walker-scale. (The weapon’s description will list "
                         "which skill it uses.) Vehicle blasters can also be used to fire speeder or walker scale "
                         "weapons mounted on starships.",
                         "Type or model of vehicle-mounted blaster — heavy blaster cannon, heavy laser cannon, light "
                         "blaster cannon, light laser cannon, medium blaster cannon, medium laser cannon."),
    'Walker Operation': (96, 'skill', 'Walker Operation', 'Walker Operation', 3, '1 Round+', '1rnd+', 1,
                         "Walkers are difficult vehicles to learn how to operate. Generally only military characters "
                         "or characters who formally worked in an industrial field would have this specialized vehicle"
                         " skill. A character with this skill can pilot AT-ATs, AT-STs, AT-PTs, personal walkers and "
                         "various other types of walkers.\nWalker operation can be used for a vehicle dodge — a "
                         "“reaction skill” — to avoid enemy fire.",
                         "Particular kind of walker — AT-AT, ATST, AT-PT."),
    'Walker Repair': (97, 'skill', 'Walker Repair', 'Walker Repair', 6, 'Various', 'var', 1,
                      "Characters use this skill when repairing or modifying walker systems. Each roll may fix one "
                      "damaged component aboard a particular walker. The cost and difficulty to repair a walker "
                      "depends on how badly it is hit, and what systems have been damaged.",
                      "Particular kind of walker — AT-AT, AT-ST, AT-PT."),
    'Willpower': (98, 'skill', 'Willpower', 'Willpower', 2, '1 Round', '1rnd', 1,
                  "Willpower is a character’s strength of will and determination. It is used to resist intimidation "
                  "and persuasion attempts.\nAlso, when a character fails a stamina check, if the character can make "
                  "a willpower check at one higher level of difficulty, he can drive himself on through sheer "
                  "willpower. A character doing this has to make a willpower check as often as he would normally "
                  "have had to make a stamina check, with all checks at one difficulty level higher. Once the character"
                  " fails a check or stops pushing himself, he is completely exhausted and must rest double the "
                  "normal length of time. If, as a result of failing a stamina check, the character would have "
                  "suffered any damage, the character suffers one worse wound level as a result of pushing his body "
                  "far beyond its limitations.",
                  "Kind of coercion to be resisted — persuasion, intimidation.")}
# Species Dictionary. Key = Skill Name, Value = Tuple
# Tuple values in order below with explanation of each field.
#
#  species_id  - ID for species - Incremental number
#  name        - Name of the species
#  description - Description of the species
#  attr_dice   - Attribute dice allowed for character creation
#  min move    - Minimum movement value allowed
#  max move    - Maximum movement value allowed
#  min dex     - Minimum dexterity dice code
#  max dex     - Maximum dexterity dice code
#  min know    - Minimum knowledge dice code
#  max know    - Maximum knowledge dice code
#  min mech    - Minimum mechanical dice code
#  max mech    - Maximum mechanical dice code
#  min per     - Minimum perception dice code
#  max per     - Maximum perception dice code
#  min str     - Minimum strength dice code
#  max str     - Maximum strength dice code
#  min tech    - Minimum technical dice code
#  max tech    - Maximum technical dice code
species = {'Human': (1, 'Human', 'Bog Standard Human. Boring.', 12, 10, 12,
                     '2D', '4D', '2D', '4D', '2D', '4D', '2D', '4D', '2D', '4D', '2D', '4D')}
