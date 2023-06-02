"""

oid = 'ddr-testing-141'
oid = 'ddr-testing-141-1'
oid = 'ddr-testing-141-1-master-96c048001e'

from DDR import docstore
from DDR import identifier
from DDR import modules
ds = docstore.Docstore(hosts='192.168.56.1:9200', index='ddrlocal-20171101a')
oi = identifier.Identifier(oid, '/var/www/media/ddr')
document = oi.object()
document
esclass = identifier.ELASTICSEARCH_CLASSES_BY_MODEL[oi.model]
d = esclass()
d.meta.id = document.identifier.id

for fieldname in docstore.doctype_fields(esclass):

    # index_* for complex fields
    if hasattr(oi.fields_module(), 'index_%s' % fieldname):
        field_data = modules.Module(oi.fields_module()).function(
            'index_%s' % fieldname,
            getattr(document, fieldname),
        )

    # everything else
    else:
        try:
            field_data = getattr(document, fieldname)
        except AttributeError:
            print('Error: %s' % (fieldname))
            field_data = None

    if field_data:
        setattr(d, fieldname, field_data)

for key in ['repo', 'org', 'cid', 'eid', 'sid', 'role', 'sha1']:
    setattr(d, key, document.identifier.parts.get(key, ''))

d.parent_id = document.identifier.parent_id()
d.collection_id = document.identifier.collection_id()

d.meta.id
d.title

d.save(using=ds.es, index=ds.indexname)

"""


import elasticsearch_dsl as dsl

#from DDR.models.common import ESObject

from . import collection, entity, segment, files

# superclasses

class ESObjectFields(dsl.Document):
    """List of fields in order for each class
    """
    model = dsl.Keyword()
    fields = dsl.Keyword()
    
    class Meta:
        doc_type = 'esobjectfields'

class ESLineage(dsl.InnerDoc):
    id = dsl.Keyword()
    model = dsl.Keyword()
    idpart = dsl.Keyword()
    label = dsl.Keyword()

class ESObject(dsl.Document):
    """Base for Elasticsearch-DSL versions of model classes
    
    TODO This belongs in DDR.models.common but putting it there
    causes an import loop or something.
    """
    id = dsl.Keyword()
    model = dsl.Keyword()
    parent_id = dsl.Keyword()
    collection_id = dsl.Keyword()
    organization_id = dsl.Keyword()
    signature_id = dsl.Keyword()
    #
    links_html = dsl.Keyword()
    links_json = dsl.Keyword()
    links_img = dsl.Keyword()
    links_thumb = dsl.Keyword()
    links_parent = dsl.Keyword()
    links_children = dsl.Keyword()
    links_children_objects = dsl.Keyword()
    links_children_files = dsl.Keyword()
    lineage = dsl.Nested(ESLineage)
    url = dsl.Keyword()
    #
    repo = dsl.Keyword()
    org = dsl.Keyword()
    cid = dsl.Long()
    eid = dsl.Long()
    sid = dsl.Long()
    role = dsl.Keyword()
    sha1 = dsl.Keyword()
    #
    title = dsl.Text()
    description = dsl.Text()
    
    #class Index:
    #    name = ???
    # We don't define Index here because this module cannot know anything
    # about the application configs.
    # Instead we specify "index=OBJECT.index_name(model)" to Elasticsearch
    # create_index(), get(), search(), delete(), etc.
    
    class Meta:
        doc_type = 'esobject'
    
    def __repr__(self):
        return "<%s.%s %s:\"%s\">" % (
            self.__module__, self.__class__.__name__,
            self.id, self.title
        )

class ESRepositoryObject(ESObject):
    """classes that form the Repository structure"""
    pass

class ESCollectionObject(ESRepositoryObject):
    """classes that are part of collections"""
    pass


# subclasses

class Facet(dsl.Document):
    id = dsl.Keyword()
    links_html = dsl.Keyword()
    links_json = dsl.Keyword()
    links_children = dsl.Keyword()
    title = dsl.Text()
    description = dsl.Text()
    
    class Meta:
        doc_type = 'facet'


class Elinks(dsl.InnerDoc):
    label = dsl.Text()
    url = dsl.Text()

class Geopoint(dsl.InnerDoc):
    lat = dsl.Double()
    lng = dsl.Double()

class Location(dsl.InnerDoc):
    geopoint = dsl.Nested(Geopoint)
    label = dsl.Text()

class FacetTerm(dsl.Document):
    id = dsl.Keyword()
    facet = dsl.Keyword()
    term_id = dsl.Keyword()
    links_html = dsl.Keyword()
    links_json = dsl.Keyword()
    links_children = dsl.Keyword()
    title = dsl.Text()
    description = dsl.Text()
    # topics
    path = dsl.Text()
    parent_id = dsl.Keyword()
    ancestors = dsl.Long()
    siblings = dsl.Long()
    children = dsl.Long()
    weight = dsl.Long()
    encyc_urls = dsl.Text()
    # facility
    type = dsl.Text()
    elinks = dsl.Nested(Elinks)
    location_geopoint = dsl.Nested(Location)
    
    class Meta:
        doc_type = 'facetterm'


class Narrator(dsl.Document):
    id = dsl.Keyword()
    #title
    nr_id = dsl.Keyword()
    created = dsl.Date(format="yyyy-MM-dd'T'HH:mm:ss")
    modified = dsl.Date(format="yyyy-MM-dd'T'HH:mm:ss")
    b_date = dsl.Date(format="yyyy-MM-dd'T'HH:mm:ss")
    d_date = dsl.Date(format="yyyy-MM-dd'T'HH:mm:ss")
    last_name = dsl.Keyword()
    first_name = dsl.Keyword()
    middle_name = dsl.Keyword()
    #display_name
    #bio
    title = dsl.Text()
    description = dsl.Text()
    gender = dsl.Keyword()
    generation = dsl.Keyword()
    ethnicity = dsl.Keyword()
    nationality = dsl.Keyword()
    religion = dsl.Keyword()
    birth_location = dsl.Text()
    #notes
    nickname = dsl.Text()
    image_url = dsl.Text()
    
    class Meta:
        doc_type = 'narrator'


class Repository(ESRepositoryObject):
    class Meta:
        doc_type= 'repository'

    @staticmethod
    def list_fields():
        return ['id', 'title', 'description', 'logo', 'url',]


class Organization(ESRepositoryObject):
    class Meta:
        doc_type= 'organization'

    @staticmethod
    def list_fields():
        return ['id', 'title', 'description', 'logo', 'url',]


class Persons(dsl.InnerDoc):
    nr_id = dsl.Keyword()
    namepart = dsl.Keyword()
    id = dsl.Integer()
    role = dsl.Keyword()

class Collection(ESObject):
    """IMPORTANT: keep in sync with fields in repo_models/collections.py
    """
    #title
    #description
    record_created = dsl.Date()
    record_lastmod = dsl.Date()
    status = dsl.Keyword()
    public = dsl.Keyword()
    unitdateinclusive = dsl.Text()
    unitdatebulk = dsl.Text()
    creators = dsl.Nested(Persons)
    extent = dsl.Text()
    language = dsl.Keyword()
    contributor = dsl.Keyword()
    description = dsl.Text()
    physloc = dsl.Text()
    acqinfo = dsl.Text()
    custodhist = dsl.Text()
    accruals = dsl.Text()
    processinfo = dsl.Text()
    rights = dsl.Keyword()
    accessrestrict = dsl.Text()
    userrestrict = dsl.Text()
    prefercite = dsl.Text()
    bioghist = dsl.Text()
    scopecontent = dsl.Text()
    relatedmaterial = dsl.Text()
    separatedmaterial = dsl.Text()
    search_hidden = dsl.Text()
    
    class Meta:
        doc_type= 'collection'
    
    @staticmethod
    def list_fields():
        return [
            field['name']
            for field in collection.FIELDS
            if field['elasticsearch']['public']
        ]


class Topics(dsl.InnerDoc):
    id = dsl.Keyword()
    term = dsl.Keyword()

class Facility(dsl.InnerDoc):
    id = dsl.Keyword()
    term = dsl.Keyword()

class Chronology(dsl.InnerDoc):
    startdate = dsl.Keyword()
    enddate = dsl.Keyword()
    term = dsl.Keyword()

class Geography(dsl.InnerDoc):
    id = dsl.Keyword()
    geo_lat = dsl.Keyword()
    geo_lng = dsl.Keyword()
    term = dsl.Keyword()

class Entity(ESCollectionObject):
    """IMPORTANT: keep in sync with fields in repo_models/entity.py
    """
    #title
    #description
    record_created = dsl.Date()
    record_lastmod = dsl.Date()
    status = dsl.Keyword()
    sort = dsl.Integer()
    creation = dsl.Text()
    location = dsl.Keyword()
    creators = dsl.Nested(Persons)
    language = dsl.Keyword()
    genre = dsl.Keyword()
    format = dsl.Keyword()
    extent = dsl.Text()
    contributor = dsl.Keyword()
    alternate_id = dsl.Text()
    digitize_person = dsl.Text()
    digitize_organization = dsl.Keyword()
    digitize_date = dsl.Keyword()
    credit = dsl.Text()
    rights = dsl.Keyword()
    rights_statement = dsl.Text()
    topics = dsl.Nested(Topics)
    persons = dsl.Nested(Persons)
    facility = dsl.Nested(Facility)
    chronology = dsl.Nested(Chronology)
    geography = dsl.Nested(Geography)
    search_hidden = dsl.Text()
    
    class Meta:
        doc_type= 'entity'
    
    @staticmethod
    def list_fields():
        return [
            field['name']
            for field in entity.FIELDS
            if field['elasticsearch']['public']
        ]


class ExternalUrls(dsl.InnerDoc):
    label = dsl.Keyword() # store=no
    url = dsl.Keyword() # store=no

class File(ESCollectionObject):
    """IMPORTANT: keep in sync with fields in repo_models/file.py
    """
    #title
    #description
    record_created = dsl.Date()
    record_lastmod = dsl.Date()
    external = dsl.Integer()
    sha256 = dsl.Keyword()
    md5 = dsl.Keyword()
    size = dsl.Long()
    basename_orig = dsl.Text()
    access_rel = dsl.Text()
    mimetype = dsl.Keyword()
    public = dsl.Keyword()
    rights = dsl.Keyword()
    sort = dsl.Integer()
    thumb = dsl.Text()
    #label
    digitize_person = dsl.Text()
    tech_notes = dsl.Text()
    external_urls = dsl.Nested(ExternalUrls)
    links = dsl.Text()
    
    class Meta:
        doc_type= 'file'

    @staticmethod
    def list_fields():
        return [
            field['name']
            for field in files.FIELDS
            if field['elasticsearch']['public']
        ]


# Help (ddr-cmdln) DDR.docstore access these classes
ELASTICSEARCH_CLASSES = {

    # all classes to be included in Elasticsearch
    'all': [
        {'doctype':'repository', 'class':Repository, 'doc_type': 'ddrrepository'},
        {'doctype':'organization', 'class':Organization, 'doc_type': 'ddrorganization'},
        {'doctype':'collection', 'class':Collection, 'doc_type': 'ddrcollection'},
        {'doctype':'entity', 'class':Entity, 'doc_type': 'ddrentity'},
        {'doctype':'segment', 'class':Entity, 'doc_type': 'ddrsegment'},
        {'doctype':'file', 'class':File, 'doc_type': 'ddrfile'},
        {'doctype':'facet', 'class':Facet, 'doc_type': 'ddrfacet'},
        {'doctype':'facetterm', 'class':FacetTerm, 'doc_type': 'ddrfacetterm'},
        {'doctype':'narrator', 'class':Narrator, 'doc_type': 'ddrnarrator'},
    ],

    # classes that form the Repository structure
    'repository': [
        {'doctype':'repository', 'class':Repository, 'doc_type': 'ddrrepository'},
        {'doctype':'organization', 'class':Organization, 'doc_type': 'ddrorganization'},
        {'doctype':'collection', 'class':Collection, 'doc_type': 'ddrcollection'},
        {'doctype':'entity', 'class':Entity, 'doc_type': 'ddrentity'},
        {'doctype':'segment', 'class':Entity, 'doc_type': 'ddrsegment'},
        {'doctype':'file', 'class':File, 'doc_type': 'ddrfile'},
    ],

    # class that are part of collections
    'collection': [
        {'doctype':'collection', 'class':Collection, 'doc_type': 'ddrcollection'},
        {'doctype':'entity', 'class':Entity, 'doc_type': 'ddrentity'},
        {'doctype':'segment', 'class':Entity, 'doc_type': 'ddrsegment'},
        {'doctype':'file', 'class':File, 'doc_type': 'ddrfile'},
    ],

}

ELASTICSEARCH_LIST_FIELDS = (
    'id',
    'signature_id',
    'access_rel',
    'status',
    'public',
    'title',
    'label',
    'description',
    'url',
    'role',
    'extent',
    'mimetype',
    'topics',
    'facility',
)
