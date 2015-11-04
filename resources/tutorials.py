tutorials_schema = {
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
    'type': {
        'type': 'string',
        'required': True,
        'maxlength': 100
    }
}

tutorials = {
    'item_url': 'regex("\d*")',
    'schema': tutorials_schema
}
