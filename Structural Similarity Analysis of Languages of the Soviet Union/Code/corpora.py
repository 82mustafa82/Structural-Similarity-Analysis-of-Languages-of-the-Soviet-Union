import nltk
from nltk.corpus import udhr

# Diğer dillerde corpora
# Cyrillic Analysis
languages = ['Russian',
'Russian_Russky',
'Ukrainian',
'Belorus_Belaruski',
'Kazakh']
cfd = nltk.ConditionalFreqDist( # Kelime uzunluğu koşullu frekans dağılımı
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Cyrillic'))
cfd.plot(cumulative=True)

# UTF-8 Analysis
languages = ['Russian',
'Russian_Russky',
'Ukrainian',
'Belorus_Belaruski',
'Kazakh']
cfd = nltk.ConditionalFreqDist( # Kelime uzunluğu koşullu frekans dağılımı
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-UTF8'))
cfd.plot(cumulative=True)

# Latin Analysis
languages = ['Uzbek',
'Latvian',
'Estonian_Eesti']
cfd = nltk.ConditionalFreqDist( # Kelime uzunluğu koşullu frekans dağılımı
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Latin1'))
cfd.plot(cumulative=True)

# Baltic Analysis
languages = ['Lithuanian_Lietuviskai']
cfd = nltk.ConditionalFreqDist( # Kelime uzunluğu koşullu frekans dağılımı
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Baltic'))
cfd.plot(cumulative=True)