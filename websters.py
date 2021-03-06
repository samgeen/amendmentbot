'''
Corpus of words for each category of word
Sam Geen & Mike Cook, August 2014
'''

websters = { \
    "ACTION":["free speech","freedom of assembly","freedom of the press",
               "covering yourself in honey","eating bees","owning a pet rock",
               "lying about your age on the internet","staying up past 2am",
               "sassing your elders","running for office",
               "shooting black people","tasering black people",
               "beating black people","arresting black people",
               "going to Applebee's at 4am","quoting Terminator",
               "quoting Airplane","backpacking around Europe",
               "disliking Indian food","eating a whole slab of butter",
               "liking a Facebook post","manually retweeting",
               "singing in the shower","singing while drunk",
               "shouting on top of parked cars","whaling on that a-hole",
               "stealing elections","jacking shit","drinking gravy",
               "barbecuing","draft dodging","sticking it to the man",
               "patronising minors","putting it all on red",
               "putting it all on black","shanking a fellow inmate",
               "dogging","felching","caped crusading","showboating",
               "putting on weight","failing to lose weight","screaming",
               "losing your job","losing it","weeping openly",
               "crying on public transport","getting stuck in traffic",
               "super-sizing","huffing glue","blogging","jammin'",
               "taking out anger on the barista","losing it at Walmart",
               "shopping at Whole Foods","wearing socks and sandals",
               "flashing tits","opening overcoats to passers-by",
               "dumpster diving","catching ebola","losing health insurance",
               "slashing tires","bowling for Columbine","haxxing",
               "leaking secret documents","moping","sleeping in until noon",
               "tweeting","livestreaming","writing a novel in Starbucks",
               "buying coffee at Dunkin' Donuts","twerking",
               "driving across America","sneaking into the US",
               "dating a footballer","drifting","drift racing",
               "picking up your room","minding your own goddamn business",
               "licking street signs","taking out the trash",
               "'taking out the trash'","dancing in the moonlight",
               "cutting off ears","chainsmoking","being evicted",
               "caring about soccer","drinking seasonal lattes",
               "shouting at the TV","being a jackass",
               "beating on cars with a golf club","twisting",
               "lying to a federal judge","lying to Congress",
               "sleeping under your desk","sleeping in your car",
               "beating Super Mario","cheating at poker","splitting the atom",
               "defecting to Russia","holing up in the Ecuadorian Embassy"],
    "RULESOURCE":["common law","basic decency","he who smelt it","Vegas rules",
                  "whatever you imagine the founding fathers wanted",
                  "the police officer with the largest mustache",
                  "four score and twenty, whatever that is",
                  "federal law","cosmic justice","the Ten Commandments",
                  "Sharia law","state or federal laws",
                  "that road sign back there","Royal Edict",
                  "the End User License Agreement","federal laws","state laws",
                  "state or federal laws","the Chekov gambit","en passant",
                  "that Yo Gabba Gabba song","that FOX News segment",
                  "the iPhone manual","Microsoft","a firey sermon",
                  "trial by ordeal","trial by fire","prison rules",
                  "natural law","federal guidelines","the President's whim",
                  "the loading screen message","gang rules",
                  "the edict of Zoltan","handshake agreement",
                  "Amish social mores","the laws of the Mole People",
                  "wasteland law","frontier justice","frontier law",
                  "that racist taxi driver","the in-flight safety instructions",
                  "the emergency broadcast","your homophobic Facebook friend",
                  "transphobic screed","the bossman","the sign above the bar",
                  "the back of the packet","state guidelines","Mike",
                  "Judge Judy","Big Bird"],
    "EVENTS":["times of war","times of peace","public trials by jury",
              "nights on the town","bar fights","road trips across the desert",
              "county fairs","bake-offs","really boring sermons",
              "epic drum solos","lazy Sundays","knife duels","Labor Day",
              "Veteran's Day", "rush hour", "Lost marathons","Superbowl",
              "Thanksgiving dinner with your racist family","dad's rants",
              "mom's stories","lycanthropic episodes",
              "Presidential turkey pardonings","spelling bees",
              "lobster festivals","high school reunions",
              "eating contests","cougar maulings","eagle attacks",
              "gunfights with the terrorists","accidental gunfire",
              "showings of another goddamn Spiderman film",
              "the hours of 9am and 5pm", "open heart surgeries",
              "Presidential speeches","sessions of the Congress",
              "times when the Vice-President feels important",
              "an episode of WWE","a wardrobe malfunction",
              "the White House Correspondent's Dinner","Saturday Night Live",
              "the 'Whacky Races'","the World Series","commercial breaks",
              "Moon landings","Mars landings","Trails of Tears",
              "foreclosures","avoidable tragedies","police shootings",
              "police beatings","illegal street races","boxing montages",
              "incoherent monologues","alien attacks","wars in Europe",
              "Bon Jovi concerts","Bruce Springsteen songs","mudfights",
              "bumfights","artificial inseminations","abortions",
              "unwanted pregnancies","religious conversions",
              "wagon rides west","snake poisonings","dinosaur attacks",
              "Zeppelin crashes","liposuctions","botox treatments",
              "office Christmas parties","keggers","keggers (sick or non-sick)",
              "hazings","racially motivated acts of violence",
              "racist diatribes","transphobic rants","homophobic sermons",
              "pie-eating contests","hamburger-eating contests",
              "zombie attacks","zombifications","snooze/lose scenarios",
              "underground dogfights","draft seasons","curb stompings",
              "denials of white privilege","Republican Party primaries",
              "Democratic Party primaries","Free Soil Party rallies",
              "gun shows","Monday mornings","boozy lunches",
              "North Korean invasions","mass suicides","kegstands",
              "Friday afternoons","red-eye flights","revolutions",
              "destruction derbys","brutal slayings","felchings"],
    "VERB":["eat","fight","try to have sex with","lick","run over","talk to",
            "own","lie to","slap some sense into","dance with","like",
            "mine","burrow into","immolate","roughhouse with","wrestle",
            "wrastle","abort","enslave","hitch a ride with","marry",
            "elect as President","condemn","overthrow","shank",
            "hightail away from","hike across","showboat at","argue with",
            "boil","broil","deep fry","stir-fry","slather in butter",
            "mobilise","deploy","conscript","bitch about","bitch at",
            "cry into","weep openly at","foreclose","reposess",
            "saddle your parents with","hide pornography in",
            "binge on","lash out at","watch Big Bang Theory with",
            "sing about","lie about","enthuse about","write","dine on",
            "drink with","infect","give herpes to","stew","bicker about",
            "stamp on","arrest","drop","televize","cauterize","molest",
            "bottle","beat the crap out of","tear asunder","vaporize",
            "haul off","rotate","mount","rap about","write country songs about",
            "mine","double down on","botch a painting of","hate on",
            "completely forget about","drone on and on about",
            "listen to dad rant about","correct mom's misconceptions about",
            "log fifty hours with","burn all your savings on","widdle on",
            "go number two on","switch shirts with","bleed all over",
            "enrobe in dark chocolate","listen to k-pop songs about",
            "watch anime featuring","sic your dog on","die from lack of",
            "horse about with","stick your dick in","stick your fanny on",
            "hose off","wrench out","buy","wait in line for","smack",
            "shoot up some","lop off"],
    "VERBTGTED":["transportation","exploitation","glorification","removal",
                 "emancipation","discombobulation","denial","sentencing",
                 "inditement","interdiction","inception","termination",
                 "vaporization","defenestration","defeat","schooling",
                 "embarcation","moistening","misplacement","disarmament",
                 "conscription","impeachment","decampment","vacationing",
                 "kidnapping","haunting","carb-loading","tab-completion",
                 "sale","foreclosure","reposession","sexing",
                 "gender reassignment","motor boating","imprisonment",
                 "loss","banning","banishment","shaming","drowning",
                 "stretching","bullwhipping","misconception","handcuffing",
                 "bitch-slapping","trapping","winging","wounding",
                 "accidental shooting","bruising","marinading",
                 "cock-blocking","topical application","friendzoning",
                 "mortification"],
    "OBJECTS":["cats","arms","mountains","drive-thrus","churches",
               "federal prisons","sweet rides","fat dogs","socialists",
               "shopping trolleys","trucks","paper towels",
               "intoxicating liquors","police cruisers","slime monsters",
               "pirates","stank bootys","dune buggys","friendly ghosts",
               "zombies","scary old people","buff pensioners","preachers",
               "gunshot wounds","tasers","black people","white people",
               "bibles","federal hellholes","Presidential pets","dogs",
               "pugs","Marmaduke comics","ebola viruses","craft beers",
               "coffee cups","fancy lattes","seasonal colds","eagles",
               "bald eagles","constapation creams","prescription pills",
               "hardcore drugs","illegal drugs","narcotics","swag bags",
               "stolen goods","fenced goods","gated communities",
               "gold-plated iPhones","supermarket-brand sneakers",
               "holy relics","cowboy boots","ten-gallon hats","fedoras",
               "brown overcoats","anti-tank mines","drones","sex toys",
               "flacid members","huge black cocks","stale donuts",
               "flat sodas","stale bagels","big fat titties","prarie dogs",
               "cougars","baseball bats","two by fours",
               "planks with nails in them","wiffle bats","old timey movies",
               "country albums","dangerous dogs","illegal clones",
               "taquitos","tacos","deep-fried pizzas","bananaphones",
               "double-decker burgers","bottomless fries","Swiss cheeses",
               "thunderdomes", "fat suits", "crash test dummies","bacon bits",
               "Elvis wigs","bags o' meth","fixie bikes","handlebar mustaches",
               "hipster beards","checked shirts","skinny jeans","footlongs",
               "criminal elements","parking tickets","aviator sunglasses",
               "cool leather jackets","roadsters","fast food wrappers",
               "tubs of hair gel","onion rings","nacho chips","candy corns",
               "spooky masks","PB jelly sandwiches","bass guitars",
               "spicy wings","red plastic cups","swivelly diner stools"],
    "PEOPLE":["federal judges","my friend Mike","black people and asians",
              "dirty socialists","country club members","blue collar workers",
              "the middle class","really, really fat people",
              "muscle fatties","husky children","democrats","republicans",
              "farmers","freemasons","confederate rebels",
              "free soil party members","buffalo girls",
              "people who dress like they're from 1776",
              "child beauty pageant contestants","leprechauns","hipsters",
              "greasers","frat boys","Disneyworld mascots","cheerleaders",
              "motivational speakers","Wall Street traders","Obama",
              "Dubya","The King","Nat King Cole","BB King","The Boss",
              "Bruce Springsteen","the Lakers","crooked cops",
              "racist police officers","weapons manufacturers","kids",
              "chubby little boys","kids wearing beanies","Catholics",
              "Mormons","Space Marines","US Marines","military police",
              "the National Guard","Donkey Kong","the brothers Mario",
              "aging diner waitresses","accordion repo men","furries",
              "liberal arts majors","liberal arts professors",
              "dangerous criminals","ex-cons","dumb fucks","assholes",
              "jumped-up pricks","sexy vampires","shirtless drunks",
              "survivalists","gun advocates","veterans","bronies",
              "Civil War reenactors","the Illuminati","Muslims",
              "banjo-playing hicks","southerners","northerners",
              "valley girls", "techie dweebs","internet billionaires",
              "sysadmins","mall santas","Miami Heat","goldbugs",
              "sixty-niners","gunshop owners","strippers","bassists",
              "keytarists","Spanish teachers","teachers","British actors",
              "sociopathic doctors","serial killers","football mascots",
              "wig makers","garbagemen","elderly karate masters","frymen",
              "programmers","script kiddies","internet misogynists",
              "goons","pasty kids","pastors","shamen","Native Americans",
              "Hessian mercenaries","sperm donors"],
    "PLACE":["a federal school or prison","the White House",
             "the Congressional Chamber",
             "Capitol Hill","Washington State","the District of Columbia",
             "New York, New York","the Congressional Bike Sheds",
             "the back of a limo",
             "the head of the Statue of Liberty","France","Europe",
             "that pizza place on 4th and Union","the sidewalk",
             "private residences","rented apartments","loft apartments",
             "the shower","the break room at work","your desk","Portland",
             "Buttfuck, Missouri","the Beltway","the streets","an alleyway",
             "Disneyland","Disneyworld","Disneyplace","Disneyreich",
             "a place of worship","an abbatoir","a post office","Kansas",
             "Confederate states","the locker room","the thunderdome",
             "Canada","the Mexican border","Alaska","Hawai'i","the walk-in",
             "cool fight locations","Tekken levels","cyberpunk streets",
             "the basement","a porn dungeon","Salt Lake City","Chicago",
             "the state of California","US highways","Route 66","Puerto Rico",
             "anywhere whose regional delicacy is 'butter'",
             "state fairs","Norleans","the Vice-President's residence",
             "the reflecting pool","the Washington Monument","Walmart",
             "the mall","a creationist dinosaur park","a failing school",
             "the School of Rock","that street with the film stars' handprints",
             "Sunset Boulevard","a missile silo or black site","Area 51",
             "the Bermuda Triangle","Yellowstone National Park",
             "Deroit","military bases","bordellos","sleazy joints",
             "classy restaurants","restaurants with cloth napkins",
             "saloons","film sets","Top Gun Academy","the ranch",
             "the in-laws'","that house with too many Christmas lights",
             "Winter Wonderland","San Diego","pawn shops","sketchy bars",
             "my place","the 'Bang Bus'","the stratosphere","Mars","the Moon",
             "Houston, Texas","a school cafeteria","the classroom",
             "the back of my van","the President's yacht","a spooky castle",
             "and abandoned mine","Main Street","Hicksville, Iowa",
             "the Catskills","a dive bar","a biker joint","a truck stop"],
    "NUMBERTH":["first","second","third","forth","fifth","sixth","seventh",
                "eighth","nineth","tenth","eleventh","twelth","twelf [sic]",
                "six hundred and sixty sixth","fourteenth","fiftyeenth",
                "sixtenth","twebtyeth","thorbty-foist","thorbty-socund",
                "foist","thoid","numberless","zeroth","minus oneth",
                "eighth and three quartersth","eleventieth","splebentieth",
                "jillionth","gazillionth","brazillionth","infinityth",
                "'Barry White'","pi(Franklin you nerd - TJ)th","twenty-second",
                "thoity-foist","thoity-thoid","trobteenth","nineteenth",
                "eighteenth","fiveteenth","oneteenth","four-twentieth",
                "four-score and twentieth","thirtieth","fiftieth","hundredth",
                "quarteenth","five hundred and ninety-second","oneth",
                "thirst (sponsored by Pepsicorp)","sec-gun-ed"],
    "SAME":[""]}
    # NOTE: SAME IS TO PROVIDE REPEATED PHRASES IN THE PARSING BELOW

if __name__=="__main__":
    for keyword, words in websters.iteritems():
        # Ignore same as it's just a placeholder
        if keyword != "SAME":
            num = len(words)
            value = "BAD"
            if num >= 50:
                value = "OK"
            if num >= 100:
                value = "GOOD"
            if num > 200:
                value = "SUPER EXCELLENT"
            if num > 500:
                value = "LUDICROUS (seriously)"
            print keyword, "has", num, "entries -", value
