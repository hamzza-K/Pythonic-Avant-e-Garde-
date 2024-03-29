#A go-to notes on NLTK


### Chunking, Chinking, Stop-Words and Named-Entity Recognition with NLTK
#======================================================================



#---------------------------------------------
# One of the most major forms of chunking
# in natural language processing is called
# "Named Entity Recognition." 
# The idea is to have the
# machine immediately be able to pull out "entities"
# like people, places, things, locations, monetary figures, and more.
#--------------------------------------------

#--------------------------------------------
# In order to chunk,
#  we combine the part of
#  speech tags with regular expressions
# . Mainly from regular expressions,
#  we are going to utilize the following:

# + = match 1 or more
# ? = match 0 or 1 repetitions.
# * = match 0 or MORE repetitions	  
# . = Any character except a new line


import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import stopwords
#PunktSentenceTokenizer  
#is the abstract class for the default sentence tokenizer,
#i.e. sent_tokenize()

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sentence_tokenizer = PunktSentenceTokenizer(train_text) #training our module, which is optional

tokenized = custom_sentence_tokenizer.tokenize(sample_text) # you can also do, tokenized = PunktSentenceTokenizer().tokenize(sample_text)

def process_content():
    try:
        example_sent = "This is merely an example sentence, which shows the use of stopwords"
        stop_words = set(stopwords.words("english"))
        #we can also add our own stop_words
        stop_words.add("Hiiii")
        
        # stopwords are those words which have no meaning, thus removing them is quite appreciated
        word_tokens = word_tokenize(example_sent)
        filtered_sentence = [w for w in word_tokens if not w in stop_words] #List-Complrehension
        #            OR
        # for w in word_tokens:
        #     if w not in stop_words:
        #         filtered_sentence.append(w)
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            """Chunking and Chinking"""
            chunkGram = r""" Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}
                                    }<DT.?>|IN||TO>+{"""  #Chunking = {} // Chinking = }{
                                        #chunking finds all the give regexs, while chinking ignores them
            #<RB.?>* = "0 or more of any tense of adverb," followed by:
            #<VB.?>* = "0 or more of any tense of verb," followed by:
            #<NNP>+ = "One or more proper nouns," followed by
            #<NN>? = "zero or one singular noun."
            chunkParser = nltk.RegexpParser(chunkGram)
            """-------------------------"""

            """Named-Entity-Recognition"""
            named_entity = nltk.ne_chunk(tagged, binary=True)
            #You can also do binary=False, it will yield a slightly different result
            """"------------------------"""
            chunked  = chunkParser.parse(tagged) #chunked = NLTK tree
            #We might be only interested in getting just the chunks, ignoring the rest.
            # We can use the filter parameter in the chunked.subtrees() call.

            # for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
            #     print(subtree)

            print(chunked)
            # Or 
            #chunked.draw()      given that you have the matplotlib
    except Exception as e:
        print(str(e))

process_content()

def P_O_S_taggers():
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
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when"""
return P_O_S_taggers.__doc__

#P_O_S_taggers()
