from bs4 import BeautifulSoup as BS
from wordType import wordType
from main import DatabaseError
from LoopThrough import loopThrough
import db
import json

# Resource Sample
# sample_url = requests.get("https://sil-philippines-languages.org/online/ivb/dict/lexicon/lx00003.html")

def App(text):
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
            definitionItem['semantics'] = semanticsSampleList;

            # Morphonemics
            morphophonemics = groupItem.findChildren(class_='mo') if groupItem.findChildren(class_='mo') != None else []
            morphophonemicsList = []
            for morpho in morphophonemics:
                morphophonemicsList.append(morpho.text)
            definitionItem['morphophonemics'] = morphophonemicsList

            # Synonyms Words
            synonyms = groupItem.findChild(class_='rsGroup')
            
            #related
            relatedWords = groupItem.findChild(class_='reGroup')

            # Antonyms
            antonyms = groupItem.findChild(class_='raGroup')        
            
            definitionItem['synonym'] = synonyms.text if synonyms != None else None
            definitionItem['related'] = relatedWords.text if relatedWords != None else None
            definitionItem['antonym'] = antonyms.text if antonyms != None else None

            # Derivatives
            derivative = groupItem.findChild(class_='ode')
            derivativeDesc = derivative.find_next_sibling().text if derivative != None else None
            
            
            # Derivative Word
            derivatedDefinition = {
                'derivative': derivative.findChild(class_='d').text if derivative != None else None,
                'derivative_def': derivativeDesc
            }
            
            definitionItem['derivative'] = derivatedDefinition

            # Sayings
            sayings = groupItem.findChildren(class_='ose') if groupItem.findChildren(class_='ose') != None else []
            sayingsList = []
            for saying in sayings:
                sayingItem = {
                    'saying': saying.text,
                    'saying_desc': saying.find_next_sibling().text if saying.find_next_sibling() != None else None
                }
                sayingsList.append(sayingItem)

            definitionItem['sayings'] = sayingsList
            rowData['definitions'].append(definitionItem) # add descriptionlist to "definition" property

        # pprint(rowData.get('definitions'), indent=3) # Preview Data
        data = (rowData.get('title'), rowData.get('origin'), json.dumps(rowData.get('definitions')),)
        db.insertInto(data) # commit to Database
        

    except Exception as e:
        print("Database Error")
        print(e)
        raise DatabaseError("")

# Start App
def Main(start, count, initDB=False):
    if(initDB):
        db.createDatabaseFile()
        db.createTable()
        loopThrough(fun=App, end=count, start=start)
    else:
        loopThrough(fun=App, end=count, start=start)