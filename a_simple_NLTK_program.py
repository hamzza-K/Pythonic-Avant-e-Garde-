#Made this project in my first semester in my University when I had a little or subtle knowledge about programming and languages.


try:
    import nltk
    from nltk.tokenize import PunktSentenceTokenizer
    from nltk.corpus import stopwords
except Exception as e:
	print("Whoops! {}. make sure that you're saving the file in the right directory".format(e))
    # it won't work, unless you save this file in the directory ---->  Python3/Scripts, or somewhere else where the module is installed  

def processing_contents():
    input_from_user = str(input("Enter a Sentence: "))

    stop_words = set(stopwords.words("english")) 
    # stopwords --> words that have no meaning, better to remove them first
    #for I would rather not let them sloppy words ruin my program



    words = nltk.word_tokenize(input_from_user) # Tokenizing the given String to add the POS-tags
    filtered_sentence = [w for w in words if not w in stop_words] #Filtering the input with list-comprehension
    #                               OR
    # filtered_sentence = []
    # for w in words:
    #     if w not in stop_words:
    #         filtered_sentence.append(w)
    tokenized  = nltk.pos_tag(filtered_sentence) # Adding the POS-tags
    #Variables that counts
    #------------------------
    #This is a Sentence Counter..
    sentence_sum = 0
    sentence_counter = PunktSentenceTokenizer().tokenize(input_from_user)
    for counter in sentence_counter:
        sentence_sum = sentence_sum + 1
   #---------------------
    nouns_count = 0
    nouns_display = []           #- making some lists to store the appended values
    adverbs_count = 0           
    adverbs_display = []
    verbs_count = 0
    verbs_display = []
    adjective_count = 0
    adjective_display = []
    proper_noun_count = 0
    proper_noun_display = []
    #---------------------
    for i in tokenized:
            x,y = i
            if y in ["NN", "NNS"]:
                nouns_count += 1
                nouns_display.append(x)
            elif y in ["RB", "RBR", "RBS", "RP"]:
                adverbs_count += 1
                adverbs_display.append(x)
            elif y in ["JJ", "JJR", "JJS"]:
                adjective_count +=1
                adjective_display.append(x)
            elif y in ["NNP", "NNPS"]:
                proper_noun_count += 1
                proper_noun_display.append(x)
            elif y in ["VB", "VBG", "VBD", "VBN", "VBP", "VBZ"]:
                verbs_count +=1
                verbs_display.append(x)

    """I could have used decorators here but that would have consumed too much of my time; altering content, creating global variables and calling other functions xd
    Hence I approached a ugly looking cheap trick here,  pray pardon my laziness"""
#========================================  
    if proper_noun_display is not None:
        a = ", ".join(proper_noun_display)
        print("proper-Noun ---> {}".format(a))
    if nouns_display is not None:
        a = ", ".join(nouns_display)
        print("Noun ---> {}".format(a))
    if adverbs_display is not None:
        a = ", ".join(adverbs_display)
        print("Adverb ---> {}".format(a))
    if adjective_display is not None:
        a = ", ".join(adjective_display)
        print("Adjective ---> {}".format(a))
    if verbs_display is not None:
        a = ", ".join(verbs_display)
        print("Verb ---> {}".format(a))

    print("There are {}: proper-nouns, {}:nouns, {}:verbs, {}: adverbs and {}: adjectives in the sentence.".format(proper_noun_count, nouns_count, verbs_count, adverbs_count, adjective_count))

    print("Total Sentences: {}".format(sentence_sum))
    
    
if __name__ == '__main__':
    processing_contents()

#=-=-=-Part Of Speech Tag-list-=-=-=-=-=#
"""CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent's
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verbs_count, base form	take
VBD	verbs_count, past tense	took
VBG	verbs_count, gerund/present participle	taking
VBN	verbs_count, past participle	taken
VBP	verbs_count, sing. present, non-3d	take
VBZ	verbs_count, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when"""
