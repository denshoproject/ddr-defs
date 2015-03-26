import logging
logger = logging.getLogger(__name__)


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
        'name':       'role',
        'xpath':      "",
        'xpath_dup':  [],
        'model_type': str,
        # no form_type
        # no form
        'default':    '',
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "no",
                'index': "not_analyzed"
            },
            'display': ""
        },
    },
    {
        'name':       'sha1',
        'xpath':      "",
        'xpath_dup':  [],
        'model_type': str,
        # no form_type
        # no form
        'default':    '',
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "no",
                'index': "not_analyzed"
            },
            'display': ""
        },
    },
    {
        'name':       'sha256',
        'xpath':      "",
        'xpath_dup':  [],
        'model_type': str,
        # no form_type
        # no form
        'default':    '',
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "no",
                'index': "not_analyzed"
            },
            'display': ""
        },
    },
    {
        'name':       'md5',
        'xpath':      "",
        'xpath_dup':  [],
        'model_type': str,
        # no form_type
        # no form
        'default':    '',
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "no",
                'index': "not_analyzed"
            },
            'display': ""
        },
    },
    {
        'name':       'size',
        'xpath':      "",
        'xpath_dup':  [],
        'model_type': str,
        # no form_type
        # no form
        'default':    '',
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "integer",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "filesize"
        },
    },
    {
        'name':       'basename_orig',
        'xpath':      "",
        'xpath_dup':  [],
        'model_type': str,
        # no form_type
        # no form
        'default':    '',
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes"
            },
            'display': "string"
        },
    },
    {
        'name':       'access_rel',
        'xpath':      "",
        'xpath_dup':  [],
        'model_type': str,
        # no form_type
        # no form
        'default':    '',
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes"
            },
            'display': ""
        },
    },
    {
        'name':       'public',
        'group':      '',
        'xpath':      "",
        'xpath_dup':  [],
        'model_type': int,
        'form_type':  'ChoiceField',
        'form': {
            'label':      'Privacy Level',
            'help_text':  'Whether this file should be accessible from the public website.',
            'widget':     '',
            'choices':    PERMISSIONS_CHOICES,
            'initial':    PERMISSIONS_CHOICES_DEFAULT,
            'required':   True,
        },
        'default':    '',
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': ""
        },
    },
    {
        'name':       'rights',
        'group':      '',
        'xpath':      "",
        'xpath_dup':  [],
        'model_type': str,
        'form_type':  'ChoiceField',
        'form': {
            'label':      'Rights',
            'help_text':  'The use license for this file.',
            'widget':     '',
            'choices':    RIGHTS_CHOICES,
            'initial':    RIGHTS_CHOICES_DEFAULT,
            'required':   True,
        },
        'default':    '',
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "rights"
        },
    },

    {
        'name':       'sort',
        'group':      '',
        'xpath':      "",
        'xpath_dup':  [],
        'model_type': int,
        'form_type':  'IntegerField',
        'form': {
            'label':      'Sort',
            'help_text':  'Order of this file in relation to others for this object (ordered low to high). Can be used to arrange images in a multi-page document.',
            'widget':     '',
            'initial':    1,
            'required':   True,
        },
        'default':    '',
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "integer",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': ""
        },
    },
    {
        'name':       'thumb',
        'group':      '',
        'xpath':      "",
        'xpath_dup':  [],
        'model_type': int,
        'form_type':  'IntegerField',
        'form': {
            'label':      'Thumbnail',
            'help_text':  '',
            'widget':     'HiddenInput',
            'initial':    -1,
            'required':   True,
        },
        'default':    '',
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes"
            },
            'display': ""
        },
    },
    {
        'name':       'label',
        'group':      '',
        'xpath':      "",
        'xpath_dup':  [],
        'model_type': str,
        'form_type':  'CharField',
        'form': {
            'label':      'Label',
            'help_text':  '(Optional) Friendly label for file describing partitive role (i.e., \"Page 1\", \"Cover\", \"Envelope\")',
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   False,
        },
        'default':    '',
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes"
            },
            'display': "string"
        },
    },
    {
        'name':       'digitize_person',
        'group':      '',
        'xpath':      "",
        'xpath_dup':  [],
        'model_type': str,
        'form_type':  'CharField',
        'form': {
            'label':      'digitize_person',
            'help_text':  '',
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   False,
        },
        'default':    '',
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "string"
        },
    },
    {
        'name':       'tech_notes',
        'xpath':      "",
        'xpath_dup':  [],
        'model_type': str,
        'form_type':  'CharField',
        'form': {
            'label':      'Technical Notes',
            'help_text':  '',
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'default':    '',
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "no",
                'index': "no"
            },
            'display': "string"
        },
    },
    {
        'name':       'xmp',
        'group':      '',
        'xpath':      "",
        'xpath_dup':  [],
        'model_type': str,
        'form_type':  'CharField',
        'form': {
            'label':      'XMP Metadata',
            'help_text':  '',
            'widget':     'HiddenInput',
            'initial':    '',
            'required':   False,
        },
        'default':    '',
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "no",
                'index': "no"
            },
            'display': "string_collapsed"
        },
    },
    {
        'name':       'links',
        'xpath':      "",
        'xpath_dup':  [],
        'model_type': str,
        'form_type':  'CharField',
        'form': {
            'label':      'Associated Files',
            'help_text':  'Semicolon-separated list of file.path_rels that this file points to.',
            'max_length': 255,
            'widget':     'HiddenInput',
            'initial':    '',
            'required':   False,
        },
        'default':    '',
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes"
            },
            'display': ""
        },
    },
]

# Subset of FILE_FIELDS that are used when creating a new File.
newfile_fields = ['public', 'rights', 'path', 'role', 'label', 'sort',]
FIELDS_NEW = [field for field in FIELDS if field['name'] in newfile_fields]

# List of FIELDS to be excluded when exporting and updating.
FIELDS_CSV_EXCLUDED = ['role','size','access_rel','sha1','sha256','md5','xmp']



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

def display_links( data ):
    return ''



# formprep_* --- Form pre-processing functions.--------------------------
#
# These functions take Python data from the corresponding Collection field
# and format it so that it can be used in an HTML form.
#



# formpost_* --- Form post-processing functions ------------------------
#
# These functions take data from the corresponding form field and turn it
# into Python objects that are inserted into the Collection.
#
