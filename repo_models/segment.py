from datetime import datetime, date
import json
import logging
logger = logging.getLogger(__name__)
import re

from DDR import converters
from DDR import vocab
from . import common


MODEL = 'segment'

REQUIRED_FIELDS_EXCEPTIONS = ['record_created', 'record_lastmod', 'files',]

FIELDS = [
    
    {
        'model':      'segment',
        'name':       'id',
        'model_type': str,
        'default': None,
        'csv': {
            'export': 'require',
            'import': 'require',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Object ID',
            'help_text':  '',
            'max_length': 255,
            'widget':     'HiddenInput',
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "keyword",
                'index': 'not_analyzed',
            },
            'display': "string"
        },
        'xpath':      "/mets:mets/@OBJID",
        'xpath_dup':  [
            "/mets:mets/mets:dmdSec[@ID='DM1']/mets:mdWrap/mets:xmlData/mods:mods/mods:identifier",
            #"/mets:mets/mets:amdSec/mets:digiProvMD[@ID='PROV1']/mets:mdWrap/mets:xmlData/premis:premis/premis:object/premis:objectIdentifierValue",
            ],
    },
    
    {
        'model':      'segment',
        'name':       'record_created',
        'model_type': datetime,
        'default':    datetime.now,
        'csv': {
            'export': '',
            'import': 'ignore',
        },
        'form_type':  'DateTimeField',
        'form': {
            'label':      'Record Created',
            'help_text':  '',
            'widget':     'HiddenInput',
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "date",
                'index': "not_analyzed",
                'store': "yes",
                'format': converters.config.ELASTICSEARCH_DATETIME_MAPPING
            },
            'display': "datetime"
        },
        'xpath':      "/mets:mets/mets:metsHdr@CREATEDATE",
        'xpath_dup':  [],
    },
    
    {
        'model':      'segment',
        'name':       'record_lastmod',
        'model_type': datetime,
        'default':    datetime.now,
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'DateTimeField',
        'form': {
            'label':      'Record Modified',
            'help_text':  '',
            'widget':     'HiddenInput',
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "date",
                'index': "not_analyzed",
                'store': "yes",
                'format': converters.config.ELASTICSEARCH_DATETIME_MAPPING
            },
            'display': "datetime"
        },
        'xpath':      "/mets:mets/mets:metsHdr@LASTMODDATE",
        'xpath_dup':  [],
    },
    
    {
        'model':      'segment',
        'name':       'status',
        'group':      '',
        'inherits':   ['collection.status', 'entity.status'],
        'model_type': int,
        'vocab':      True,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'ChoiceField',
        'form': {
            'label':      'Production Status',
            'help_text':  '"In Progress" = the object is not ready for release on the DDR public website. (The object will not be published even if the collection has a status of "Complete".) "Complete" = the object is ready for release on the DDR public website. (The object can only be published if the collection has a status of "Complete".)',
            'widget':     '',
            'choices':    common.STATUS_CHOICES,
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "keyword",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': ""
        },
        'xpath':      "",
        'xpath_dup':  [],
    },
    
    {
        'model':      'segment',
        'name':       'public',
        'group':      '',
        'inherits':   ['collection.public', 'entity.public'],
        'model_type': int,
        'vocab':      True,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'ChoiceField',
        'form': {
            'label':      'Privacy Level',
            'help_text':  '"Public" = the object is viewable through the DDR public website. (Any files under the object with a status of "Private" will not be viewable regardless of the object\'s privacy level. If the entire collection has a status of "Private" no objects or files will be viewable). "Private" = the object is restricted and not viewable through the DDR public website. (Any files under the object inherit this privacy level and will not be viewable either. If the entire collection has a status of "Public" the object will remain not viewable).',
            'widget':     '',
            'choices':    common.PERMISSIONS_CHOICES,
            'initial':    common.PERMISSIONS_CHOICES_DEFAULT,
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "keyword",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': ""
        },
        'xpath':      "",
        'xpath_dup':  [],
    },

    {
        'model':      'segment',
        'name':       'sort',
        'group':      '',
        'model_type': int,
        'default':    1,
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'IntegerField',
        'form': {
            'label':      'Sort',
            'help_text':  'Order of this object in relation to others for this object (ordered low to high).',
            'widget':     '',
            'initial':    1,
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "integer",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': ""
        },
        'xpath':      "",
        'xpath_dup':  [],
    },

    {
        'model':      'segment',
        'name':       'title',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Title',
            'help_text':  'Use an original or previously designated title if one exists. If an original does not exist one should be derived. For derived titles, capitalize the first word and proper nouns and there is no period at end of the title. If the subject is completely unidentifiable, then use of "Unknown" can be appropriate.',
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "text",
                'store': "yes",
                'index': "analyzed"
            },
            'display': "string"
        },
        'xpath':      "/mets:mets/@LABEL",
        'xpath_dup':  [
            "/mets:mets/mets:dmdSec[@ID='DM1']/mets:mdWrap/mets:xmlData/mods:mods/mods:titleInfo/mods:title",
            ],
    },
    
    {
        'model':      'segment',
        'name':       'description',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Description',
            'help_text':  'Use if the title field is not sufficient for the amount of information you have about the object. The description can also include transcriptions of anything handwritten, stamped, or printed on the material. In such cases, specify that is how the information originated. Follow Chicago Manual of Style guidelines for text.',
            'max_length': 4000,
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "text",
                'store': "yes",
                'index': "analyzed"
            },
            'display': "string"
        },
        'xpath':      "/mets:mets/mets:dmdSec[@ID='DM1']/mets:mdWrap/mets:xmlData/mods:mods/mods:abstract",
        'xpath_dup':  [],
    },
    
    {
        'model':      'segment',
        'name':       'creation',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Date (Created)',
            'help_text':  'f the exact date is known use MM/DD/YYY for the format. If the exact date is unknown, then use circa (c.1931) or if applicable, a date range (1930-1940).',
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "keyword",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "string"
        },
        'xpath':      "/mets:mets/mets:dmdSec[@ID='DM1']/mets:mdWrap/mets:xmlData/mods:mods/mods:originInfo/mods:dateCreated",
        'xpath_dup':  [],
    },
    
    {
        'model':      'segment',
        'name':       'location',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Location',
            'help_text':  'When possible use the Getty Thesaurus of Geographic names as an authority. Format the names as follows: City, State (state name spelled out). Include country if outside the United States (i.e., City, State, Country).',
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "keyword",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "facet"
        },
        'xpath':      "/mets:mets/mets:dmdSec[@ID='DM1']/mets:mdWrap/mets:xmlData/mods:mods/mods:originInfo/mods:place/mods:placeTerm[@type='text']",
        'xpath_dup':  [],
    },
    
    {
        'model':      'segment',
        'name':       'creators',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Creator',
            'help_text':  'When possible use the Library of Congress Name Authority Headings. For individuals use the following format: "Last Name, First Name: Creator Role" (e.g., Adams, Ansel:photographer). For organizations use the following format: "Organization Name: Creator Role" (e.g., Associated Press:publisher). Multiple creators are allowed, but must be separated using a semi-colon.',
            'max_length': 4000,
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "object",
                'properties': {
                    'namepart': {
                        'type': "keyword",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                    'nr_id': {
                        'type': "keyword",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                    'matching': {
                        'type': "keyword",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                    'role': {
                        'type': "keyword",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                    'id': {
                        'type': "integer",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                }
            }
        },
        'xpath':      "/mets:mets/mets:dmdSec[@ID='DM1']/mets:mdWrap/mets:xmlData/mods:mods/mods:name/mods:namePart",
        'xpath_dup':  [],
    },
    
    {
        'model':      'segment',
        'name':       'language',
        'model_type': str,
        'vocab':      True,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'MultipleChoiceField',
        'form': {
            'label':      'Language',
            'help_text':  'Only needed for objects containing textual content (i.e. caption on a photograph, text of a letter). To select multiple languages hold the Ctrl key down and click on each language.',
            'choices':  common.LANGUAGE_CHOICES,
            'widget':     '',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "keyword",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "facet"
        },
        'xpath':      "/mets:mets/mets:dmdSec[@ID='DM1']/mets:mdWrap/mets:xmlData/mods:mods/mods:language/mods:languageTerm",
        'xpath_dup':  [],
    },
    
    {
        'model':      'segment',
        'name':       'genre',
        'model_type': str,
        'vocab':      True,
        'default':    '',
        'csv': {
            'export': 'require',
            'import': 'require',
        },
        'form_type':  'ChoiceField',
        'form': {
            'label':      'Object Genre',
            'help_text':  'The genre, form, and/or physical characteristics of the object.	Use the Library of Congress Basic Genre Terms for Cultural Heritage Materials controlled vocabulary list. See Appendix E: Controlled Vocabularies or the Library of Congress website: http://memory.loc.gov/ammem/techdocs/genre.html',
            'choices': common.GENRE_CHOICES,
            'widget':     '',
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "keyword",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "facet"
        },
        'xpath':      "/mets:mets/mets:dmdSec[@ID='DM1']/mets:mdWrap/mets:xmlData/mods:mods/mods:genre",
        'xpath_dup':  [],
    },
    
    {
        'model':      'segment',
        'name':       'format',
        'model_type': str,
        'vocab':      True,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'ChoiceField',
        'form': {
            'label':      'Object Format',
            'help_text':  'A descriptor for indicating the type of object.	Use the Densho Object Type Controlled Vocabulary List found in Appendix E: Controlled Vocabularies.',
            'choices': common.FORMAT_CHOICES,
            'widget':     '',
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "keyword",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "facet"
        },
        'xpath':      "/mets:mets/mets:dmdSec[@ID='DM1']/mets:mdWrap/mets:xmlData/mods:mods/mods:typeOfResource",
        'xpath_dup':  [],
    },
    
    {
        'model':      'segment',
        'name':       'extent',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Physical Description',
            'help_text':  'Optional: extent, media-type, and any additional relevant information about the material. (e.g. 1 scrapbook, 1 photograph). Construct the statement using a standard like AACR2, RDA, DACS or DCRM(G). Required: width in inches, followed by height in inches, in the following format: "5.25W x 3.5H". For photographs, do not include border, mounts and/or frames. Separate the extent/media-type and the dimensions with a colon. (e.g. 1 scrapbook: 8W x 10H).',
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "text",
                'store': "yes",
                'index': "analyzed"
            },
            'display': "string"
        },
        'xpath':      "/mets:mets/mets:dmdSec[@ID='DM1']/mets:mdWrap/mets:xmlData/mods:mods/mods:physicalDescription/mods:extent",
        'xpath_dup':  [],
    },
    
    {
        'model':      'segment',
        'name':       'contributor',
        'inherits':   ['collection.contributor', 'entity.contributor'],
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Contributing Institution',
            'help_text':  'Name of the organization that owns the physical materials. Will probably be the name of the partner, unless materials were borrowed from external institution for scanning.',
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "keyword",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "string"
        },
        'xpath':      "/mets:mets/mets:dmdSec[@ID='DM1']/mets:mdWrap/mets:xmlData/mods:mods/mods:location/mods:physicalLocation",
        'xpath_dup':  [],
    },
    
    {
        'model':      'segment',
        'name':       'alternate_id',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Alternate ID',
            'help_text':  'May be a physical or virtual record identifier. For example, a physical shelf/folder location, a negative number, an accession number, or a URI of an external database record.',
            'max_length': 512,
            'widget':     '',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "text",
                'store': "yes",
                'index': "analyzed"
            },
            'display': "string"
        },
        'xpath':      "/mets:mets/mets:dmdSec[@ID='DM1']/mets:mdWrap/mets:xmlData/mods:mods/mods:location/mods:holdingExternal/mods:institutionIdentifier/mods:value",
        'xpath_dup':  [],
    },
    
    {
        'model':      'segment',
        'name':       'digitize_person',
        'inherits':   ['entity.digitize_person'],
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Digitizer',
            'help_text':  'Name of person who created the scan. LastName, FirstName',
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "text",
                'store': "yes",
                'index': "analyzed"
            },
            'display': "string"
        },
        'xpath':      '',
        'xpath_dup':  [],
    },
    
    {
        'model':      'segment',
        'name':       'digitize_organization',
        'inherits':   ['entity.digitize_organization'],
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Digitizing Institution',
            'help_text':  'Name of organization responsible for scanning. Will probably be the name of the partner.',
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "keyword",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "string"
        },
        'xpath':      '',
        'xpath_dup':  [],
    },
    
    {
        'model':      'segment',
        'name':       'digitize_date',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Digitize Date',
            'help_text':  'Date of scan. M/D/YYYY.',
            'widget':     '',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "keyword",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "string"
        },
        'xpath':      '',
        'xpath_dup':  [],
    },
    
    # technical
    {
        'model':      'segment',
        'name':       'credit',
        'inherits':   ['collection.prefercite', 'entity.credit'],
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Preferred Citation',
            'help_text':  'Short courtesy text relating to use of object. Could identify either collection contributor and/or donor depending on deed of gift and/or usage agreement for object. Often begins with: "Courtesy of..."',
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "text",
                'store': "yes",
                'index': "analyzed"
            },
            'display': "string"
        },
        'xpath':      '',
        'xpath_dup':  [],
    },
    
    {
        'model':      'segment',
        'name':       'rights',
        'group':      '',
        'inherits':   ['collection.rights', 'entity.rights'],
        'model_type': str,
        'vocab':      True,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'ChoiceField',
        'form': {
            'label':      'Rights',
            'help_text':  'Use rights for the object. Setting will determine the initial default for files associated with this object.',
            'widget':     '',
            'choices':    common.RIGHTS_CHOICES,
            'initial':    common.RIGHTS_CHOICES_DEFAULT,
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "keyword",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "rights"
        },
        'xpath':      "",
        'xpath_dup':  [],
    },
    
    {
        'model':      'segment',
        'name':       'rights_statement',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Restrictions on Reproduction and Use',
            'help_text':  'Short text statement about copyright status, who owns copyright, contact information for requests for use, etc.',
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "text",
                'store': "yes",
                'index': "analyzed"
            },
            'display': "string"
        },
        'xpath':      '',
        'xpath_dup':  [],
    },
    
    {
        'model':      'segment',
        'name':       'topics',
        'model_type': str,
        'vocab':      True,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Topic',
            'help_text':  'Use the <a id="vocab-topics-list" href="#">Densho Topics Controlled Vocabulary List</a> found in Appendix E: Controlled Vocabularies. Multiple entries allowed; separate with a semi-colon. Include the topic ID in brackets after each topic.',
            'widget':     '',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "object",
                'properties': {
                    'id': {
                        'type': "keyword",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                    'term': {
                        'type': "keyword",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                }
            },
            'display': "string"
        },
        'xpath':      "/mets:mets/mets:dmdSec[@ID='DM1']/mets:mdWrap/mets:xmlData/mods:mods/mods:subject/mods:topic/@xlink:href",
        'xpath':      "/mets:mets/mets:dmdSec[@ID='DM1']/mets:mdWrap/mets:xmlData/mods:mods/mods:subject",
        'xpath_dup':  [],
    },
    
    {
        'model':      'segment',
        'name':       'persons',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Person/Organization',
            'help_text':  'When possible use the Library of Congress Name Authority Headings. For individuals use the following format: "Last Name, First Name" (e.g., Adams, Ansel). For organizations use the following format: "Organization Name" (e.g., Associated Press). 			Multiple creators are allowed, but must be separated using a semi-colon.',
            'max_length': 4000,
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "object",
                'properties': {
                    'namepart': {
                        'type': "keyword",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                    'nr_id': {
                        'type': "keyword",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                    'matching': {
                        'type': "keyword",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                    'id': {
                        'type': "integer",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                }
            }
        },
        'xpath':      "/mets:mets/mets:dmdSec[@ID='DM1']/mets:mdWrap/mets:xmlData/mods:mods/mods:subject[@ID='persons']",
        'xpath_dup':  [],
    },
    
    {
        'model':      'segment',
        'name':       'facility',
        'model_type': str,
        'vocab':      True,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Facility',
            'help_text':  'Use the <a id="vocab-facility-list" href="#">Densho Facilities Controlled Vocabulary List</a> found in Appendix E: Controlled Vocabularies. Multiple entries allowed; separate with a semi-colon.',
            'widget':     '',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "object",
                'properties': {
                    'id': {
                        'type': "keyword",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                    'term': {
                        'type': "keyword",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                }
            },
            'display': "string"
        },
        'xpath':      "/mets:mets/mets:dmdSec[@ID='DM1']/mets:mdWrap/mets:xmlData/mods:mods/mods:subject/mods:geographic",
        'xpath_dup':  [],
    },

    {
        'model':      'segment',
        'name':       'chronology',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Chronology',
            'help_text':  'Use the following format: "Label:URL" (e.g., "Internet Archive download:https://archive.org/download/..."). Multiple URLs are allowed, but must be separated using a semi-colon.',
            'max_length': 4000,
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "object",
                'properties': {
                    'startdate': {
                        'type': "keyword",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                    'enddate': {
                        'type': "keyword",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                    'term': {
                        'type': "keyword",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                }
            },
            'display': "string"
        },
        'xpath':      '',
        'xpath_dup':  [],
    },

    {
        'model':      'segment',
        'name':       'geography',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Geography',
            'help_text':  'Use the following format: "Label:URL" (e.g., "Internet Archive download:https://archive.org/download/..."). Multiple URLs are allowed, but must be separated using a semi-colon.',
            'max_length': 4000,
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "object",
                'properties': {
                    'id': {
                        'type': "keyword",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                    'geo_lat': {
                        'type': "keyword",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                    'geo_lng': {
                        'type': "keyword",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                    'term': {
                        'type': "keyword",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                }
            },
            'display': "string"
        },
        'xpath':      '',
        'xpath_dup':  [],
    },

    {
        'model':      'segment',
        'name':       'parent',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Parent Object',
            'help_text':  'Identifier of the object that contains this object. (I.e., the scrapbook that the photo belongs to)	Must be an existing DDR Object ID',
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "keyword",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "string"
        },
        'xpath':      "/mets:mets/mets:dmdSec[@ID='DM1']/mets:mdWrap/mets:xmlData/mods:mods/mods:relatedItem/mods:identifier[@type='local']",
        'xpath_dup':  [],
    },
    
    {
        'model':      'segment',
        'name':       'signature_id',
        'group':      '',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Signature',
            'help_text':  "DDR ID of the file to use as this object's thumbnail.",
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "keyword",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "string"
        },
    },
    
    {
        'model':      'segment',
        'name':       'notes',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Notes',
            'help_text':  'This is an internal field that is not viewable through the public website.',
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': False,
        },
        'xpath':      "/mets:mets/mets:dmdSec[@ID='DM1']/mets:mdWrap/mets:xmlData/mods:mods/mods:note/",
        'xpath_dup':  [],
    },

]

# List of FIELDS to be excluded when exporting and updating.
FIELDS_CSV_EXCLUDED = [
    'record_created',
    'record_lastmod',
    'files',
]

CREATORS_DEFAULT_DICT = {'namepart':'', 'role':'author'}
PERSONS_DEFAULT_DICT = {'namepart':''}

def subfield_fieldnames_in_order(fieldname):
    for field in FIELDS:
        if field['name'] == fieldname:
            return field['elasticsearch']['properties']['properties'].keys()

PERSONS_FIELD_ORDER = subfield_fieldnames_in_order('persons')


# jsonload_* --- load-from-json functions ----------------------------
#
# These functions take raw JSON and convert it to a Python data type.
#

def jsonload_record_created(text): return converters.text_to_datetime(text)
def jsonload_record_lastmod(text): return converters.text_to_datetime(text)
def jsonload_creators(text):
    return converters.text_to_rolepeople(
        text, CREATORS_DEFAULT_DICT
    )
#def jsonload_topics(text): return converters.text_to_bracketids(text, ['term','id'])

def jsonload_topics(text):
    return vocab.TEMP_scrub_topicdata(
        converters.text_to_bracketids(text, ['term','id'])
    )

def jsonload_persons(text):
    return converters.text_to_rolepeople(
        text, PERSONS_DEFAULT_DICT
    )
def jsonload_facility(text): return converters.text_to_bracketids(text, ['term','id'])


# jsondump_* --- export-to-json functions ------------------------------
#
# These functions take Python data and format it for JSON.
#

def jsondump_record_created(data): return converters.datetime_to_text(data)
def jsondump_record_lastmod(data): return converters.datetime_to_text(data)



# display_* --- Display functions --------------------------------------
#
# These functions take Python data from the corresponding Entity field
# and format it for display.
#

# id

def display_record_created(data):
    return converters.datetime_to_text(
        data, converters.config.PRETTY_DATETIME_FORMAT
    )
def display_record_lastmod(data):
    return converters.datetime_to_text(
        data, converters.config.PRETTY_DATETIME_FORMAT
    )

def display_status( data ):
    for c in common.STATUS_CHOICES:
        if data == c[0]:
            return c[1]
    return data

def display_public( data ):
    for c in common.PERMISSIONS_CHOICES:
        if data == c[0]:
            return c[1]
    return data

def display_rights( data ):
    for c in common.RIGHTS_CHOICES:
        if data == c[0]:
            return c[1]
    return data

# collection
# title
# description
# creation
# location

DISPLAY_CREATORS = '{% if data.id %}' \
                   + '<a href="{{ data.id }}">{{ data.role }}: {{ data.namepart }}</a>' \
                   + '{% else %}' \
                   + '{{ data.role }}: {{ data.namepart }}' \
                   + '{% endif %}'

def display_creators( data ):
    return _display_multiline_dict(DISPLAY_CREATORS, data)

def display_language( data ):
    labels = []
    for c in common.LANGUAGE_CHOICES:
        if c[0] in data:
            labels.append(c[1])
    if labels:
        return ', '.join(labels)
    return ''

def display_genre( data ):
    for c in common.GENRE_CHOICES:
        if data == c[0]:
            return c[1]
    return data

def display_format( data ):
    for c in common.FORMAT_CHOICES:
        if data == c[0]:
            return c[1]
    return data

# dimensions
# organization
# organization_id
# digitize_person
# digitize_organization
# digitize_date
# credit

def display_topics( data ):
    return _display_multiline_dict('<a href="{{ data.id }}">{{ data.term }}</a>', data)

def display_persons( data ):
    return _display_multiline_dict(DISPLAY_CREATORS, data)

def display_facility( data ):
    return _display_multiline_dict('<a href="{{ data.id }}">{{ data.term }}</a>', data)

def display_chronology( data ):
    return _display_multiline_dict('{{ data.term }}', data)

def display_geography( data ):
    return _display_multiline_dict('<a href="{{ data.id }}">{{ data.term }}</a>', data)

# parent
# notes
# files

# The following are utility functions used by functions.

def _display_multiline_dict( template, data ):
    t = []
    for d in data:
        if type(d) == type({}):
            t.append(converters.render(template, d))
        else:
            t.append(d)
    return '\n'.join(t)


# index_* --- format for Elasticsearch functions -----------------------
#
# These functions take Python data and format it for JSON.
#

def index_record_created(data):
    return converters.datetime_to_text(
        data, converters.config.ELASTICSEARCH_DATETIME_FORMAT
    )
def index_record_lastmod(data):
    return converters.datetime_to_text(
        data, converters.config.ELASTICSEARCH_DATETIME_FORMAT
    )



# formprep_* --- Form pre-processing functions.--------------------------
#
# These functions take Python data from the corresponding Entity field
# and format it so that it can be used in an HTML form.
#
                   
# id

def formprep_record_created(data):
    if not data:
        data = datetime.now(converters.config.TZ)
    return data

def formprep_record_lastmod(data):
    if not data:
        data = datetime.now(converters.config.TZ)
    return data

# public
# rights

def formprep_parent(data):     return _formprep_basic(data)

# title
# description
# creation
# location

def formprep_creators(data):
    return converters.rolepeople_to_text(data)

# genre
# format
# dimensions
# organization
# organization_id
# digitize_person
# digitize_organization
# digitize_date
# credit

def formprep_topics(data):
    return converters.listofdicts_to_textnolabels(data, ['term','id'])

def formprep_persons(data):
    return converters.rolepeople_to_text(data, field_order=PERSONS_FIELD_ORDER)

def formprep_facility(data):
    return converters.listofdicts_to_textnolabels(data, ['term','id'])

def formprep_chronology(data):
    return converters.listofdicts_to_text(data, ['startdate', 'enddate', 'term'])

def formprep_geography(data):
    return converters.listofdicts_to_text(data, ['id', 'geo_lat', 'geo_lng', 'term'])

# notes

# The following are utility functions used by formprep_* functions.

def _formprep_basic(data):
    if data:
        return json.dumps(data)
    return ''



# formpost_* --- Form post-processing functions ------------------------
#
# These functions take data from the corresponding form field and turn it
# into Python objects that are inserted into the Entity.
#

# id
# record_created
# record_lastmod
# public
# rights

def formpost_parent(data):     return _formpost_basic(data)

# title
# description
# creation
# location

def formpost_creators(text):
    return converters.text_to_rolepeople(
        text, CREATORS_DEFAULT_DICT
    )

# genre
# format
# dimensions
# organization
# organization_id
# digitize_person
# digitize_organization
# digitize_date
# credit

def formpost_topics(text):
    return converters.text_to_dicts(text, ['term', 'id'])

def formpost_persons(text):
    return converters.text_to_rolepeople(
        text, PERSONS_DEFAULT_DICT
    )

def formpost_facility(text):
    return converters.text_to_dicts(text, ['term', 'id'])

def formpost_chronology(text):
    return converters.text_to_dicts(text, ['startdate', 'enddate', 'term'])

def formpost_geography(text):
    return converters.text_to_dicts(text, ['id', 'geo_lat', 'geo_lng', 'term'])

# notes

# The following are utility functions used by formpost_* functions.

def _formpost_basic(data):
    if data:
        try:
            return json.loads(data)
        except:
            return data
    return ''



# csvvalidate_* --------------------------------------------------------
#
# These functions examine data in a CSV field and return True if valid.
#

def _choice_is_valid(field, valid_values, value):
    """
    @param field: str
    @param valid_values: dict {'field': ['list', 'of', 'valid', 'values']
    @param value: str
    @returns: boolean
    """
    if value in valid_values[field]:
        return True
    return False

def _validate_labelled_kvlist(field, data):
    """Validate list of keyvalve pairs in which we only care about the keys.
    """
    valid_values = data[0]
    data = data[1]
    for datum in data:
        if ':' in datum:
            code = datum.strip().split(':')[0]
        else:
            code = datum.strip()
        if not _choice_is_valid('language', valid_values, datum):
            return False
    return True

def _validate_vocab_list(field, valid_values, data):
    """Validate list of keyvalve pairs in which we only care about the keys.
    
    Matches terms from the topics and facility controlled vocabs as str:
        'Activism and involvement: Politics [235]'
        'Arts and literature: Literary arts: Fiction: Adult [242]'
    And as dict:
        {u'id': u'235', u'term': u'Activism and involvement: Politics'}
        {u'id': u'242', u'term': u'Arts and literature: Literary arts: Fiction: Adult'}
    
    @param field: str
    @param valid_values: dict {'field': ['list', 'of', 'valid', 'values']
    @param data: str,dict
    @returns: boolean
    """
    pattern = '\[([0-9]+)\]'
    for datum in data:
        if isinstance(datum, str):
            m = re.search(pattern, datum)
            if m:
                code = m.group(1)
                raw_is_valid = _choice_is_valid(field, valid_values, code)
                int_is_valid = _choice_is_valid(field, valid_values, int(code))
                if not (raw_is_valid or int_is_valid):
                    return False
        elif isinstance(datum, dict) and datum.get('id'):
            raw_is_valid = _choice_is_valid(field, valid_values, datum['id'])
            int_is_valid = _choice_is_valid(field, valid_values, int(datum['id']))
            if not (raw_is_valid or int_is_valid):
                return False
        else:
            raise Exception('Datum is malformed: "%s"' % datum)
    return True

def csvvalidate_status( data ): return _choice_is_valid('status', data[0], data[1])
def csvvalidate_public( data ): return _choice_is_valid('public', data[0], data[1])
def csvvalidate_rights( data ): return _choice_is_valid('rights', data[0], data[1])
def csvvalidate_language( data ): return _validate_labelled_kvlist('language', data)
def csvvalidate_genre( data ): return _choice_is_valid('genre', data[0], data[1])
def csvvalidate_format( data ): return _choice_is_valid('format', data[0], data[1])
def csvvalidate_topics( data ): return _validate_vocab_list('topics', data[0], data[1])
def csvvalidate_facility( data ): return _validate_vocab_list('facility', data[0], data[1])
# chronology
# geography

# csvload_* --- import-from-csv functions ----------------------------
#
# These functions take data from a CSV field and convert it to Python
# data for the corresponding Entity field.
#

def csvload_creators( text ):
    return converters.text_to_rolepeople(
        text, CREATORS_DEFAULT_DICT
    )
def csvload_language( text ): return converters.text_to_labelledlist(text)
def csvload_topics( text ): return converters.text_to_listofdicts(text)
def csvload_persons( text ):
    return converters.text_to_rolepeople(
        text, PERSONS_DEFAULT_DICT
    )
def csvload_facility( text ): return converters.text_to_listofdicts(text)
def csvload_chronology( text ): return converters.text_to_listofdicts(text)
def csvload_geography( text ): return converters.text_to_listofdicts(text)

# csvdump_* --- export-to-csv functions ------------------------------
#
# These functions take Python data from the corresponding Entity field
# and format it for export in a CSV field.
#

def csvdump_record_created(data): return converters.datetime_to_text(data)
def csvdump_record_lastmod(data): return converters.datetime_to_text(data)
def csvdump_creators(data): return converters.rolepeople_to_text(data)
def csvdump_language(data): return converters.labelledlist_to_text(data)
def csvdump_topics(data): return converters.listofdicts_to_text(data)
def csvdump_persons(data): return converters.rolepeople_to_text(data)
def csvdump_facility(data): return converters.listofdicts_to_text(data)
def csvdump_chronology(data): return converters.listofdicts_to_text(data)
def csvdump_geography(data): return converters.listofdicts_to_text(data)
