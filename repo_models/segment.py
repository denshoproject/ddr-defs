from datetime import datetime, date


PERMISSIONS_CHOICES = [['1','Public'],
                       ['0','Private'],]
PERMISSIONS_CHOICES_DEFAULT = 1

REQUIRED_FIELDS_EXCEPTIONS = []


FIELDS = [
    
    {
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
                'type': "string",
                'store': "yes"
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
        'name':       'record_created',
        'model_type': datetime,
        'default': datetime.now(),
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
                'format': "yyyy-MM-dd'T'HH:mm:ss"
            },
            'display': "datetime"
        },
        'xpath':      "/mets:mets/mets:metsHdr@CREATEDATE",
        'xpath_dup':  [],
    },
    
    {
        'name':       'record_lastmod',
        'model_type': datetime,
        'default': datetime.now(),
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
                'format': "yyyy-MM-dd'T'HH:mm:ss"
            },
            'display': "datetime"
        },
        'xpath':      "/mets:mets/mets:metsHdr@LASTMODDATE",
        'xpath_dup':  [],
    },
    
    {
        'name':       'status',
        'group':      '',
        'inheritable':True,
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
            'choices':    'http://partner.densho.org/vocab/api/0.2/status.json',
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': ""
        },
        'xpath':      "",
        'xpath_dup':  [],
    },
    
    {
        'name':       'public',
        'group':      '',
        'inheritable':True,
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
            'choices':    PERMISSIONS_CHOICES,
            'initial':    PERMISSIONS_CHOICES_DEFAULT,
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': ""
        },
        'xpath':      "",
        'xpath_dup':  [],
    },

    {
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
                'type': "string",
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
                'type': "string",
                'store': "yes",
                'index': "analyzed"
            },
            'display': "string"
        },
        'xpath':      "/mets:mets/mets:dmdSec[@ID='DM1']/mets:mdWrap/mets:xmlData/mods:mods/mods:abstract",
        'xpath_dup':  [],
    },
    
    {
        'name':       'segment',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Segment',
            'help_text':  'If you see this you are definitely looking at a segment not an entity.',
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': False,
            'properties': {
                'type': "string",
                'store': "no",
                'index': "no"
            },
            'display': ""
        },
        'xpath':      "/mets:mets/mets:dmdSec[@ID='DM1']/mets:mdWrap/mets:xmlData/mods:mods/mods:note/",
        'xpath_dup':  [],
    },
    
    {
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
            'properties': {
                'type': "string",
                'store': "no",
                'index': "no"
            },
            'display': ""
        },
        'xpath':      "/mets:mets/mets:dmdSec[@ID='DM1']/mets:mdWrap/mets:xmlData/mods:mods/mods:note/",
        'xpath_dup':  [],
    },
    
    {
        'name':       'files',
        'model_type': str,
        'default':    [],
        'csv': {
            'export': 'ignore',
            'import': 'ignore',
        },
        # no form_type
        # no form
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "object",
                'properties': {
                    'path_rel': {
                        'type': "string",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                    'public': {
                        'type': "integer",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                    'md5': {
                        'type': "string",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                    'sha1': {
                        'type': "string",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                    'sha256': {
                        'type': "string",
                        'store': "no",
                        'index': "not_analyzed"
                    }
                }
            },
            'display': ""
        },
        'xpath':      "",
        'xpath_dup':  [],
    },
]
