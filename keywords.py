textFile = open('twitterFeed.txt', encoding="Latin-1")

text = textFile.read()

keywordsClimate = ["green", "greta thunberg", "planet", "zero", "emissions", "carbon",
"sustainable", "future", "global", "goals", "climate", "change", "action", "greenhouse", "gases",
"fossil", "fuels"]

keywordsVaccine = ["corona", "pandemic", "health", "who", "herd", "immunity", "covid-19",
                   "covid certificate", "vaccine", "pfizer"]

keywordsAbortion = ["human", "rights", "abortion", "laws","female", "bodies", "women’s", "choice", "fetus",
                    "embryo", "pregnancy"]

keywordsFlatEarth = ["flat", "earth", "platygaean", "hypothesis", "springfield", "effect", "cryptogeographica",
                     "round","disk", "cosmography"]

def keywords(text):
    climateBubble=0
    vaccineBubble=0
    abortionBubble=0
    flatEarthBubble=0

    newWords = []
    
    for line in text.splitlines():
        line = line.lower()
        words = line.split(" ")
           
        for word in words:
            word = word.strip('."').strip(',').strip('#').strip(':').strip(';')
            newWords.append(word)
       
    for word in newWords:
        if word in keywordsClimate:
            climateBubble += 1
        if word in keywordsVaccine:
            vaccineBubble += 1
        if word in keywordsAbortion:
            abortionBubble += 1
        if word in keywordsFlatEarth:
            flatEarthBubble += 1

    print(f"Number of climate related keywords: {climateBubble} \n Number of vaccine related keywords: {vaccineBubble} \n Number of abortion related keywords: {abortionBubble} \n Number of flat earth related keywords: {flatEarthBubble}") 

keywords(text)