mentors_schema = {
    'firstname': {
        'type': 'string',
        'required': True,
        'maxlength': 30
    },
    'lastname': {
        'type': 'string',
        'required': True,
        'maxlength': 30
    },
    'description' : {
        'type': 'string',
        'required': True,
        'maxlength': 1000
    },
    'roles': {
        'type': 'list',
        'schema': {
            'type': 'string',
            'maxlength': 50
        }
    },
    'img': {
        'type': 'media'
    }
}

mentors = {
    'item_url' : 'regex("\d*")',
    'schema': mentors_schema
}