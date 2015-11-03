events_schema = {
    'title': {
        'type': 'string',
        'required': True,
        'maxlength': 100
    },
    'description': {
        'type': 'string',
        'required': True,
        'maxlength': 600
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
    }
}

events = {
    'item_url' : 'regex("\d*")',
    'schema': events_schema
}