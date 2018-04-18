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


# superclasses

class ESObjectFields(dsl.DocType):
    """List of fields in order for each class
    """
    model = dsl.String(index='not_analyzed')
    fields = dsl.String(index='not_analyzed')
    
    class Meta:
        doc_type = 'esobjectfields'

class ESLineage(dsl.InnerObjectWrapper): pass

class ESObject(dsl.DocType):
    """Base for Elasticsearch-DSL versions of model classes
    
    TODO This belongs in DDR.models.common but putting it there
    causes an import loop or something.
    """
    id = dsl.String(index='not_analyzed')
    model = dsl.String(index='not_analyzed')
    parent_id = dsl.String(index='not_analyzed')
    collection_id = dsl.String(index='not_analyzed')
    organization_id = dsl.String(index='not_analyzed')
    signature_id = dsl.String(index='not_analyzed')
    #
    links_html = dsl.String(index='not_analyzed')
    links_json = dsl.String(index='not_analyzed')
    links_img = dsl.String(index='not_analyzed')
    links_thumb = dsl.String(index='not_analyzed')
    links_parent = dsl.String(index='not_analyzed')
    links_children = dsl.String(index='not_analyzed')
    links_children_objects = dsl.String(index='not_analyzed')
    links_children_files = dsl.String(index='not_analyzed')
    lineage = dsl.Nested(
        doc_class=ESLineage,
        properties={
            'id': dsl.String(index='not_analyzed'),
            'model': dsl.String(index='not_analyzed'),
            'idpart': dsl.String(index='not_analyzed'),
            'label': dsl.String(index='not_analyzed'),
        }
    )
    url = dsl.String(index='not_analyzed')
    #
    repo = dsl.String(index='not_analyzed')
    org = dsl.String(index='not_analyzed')
    cid = dsl.Long()
    eid = dsl.Long()
    sid = dsl.Long()
    role = dsl.String(index='not_analyzed')
    sha1 = dsl.String(index='not_analyzed')
    #
    title = dsl.String()
    description = dsl.String()
    
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
    id = dsl.String(index='not_analyzed')
    links_html = dsl.String(index='not_analyzed')
    links_json = dsl.String(index='not_analyzed')
    links_children = dsl.String(index='not_analyzed')
    title = dsl.String()
    description = dsl.String()
    
    class Meta:
        doc_type = 'facet'


class Elinks(dsl.InnerObjectWrapper): pass
class Location(dsl.InnerObjectWrapper): pass
class Geopoint(dsl.InnerObjectWrapper): pass

class FacetTerm(dsl.DocType):
    id = dsl.String(index='not_analyzed')
    facet = dsl.String(index='not_analyzed')
    term_id = dsl.String(index='not_analyzed')
    links_html = dsl.String(index='not_analyzed')
    links_json = dsl.String(index='not_analyzed')
    links_children = dsl.String(index='not_analyzed')
    title = dsl.String()
    description = dsl.String()
    # topics
    path = dsl.String()
    parent_id = dsl.String(index='not_analyzed')
    ancestors = dsl.Long()
    siblings = dsl.Long()
    children = dsl.Long()
    weight = dsl.Long()
    encyc_urls = dsl.String()
    # facility
    type = dsl.String()
    elinks = dsl.Nested(
        doc_class=Elinks,
        properties={
            'label': dsl.String(),
            'url': dsl.String(),
        }
    )
    location_geopoint = dsl.Nested(
        doc_class=Location,
        properties={
            'geopoint': dsl.Nested(
                doc_class=Geopoint,
                properties={
                    'lat': dsl.Double(),
                    'lng': dsl.Double(),
                }
            ),
            'label': dsl.String(),
        }
    )
    
    class Meta:
        doc_type = 'facetterm'


class Narrator(ESObject):
    #id
    #title
    nr_id = dsl.String(index='not_analyzed')
    created = dsl.Date(index='not_analyzed', format="yyyy-MM-dd'T'HH:mm:ss")
    modified = dsl.Date(index='not_analyzed', format="yyyy-MM-dd'T'HH:mm:ss")
    b_date = dsl.Date(index='not_analyzed', format="yyyy-MM-dd'T'HH:mm:ss")
    d_date = dsl.Date(index='not_analyzed', format="yyyy-MM-dd'T'HH:mm:ss")
    last_name = dsl.String()
    first_name = dsl.String()
    middle_name = dsl.String()
    display_name = dsl.String(index="no", copy_to="title")
    bio = dsl.String(index="no", copy_to="description")
    description = dsl.String()
    gender = dsl.String()
    generation = dsl.String()
    ethnicity = dsl.String()
    nationality = dsl.String()
    religion = dsl.String()
    birth_location = dsl.String()
    notes = dsl.String(index="no", copy_to="notes_private")
    nickname = dsl.String()
    image_url = dsl.String()
    
    class Meta:
        doc_type = 'narrator'


class Repository(ESRepositoryObject):
    class Meta:
        doc_type= 'repository'


class Organization(ESRepositoryObject):
    class Meta:
        doc_type= 'organization'


class Creators(dsl.InnerObjectWrapper): pass

class Collection(ESObject):
    """IMPORTANT: keep in sync with fields in repo_models/collections.py
    """
    #title
    #description
    record_created = dsl.Date()
    record_lastmod = dsl.Date()
    status = dsl.String(index='not_analyzed')
    public = dsl.String(index='not_analyzed')
    unitdateinclusive = dsl.String()
    unitdatebulk = dsl.String()
    creators = dsl.Nested(
        doc_class=Creators,
        properties={
            'namepart': dsl.String(index='not_analyzed'),
            'id': dsl.Integer(index='not_analyzed'),
            'role': dsl.String(index='not_analyzed'),
        }
    )
    extent = dsl.String()
    language = dsl.String(index='not_analyzed')
    contributor = dsl.String(index='not_analyzed')
    description = dsl.String()
    physloc = dsl.String()
    acqinfo = dsl.String()
    custodhist = dsl.String()
    accruals = dsl.String()
    processinfo = dsl.String()
    rights = dsl.String(index='not_analyzed')
    accessrestrict = dsl.String()
    userrestrict = dsl.String()
    prefercite = dsl.String()
    bioghist = dsl.String()
    scopecontent = dsl.String()
    relatedmaterial = dsl.String()
    separatedmaterial = dsl.String()
    
    class Meta:
        doc_type= 'collection'


class Creators(dsl.InnerObjectWrapper): pass
class Topics(dsl.InnerObjectWrapper): pass
class Facility(dsl.InnerObjectWrapper): pass
class Chronology(dsl.InnerObjectWrapper): pass
class Geography(dsl.InnerObjectWrapper): pass

class Entity(ESCollectionObject):
    """IMPORTANT: keep in sync with fields in repo_models/entity.py
    """
    #title
    #description
    record_created = dsl.Date()
    record_lastmod = dsl.Date()
    status = dsl.String(index='not_analyzed')
    sort = dsl.Integer()
    creation = dsl.String()
    location = dsl.String(index='not_analyzed')
    creators = dsl.Nested(
        doc_class=Creators,
        properties={
            'namepart': dsl.String(index='not_analyzed'),
            'id': dsl.Integer(index='not_analyzed'),
            'role': dsl.String(index='not_analyzed'),
        }
    )
    language = dsl.String(index='not_analyzed')
    genre = dsl.String(index='not_analyzed')
    format = dsl.String(index='not_analyzed')
    extent = dsl.String()
    contributor = dsl.String(index='not_analyzed')
    alternate_id = dsl.String()
    digitize_person = dsl.String()
    digitize_organization = dsl.String(index='not_analyzed')
    digitize_date = dsl.String(index='not_analyzed')
    credit = dsl.String()
    rights = dsl.String(index='not_analyzed')
    rights_statement = dsl.String()
    topics = dsl.Nested(
        doc_class=Topics,
        properties={
            'id': dsl.String(index='not_analyzed'),
            'term': dsl.String(index='not_analyzed'),
        }
    )
    persons = dsl.String(index='not_analyzed')
    facility = dsl.Nested(
        doc_class=Facility,
        properties={
            'id': dsl.String(index='not_analyzed'),
            'term': dsl.String(index='not_analyzed'),
        }
    )
    chronology = dsl.Nested(
        doc_class=Chronology,
        properties={
            'startdate': dsl.String(index='not_analyzed'),
            'enddate': dsl.String(index='not_analyzed'),
            'term': dsl.String(index='not_analyzed'),
        }
    )
    geography = dsl.Nested(
        doc_class=Geography,
        properties={
            'id': dsl.String(index='not_analyzed'),
            'geo_lat': dsl.String(index='not_analyzed'),
            'geo_lng': dsl.String(index='not_analyzed'),
            'term': dsl.String(index='not_analyzed'),
        }
    )
    
    class Meta:
        doc_type= 'entity'


class ExternalUrls(dsl.InnerObjectWrapper): pass

class File(ESCollectionObject):
    """IMPORTANT: keep in sync with fields in repo_models/file.py
    """
    #title
    #description
    record_created = dsl.Date()
    record_lastmod = dsl.Date()
    external = dsl.Integer()
    sha256 = dsl.String(index='not_analyzed')
    md5 = dsl.String(index='not_analyzed')
    size = dsl.Long()
    basename_orig = dsl.String()
    access_rel = dsl.String()
    mimetype = dsl.String(index='not_analyzed')
    public = dsl.String(index='not_analyzed')
    rights = dsl.String(index='not_analyzed')
    sort = dsl.Integer()
    thumb = dsl.String()
    label = dsl.String(copy_to="title")
    digitize_person = dsl.String()
    external_urls = dsl.Nested(
        doc_class=ExternalUrls,
        properties={
            'label': dsl.String(store='no', index='not_analyzed'),
            'url': dsl.String(store='no', index='not_analyzed'),
        }
    )
    links = dsl.String()
    
    class Meta:
        doc_type= 'file'


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
