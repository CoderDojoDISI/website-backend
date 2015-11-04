events_schema = {
    'title': {
        'type': 'string',
        'required': True,
        'maxlength': 100
    },
    'description': {
        'type': 'string',
        'required': True,
        'maxlength': 1000
    },
    'urls': {
        'type' : 'dict',
        'schema' : {
            'googleForm': {
                'type' : 'string'
            },
            'facebook': {
                'type' : 'string'
            }
        },
    },
    'date': {
        'type': 'string',
        'required': True
    }
}

events = {
    'item_url' : 'regex("\d*")',
    'schema': events_schema
}