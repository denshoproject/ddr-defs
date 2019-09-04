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

class ESObjectFields(dsl.DocType):
    """List of fields in order for each class
    """
    model = dsl.Keyword(index='not_analyzed')
    fields = dsl.Keyword(index='not_analyzed')
    
    class Meta:
        doc_type = 'esobjectfields'

class ESLineage(dsl.InnerDoc):
    id = dsl.Keyword(index='not_analyzed')
    model = dsl.Keyword(index='not_analyzed')
    idpart = dsl.Keyword(index='not_analyzed')
    label = dsl.Keyword(index='not_analyzed')

class ESObject(dsl.DocType):
    """Base for Elasticsearch-DSL versions of model classes
    
    TODO This belongs in DDR.models.common but putting it there
    causes an import loop or something.
    """
    id = dsl.Keyword(index='not_analyzed')
    model = dsl.Keyword(index='not_analyzed')
    parent_id = dsl.Keyword(index='not_analyzed')
    collection_id = dsl.Keyword(index='not_analyzed')
    organization_id = dsl.Keyword(index='not_analyzed')
    signature_id = dsl.Keyword(index='not_analyzed')
    #
    links_html = dsl.Keyword(index='not_analyzed')
    links_json = dsl.Keyword(index='not_analyzed')
    links_img = dsl.Keyword(index='not_analyzed')
    links_thumb = dsl.Keyword(index='not_analyzed')
    links_parent = dsl.Keyword(index='not_analyzed')
    links_children = dsl.Keyword(index='not_analyzed')
    links_children_objects = dsl.Keyword(index='not_analyzed')
    links_children_files = dsl.Keyword(index='not_analyzed')
    lineage = dsl.Nested(ESLineage)
    url = dsl.Keyword(index='not_analyzed')
    #
    repo = dsl.Keyword(index='not_analyzed')
    org = dsl.Keyword(index='not_analyzed')
    cid = dsl.Long()
    eid = dsl.Long()
    sid = dsl.Long()
    role = dsl.Keyword(index='not_analyzed')
    sha1 = dsl.Keyword(index='not_analyzed')
    #
    title = dsl.Text()
    description = dsl.Text()
    
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

class Facet(dsl.DocType):
    id = dsl.Keyword(index='not_analyzed')
    links_html = dsl.Keyword(index='not_analyzed')
    links_json = dsl.Keyword(index='not_analyzed')
    links_children = dsl.Keyword(index='not_analyzed')
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

class FacetTerm(dsl.DocType):
    id = dsl.Keyword(index='not_analyzed')
    facet = dsl.Keyword(index='not_analyzed')
    term_id = dsl.Keyword(index='not_analyzed')
    links_html = dsl.Keyword(index='not_analyzed')
    links_json = dsl.Keyword(index='not_analyzed')
    links_children = dsl.Keyword(index='not_analyzed')
    title = dsl.Text()
    description = dsl.Text()
    # topics
    path = dsl.Text()
    parent_id = dsl.Keyword(index='not_analyzed')
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


class Narrator(ESObject):
    #id
    #title
    nr_id = dsl.Keyword(index='not_analyzed')
    created = dsl.Date(index='not_analyzed', format="yyyy-MM-dd'T'HH:mm:ss")
    modified = dsl.Date(index='not_analyzed', format="yyyy-MM-dd'T'HH:mm:ss")
    b_date = dsl.Date(index='not_analyzed', format="yyyy-MM-dd'T'HH:mm:ss")
    d_date = dsl.Date(index='not_analyzed', format="yyyy-MM-dd'T'HH:mm:ss")
    last_name = dsl.Text()
    first_name = dsl.Text()
    middle_name = dsl.Text()
    display_name = dsl.Text(index="no", copy_to="title")
    bio = dsl.Text(index="no", copy_to="description")
    description = dsl.Text()
    gender = dsl.Text()
    generation = dsl.Text()
    ethnicity = dsl.Text()
    nationality = dsl.Text()
    religion = dsl.Text()
    birth_location = dsl.Text()
    notes = dsl.Text(index="no", copy_to="notes_private")
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


class Creators(dsl.InnerDoc):
    namepart = dsl.Keyword(index='not_analyzed')
    id = dsl.Integer(index='not_analyzed')
    role = dsl.Keyword(index='not_analyzed')

class Collection(ESObject):
    """IMPORTANT: keep in sync with fields in repo_models/collections.py
    """
    #title
    #description
    record_created = dsl.Date()
    record_lastmod = dsl.Date()
    status = dsl.Keyword(index='not_analyzed')
    public = dsl.Keyword(index='not_analyzed')
    unitdateinclusive = dsl.Text()
    unitdatebulk = dsl.Text()
    creators = dsl.Nested(Creators)
    extent = dsl.Text()
    language = dsl.Keyword(index='not_analyzed')
    contributor = dsl.Keyword(index='not_analyzed')
    description = dsl.Text()
    physloc = dsl.Text()
    acqinfo = dsl.Text()
    custodhist = dsl.Text()
    accruals = dsl.Text()
    processinfo = dsl.Text()
    rights = dsl.Keyword(index='not_analyzed')
    accessrestrict = dsl.Text()
    userrestrict = dsl.Text()
    prefercite = dsl.Text()
    bioghist = dsl.Text()
    scopecontent = dsl.Text()
    relatedmaterial = dsl.Text()
    separatedmaterial = dsl.Text()
    
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
    id = dsl.Keyword(index='not_analyzed')
    term = dsl.Keyword(index='not_analyzed')

class Facility(dsl.InnerDoc):
    id = dsl.Keyword(index='not_analyzed')
    term = dsl.Keyword(index='not_analyzed')

class Chronology(dsl.InnerDoc):
    startdate = dsl.Keyword(index='not_analyzed')
    enddate = dsl.Keyword(index='not_analyzed')
    term = dsl.Keyword(index='not_analyzed')

class Geography(dsl.InnerDoc):
    id = dsl.Keyword(index='not_analyzed')
    geo_lat = dsl.Keyword(index='not_analyzed')
    geo_lng = dsl.Keyword(index='not_analyzed')
    term = dsl.Keyword(index='not_analyzed')

class Entity(ESCollectionObject):
    """IMPORTANT: keep in sync with fields in repo_models/entity.py
    """
    #title
    #description
    record_created = dsl.Date()
    record_lastmod = dsl.Date()
    status = dsl.Keyword(index='not_analyzed')
    sort = dsl.Integer()
    creation = dsl.Text()
    location = dsl.Keyword(index='not_analyzed')
    creators = dsl.Nested(Creators)
    language = dsl.Keyword(index='not_analyzed')
    genre = dsl.Keyword(index='not_analyzed')
    format = dsl.Keyword(index='not_analyzed')
    extent = dsl.Text()
    contributor = dsl.Keyword(index='not_analyzed')
    alternate_id = dsl.Text()
    digitize_person = dsl.Text()
    digitize_organization = dsl.Keyword(index='not_analyzed')
    digitize_date = dsl.Keyword(index='not_analyzed')
    credit = dsl.Text()
    rights = dsl.Keyword(index='not_analyzed')
    rights_statement = dsl.Text()
    topics = dsl.Nested(Topics)
    persons = dsl.Keyword(index='not_analyzed')
    facility = dsl.Nested(Facility)
    chronology = dsl.Nested(Chronology)
    geography = dsl.Nested(Geography)
    
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
    label = dsl.Keyword(store='no', index='not_analyzed')
    url = dsl.Keyword(store='no', index='not_analyzed')

class File(ESCollectionObject):
    """IMPORTANT: keep in sync with fields in repo_models/file.py
    """
    #title
    #description
    record_created = dsl.Date()
    record_lastmod = dsl.Date()
    external = dsl.Integer()
    sha256 = dsl.Keyword(index='not_analyzed')
    md5 = dsl.Keyword(index='not_analyzed')
    size = dsl.Long()
    basename_orig = dsl.Text()
    access_rel = dsl.Text()
    mimetype = dsl.Keyword(index='not_analyzed')
    public = dsl.Keyword(index='not_analyzed')
    rights = dsl.Keyword(index='not_analyzed')
    sort = dsl.Integer()
    thumb = dsl.Text()
    label = dsl.Text(copy_to="title")
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
        {'doctype':'repository', 'class':Repository},
        {'doctype':'organization', 'class':Organization},
        {'doctype':'collection', 'class':Collection},
        {'doctype':'entity', 'class':Entity},
        {'doctype':'segment', 'class':Entity},
        {'doctype':'file', 'class':File},
        {'doctype':'facet', 'class':Facet},
        {'doctype':'facetterm', 'class':FacetTerm},
        {'doctype':'narrator', 'class':Narrator},
    ],

    # classes that form the Repository structure
    'repository': [
        {'doctype':'repository', 'class':Repository},
        {'doctype':'organization', 'class':Organization},
        {'doctype':'collection', 'class':Collection},
        {'doctype':'entity', 'class':Entity},
        {'doctype':'segment', 'class':Entity},
        {'doctype':'file', 'class':File},
    ],

    # class that are part of collections
    'collection': [
        {'doctype':'collection', 'class':Collection},
        {'doctype':'entity', 'class':Entity},
        {'doctype':'segment', 'class':Entity},
        {'doctype':'file', 'class':File},
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
