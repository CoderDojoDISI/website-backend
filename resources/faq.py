faq_schema = {
    'title': {
        'type': 'string',
        'required': True,
        'maxlength': 100
    },
    'description': {
        'type': 'string',
        'required': True,
        'maxlength': 600
    }
}

faq = {
    'item_url' : 'regex("\d*")',
    'schema': faq_schema
}
