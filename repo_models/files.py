import logging
logger = logging.getLogger(__name__)

from DDR import converters


MODEL = 'file'

DATE_FORMAT            = '%Y-%m-%d'
TIME_FORMAT            = '%H:%M:%S'
DATETIME_FORMAT        = '%Y-%m-%dT%H:%M:%S'
PRETTY_DATE_FORMAT     = '%d %B %Y'
PRETTY_TIME_FORMAT     = '%I:%M %p'
PRETTY_DATETIME_FORMAT = '%d %B %Y, %I:%M %p'

PERMISSIONS_CHOICES = [['1','Public'],
                       ['0','Private'],]
PERMISSIONS_CHOICES_DEFAULT = 1

RIGHTS_CHOICES = [["cc", "DDR Creative Commons"],
                  ["pcc", "Copyright, with special 3rd-party grant permitted"],
                  ["nocc", "Copyright restricted"],
                  ["pdm", "Public domain" ],]
RIGHTS_CHOICES_DEFAULT = 'cc'

REQUIRED_FIELDS_EXCEPTIONS = ['thumb', 'sha1', 'sha256', 'md5', 'size', 'access_rel', 'xmp', 'links']


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
        'name':       'external',
        'group':      '',
        'model_type': int,
        'default':    0,
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'IntegerField',
        'form': {
            'label':      'External',
            'help_text':  '',
            'widget':     'HiddenInput',
            'initial':    0,
            'required':   False,
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
        'name':       'role',
        'model_type': str,
        'default':    None,
        'csv': {
            'export': '',
            'import': '',
        },
        # no form_type
        # no form
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "no",
                'index': "not_analyzed"
            },
            'display': ""
        },
        'xpath':      "",
        'xpath_dup':  [],
    },
    
    {
        'name':       'sha1',
        'model_type': str,
        'default':    None,
        'csv': {
            'export': 'ignore',
            'import': '',
        },
        # no form_type
        # no form
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "no",
                'index': "not_analyzed"
            },
            'display': ""
        },
        'xpath':      "",
        'xpath_dup':  [],
    },
    
    {
        'name':       'sha256',
        'model_type': str,
        'default':    None,
        'csv': {
            'export': 'ignore',
            'import': '',
        },
        # no form_type
        # no form
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "no",
                'index': "not_analyzed"
            },
            'display': ""
        },
        'xpath':      "",
        'xpath_dup':  [],
    },
    
    {
        'name':       'md5',
        'model_type': str,
        'default':    None,
        'csv': {
            'export': 'ignore',
            'import': '',
        },
        # no form_type
        # no form
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "no",
                'index': "not_analyzed"
            },
            'display': ""
        },
        'xpath':      "",
        'xpath_dup':  [],
    },
    
    {
        'name':       'size',
        'model_type': str,
        'default':    None,
        'csv': {
            'export': 'ignore',
            'import': '',
        },
        # no form_type
        # no form
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "integer",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "filesize"
        },
        'xpath':      "",
        'xpath_dup':  [],
    },
    
    {
        'name':       'basename_orig',
        'model_type': str,
        'default':    None,
        'csv': {
            'export': '',
            'import': '',
        },
        # no form_type
        # no form
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes"
            },
            'display': "string"
        },
        'xpath':      "",
        'xpath_dup':  [],
    },
    
    {
        'name':       'access_rel',
        'model_type': str,
        'default':    None,
        'csv': {
            'export': 'ignore',
            'import': 'ignore',
        },
        # no form_type
        # no form
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes"
            },
            'display': ""
        },
        'xpath':      "",
        'xpath_dup':  [],
    },
    
    {
        'name':       'mimetype',
        'group':      '',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Mimetype',
            'help_text':  'Media type. Leave field blank to reset based on original filename.',
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes"
            },
            'display': "string"
        },
        'xpath':      "",
        'xpath_dup':  [],
    },

    {
        'name':       'public',
        'group':      '',
        'model_type': int,
        'vocab':      True,
        'default':    PERMISSIONS_CHOICES_DEFAULT,
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'ChoiceField',
        'form': {
            'label':      'Privacy Level',
            'help_text':  'Whether this file should be accessible from the public website.',
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
        'name':       'rights',
        'group':      '',
        'model_type': str,
        'vocab':      True,
        'default':    RIGHTS_CHOICES_DEFAULT,
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'ChoiceField',
        'form': {
            'label':      'Rights',
            'help_text':  'The use license for this file.',
            'widget':     '',
            'choices':    RIGHTS_CHOICES,
            'initial':    RIGHTS_CHOICES_DEFAULT,
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "rights"
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
            'help_text':  'Order of this file in relation to others for this object (ordered low to high). Can be used to arrange images in a multi-page document.',
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
        'name':       'thumb',
        'group':      '',
        'model_type': int,
        'default':    -1,
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'IntegerField',
        'form': {
            'label':      'Thumbnail',
            'help_text':  '',
            'widget':     'HiddenInput',
            'initial':    -1,
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes"
            },
            'display': ""
        },
        'xpath':      "",
        'xpath_dup':  [],
    },
    
    {
        'name':       'label',
        'group':      '',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Label',
            'help_text':  '(Optional) Friendly label for file describing partitive role (i.e., \"Page 1\", \"Cover\", \"Envelope\")',
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes"
            },
            'display': "string"
        },
        'xpath':      "",
        'xpath_dup':  [],
    },
    
    {
        'name':       'digitize_person',
        'group':      '',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'digitize_person',
            'help_text':  '',
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "string"
        },
        'xpath':      "",
        'xpath_dup':  [],
    },
    
    {
        'name':       'tech_notes',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Technical Notes',
            'help_text':  '',
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "no",
                'index': "no"
            },
            'display': "string"
        },
        'xpath':      "",
        'xpath_dup':  [],
    },
    
    {
        'name':       'xmp',
        'group':      '',
        'model_type': str,
        'default':    None,
        'csv': {
            'export': 'ignore',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'XMP Metadata',
            'help_text':  '',
            'widget':     'HiddenInput',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "no",
                'index': "no"
            },
            'display': "string_collapsed"
        },
        'xpath':      "",
        'xpath_dup':  [],
    },
    
    {
        'name':       'external_urls',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'External URLs',
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
                    'label': {
                        'type': "string",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                    'url': {
                        'type': "string",
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
        'name':       'links',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Associated Files',
            'help_text':  'Semicolon-separated list of file.path_rels that this file points to.',
            'max_length': 255,
            'widget':     'HiddenInput',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes"
            },
            'display': ""
        },
        'xpath':      "",
        'xpath_dup':  [],
    },

]

# Subset of FILE_FIELDS that are used when creating a new File.
newfile_fields = ['public', 'rights', 'path', 'role', 'label', 'sort',]
FIELDS_NEW = [field for field in FIELDS if field['name'] in newfile_fields]

# List of FIELDS to be excluded when exporting and updating.
FIELDS_CSV_EXCLUDED = ['role','size','access_rel','sha1','sha256','md5','xmp']



# jsonload_* --- load-from-json functions ----------------------------
#
# These functions take raw JSON and convert it to a Python data type.
#



# jsondump_* --- export-to-json functions ------------------------------
#
# These functions take Python data and format it for JSON.
#



# display_* --- Display functions --------------------------------------
#
# These functions take Python data from the corresponding Collection field
# and format it for display.
#

def display_public( data ):
    for c in PERMISSIONS_CHOICES:
        if data == c[0]:
            return c[1]
    return data

def display_rights( data ):
    for c in RIGHTS_CHOICES:
        if data == c[0]:
            return c[1]
    return data

def display_sort( data ):
    return ''

def display_thumb( data ):
    return ''

def display_xmp( data ):
    return ''

TEMPLATE_EXTERNAL_URLS = """
{% for line in data %}
<a href="{{ line.url }}" target="iarchive">{{ line.label }}</a>
{% endfor %}
"""

def display_external_urls(data):
    return converters.render(TEMPLATE_EXTERNAL_URLS, data)

def display_links( data ):
    return ''



# formprep_* --- Form pre-processing functions.--------------------------
#
# These functions take Python data from the corresponding Collection field
# and format it so that it can be used in an HTML form.
#

def formprep_external_urls(data):
    return converters.listofdicts_to_text(data, ['label', 'url'])


# formpost_* --- Form post-processing functions ------------------------
#
# These functions take data from the corresponding form field and turn it
# into Python objects that are inserted into the Collection.
#

def formpost_external_urls(text):
    return converters.text_to_dicts(text, ['label', 'url'])



# csvvalidate_* --------------------------------------------------------
#
# These functions examine data in a CSV field and return True if valid.
#

def _choice_is_valid(field, valid_values, value):
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
    
    Matches terms from the topics and facility controlled vocabs:
        Activism and involvement: Politics [235]
        Arts and literature: Literary arts: Fiction: Adult [242]
    """
    pattern = '\[([0-9]+)\]'
    for datum in data:
        m = re.search(pattern, datum)
        if m:
            code = m.group(1)
            raw_is_valid = _choice_is_valid(field, valid_values, code)
            int_is_valid = _choice_is_valid(field, valid_values, int(code))
            if not (raw_is_valid or int_is_valid):
                return False
    return True

#role
#sha1
#sha256
#md5
#size
#basename_orig
#access_rel
#public
#rights
#sort
#thumb
#label
#digitize_person
#tech_notes
#xmp
#external_urls
#links

#def csvvalidate_status( data ): return _choice_is_valid('status', data[0], data[1])
#def csvvalidate_language( data ): return _validate_labelled_kvlist('language', data)
#def csvvalidate_topics( data ): return _validate_vocab_list('topics', data[0], data[1])

# csvload_* --- import-from-csv functions ----------------------------
#
# These functions take data from a CSV field and convert it to Python
# data for the corresponding Entity field.
#

#def csvload_role(text):
#def csvload_sha1(text):
#def csvload_sha256(text):
#def csvload_md5(text):
#def csvload_size(text):
#def csvload_basename_orig(text):
#def csvload_access_rel(text):
#def csvload_public(text):
#def csvload_rights(text):
#def csvload_sort(text):
#def csvload_thumb(text):
#def csvload_label(text):
#def csvload_digitize_person(text):
#def csvload_tech_notes(text):
#def csvload_xmp(text):

def csvload_external_urls(text):
    return converters.text_to_dicts(text, ['label', 'url'])

#def csvload_links(text):

# csvdump_* --- export-to-csv functions ------------------------------
#
# These functions take Python data from the corresponding Entity field
# and format it for export in a CSV field.
#

#def csvdump_role(data):
#def csvdump_sha1(data):
#def csvdump_sha256(data):
#def csvdump_md5(data):
#def csvdump_size(data):
#def csvdump_basename_orig(data):
#def csvdump_access_rel(data):
#def csvdump_public(data):
#def csvdump_rights(data):
#def csvdump_sort(data):
#def csvdump_thumb(data):
#def csvdump_label(data):
#def csvdump_digitize_person(data):
#def csvdump_tech_notes(data):
#def csvdump_xmp(data):

def csvdump_external_urls(data):
    return converters.listofdicts_to_text(data, ['label', 'url'])

#def csvdump_links(data):

#def csvdump_creators(data): return csv.dump_rolepeople(data)
#def csvdump_language(data): return csv.dump_labelledlist(data)
#def csvdump_topics(data): return csv.dump_list(data)
