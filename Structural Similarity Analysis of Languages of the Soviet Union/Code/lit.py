import nltk
from nltk import FreqDist, bigrams

f = open('Sentences/Latin/lit_wikipedia_2014_30K-sentences.txt')
raw = f.read()
tokens = nltk.word_tokenize(raw)
words = [w.lower() for w in tokens]
vocab = sorted(set(words))
fdist1 = FreqDist(words)
count = 0
total = 0
for token in tokens:
    count += 1
    total += len(token)
print("Ortalama kelime uzunluğu : %2.2f" % (total/count))
cumulative = 0.0
tagged_tokens = [[]]
for rank, word in enumerate(fdist1): # %25'e kadar yer kaplayan kelimeler
    cumulative += fdist1[word] * 100 / fdist1.N()
    print("%3d %6.2f%% %s" % (rank+1, cumulative, word))
    tagged_tokens[0].append((word, word))
    if cumulative > 25:
        break
longest = ''
for word in vocab:
    if len(word) > len(longest):
        longest = word
print("\nEn uzun kelimeler : ")
maxlen = max(len(word) for word in vocab) # En büyük uzunluk
print([word for word in vocab if len(word) == maxlen])

f = open('Sentences/Latin/aze_wikipedia_2016_30K-sentences.txt')
raw2 = f.read()

s_tokens = nltk.word_tokenize(raw2)
unigram_tagger = nltk.UnigramTagger(tagged_tokens)
tagged_sentence = unigram_tagger.tag(s_tokens)
fdist2 = FreqDist(tagged_sentence)
count = 0
for item in fdist2.items():
    if item[0][1] == None:
        count = count + item[1]
percentage = 100 - ((count*100)/len(s_tokens))
print("\nBenzerlik yüzdesi(Azerice) : %2.2f%%" % percentage)

f = open('Sentences/Latin/est_wikipedia_2014_30K-sentences.txt')
raw2 = f.read()

s_tokens = nltk.word_tokenize(raw2)
unigram_tagger = nltk.UnigramTagger(tagged_tokens)
tagged_sentence = unigram_tagger.tag(s_tokens)
fdist2 = FreqDist(tagged_sentence)
count = 0
for item in fdist2.items():
    if item[0][1] == None:
        count = count + item[1]
percentage = 100 - ((count*100)/len(s_tokens))
print("Benzerlik yüzdesi(Estonca) : %2.2f%%" % percentage)

f = open('Sentences/Latin/lav_wikipedia_2014_30K-sentences.txt')
raw2 = f.read()

s_tokens = nltk.word_tokenize(raw2)
unigram_tagger = nltk.UnigramTagger(tagged_tokens)
tagged_sentence = unigram_tagger.tag(s_tokens)
fdist2 = FreqDist(tagged_sentence)
count = 0
for item in fdist2.items():
    if item[0][1] == None:
        count = count + item[1]
percentage = 100 - ((count*100)/len(s_tokens))
print("Benzerlik yüzdesi(Letonca) : %2.2f%%" % percentage)

f = open('Sentences/Latin/ron_wikipedia_2014_30K-sentences.txt')
raw2 = f.read()

s_tokens = nltk.word_tokenize(raw2)
unigram_tagger = nltk.UnigramTagger(tagged_tokens)
tagged_sentence = unigram_tagger.tag(s_tokens)
fdist2 = FreqDist(tagged_sentence)
count = 0
for item in fdist2.items():
    if item[0][1] == None:
        count = count + item[1]
percentage = 100 - ((count*100)/len(s_tokens))
print("Benzerlik yüzdesi(Rumence) : %2.2f%%" % percentage)

f = open('Sentences/Latin/tuk_wikipedia_2016_30K-sentences.txt')
raw2 = f.read()

s_tokens = nltk.word_tokenize(raw2)
unigram_tagger = nltk.UnigramTagger(tagged_tokens)
tagged_sentence = unigram_tagger.tag(s_tokens)
fdist2 = FreqDist(tagged_sentence)
count = 0
for item in fdist2.items():
    if item[0][1] == None:
        count = count + item[1]
percentage = 100 - ((count*100)/len(s_tokens))
print("Benzerlik yüzdesi(Türkmence) : %2.2f%%" % percentage)

f = open('Sentences/Latin/uzb_wikipedia_2014_30K-sentences.txt')
raw2 = f.read()

s_tokens = nltk.word_tokenize(raw2)
unigram_tagger = nltk.UnigramTagger(tagged_tokens)
tagged_sentence = unigram_tagger.tag(s_tokens)
fdist2 = FreqDist(tagged_sentence)
count = 0
for item in fdist2.items():
    if item[0][1] == None:
        count = count + item[1]
percentage = 100 - ((count*100)/len(s_tokens))
print("Benzerlik yüzdesi(Özbekçe) : %2.2f%%" % percentage)