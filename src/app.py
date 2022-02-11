from bs4 import BeautifulSoup as BS
from wordType import wordType
from main import DatabaseError
from LoopThrough import loopThrough
from os import path
import sys
import db
import json
from log import logger
# Resource Sample
# sample_url = requests.get("https://sil-philippines-languages.org/online/ivb/dict/lexicon/lx00003.html")

def App(text, currentIndex):
    '''
    Row Data Structure\n
    '''
    try:
        rowData = {}
        doc = BS(text, 'html.parser')
        
        # Fetch Group HTML
        group = doc.find(class_="lxGroup")
        # Get "Word"
        title = group.findChild(class_='lx').findChild(class_="d")
        # TODO: Parse Origin Type
        wordOrigin =  group.findChild(class_='dc').findChild(class_='d').text if group.findChild(class_='dc') != None else 'N/A'
        # Definition Group
        definitionGroups = group.find_all(class_='psGroup') # Description List

        rowData["title"] = title.text # Title
        rowData["origin"] = wordOrigin # Word Origin
        rowData['definitions'] = [] # Description List

        # Description Sections
        for groupItem in definitionGroups:
            # Description List
            definitionItem = {} # definition Item
            exampleList = [] # Example List
            # Get Defintion Item Group Type
            defType = groupItem.findChild(class_='ps')
            definitionItem['type'] = wordType(defType.get_attribute_list('class')[-1])
            
            # Definition's Description
            descriptions = groupItem.findChild(class_='gl')
            definitionItem['description'] = descriptions.text

            # Word Variants
            ilokanoWord = groupItem.findChild(class_="iiGroup")
            variant = {} # Word Variants
            variant['ilokano'] = ilokanoWord.findChild(class_='d').text if ilokanoWord != None else None
            tagalogWord = groupItem.findChild(class_="itGroup")
            variant['tagalog'] = tagalogWord.findChild(class_='d').text if tagalogWord != None else None
            ivatanWord = groupItem.findChild(class_="ivGroup")
            variant['ivatan'] = ivatanWord.findChild(class_='d').text if ivatanWord != None else None
            
            definitionItem['variant'] = variant # set the word Variants

            # Sample Groups
            for sampleGroup in groupItem.find_all(class_="exGroup"):
                sampleItem = {}
                # Ivatan Sample
                ivatanExample = sampleGroup.findChild(class_='ex')
                # English Translation
                englishTranslation = sampleGroup.findChild(class_='tr')

                sampleItem['sample'] = ivatanExample.findChild(class_='d').text
                sampleItem['translation'] = englishTranslation.findChild(class_='d').text
                if(sampleItem['sample'] != None and sampleItem['translation'] != None):
                    exampleList.append(sampleItem)

            definitionItem['samples'] = exampleList # add list to the parent object

            # Grammar
            grammar = groupItem.findChild(class_='eg').text if groupItem.findChild(class_='eg') != None else None
            definitionItem['grammar'] = grammar

            # Cultural Meaning
            culturalNote = groupItem.findChild(class_='ec').text if groupItem.findChild(class_='ec') != None else None             
            definitionItem['cultural_note'] = culturalNote
            
            # Semantics
            semantics = groupItem.findChildren(class_='es') if groupItem.findChildren(class_='es') != None else []
            semanticsSampleList = []
            for semanticSample in semantics:
                semanticsSampleList.append(semanticSample.text)

            definitionItem['semantics'] = semanticsSampleList if len(semanticsSampleList) > 0 else None

            # Morphonemics
            morphophonemics = groupItem.findChildren(class_='mo') if groupItem.findChildren(class_='mo') != None else []
            morphophonemicsList = []
            for morpho in morphophonemics:
                morphophonemicsList.append(morpho.text)
            definitionItem['morphophonemics'] = morphophonemicsList if len(morphophonemicsList) > 0 else None

            # Synonyms Words
            synonyms = groupItem.findChild(class_='rsGroup').findChild(class_='d') if groupItem.findChild(class_='rsGroup') != None else []
            synonymsList = []
            for synonym in synonyms:
                if synonym.text != None:
                    synonymsList.append(synonym.text)

            #related
            relatedWords = groupItem.findChild(class_='reGroup').findChild(class_='d') if groupItem.findChild(class_='reGroup') else []
            relatedWordsList = []
            for related in relatedWords:
                if(related.text != None):
                    relatedWordsList.append(related.text)

            # Antonyms
            antonyms = groupItem.findChild(class_='raGroup').findChild(class_='d') if groupItem.findChild(class_='raGroup') != None else []        
            antonymsList = []
            for antonym in antonyms:
                if(antonym.text != None):
                    antonymsList.append(antonym.text)
            
            definitionItem['synonym'] = synonymsList if len(synonymsList) > 0 else None
            definitionItem['related'] = relatedWordsList if len(relatedWords) > 0 else None
            definitionItem['antonym'] = antonymsList if len(antonymsList) > 0 else None

            # Derivatives
            derivative = groupItem.findChild(class_='ode')
            derivativeDesc = derivative.find_next_sibling().text if derivative != None else None
            
            
            # Derivative Word
            derivatedDefinition = {
                'derivative': derivative.findChild(class_='d').text if derivative != None else None,
                'derivative_def': derivativeDesc
            }
            definitionItem['derivative'] = derivatedDefinition if(derivatedDefinition['derivative'] != None and derivatedDefinition['derivative_def'] != None) else None
            
            # Sayings
            sayings = groupItem.findChildren(class_='ose') if groupItem.findChildren(class_='ose') != None else []
            sayingsList = []
            for saying in sayings:
                sayingItem = {
                    'saying': saying.text,
                    'saying_desc': saying.find_next_sibling().text if saying.find_next_sibling() != None else None
                }
                if(sayingItem['saying'] != None and sayingItem['saying_desc'] != None):
                    sayingsList.append(sayingItem)

            definitionItem['sayings'] = sayingsList if(len(sayingsList) > 0) else None 
            rowData['definitions'].append(definitionItem) # add descriptionlist to "definition" property

        # pprint(rowData.get('definitions'), indent=3) # Preview Data
        data = (rowData.get('title'), rowData.get('origin'), json.dumps(rowData.get('definitions')), 0)
        db.insertInto(data, currentIndex=currentIndex) # commit to Database
        

    except Exception as e:
        print("Database Insert Error")
        logger.error(f"file: {__file__} -> {e}")
        raise DatabaseError("")

# Start App
def Main(start, count, initDB):
    if(initDB):
        db.createDatabaseFile()
        db.createTable()
        loopThrough(fun=App, end=count, start=start)
    else:
        if path.exists('data.sqlite'):
            loopThrough(fun=App, end=count, start=start)
        else:
            print("Database File Does Not Exist\nPrefer Running with flag \'--init\' to intialize Database file\nBefore running consecutive runs")
            sys.exit()