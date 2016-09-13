IDENTIFIERS = [
    
    # ------------------------------------------------------------------
    {
        'model': 'repository',
        'module': '',
        'class': 'DDR.models.Stub',
        'level': -2,
        'component': {
            'name': 'repo',
            'type': str,
            'valid': ['ddr'],
        },
        'parents': [],
        'parents_all': [],
        'children': ['organization'],
        'children_all': ['organization'],
        'templates': {
            'id': [
                '{repo}',
            ],
            'path': {
                'rel': [
                    '',
                ],
                'abs': [
                    '{basepath}/{repo}',
                ],
            },
            'url': {
                'editor': [
                    '/ui/{repo}',
                ],
                'public': [
                    '/{repo}',
                ],
            },
        },
        'patterns': {
            'id': [
                r'^(?P<repo>[\w]+)$',
            ],
            'path': [
                r'(?P<basepath>[\w/-]+)/(?P<repo>[\w]+)/repository.json$',
                r'(?P<basepath>[\w/-]+)/(?P<repo>[\w]+)$',
                r'^repository.json$',
            ],
            'url': [
                r'/ui/(?P<repo>[\w]+)$',
                r'^/(?P<repo>[\w]+)$',
            ],
        },
        'files': {
            'json': 'repository.json',
        },
    },
    
    # ------------------------------------------------------------------
    {
        'model': 'organization',
        'module': '',
        'class': 'DDR.models.Stub',
        'level': -1,
        'component': {
            'name': 'org',
            'type': str,
            'valid': [
                'densho', 'hmwf', 'jamsj', 'janm', 'jcch', 'manz', 'njpa',
                'one', 'pc', 'dev', 'test', 'testing',
            ],
        },
        'parents': [],
        'parents_all': ['repository'],
        'children': ['collection'],
        'children_all': ['collection'],
        'templates': {
            'id': [
                '{repo}-{org}',
            ],
            'path': {
                'rel': [
                    '',
                ],
                'abs': [
                    '{basepath}/{repo}-{org}',
                ],
            },
            'url': {
                'editor': [
                    '/ui/{repo}-{org}',
                ],
                'public': [
                    '/{repo}/{org}',
                ],
            },
        },
        'patterns': {
            'id': [
                r'^(?P<repo>[\w]+)-(?P<org>[\w]+)$'
            ],
            'path': [
                r'(?P<basepath>[\w/-]+)/(?P<repo>[\w]+)-(?P<org>[\w]+)$',
                r'^organization.json$',
            ],
            'url': [
                r'/ui/(?P<repo>[\w]+)-(?P<org>[\w]+)$',
                r'^/(?P<repo>[\w]+)/(?P<org>[\w]+)$',
            ],
        },
        'files': {
            'json': 'organization.json',
        },
    },
    
    # ------------------------------------------------------------------
    {
        'model': 'collection',
        'module': 'repo_models.collection',
        'class': 'DDR.models.Collection',
        'level': 0,
        'component': {
            'name': 'cid',
            'type': int,
            'valid': [],
        },
        'parents': [],
        'parents_all': ['organization'],
        'children': ['entity'],
        'children_all': ['entity'],
        'templates': {
            'id': [
                '{repo}-{org}-{cid}',
            ],
            'path': {
                'rel': [
                    '',
                ],
                'abs': [
                    '{basepath}/{repo}-{org}-{cid}',
                ],
            },
            'url': {
                'editor': [
                    '/ui/{repo}-{org}-{cid}',
                ],
                'public': [
                    '/{repo}/{org}/{cid}',
                ],
            },
        },
        'patterns': {
            'id': [
                r'^(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)$',
            ],
            'path': [
                r'(?P<basepath>[\w/-]+)/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)',
                r'^collection.json$',
            ],
            'url': [
                r'/ui/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)$',
                r'^/(?P<repo>[\w]+)/(?P<org>[\w]+)/(?P<cid>[\d]+)$',
            ],
        },
        'files': {
            'annex': '.git/annex',
            'changelog': 'changelog',
            'control': 'control',
            'ead': 'ead.xml',
            'files': 'files',
            'gitignore': '.gitignore',
            'git': '.git',
            'json': 'collection.json',
            'lock': 'lock',
        },
        'filename_regex': 'collection.json',
    },
    
    # ------------------------------------------------------------------
    {
        'model': 'entity',
        'module': 'repo_models.entity',
        'class': 'DDR.models.Entity',
        'level': 1,
        'component': {
            'name': 'eid',
            'type': int,
            'valid': [],
        },
        'parents': ['collection'],
        'parents_all': ['collection'],
        'children': ['segment', 'file'],
        'children_all': ['segment', 'file-role'],
        'templates': {
            'id': [
                '{repo}-{org}-{cid}-{eid}',
            ],
            'path': {
                'rel': [
                    'files/{repo}-{org}-{cid}-{eid}',
                ],
                'abs': [
                    '{basepath}/{repo}-{org}-{cid}/files/{repo}-{org}-{cid}-{eid}',
                ],
            },
            'url': {
                'editor': [
                    '/ui/{repo}-{org}-{cid}-{eid}',
                ],
                'public': [
                    '/{repo}/{org}/{cid}/{eid}',
                ],
            },
        },
        'patterns': {
            'id': [
                r'^(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)$',
            ],
            'path': [
                # ---------------------/collection-------/-----/entity
                r'(?P<basepath>[\w/-]+)/(?P<id0>[\w\d-]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)/entity.json',
                r'(?P<basepath>[\w/-]+)/(?P<id0>[\w\d-]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)',
                # ------/entity
                r'^files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)/entity.json$',
                r'^files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)$',
            ],
            'url': [
                # editor
                r'/ui/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)$',
                # public
                r'^/(?P<repo>[\w]+)/(?P<org>[\w]+)/(?P<cid>[\d]+)/(?P<eid>[\d]+)$',
            ],
        },
        'files': {
            'changelog': 'changelog',
            'control': 'control',
            'files': 'files',
            'json': 'entity.json',
            'lock': 'lock',
            'mets': 'mets.xml',
        },
        'filename_regex': 'entity.json',
    },
    
    # ------------------------------------------------------------------
    {
        'model': 'segment',
        'module': 'repo_models.segment',
        'class': 'DDR.models.Entity',
        'level': 2,
        'component': {
            'name': 'sid',
            'type': int,
            'valid': [],
        },
        'parents': ['entity'],
        'parents_all': ['entity'],
        'children': ['file'],
        'children_all': ['file-role'],
        'templates': {
            'id': [
                '{repo}-{org}-{cid}-{eid}-{sid}',
            ],
            'path': {
                'rel': [
                    'files/{repo}-{org}-{cid}-{eid}/files/{repo}-{org}-{cid}-{eid}-{sid}',
                ],
                'abs': [
                    '{basepath}/{repo}-{org}-{cid}/files/{repo}-{org}-{cid}-{eid}/files/{repo}-{org}-{cid}-{eid}-{sid}',
                ],
            },
            'url': {
                'editor': [
                    '/ui/{repo}-{org}-{cid}-{eid}-{sid}',
                ],
                'public': [
                    '/{repo}/{org}/{cid}/{eid}/{sid}',
                ],
            },
        },
        'patterns': {
            'id': [
                r'^(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<sid>[\d]+)$',
            ],
            'path': [
                # ---------------------/collection-------/-----/entity-----------/-----/segment
                r'(?P<basepath>[\w/-]+)/(?P<id0>[\w\d-]+)/files/(?P<id1>[\w\d-]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<sid>[\d]+)/entity.json$',
                r'(?P<basepath>[\w/-]+)/(?P<id0>[\w\d-]+)/files/(?P<id1>[\w\d-]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<sid>[\d]+)$',
                # ------/entity-----------/-----/segment
                r'^files/(?P<id0>[\w\d-]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<sid>[\d]+)/entity.json$',
                r'^files/(?P<id0>[\w\d-]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<sid>[\d]+)$',
            ],
            'url': [
                # editor
                r'/ui/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<sid>[\d]+)$',
                # public
                r'^/(?P<repo>[\w]+)/(?P<org>[\w]+)/(?P<cid>[\d]+)/(?P<eid>[\d]+)/(?P<sid>[\d]+)$',
            ],
        },
        'files': {
            'changelog': 'changelog',
            'control': 'control',
            'files': 'files',
            'json': 'entity.json',
            'lock': 'lock',
            'mets': 'mets.xml',
        },
        'filename_regex': 'entity.json',
    },
    
    # ------------------------------------------------------------------
    {
        'model': 'file-role',
        'module': '',
        'class': 'DDR.models.Stub',
        'level': 3,
        'component': {
            'name': 'role',
            'type': str,
            'valid': [
                'master',
                'mezzanine',
                'transcript',
                'gloss',
                'preservation',
                'administrative',
            ],
        },
        'parents': [],
        'parents_all': ['segment', 'entity'],
        'children': ['file'],
        'children_all': ['file'],
        'templates': {
            'id': [
                '{repo}-{org}-{cid}-{eid}-{sid}-{role}',
                '{repo}-{org}-{cid}-{eid}-{role}',
            ],
            'path': {
                'rel': [],
                'abs': [],
            },
            'url': {
                'editor': [
                    '/ui/{repo}-{org}-{cid}-{eid}-{sid}-{role}',
                    '/ui/{repo}-{org}-{cid}-{eid}-{role}',
                ],
                'public': [
                    '/{repo}/{org}/{cid}/{eid}/{sid}/{role}',
                    '/{repo}/{org}/{cid}/{eid}/{role}',
                ],
            },
        },
        'patterns': {
            'id': [
                r'^(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<sid>[\d]+)-(?P<role>[a-zA-Z]+)$',
                r'^(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<role>[a-zA-Z]+)$',
            ],
            'path': [
            ],
            'url': [
                # editor
                r'/ui/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<sid>[\d]+)-(?P<role>[a-zA-Z]+)$',
                r'/ui/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<role>[a-zA-Z]+)$',
                # public
                r'^/(?P<repo>[\w]+)/(?P<org>[\w]+)/(?P<cid>[\d]+)/(?P<eid>[\d]+)/(?P<sid>[\d]+)/(?P<role>[a-zA-Z]+)$',
                r'^/(?P<repo>[\w]+)/(?P<org>[\w]+)/(?P<cid>[\d]+)/(?P<eid>[\d]+)/(?P<role>[a-zA-Z]+)$',
            ],
        },
        'files': {
        },
    },

    # ------------------------------------------------------------------
    {
        'model': 'file',
        'module': 'repo_models.files',
        'class': 'DDR.models.File',
        'level': 4,
        'component': {
            'name': 'sha1',
            'type': str,
            'valid': [],
        },
        'parents': ['segment', 'entity'],
        'parents_all': ['file-role'],
        'children': [],
        'children_all': [],
        'templates': {
            'id': [
                '{repo}-{org}-{cid}-{eid}-{sid}-{role}-{sha1}',
                '{repo}-{org}-{cid}-{eid}-{role}-{sha1}',
            ],
            'path': {
                'rel': [
                    # ----/entity------------------/-----/segment-----------------------/-----/file
                    'files/{repo}-{org}-{cid}-{eid}/files/{repo}-{org}-{cid}-{eid}-{sid}/files/{repo}-{org}-{cid}-{eid}-{sid}-{role}-{sha1}',
                    # ----/entity------------------/-----/file
                    'files/{repo}-{org}-{cid}-{eid}/files/{repo}-{org}-{cid}-{eid}-{role}-{sha1}',
                ],
                'abs': [
                    # ---------/collection--------/-----/entity------------------/-----/segment-----------------------/-----/file
                    '{basepath}/{repo}-{org}-{cid}/files/{repo}-{org}-{cid}-{eid}/files/{repo}-{org}-{cid}-{eid}-{sid}/files/{repo}-{org}-{cid}-{eid}-{sid}-{role}-{sha1}',
                    # ---------/collection--------/-----/entity------------------/-----/file
                    '{basepath}/{repo}-{org}-{cid}/files/{repo}-{org}-{cid}-{eid}/files/{repo}-{org}-{cid}-{eid}-{role}-{sha1}',
                ],
            },
            'url': {
                'editor': [
                    '/ui/{repo}-{org}-{cid}-{eid}-{sid}-{role}-{sha1}',
                    '/ui/{repo}-{org}-{cid}-{eid}-{role}-{sha1}',
                ],
                'public': [
                    '/{repo}/{org}/{cid}/{eid}/{sid}/{role}/{sha1}',
                    '/{repo}/{org}/{cid}/{eid}/{role}/{sha1}',
                ],
            },
        },
        'patterns': {
            'id': [
                r'^(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<sid>[\d]+)-(?P<role>[a-zA-Z]+)-(?P<sha1>[\w]+)$',
                r'^(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<role>[a-zA-Z]+)-(?P<sha1>[\w]+)$',
            ],
            'path': [
                # file-abs
                # ---------------------/collection-------/-----/entity-----------/-----/segment----------/-----/file
                r'(?P<basepath>[\w/-]+)/(?P<id0>[\w\d-]+)/files/(?P<id1>[\w\d-]+)/files/(?P<id2>[\w\d-]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<sid>[\d]+)-(?P<role>[a-zA-Z]+)-(?P<sha1>[\w\d]+)\.(?P<ext>[\w]+)$',
                r'(?P<basepath>[\w/-]+)/(?P<id0>[\w\d-]+)/files/(?P<id1>[\w\d-]+)/files/(?P<id2>[\w\d-]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<sid>[\d]+)-(?P<role>[a-zA-Z]+)-(?P<sha1>[\w\d]+)\.json$',
                r'(?P<basepath>[\w/-]+)/(?P<id0>[\w\d-]+)/files/(?P<id1>[\w\d-]+)/files/(?P<id2>[\w\d-]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<sid>[\d]+)-(?P<role>[a-zA-Z]+)-(?P<sha1>[\w\d]+)$',
                # ---------------------/collection-------/-----/entity-----------/-----/file
                r'(?P<basepath>[\w/-]+)/(?P<id0>[\w\d-]+)/files/(?P<id1>[\w\d-]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<role>[a-zA-Z]+)-(?P<sha1>[\w\d]+)\.(?P<ext>[\w]+)$',
                r'(?P<basepath>[\w/-]+)/(?P<id0>[\w\d-]+)/files/(?P<id1>[\w\d-]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<role>[a-zA-Z]+)-(?P<sha1>[\w\d]+)\.json$',
                r'(?P<basepath>[\w/-]+)/(?P<id0>[\w\d-]+)/files/(?P<id1>[\w\d-]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<role>[a-zA-Z]+)-(?P<sha1>[\w\d]+)$',
                # file-rel
                # ------/enity------------/-----/segment----------------/file
                r'^files/(?P<id0>[\w\d-]+)/files/(?P<id1>[\w\d-]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<sid>[\d]+)-(?P<role>[a-zA-Z]+)-(?P<sha1>[\w\d]+)\.(?P<ext>[\w]+)$',
                r'^files/(?P<id0>[\w\d-]+)/files/(?P<id1>[\w\d-]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<sid>[\d]+)-(?P<role>[a-zA-Z]+)-(?P<sha1>[\w\d]+)\.json$',
                r'^files/(?P<id0>[\w\d-]+)/files/(?P<id1>[\w\d-]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<sid>[\d]+)-(?P<role>[a-zA-Z]+)-(?P<sha1>[\w\d]+)$',
                # ------/enity------------/-----/file
                r'^files/(?P<id0>[\w\d-]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<role>[a-zA-Z]+)-(?P<sha1>[\w\d]+)\.(?P<ext>[\w]+)$',
                r'^files/(?P<id0>[\w\d-]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<role>[a-zA-Z]+)-(?P<sha1>[\w\d]+)\.json$',
                r'^files/(?P<id0>[\w\d-]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<role>[a-zA-Z]+)-(?P<sha1>[\w\d]+)$',
            ],
            'url': [
                # editor
                r'/ui/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<sid>[\d]+)-(?P<role>[a-zA-Z]+)-(?P<sha1>[\w]+)$',
                r'/ui/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<role>[a-zA-Z]+)-(?P<sha1>[\w]+)$',
                # public
                r'^/(?P<repo>[\w]+)/(?P<org>[\w]+)/(?P<cid>[\d]+)/(?P<eid>[\d]+)/(?P<sid>[\d]+)/(?P<role>[a-zA-Z]+)/(?P<sha1>[\w]+)$',
                r'^/(?P<repo>[\w]+)/(?P<org>[\w]+)/(?P<cid>[\d]+)/(?P<eid>[\d]+)/(?P<role>[a-zA-Z]+)/(?P<sha1>[\w]+)$',
            ],
        },
        'files': {
            'access': '{id}-a.jpg',
            'json': '{id}.json',
        },
        'filename_regex': '-([\d]+)-([\w]+)-([\w\d]+).json',
    },
]
