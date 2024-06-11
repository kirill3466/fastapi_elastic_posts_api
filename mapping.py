MAPPING_FOR_INDEX = {
    "properties": {
        "username": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "content": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "date": {
            "type": "date"
        },
        "views": {
            "type": "integer"
        },
    }
}
