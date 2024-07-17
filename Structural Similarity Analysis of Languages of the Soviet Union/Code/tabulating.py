# Cyrillic Analysis
import nltk
from nltk.corpus import udhr

languages = ['Russian',
'Russian_Russky',
'Ukrainian',
'Belorus_Belaruski',
'Kazakh']
cfd = nltk.ConditionalFreqDist( # Kelime uzunluklarına göre koşullu frekans dağılımı
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Cyrillic')
)
cfd.tabulate(conditions=['Russian', 'Russian_Russky', 'Ukrainian', 'Belorus_Belaruski', 'Kazakh'],
    samples=range(10), cumulative=True)
# Latin Analysis
languages = ['Uzbek',
'Latvian',
'Estonian_Eesti']
cfd = nltk.ConditionalFreqDist( # Kelime uzunluklarına göre koşullu frekans dağılımı
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Latin1')
)
cfd.tabulate(conditions=['Uzbek', 'Latvian', 'Estonian_Eesti'],
    samples=range(10), cumulative=True)
# Baltic Analysis
languages = ['Lithuanian_Lietuviskai']
cfd = nltk.ConditionalFreqDist( # Kelime uzunluklarına göre koşullu frekans dağılımı
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Baltic')
)
cfd.tabulate(conditions=['Lithuanian_Lietuviskai'],
    samples=range(10), cumulative=True)