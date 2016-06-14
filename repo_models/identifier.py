IDENTIFIERS = [
    
    # ------------------------------------------------------------------
    {
        'model': 'repository',
        'class': 'DDR.models.Stub',
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
        'class': 'DDR.models.Stub',
        'component': {
            'name': 'org',
            'type': str,
            'valid': [
                'densho', 'hmwf', 'jamsj', 'janm', 'jcch', 'njpa', 'one', 'pc',
                'dev', 'test', 'testing',
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
        'class': 'DDR.models.Collection',
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
    },
    
    # ------------------------------------------------------------------
    {
        'model': 'entity',
        'class': 'DDR.models.Entity',
        'component': {
            'name': 'eid',
            'type': int,
            'valid': [],
        },
        'parents': ['collection'],
        'parents_all': ['collection'],
        'children': ['file'],
        'children_all': ['file-role'],
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
                r'(?P<basepath>[\w/-]+)/(?P<repo0>[\w]+)-(?P<org0>[\w]+)-(?P<cid0>[\d]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)',
                r'^files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)$',
            ],
            'url': [
                r'/ui/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)$',
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
    },
    
    # ------------------------------------------------------------------
    {
        'model': 'segment',
        'class': 'DDR.models.Entity',
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
                    'files/{repo}-{org}-{cid}-{eid}-{sid}',
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
                r'(?P<basepath>[\w/-]+)/(?P<id0>[\w\d-]+)/files/(?P<id1>[\w\d-]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<sid>[\d]+)',
                # ------/entity-----------/-----/segment
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
    },
    
    # ------------------------------------------------------------------
    {
        'model': 'file-role',
        'class': 'DDR.models.Stub',
        'component': {
            'name': 'role',
            'type': str,
            'valid': [
                'master', 'mezzanine',
            ],
        },
        'parents': [],
        'parents_all': ['entity'],
        'children': ['file'],
        'children_all': ['file'],
        'templates': {
            'id': [
                '{repo}-{org}-{cid}-{eid}-{role}',
            ],
            'path': {
                'rel': None,
                'abs': None,
            },
            'url': {
                'editor': [
                    '/ui/{repo}-{org}-{cid}-{eid}-{role}',
                ],
                'public': [
                    '/{repo}/{org}/{cid}/{eid}/{role}',
                ],
            },
        },
        'patterns': {
            'id': [
                r'^(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<role>[\w]+)$',
            ],
            'path': [
            ],
            'url': [
                r'/ui/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<role>[\w]+)$',
                r'^/(?P<repo>[\w]+)/(?P<org>[\w]+)/(?P<cid>[\d]+)/(?P<eid>[\d]+)/(?P<role>[\w]+)$',
            ],
        },
        'files': {
        },
    },

    # ------------------------------------------------------------------
    {
        'model': 'file',
        'class': 'DDR.models.File',
        'component': {
            'name': 'sha1',
            'type': str,
            'valid': [],
        },
        'parents': ['entity'],
        'parents_all': ['file-role'],
        'children': [],
        'children_all': [],
        'templates': {
            'id': [
                '{repo}-{org}-{cid}-{eid}-{role}-{sha1}',
            ],
            'path': {
                'rel': [
                    'files/{repo}-{org}-{cid}-{eid}/files/{repo}-{org}-{cid}-{eid}-{role}-{sha1}',
                ],
                'abs': [
                    '{basepath}/{repo}-{org}-{cid}/files/{repo}-{org}-{cid}-{eid}/files/{repo}-{org}-{cid}-{eid}-{role}-{sha1}',
                ],
            },
            'url': {
                'editor': [
                    '/ui/{repo}-{org}-{cid}-{eid}-{role}-{sha1}',
                ],
                'public': [
                    '/{repo}/{org}/{cid}/{eid}/{role}/{sha1}',
                ],
            },
        },
        'patterns': {
            'id': [
                r'^(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<role>[\w]+)-(?P<sha1>[\w]+)$',
            ],
            'path': [
                # file-abs
                r'(?P<basepath>[\w/-]+)/(?P<repo0>[\w]+)-(?P<org0>[\w]+)-(?P<cid0>[\d]+)/files/(?P<repo1>[\w]+)-(?P<org1>[\w]+)-(?P<cid1>[\d]+)-(?P<eid1>[\d]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<role>[\w]+)-(?P<sha1>[\w\d]+)\.(?P<ext>[\w]+)$',
                r'(?P<basepath>[\w/-]+)/(?P<repo0>[\w]+)-(?P<org0>[\w]+)-(?P<cid0>[\d]+)/files/(?P<repo1>[\w]+)-(?P<org1>[\w]+)-(?P<cid1>[\d]+)-(?P<eid1>[\d]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<role>[\w]+)-(?P<sha1>[\w\d]+)\.json$',
                r'(?P<basepath>[\w/-]+)/(?P<repo0>[\w]+)-(?P<org0>[\w]+)-(?P<cid0>[\d]+)/files/(?P<repo1>[\w]+)-(?P<org1>[\w]+)-(?P<cid1>[\d]+)-(?P<eid1>[\d]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<role>[\w]+)-(?P<sha1>[\w\d]+)$',
                # file-rel
                r'^files/(?P<repo0>[\w]+)-(?P<org0>[\w]+)-(?P<cid0>[\d]+)-(?P<eid0>[\d]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<role>[\w]+)-(?P<sha1>[\w\d]+)\.(?P<ext>[\w]+)$',
                r'^files/(?P<repo0>[\w]+)-(?P<org0>[\w]+)-(?P<cid0>[\d]+)-(?P<eid0>[\d]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<role>[\w]+)-(?P<sha1>[\w\d]+)\.json$',
                r'^files/(?P<repo0>[\w]+)-(?P<org0>[\w]+)-(?P<cid0>[\d]+)-(?P<eid0>[\d]+)/files/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<role>[\w]+)-(?P<sha1>[\w\d]+)$',
            ],
            'url': [
                r'/ui/(?P<repo>[\w]+)-(?P<org>[\w]+)-(?P<cid>[\d]+)-(?P<eid>[\d]+)-(?P<role>[\w]+)-(?P<sha1>[\w]+)$',
                r'^/(?P<repo>[\w]+)/(?P<org>[\w]+)/(?P<cid>[\d]+)/(?P<eid>[\d]+)/(?P<role>[\w]+)/(?P<sha1>[\w]+)$',
            ],
        },
        'files': {
            'access': '{id}-a.jpg',
            'json': '{id}.json',
        },
    },
    
]
