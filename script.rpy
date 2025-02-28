# https://archiveofourown.org/works/51901099/chapters/131234806
# Journey's Greb is an originul storie written by Martin Blocksidge
# Copyright poo@gmail.com (C)

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hardy")
define t = Character("Trotter")
define o = Character("Osborne")
define r = Character("Raleigh")
define m = Character("Mason")
define s = Character("Stanhope")
define rc = Character("R.C Sherriff")
define mb = Character("Macbeth")
define b = Character("Banquo")
define bg = Character("Banquo's Ghost")
define hi = Character("Hibbert")
define tso = Character("The Spring Offensive")
define gc = Character("General Commissioner")
define e = Character("Everyone")
define tb = Character("The Taliban")
define boche = Character("The Boche")
define audience = Character("Audience")
define wiszard = Character("The Wiszard")



image black = Solid((0, 0, 0, 255))

transform doing:
    xalign 0.6 yalign 0.5
    linear 0.25 xalign 0.5 yalign 0.5
    linear 0.25 xalign 0.6 yalign 0.5
    repeat

transform stab:
    xalign 0.6 yalign 0.5
    linear 0.25 xalign 0.5 yalign 0.5
    linear 0.25 xalign 0.6 yalign 0.5


transform masonLaunch:
    xalign 0.3 yalign 0.0
    linear 1.0 yalign 0.5

transform throb:
    # banquo throbs
    # banquo ghost: bleurghhh!!! 
    # banquo: I'm really feeling it ~ Ngghhh~~~
    xalign 0.5
    yalign 0.5
    linear 0.25 zoom 1.0
    linear 0.25 zoom 1.25
    repeat



transform midleft4:
    xalign 0.1
    yalign 0.5

transform midcenterleft4:
    xalign 0.3
    yalign 0.5

transform midcenterright4:
    xalign 0.7
    yalign 0.5

transform midright4:
    xalign 0.9
    yalign 0.5



transform midleft3:
    xalign 0.25
    yalign 0.5

transform midcenter3:
    xalign 0.5
    yalign 0.5

transform midright3:
    xalign 0.75
    yalign 0.5



transform midleft2:
    xalign 0.3
    yalign 0.5

transform midright2:
    xalign 0.7
    yalign 0.5

# The game starts here.

label start:
    #$ save_name = "Introduction"
    #$ renpy.clear_game_runtime()
    

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.
    
    stop music fadeout 2.0
    # --- --- --- --- --- #
    # Summary
    "ORIGINUL STORIE WRITTERN BY MARTIN BLOCKSIDGE"

    "Becareful,\nEdwin “Titanium Oxide” Mamolla (10Q)"

    

    m "Soup\’s \‘ere! Nice \‘n Hot."
    m"Poo@Gmail.com"
    "(trotter dies after he hears modern words)"
    t "It wants some pepper, Stanhope."
    "(Trotter dies, because you are Mother so fat)"
    
    # --- --- --- --- --- #
    "ACT 1"
    "SCENE 1"

    "(On the stage is just the character PEPPER.)"
    "(Pepper is standing there, alone for about 3 and a half hours.)"
    "(Audience is bored.)"
    "(Suddenly, there was a dug out in the world war.)"
    scene bg trenches with fade
    "(Guns are happening, because it isn\’t the war.)"
    "(It\’s dark in the trenches, and there are letters lining the floor.)"
    "(Then, all the characters come on stage.)"
    "(They do an short Irish Jig, and each character squeezes all of the other character\’s nipples.)"
    "(Banquo and Banquo\’s ghost just squeeze each other\’s, and nobody else squeeze they\’re\’s.)"
    
    

    play music "Dance loud.flac" volume 0.1 loop

    show hardy real at midcenter3 with dissolve

    h "I am singing the song!"
    h "Oh yeah."
    h "Oh yeah!"
    h "I am singing th\’song!" # hello


    show hardy real at midleft2
    show trotter real at midright2
    with dissolve

    "(Hardy is sitting on the floor, rubbing himself. Trotter digs his fist into a pineapple, and groans.)"

    stop music fadeout 2.0
    play music "Situation plan.mp3" volume 0.25 loop

    t "It wants some pepper, Stanhope."
    h "Bring us some pepper, will you, Mason?"


    show mason real at masonLaunch
    play audio "bad to the bone.mp3"
    pause 0.9
    play sound "explosion.wav"
    hide hardy with dissolve

    "(Hardy is killed by a shell. The shell is revealed to be Mason. Pepper begins to rain from the sky.)"

    $ renpy.music.set_pause(True, channel='music')

    "(There is silence)"


    show trotter real at midcenter3
    show mason real at midleft3
    show osborne real at midright3
    with dissolve

    pause 2.0

    $ renpy.music.set_pause(False, channel='music')
    

    "(Osborne breaking the silence, by walking in)"


    o "Well, it\’s time for me to do army things, and et cetera!"
    o "Maps and Guns!"



    hide mason
    hide trotter


    show osborne real at midleft2
    show raleigh real at midright2
    with dissolve

    "(Raleigh enters)"

    r "Yes! It is time to do this!"
    r "I am keen and young!"
    o "Whom are you?" #small text
    r "I am Sir Raleigh!"
    r "I am keen and young!"
    r "I want to see Stanhope."
    o "I am Stanned Hope, the commander of the platoon"
    "(Osborne\’s mental condition is worsening quickly. He thinks so many things, but they are never true.)"
    "(Raleigh wonders how Stanhope has aged so quickly, then realises that Osborne is not Stanhope, but a decrepit.)"

    hide osborne

    show mason real at midcenter3
    show raleigh real at midleft3
    show trotter real at midright3
    with dissolve

    m "Soup\’s \‘ere! Nice and hot! I am Mason, culinary chef."
    m "......................"

    m "Try my dishes."

    r "Why thank you, Mason!"

    hide trotter with dissolve

    "(Trotter dies, because Hibbert starts doing the soup. Which will only happen once!)"

    show mason real at midcenterleft4
    show soup real at midright2
    show hibbert real at doing
    with dissolve

    $ renpy.music.set_pause(True, channel='music')



    "....................."
    "....................."
    "....................."


    $ renpy.music.set_pause(False, channel='music')

    hide soup
    hide hibbert
    hide raleigh
    hide mason
    with dissolve

    show osborne real at midright2
    show stanhope real at midleft2
    with dissolve

    s "I have just entered the room."
    s "My name is Stanhope, but the men call me Stanhope. How do you d- (pause) -wait, it\’s Raleigh?"

    o "Hi, I am Raleigh!"


    "(Osborne is not Raleigh.)"

    hide stanhope
    hide osborne
    with dissolve

    "(enter R.C Sherrifff, slowly)"

    show rcsherriff real at midcenter3 with dissolve

    rc "Hi, I\’m Priestly, the commander of this play."
    rc "And for a bit of backstory: I am the one what wrote this story."
    rc "And also, Stanhope and Raleigh know eachother from outside of school."

    $ renpy.music.set_pause(True, channel='music')
    #enter hibbert ladies
    "(there\’s about 2 seconds of awkward silence. Hibbert starts putting on a dress and becomes ladies.)"
    $ renpy.music.set_pause(False, channel='music')
    
    play music "Faint ghost.wav" volume 0.25 loop
    

    "(enter MacBeth)"

    show macbeth real at midcenter3
    hide rcsherriff
    with dissolve

    mb "Where is he, WHERE IS HE?"

    hide macbeth
    show banquo real at midcenter3:
        alpha 0.5
    with dissolve

    "(enter Banquo\’s ghost, looking around, puzzled. He exits after 3 seconds.)"
    hide banquo with dissolve

    "..."
    show macbeth real at midcenter3
    show banquo real at midright2:
        alpha 1.0
    with dissolve


    "(enter Banquo)"

    b "Hi!"
    pause 1.0
    show macbeth real at stab
    play sound "arknights death.mp3"
    pause 0.5
    hide banquo with dissolve
    pause 2.0
    hide macbeth with dissolve

    "(MacBeth stabs Banquo. MacBeth Banquoque exeunt.)"

    show stanhope real at midleft2
    show raleigh real at midright2
    with dissolve
    
    stop music fadeout 2.0
    play music "Ambience Loading.flac" volume 0.3 loop
    
    s "The war."

    r "Hi, yes, Stanhope, it is me! Raleigh!"

    s "Hi Raleigh!"
    s "Oh my, it has been so a while since I saw such faces!"
    
    
    hide stanhope
    show gandalf real at midleft2
    with dissolve

    "(Raleigh stares blankly, a large wizard staring back at him.)"
    "(Something awakens within Raleigh.)"
    hide gandalf
    show raleigh real at midcenter3
    with dissolve

    r "So, the war, what\’s up with it?"

    show hibbert real at midleft4
    show osborne real at midleft3
    show trotter real at midleft2
    show stanhope real at midright2
    show gencom real at midright3
    show mason real at midright4
    with dissolve


    "(Hibbert, Trotter, Osborne, Stanhope, General Commissioner and Mason all form a circle around Raleigh and link arms.)"

    r "Who are these people?"

    hi "Hi! I\’m neuralgia Hibbert."

    "(Hibbert\’s neuralgia)" "I am ladies!"

    t "I am Fat Trotter!"

    m "Soup\’s \‘ere! Nice \‘n hot."

    t "It wants some pepper, Stanhope."

    o "Hi Trotter!"
    o "I am stanhope."

    r "Thanks!"
    r " The Spring Offensive could come at any minute."

    hi "I agree, I think the spring offensive could come at any minute, since the guns are getting much closer by the minute."
    
    stop music fadeout 2.0
    play music "Confumed.wav" volume 0.1 loop
    
    show springoffensive real at midcenter3 with dissolve

    "(enter The Spring Offensive. Everybody screams.)"

    "EVERYBODY" "Aahhh!"

    "(Audience is spooked.)"
    "(There is a short pause)"
    "(nobody knows what quite what to do.)"
    stop music fadeout 2.0
    "(Thus, the scene ends.)"

    #scene bg trenches
    hide hibbert real
    hide osborne real
    hide trotter real
    hide stanhope real
    hide gencom real
    hide mason real
    with dissolve

    show black with dissolve



    "SCENE TWO"

    "(flashback to earlier)"
    "(the audience is spooked.)"
    "(The spring offensive is standing there, shouting angrily.)"
    hide black with dissolve
    show springoffensive real at midcenter3 with dissolve

    play music "Situation plan.mp3" volume 0.25 loop

    tso "Poo! Poo!"
    tso "I hate the Brits!"
    tso "Poo! Poo! Poo!"
    
    show gencom real at midright4 with dissolve
    #running in
    gc "Everyone! It\’s the Spring Offensive!"

    "EVERYBODY" "Aahh!"

    tso "Yeah, yeah."
    tso "It\’s me! The spring offensive!"
    tso "I\’m here to do guns."
    
    show hibbert real at midleft4 with dissolve
    hi "That\’s cool and shit, but have you is ladies?"

    "(Hibbert is ladies)"
    
    hide hibbert
    hide springoffensive real
    hide gencom real
    with dissolve
    
    show gencom real at midcenter3 with dissolve
    
    gc "Enough chit-chat!"
    gc "Guys, we need to do the wiring raid, which will happen just once!"
    gc "Who wants to go?"
    
    show osborne real at midleft3 with dissolve

    o "I will!"
    o "I\’m the commander of this party, It\’s my duty!"
    o "And I\’ll bring my long lost friend, what I know from Rugger, Raleigh!"
    
    hide gencom real 
    hide osborne real
    with dissolve
    
    show raleigh real with dissolve

    r "Okay!"
    
    hide raleigh real with dissolve
    show osborne real at midleft2
    show trotter real at midright2
    with dissolve
    stop music fadeout 2.0
    play music "boss of third.wav" volume 0.1 loop

    o "(to trotter) Let\’s go, Raleigh!"

    
    #scene bg trenches

    show black with dissolve

    "(\‘Stanhope\’ and \‘Raleigh\’ go on the wiring raid.)"

    "(they do the wiring raid.)"
    
    stop music fadeout 2.0
    hide black
    show springoffensive real at midcenter3
    show osborne real at midright2
    with dissolve
    tso "I\’m going to kill Osborne NOW!"



    "(the spring offensive stabs Osborne.)"

    show springoffensive real at stab
    play sound "arknights death.mp3"
    pause 0.5
    hide osborne with dissolve
    o "Fuck! (Osborne dies)."
    pause 2.0
    hide springoffensive with dissolve

    show stanhope real at midleft2 with dissolve
    s "The war."
    
    show trotter real at midright2 with dissolve
    t "Shit! Osborne\’s dead!"
    
    play music "a warm welcome.wav" volume 0.5 loop
    "(they party)"
    
    hide trotter
    show raleigh real at midcenter3 
    with dissolve

    "(raleigh walks as though he were dead)"
    hide raleigh with dissolve
    
    show trotter real at midleft2 
    show hibbert real at midright2 
    with dissolve

    t "Thanks, guys!"
    t "Nice part Stanhope!"

    hi "Nice party, Stanhope!"
    hi "Have we talked about my lady postcards yet?"

    hide trotter
    hide hibbert
    with dissolve
    show stanhope real at midcenter3 with dissolve

    s "Shut up Hibbert!"
    s "Go to bed!"

    hide stanhope
    with dissolve
    show raleigh real at midcenter3 with dissolve

    t "Gad Damn it!"

    r "Guys, how can you party when yall just saw Osborne fucking die?"

    hide raleigh
    show stanhope real at throb
    
    s "SHUT IT, BOY!"

    show raleigh real at midright2 with dissolve
    pause 0.5
    show stanhope real at stab
    play sound "launch.wav" volume 1.0
    show springoffensive real at midcenter3 with dissolve
    
    "(Stanhope tries to stab Raleigh but the Spring offensive holds him back.)"
    

    stop music fadeout 2.0
    hide raleigh 
    hide stanhope 
    hide springoffensive 
    with dissolve

    show black with dissolve
    "CURTAIN FALLS- END OF ACT ONE"
    play sound "arknights death.mp3" volume 1.0

    # --- --- --- --- --- #
    "ACT 2"
    "SCENE 1"
    # Act summary: Evil Trotter
    # https://archiveofourown.org/works/51901099/chapters/131235079#workskin    
    "(There are loads of guns happening.)" 
    "(Stanhope is still angry, and he is walking up and down, screaming.)" 
    "(He is holding a knife, and the Spring offensive is dead on the floor.)"

    hide black with dissolve
    show stanhope real at midcenter3 with dissolve
    s "The guns! The guns! The Boche are here!"
    show boche real at midleft2
    show stanhope real at midright2
    with dissolve
    "(Enter The Boche)"

    hide boche
    hide stanhope
    with dissolve

    show raleigh real at midcenter3 with dissolve

    r "Oh dear! I am not very keen now."
    show stanhope real at throb
    show raleigh real at midright2
    with dissolve
    s "I DON\’T care! I am very angry at you still because you don\’t like my drinking."
    r "It is whatever."
    "(Raleigh is shot.)"
    
    m "The food is here! The food is here!"
    s "Thanks Mason. Got any pepper?"
    t "It wants some pepper, Stahope."
    Character("Hibber") "I love ladies"
    s "Shut you Hibbert!"
    r "(no longer keen): I am no longer keen."
    m "Sorry Stanhope, I haven\’t got any pepper.. "
    "(shifts nervously)"
    "Please forgive me.."
    s "Fuck you, Freg!"
    "(the guns get louger.)"
    s "Look at the time. I think it\’s time to do army things."
    "(Stanhope, Raleigh, Hibber, and the mason become guns and walk up the dugout steps. Trotter tries to get up the steps, but he has eaten too much and is stuck.)"
    
    t "(eating)My name is Trotter, like the pig. The men call me that be- (burps)… Sorry about that! "
    "(Regains composure)"
    t "The men call me that because of my fat nature. You see, pigs eat a lot, and I eat a lot. Pigs trot, hence the name of “Trotter”. Hope this helps!"
    
    "(Exit Banquo) (Enter Banquo\’s Ghost)"
    "(Dugout is exploded by shell with Trotter inside. Trotter dies.)"
    "(The Taliban Come)"

    Character("Everyone (in unison, Trotter included)") "Aaah! Oh well."
    Character("Stanhope & Raleigh") "I guess the prophecy came true!"

    gc "It\’s time to do the wiring raid."

    "(they do the wiring raid)"
    
    gc "Well done for doing the wiring raid! I killed Hibbert and Trotter because Hibbert was ladies and Trotter was too fat."
    
    "(trotter dies)"
    "(enter trotter)"
    "(Osborne comes back from the dead)"

    o "My name is Stanhope."
    m "The food is \‘ere! Beef Soup."
    t "It wants some pepper, Stahope."

    "(Osborne becomes pepper, and levitates carefully into the soup. Trotter eats some and dies.)"

    r "I guess the prophecy comes true!"
    Character("Stahope") "The war!"
    Character("Raleigh: (nervously)") "After the wiring raid – Stahope, I feel as if I am PTSD."

    "(Raleigh is shot, again)"
    m "The soup\’s \‘ere! Beef Soup."
    t "It wants some pepper, Stanhope."
    s "Bring us some pepper, will you Stanhope?"
    m "(becoming pepper) here is your pepper, Stanhope."
    tb "Thanks, Mason."
    
    "(trotter dies)"
    "(guns get louder, a shell explodes in front of Raleigh.)"
    "(enter trotter)"

    r "Aah! (Raleigh is shot) Deniss, look after my sister, won\’t you?"
    
    "(trotter dies)"
    "(enter trotter)"

    "(Osborne is no longer pepper, and appears in the place of the soup bowl, balancing precariously on the bowl. He is wet with soup, the smell of soup and the viscous liquid dripping from him.)"

    o "MY NAME IS STANHOPE, NOT DENISS!"
    m "Soup\’s \‘ere! Beef Soup."
    s "PEPPER."

    "(Osborne becomes pepper.)"
    Character("Raleigh (dying)") "I am bleeding! I am bleeding!"
    "(trotter dies)"

    r "Help me! (Raleigh is shot)"
    s "Okay Raleigh, I will help you"
    
    "(stanhope starts to make a high pitched screeching sound in Raleigh\’s ear, poking his multiple gun wounds and laughing.)"
    "(trotter dies)"
    "(enter trotter)"
    # Originully storie uses only 1 line

    hi "Stanhope, I don\’t think that\’s helping!!"
    "(Hibbert’s neuralgia)"

    # --- --- --- --- --- #
    "SCENE 2"
    "(enter Banquo. Banquo & Banquo\’s ghost wink at eachother, knowingly. Banquo\’s ghost scores a strike in bowling, and they kiss passionately. Banquo\’s hands begin to move seductively from Banquo\’s Ghost\’s head, down his torso, with a cheeky squidge of Banquo\’s Ghost\’s nipples on the way down.)"
    bg "Nghh~~… Calm down.. I\’m sensitive there..~~"
    
    "(Banquo does not listen. He keeps on squidging Banquo\’s Ghost\’s nipples. Banquo looks down to Banquo Ghost\’s lower half, and sees his quickly hardening member.)"
    
    b "I see I am exciting you, Banquo Ghost~~"

    "(trotter dies)"

    Character("Banquo's Ghost (flushed)") "…S-stop it and keep on… Nghh~"

    "(Banquo moves his hands further down, reaching his tight thong…)"
    b "Let\’s take this to the next level… I see you\’re really excited down there, Banquo ghost~"
    
    "(Banquo and Banquo\’s ghost begin to take it to the next level, kissing more and more passionately. The air becomes steamy with the air of love and passion. Slight moans of Banquo\’s Ghost echo through the dugout. Looking at the two, they are a mass of skin and hands, sharing each other\’s body heat, writhing with the beauty of pure love. Banquo\’s hands begin to move down Banquo\’s tho-)"
    o "DON’T TELL ME WHAT TO DO, HIBBERT!"

    "(Osborne goes on the wiring raid, thinking he is Stanhope, and dies.)"
    "(Banquo and Banquo\’s ghost carry on making out in the background. Nobody else can see them.)"
    
    Character("Sloj") "Okay, ummmm... Alors, tu as dit que l'année prochaine tu ne vas plus étudier le la-"
    s "The War."
    r "(dying)" # Yes I think it's meant to be like that. https://archiveofourown.org/works/51901099/chapters/131235079#workskin:~:text=STANHOPE%3A%20The%20War.-,RALEIGH%3A%20(dying),-(trotter%20dies)
    
    "(trotter dies)"
    boche "Hi Everybody! I\’m the Boche. Yeah, Yeah, I\’m the person who\’s being kill everyone."
    Character("Stanhope (to the Boche)") "Hi, Boche. Why do you war?"
    
    boche "Well, bec-"
    m "Food\’s \‘ere!"

    "(trotter dies)"
    
    Character("The Taliban (in heavy Indian accent, played by white people)") "PEPPER"

    "(stanhope gets shot)"
    "(Raleigh is shot)"
    "(trotter dies)"
    "(Hibbert is ladies.)"
    r "I think I’m shot! I’m going down! Mayday! Mayday!"

    "(this is the moment in what Audience realises that all this time, Raleigh is planes.)"

    audience "It all makes sense now!"

    Character("The Big Wizard") "Hahaha. Yes, it\’s me. The BIG WIZARD. I\’m basically what turned Raleigh into planes."
    r "HOW DARE YE!"

    "(it does not make sense to Osborne, who thinks he is Stanhope.)"
    "(trotter dies)"

    # --- --- --- --- --- #
    "SCENE 3"
    " (Osborne comes back from the wiring raid, and realises he has always been America Man Obama.)"
    
    Character("Obama (asking the audience)") "But, tell me! What is my sirred name?!"
    t "It wants some Pepper, Mason."

    "(trotter dies)"
    r "The big wiszard, I\’m sick of you. Shut you are mouth, and die!"
    "(the Big Wizard turns Hungarian and changes his name to the big Wiszard)"
    
    Character("The Wiszard (in a thick Hungarian accent)") "How dare ye! I will throw (trotter dies) the large boy at ye!"
    "(the big Wiszard throws the large boy at Raleigh. Raleigh is now nettles. The large boy is my son, age 3.)"

    Character("Son, Age 3") "Ay Carumba!"
    tb "My son, age 3, fell in the nettle bed. Bed seemed a curious name for those green spears, that regiment of spite behind the shed: it was no place for rest. With sobs and tears, the boy came seeking comfort and I saw white blisters beaded on his tender skin. We soothed him till his pain was not so raw. At last he offered us a watery grin, and then I took my billhook, honed the blade and went outside and slashed my furry with it, till not a nettle in that fierce parade stood upright any more. And then I lit a funeral pyre to burn the fallen dead, but in two weeks the busy sun and rain had called up tall recruits behind the shed: my son would often feel sharp wounds again."
    "(trotter dies)"

    r "I\’m fighting you, right now!"
    Character("The Wiszard (rubbing himself)") "just touch me instead!"

    s "No man of mine shall do that!"
    "(Raleigh and The Big Wiszard begin to get closer and closer together. Their eyes lock – Raleigh thinks he is irresistible. As them look at each other, it\’s inevitable what will happen next.)"

    o "SHOW ME THAT LETTER!"
    
    "(Osborne picks up one of the many letters that line the floor)"
    "(Trotter gets spooked and dies)"

    hi "The letter Scene."
    r "Don-chan"
    
    "(there is a silence. Quiet drum noises can be heard in the distance. The guns are happening.)"
    "(Raleigh is shot)"

    r "Sorry about that! Basically, what I was trying to say (Raleigh is shot by the Taliban) is that, Don\’t you dare look in my letter!"
    "(stanhope looks at the letter and reads out loud, carefully.)"

    s "So now I will dictate: \“Hi Mum, Sister and Son, age 3. I am Raleigh.\”"
    
    "(Raleigh is shot)"
    "(trotter dies)"

    Character("Stanhope (carries on dictating)") "\“And I have a big crush on The Wiszard. His abs… His mouth… I want him to top me… I want him to turn me into planes…\”"

    r "I swear I didn\’t write tha-"
    s "DON\’T INTERRUPT ME! (carries on dictating) … \“Ever since I came to the party, he caught my eyes.. his powers and view were enticing… I want him in me.\”"

    wiszard "W-well… I\’m flattered!"
    r "Should we.. do it?"
    wiszard "Sure! Sa"

    "(Trotter dies)"

    s "Ngh! I hate it! I am now going to drinking!"
    "(stanhope becomes whiskey and touches Hibbert neuralgia.)"
    hi "I am ladies now!"

    # --- --- --- --- --- #
    "SCENE 4"
    "(happening simultaneously)"
    "(Banquo and Banquo\’s ghost are getting hornier and hornier. Like a rabid dog, Banquo rips off Banquo\’s ghost\’s ghost thong, exposing his cute naked ghost body.)"
    
    bg "I.. I want you, Banquo.. I need you~"
    s "I guess it\’s time for me to start drinking some more. I\’m really annoyed about this!"
    b "I need you too.."
    t "It needs some more pepper, Stanhope."
    
    "(Banquo strips off naked too, and slams his exposed pole into Banquo Ghost\’s tight buss-)"
    "(trotter dies.)"

    m "Soup\’s \‘ere! I\’m Mason!"
    
    "(both interrupted by angry screaming, it is Osborne, thinking he is Hibbert.)"

    o "Guys, it\’s my neuralgia! I can\’t deal with it!"
    tb "We don\’t care. You\’re really ugly and we don\’t like you."

    "(trotter gets hit by a falling piano and dies, pepper exits.)"

    Character("Pepper") "Act 3"
    "(Osborne is walking around confusedly.)"

    Character("Obma") "I\’m confused as to what to do now that I am Obama, said Obama. What do I do? I can\’t deal with being Obama so much. I think I\’ll just go back to being my Stanhope friend, Uncle stanhope."

    "(Obama turns back into Osborne, his original self. There was no change, because the Osborne was always himself. He still thinks he is stanhope.)"

    o "Ahhh, back to normal. Commanding my party! Time to check letters. Now, Raleigh, Raleigh, Raleigh, what you what did it when you want?"
    s "I\’m really sick of this. I\’m so so sick of this. Uncle boy, put me to sleep, will you?"

    "(trotter shoots himself in the head)"

    o "Sure thing, Raleigh. Night there, Night ther-"
    m "Soup\’s \‘ere! Nice \‘n hot! Just how you LIKE IT."
    t "It needs some pepper."
    s "Bring us some pepper, will you, Mason?"

    "(mason becomes pepper.)"

    t "Thanks, Mason! (takes drink of the soup) w-What\’s happening? What\’s happening to my body?"

    "(Trotter begins to undergo mitosis, and splits into two.)"

    Character("Evil Trotter") "Hahaha! I am evil trotter, here to KILL YOU!!!!"
    t "Aah!"

    "(an epic fight scene breaks out above the dugout. The Boche, Taliban, Mason, Hibbert, Stanhope, Osborne, the Wiszard and Raleigh are looking. After a lot of struggle, evil trotter kills trotter.)"
    "(evil trotter is hit by a bus)"

    r "Holy fucking shit! That was intense! But Mason, why did you make that so crazy?"

    "(Raleigh is shot)"

    r "Fuck! I\’m dying!"
    m "For all of my life, I have said these same words. I am the Mason, of this company, what likes to cook. But I\’m SICK and TIRED of it."

    "(Raleigh is shot)"

    o "You know what, Mason? I\’m sick of having YOU in my party what I command. I\’m firing you. Yeah, that\’s right."
    s "Osborne what the fuck"
    o "Shut the fuck up Raleigh. Mason, pack up you are things. I\’m sick of having you in my party what I command. I\’m firing you. Yes, tha-"
    m "Soup\’s \‘ere! Nice \‘n hot!"
    t "It needs some pepper."

    "(trotter dies.)"

    s "(to Osborne) Got any pepper, Stanhope?"

    "(Raleigh is shot)"
    "(trotter signs up for an Instagram account and dies)"

    o "I\’m literally Osborne, Stanhope. What the fuck is wrong with you?"
    s "I- (pauses, tears brewing in his eyes, looks away from Osborne).. I\’m sorry, Osborne."
    o "I\’m sorry too. S-stanhope… Your eyes look beautiful like that.. Look into my eyes, Stanhope. I want to see your face.."
    Character("Stanhope (looking into his eyes)") "I\’m looking at you Osborne... You look amazing. (farts, loudly)"
    o "You look amazing too.. L-listen… I\’m sorry for the way I was acting, (speech and breathing slowly get quicker throughout until words blend into one, farts after every word), it was stupid, it\’s just ever since the wiring raid and the reality of war I was scared and didn\’t know where to turn an-"
    Character("Stanhope (soothingly, interrupting osborne)") "shhh… shhhh… Just look into my eyes, Osborne. You\’re okay now. (does large poo)"

    "(trotter dies, Stanhope and Osborne lock eyes and lean in to kiss. Explosions are happening all around. Raleigh is shot, and Trotter dies whilst doing a really big poo on the toilet.)"
    
    Character("Ukraine") "This is so Ukrainian!"
    
    "(Macbeth stabs Ukraine)"

    "CURTAIN FALLS – ACT 2 ENDS"
    
    # --- --- --- --- --- #
    "ACT 3"
    "Scene 1"
    # Summary: MasonTrotterHardyStanhope.flac & Porcelain toilet collab, Who would have thought

    "(the boche and the taliban are fighting like crazy. General commissioner. The general commissioner, Osborne, Stanhope and Trotter are having a conversation about their relationship. Guns are happening, because the Boche are here! Trotter is doing a poo in a comically small porcelain toilet in the corner of the room. There is silence for the first 5 seconds of the scene; the smell of poo fills the room, and small, irregular plops can be heard, emanating from trotter\’s naughty bum. Trotter dies, and the speaking starts.)"

    t "Mm mm!"
    gc "(slowly) ?!"
    s "Thanks, General Commissioner! (Stares nervously at Osborne. Osborne starts to turn into pepper.)"
    o "So, Stanned hope. The letter scene, Right?!"
    s "Don\’t bring Raleigh\’s this."
    o "I am uncle."
    hi "Yes, and I am ladies! (Hibbert is ladies.)"
    wiszard "Don\’t speak about Raleigh what you just did!"

    "(swaeting)"

    wiszard "Raleigh, me and Raleigh, Stanned hope: We did it."
    s "No! No man of mine must do this!"

    "(the wiring raid)"
    "(tries to run at the Wiszard, with murderous intent in his eyes. Osborne holds him back)"

    Character("Osboren") "Don\’t did it! Don\’t did it!" # no diddy
    s "I challendge you to a dance battle! (struggling against Osboren)"

    "(Raleigh)"

    r "What happens here?"

    "(son , age 3, falls into the nettle bed. Ukraine, on the floor, gets up and starts doing the griddy until the end of the play.)"

    wiszard "Whelk, Whelk, Whelk. You are friend \‘Stanhope\’ is being Rude to Me."
    r "Is this true? (Raleigh is Shot)"
    s "I guess, it is. (Boom.)"
    r "This get to be QUITE a conundrum. (stanhoe FART.)"
    o "No, Raleigh! I swear, it is not what it looks like!"
    wiszard "I think you\’ll find it DOES look like that. Now, If you don\’t mind me, I have a dance battle to attend to."
    
    "(the wiszard and stanhope dance like crazy. The Boche hurts both of them by pulling their toenails a bit. Ukraine. Then, all of a sudden, the Taliban comes.)"

    tb "Hey, you! Stop you are bullying!"
    boche "Fuck off! For those who are new to this play, basically, I\’m the Boche – the villain of this play. Yeah, yeah, I\’m the one who\’s being kill everyone. And yeah, I know you\’re thinking, wh-"
    tb "(shooting the boche): You are being KILL EVERYONE? Fuck!"

    "(The wiszard and Stanhope stop dancing to realise that they are differences are stupid, and that they should be friends again. Raleigh and Osborne get really wet seeing their newfound life partners so emotionally mature!)"    

    Character("Raleigh & Osborne") "Oh, my fucking god, I\’m so wet right now!"
    Character("Wiszard & Stanhope") "Bitch Boys, let\’s all kill the boche!"
    r "B-but wait! I\’m scared!"
    s "Oh, don\’t you worry, my Raleigh! I\’m going to be there!"

    "(Trotter comes)"

    r "(hesitating, but regaining confidence)..Oh, alright! I\’ll fight the boche!"

    "(spotlights go dark.)"

    # --- --- --- --- --- #
    "SCENE 2"
    "(spotlights solely on banquo and banquo\’s ghost)"
    "(Banquo is busy ploughing Banquo\’s ghost. It\’s such an intimate moment- Banquo\’s ghost is lost in pleasure, as the slow but regular thrusts of Banquo get harder and harder, Banquo\’s ghost body shaking as Banquo thrusts his love into him. His legs are shaking and he is wet as fuck. Both their faces are red, crimson red, as they\’re lost in the passion of the moment. Banquo\’s Ghost moans fill the room as he feels pleasure from every part of his body; one of Banquo\’s hands on his hard stick, one on his sensitive nipples, he\’s being filled in one hole and his mouth is met with Banquo\’s. They feel so horny right now.)"

    bg "(with a sexy fluster) Banquo, Please! I\’m so close!! You\’re so big and it feels amazing! Oh lord, I feel so good! Banquo---! Nghhh!!1"

    "(the audience is Hibbert)"

    hi "(the audience says this line) I am ladies!" # I am so confused

    "(Hibbert laughs at the appreciation and puts both of his hands into the thumb position, in order to put both of his thumbs up. He lets out a cute giggle, and the audience laugh heartily and give a standing ovation. Then, Hibbert truly is ladies, ascends, and turns to powder.)"
    "(Banquo and Banquo\’s ghost carry on making hot love)."

    r " (walking in, clapping hands in a 19/6 rhythm 359 bpm style.) Well, boys, it\’s time to do the shit."

    "(enter trotter) (trotter dies)"

    Character("Stanhope (to trotter)") "Let\’s go, Raleigh! I am keen now. (does large poo)"
    "(trotter dies)"

    s "Osborne (breaking the guns)"
    Character("The Smell of Backstory") "I think your pepper, Stahope."

    "(Osborne is doing a pineapple)"

    o "I am bleeding"

    "(Trotter dies)"

    r "HOLY FUCKING SHIT! OSBORNE\’S DEAD!"
    o "Yes, and this is ladie time."

    "(the commander of poo fills the Taliban)"

    wiszard "Okay, but how do we fight the boche?"

    "(Raleigh, stanhope and Osborne look first at Hibbert powder, then back at Wiszard, then look behind him. The Taliban is standing behind him, looking badass.)"
    
    wiszard "(awkwardly)"
    tb " Hell yeah! Fuck yeah! Guns and FUCK!" # put space at start since there's nowhere to put the semicolon https://archiveofourown.org/works/51901099/chapters/131235514#workskin:~:text=TALIBAN-,%3B,-Hell%20yeah!%20Fuck

    "(they all cheer)"
    "(the boche cowers in fear)"

    s "Hey, Mason, fetch us some soup, will you?"
    m "What?"
    s "Mason, you heard the man. Bring some soup!"
    m "Whatevaaaa like."

    "(mason leaves, anger brewing inside him)"
    "(they all pause, joining raleigh\’s epic as shit 19/6 359 bpm style clapping.)"

    gc "Guys, enough chit chat! How do guns."

    "(Hibbert is ladies)"

    s "Oh, sorry GC! Just wanted to bite to eat, that is all, before I do my guns!"
    gc "It\’s not okay. You\’re fired."

    "(stanhope bangs bigly)"

    s "What?"
    m "What? You may not fire Stanhope."
    gc "Stanhope, your out."
    e "Noooooooo!"
    o "But, WAIT! WAIT! GC!! NOOOOOO!!!!!"
    
    "(to himself)"

    o "Hi guys. It\’s me, Raleigh, and I\’ve got a couple of things to say about this. First of all, this is a crazy plot twist. The Grand Commissioner FIRING Stanhope? Who\’s going to be the commander? Let\’s wait and see until the next scene of the hit play, Journey\’s End!"

    "(the scene ends bigly)"

    # --- --- --- --- --- #
    "SCENE 3"
    "(A dugout is there. Because it\’s the war, there is Stanhope. He has just been fired from the Captain Stanhope – \“C\” company. General commissioner in the dugout in the war.)"

    s "When do I do it! I\’m no longer a dugout in the world war. There\’s no more dugouts in the game. Tally ho!"
    t "(dying) Have you heard of this app called Instagram, sir?"
    
    "(trotter dies and respawns)"

    t "You can share all sorts of pictures with you\’re friends. I\’ve just signed up for a account. Here\’s a picture of Hardy I shared with Trotter earlier!"

    "(Trotter shows Stanhope a picture of his dead body. Stanhope is Trotter\’s Instagram account.)"

    s "Cheero, Stanhope! What I am is inside your phone right now, Hibbert!"
    Character("Trotter dead body picture") "(from inside Trotter phone) Morning, sir! I am Trotter from inside the phone. Glassbody stop me!"

    "(the smell of gunfire and backstory fills the air. Guns were going off in the air.)"

    # This ends the game.

    return
