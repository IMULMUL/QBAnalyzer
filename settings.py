__V__ = "2020.V.02.44"

defaultdb = {
    "dbname": "analyzer",
    "reportscoll": "reports",
    "filescoll": "files",
    "userscoll": "users",
    "alllogscoll": "alllogs",
    "taskfileslogscoll": "taskfileslogs",
    "taskdblogscoll": "taskdblogs"
}

json_settings = {
    "docker": {
        "mongo_settings_host": "mongodb",
        "mongo_settings": "mongodb://changeme_9620eh26sfvka017fx:changeme_0cx821ncf7qg17ahx3@mongodb:27017/?authSource=admin",
        "redis_settings": "redis://:changeme_26c845sfwbfi927234@analyzer_redis:6379/0",
        "function_timeout": 100,
        "analyzer_timeout": 120,
        "web_mongo": [{
            "ALIAS": "default",
            "DB": defaultdb["dbname"],
            "HOST": "mongodb://changeme_9620eh26sfvka017fx:changeme_0cx821ncf7qg17ahx3@mongodb:27017/analyzer?authSource=admin"
        }],
        "malware_folder": "/analyzer/folders/malware",
        "malware_output_folder": "/analyzer/folders/output",
        "logs_folder": "/analyzer/folders/logs",
        "db_folder": "/analyzer/folders/dbs"
    }
}

meta_users_settings = {
    'db_alias': 'default',
    'collection': defaultdb["userscoll"],
    'strict': False
}
meta_files_settings = {
    'db_alias': 'default',
    'collection': defaultdb["filescoll"],
    'strict': False
}
meta_reports_settings = {
    'db_alias': 'default',
    'collection': defaultdb["reportscoll"],
    'strict': False
}
meta_task_files_logs_settings = {
    'db_alias': 'default',
    'collection': defaultdb["taskfileslogscoll"],
    'strict': False
}
meta_task_logs_settings = {
    'db_alias': 'default',
    'collection': defaultdb["taskdblogscoll"],
    'strict': False
}
elastic_db = {
    u'host': u'elasticsearch',
    u'port': 9200
}

default_colors = {
    "mobile_malware_index": "yellow_color",
    "packers_index": "brown_color",
    "capabilities_index": "green_color",
    "antidebug_antivm_index": "light_blue_color",
    "exploit_kits_index": "cyan_color",
    "crypto_index": "lilac_color",
    "cve_rules_index": "orange_color",
    "malware_index": "red_color",
    "maldocs_index": "lavender_color",
    "webshells_index": "ochre_color",
    "email_index": "mauve_color"
}
