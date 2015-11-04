faq_schema = {
    'title': {
        'type': 'string',
        'required': True,
        'maxlength': 200
    },
    'description': {
        'type': 'string',
        'required': True,
        'maxlength': 2000
    }
}

faq = {
    'item_url' : 'regex("\d*")',
    'schema': faq_schema
}
