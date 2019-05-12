from pprint import pprint
import math
import json
solutions_data = [{'solutionID': 1, 'descp': ['muliple', 'configurations', 'checked', 'understand', 'push', 'notification', 'reached', 'ios', 'device', 'even', 'though', 'status', 'submittedfirst', 'check', 'whether', 'user', 'configured', 'bundle', 'identifier', 'push', 'certificate', 'based', 'bundle', 'identifier', 'needs', 'configured', 'kms', 'consolein', 'application', 'find', 'bundle', 'identifier', 'provision', 'profileif', 'step', 'correct', 'need', 'confirm', 'whether', 'used', 'correct', 'profile', 'building', 'application', 'xcode', 'using', 'developer', 'certificate', 'use', 'developer', 'profile', 'distribution', 'certificate', 'user', 'build', 'application', 'using', 'distribution', 'profileif', 'step', 'correct', 'need', 'verify', 'using', 'mobile', 'sim', 'data', 'instead', 'using', 'corporate', 'wifi', 'sometime', 'corporate', 'wifi', 'block', 'push', 'notification', 'rule', 'wifi', 'network', 'restrictionsif', 'still', 'receiving', 'push', 'notification', 'need', 'recreate', 'profile', 'certificate', 'need', 'verify', 'sending', 'notificationsplease', 'follow', 'link', 'create', 'profile', 'push', 'certificates']}, {'solutionID': 2, 'descp': ['would', '1', 'reason', 'showing', 'status', 'submitted', 'notification', 'reached', 'android', 'device', 'ie', 'fire', 'wall', 'restrictions', 'slow', 'network', 'internet', 'connectivity', 'issues', 'white', 'list', 'domains', 'mentioned', 'corporate', 'fire', 'wall', 'settings', 'link', 'httpdocskonycomkonylibrarymessagingkmsconsoleinstallermanualguidewindowsdefaulthtmprerequisiteshtm3ftocpath3d4']}, {'solutionID': 3, 'descp': ['see', 'message', 'status', 'rejected', 'kms', 'console', 'hover', 'browser', 'message', 'see', 'popup', 'message', 'like', 'registered', 'mismatch', 'sender', 'idnot', 'registered', 'even', 'though', 'subscription', 'status', 'cloud', 'status', 'active', 'moment', 'sure', 'suppose', 'uninstall', 'application', 'device', 'right', 'away', 'subscription', 'status', '’', 'become', 'inactive', 'right', 'away', 'status', 'fetched', 'kms', '24', 'hours', 'connecting', 'corresponding', 'cloudgcmfcm', 'apns', 'kms', 'still', 'show', 'active', 'device', 'try', 'send', 'push', 'kms', 'deliver', 'message', 'gcm', 'apns', 'reject', 'saying', 'device', 'registered', 'device', 'inorder', 'resolve', 'please', 'register', 'application', 'followed', 'subscriptionmismatch', 'sender', 'idit', 'means', 'gcm', 'fcm', 'server', 'key', 'configured', 'kms', 'console', 'application', 'google', 'project', 'project', 'whose', 'sender', 'id', 'used', 'registration', 'google', 'cloud', 'giving', 'appropriate', 'server', 'key', 'would', 'resolve', 'issuesuppose', 'push', 'message', 'ios', 'device', 'rejected', 'apns', 'means', 'restrictions', 'firewall', 'level', 'like', 'proxy', 'configurations', 'please', 'check', 'whether', 'firewall', 'settings', 'enabled', 'notplease', 'note', 'firewall', 'proxy', 'enable', 'socks', 'protocol', 'proxy', 'server', 'else', 'apple', '’', 'accept', 'requests', 'restriction', 'apple', 'itselfcouple', 'status', 'meaning', '1rejected', 'means', 'kms', 'requested', 'corresponding', 'push', 'manufacturer', 'clouds', 'like', 'gcmfcmapnswns', 'mpns', 'rejected', 'requests', 'due', 'variant', 'reasons', '2cancelled', 'kony', 'mobilefabric', 'messaging', 'cancelled', 'sent', 'message', 'reached', 'respective', 'cloud', 'designated', 'platform3undelivered', 'kony', 'mobilefabric', 'messaging', 'tried', 'sending', 'message', 'undelivered', 'respective', 'cloud', 'designated', 'platform', 'due', 'possible', 'reasons', 'example', 'gcm', 'key', 'missing', 'google', 'cloudnotattempted', 'kony', 'messaging', 'try', 'sending', 'message', 'subscribers', 'chosen', 'see', 'scheduled', 'push', 'messages', 'users', 'unsubscribe', 'admin', 'scheduled', 'push', 'messages']}, {'solutionID': 4, 'descp': ['1401', 'times', 'accessed', 'kms', 'api', 'get', 'authentication', 'failed', 'response', 'body', 'status', 'code', '401', 'means', 'passing', 'authorization', 'data', 'headers', 'probably', 'tokens', 'authentication', 'kms', 'two', 'types', '1basic', 'authdatabase', 'authentication', '2mbaas', 'authkony', 'rest', 'service', 'authenticationto', 'understand', 'authentication', 'use', 'please', 'follow', 'linkhttpdocskonycomkonylibrarymessagingengagementapiguidecontentapisforkonymessagingservicesauthenticationapihtmon2']}, {'solutionID': 5, 'descp': ['1403', 'see', 'kms', 'rest', 'api', '’', 'failing', '403', 'means', 'request', 'kms', 'came', 'another', 'domain', 'kms', 'default', 'kms', '’', 'allow', 'cross', 'domain', 'requests', 'order', 'resolve', 'proceed', 'follow', 'steps', 'ago', 'kms', 'console', 'bselect', 'configurationgeneral', 'cunder', 'security', 'section', 'find', '‘', 'allow', 'cross', 'domains', 'access', '’', 'check', 'box',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         'dbeneath', 'check', 'box', 'text', 'box', 'fill', 'character', '‘', '’', 'save']}, {'solutionID': 6, 'descp': ['1404', 'means', 'rest', 'api', 'using', 'exists', 'kms', 'web', 'directory', 'go', 'api', 'help', 'section', 'kms', 'console', 'check', 'rest', 'api', '’', 'provided', 'kms']}, {'solutionID': 7, 'descp': ['1android', 'go', 'kms', 'app\uf0e0settings\uf0e0android', 'configured', 'gcm', 'fcm', 'project', 'server', 'key', 'gcmfcm', 'authorization', 'key', 'cliked', 'test', 'connectivity', 'getting', '“', 'android', 'gcmfcm', 'cloud', 'connection', 'validation', 'failedthe', 'first', 'reason', 'could', 'restrictions', 'firewall', 'please', 'make', 'sure', 'access', '‘', 'fcmgoogleapiscom', '’', 'enabled', 'firewall', 'moreover', 'firewall', 'settings', 'mentioned', 'link', 'belowhttpdocskonycomkonylibrarymessagingkmsconsoleinstallermanualguidewindowsdefaulthtmprerequisiteshtm3ftocpath3d4the', 'second', 'reason', 'could', 'given', 'gcm', 'server', 'key', 'appropriate', 'cross', 'verify', 'given', 'server', 'key', 'google', 'developer', 'project', 'server', 'key']}, {'solutionID': 8, 'descp': ['1ios', 'go', 'kms', 'app', '\uf0e0settings', '\uf0e0apple', 'uploaded', 'p12', 'certificate', 'click', '“', 'test', 'connectivity', 'cloud', '”', 'get', '“', 'apple', 'cloud', 'connection', 'test', 'failed', '”', 'first', 'reason', 'would', 'may', 'due', 'uploading', 'development', 'production', 'section', 'uploading', 'production', 'certificate', 'development', 'section', 'shown', 'belowthere', 'may', 'firewall', 'restrictions', 'access', 'apple', 'cloud', 'ensure', 'settings', 'link', 'enabled', 'foremost', 'thing', 'firewall', 'proxy', 'server', 'must', 'enable', 'socks', 'protocol', 'proxy', 'server', '’', 'restriction', 'apple', 'httpdocskonycomkonylibrarymessagingkmsconsoleinstallermanualguidewindowsdefaulthtmprerequisiteshtm3ftocpath3dif', 'proxy', 'enabled', 'configure', 'details', 'configureresourceproperties', 'kpnswebinfclasses', 'web', 'directory', 'proxy', 'key', '’', 'commeted', 'default', 'uncomment', 'fill', 'values', 'restart', 'server', 'sample', 'configresourceproperties', 'file', 'shown', 'httpdocskonycomkonylibrarymessagingkmsconsoleinstallermanualguidewindowsdefaulthtmsetupkpnshtmconfigresourcepro3ftocpath3dinstall2520and2520configure2520engagement2520services7csetup2520engagement2520services7c1if', 'issue', 'still', 'exists', 'please', 'check', 'configureresourceproperties', 'kpnswebinfclasses', 'whether', 'commented', 'property', 'still', 'exists', 'kpnsdb', 'database', 'schema', 'corresponding', 'database', 'table', '“', 'configresources', '”', 'commented', 'values', 'still', 'exists', 'database', 'try', 'restarting', 'server', 'still', 'exists', 'manually', 'delete', 'entire', 'record', 'table', 'would', 'resolve', 'issue', 'commands', 'check', 'connectivity', 'apple', 'cloud1window', 'servertracert', '2linux', 'servertraceroute']}, {'solutionID': 9, 'descp': ['android', 'giving', 'workarounds', 'issue', 'already', 'taken', 'l3', 'brain', 'storm', 'people', 'workarounds', 'given', 'sme', 'validating', 'user', 'environment', 'else', 'would', 'end', 'issues']}, {'solutionID': 10, 'descp': ['duplicate', 'messages', 'received', 'ios', 'devices', '1', 'case', 'ie', 'scheduled', 'messages', 'campaigns', 'bulk', 'push', 'csv', 'using', 'bulk', 'push', 'apibulk', 'push', 'push', 'entries', 'reciprocated', 'csv', 'file', 'kms', 'fetch', 'entire', 'list', 'create', 'entries', '‘', 'messageentry', '’', 'table', 'pick', 'entries', 'table', 'push', 'corresponding', 'push', 'cloudsgcmapns…etc', 'average', 'frequency', '50', '60', 'messagessec', 'duplicate', 'entries', 'csv', 'file', 'high', 'probability', 'device', 'receive', 'back', 'back', 'messages', 'interval', '1', 'second', 'even', 'less', 'make', 'sure', 'sending', 'message', 'device', 'multiple', 'times', 'csv', 'filescheduled', 'messages', 'campaigns', 'scheduled', 'campaign', 'kms', 'first', 'fetch', 'subscribers', 'fall', 'constraints', 'mentioned', 'campaign', 'create', 'message', 'entries', 'subscribers', '‘', 'messageentry', '’', 'table', 'entries', 'table', 'unique', 'message', 'id', 'column', '‘', 'id', '’', 'duplicate', 'push', 'message', 'received', 'device', 'please', 'follow', 'steps', '1', 'kms', 'consolesubscribers', 'page', 'get', '‘', 'ksid', '”', 'device', 'registered', 'kms', 'app', '22go', '‘', 'messageentry', '’', 'table', 'run', 'sql', 'query', '‘', 'user', 'defined', 'message', '’', 'retrieved', '‘', 'ksid', '’', 'select', 'messagerequest', 'message', '’', 'message', '’', 'subscription', '’', 'ksid', '’', '3', 'query', 'definitely', '1', 'record', 'means', 'configured', 'duplicate', 'messages', 'want', 'counter', 'check', 'see', 'values', '‘', 'starttimestamp', '’', 'value', 'result', 'records', 'would', 'sure']}]


def calculate_tf_value(tokens_array):
    visited_words = []
    word_tf = {}
    total_word_count = len(tokens_array)

    for word in tokens_array:
        if word not in visited_words:
            w_count = tokens_array.count(word)
            word_tf[word] = w_count / total_word_count
            visited_words.append(word)

    return word_tf

def calculate_idf_value(tokens_array, data, word_to_doc):
    word_count = 0
    word_idf = {}
    for word in tokens_array:
        if word not in list(word_to_doc.keys()):
            for sol in data:
                if word in sol['descp']:
                    word_count = word_count + 1
            word_to_doc[word] = word_count
        
        word_idf[word] = math.log(word_to_doc[word]) / len(data)
    
    return word_idf


def calculate_tf_idf(tf_set, idf_set):
    tf_idf_values = {}

    for sol_id in tf_set:
        tf_idf_values[sol_id] = {}
        for word in tf_set[sol_id]:
            tf_idf_values[sol_id][word] = tf_set[sol_id][word] * idf_set[sol_id][word]
    
    return tf_idf_values
    
def select_keywords(tf_idf_values):
    resultant_keywords = {}

    for sol_id in tf_idf_values:
        resultant_keywords[sol_id] = {}
        words = tf_idf_values[sol_id]
        vals = list(words.values())
        avg = sum(vals) / len(vals)

        for w in words:
            if(words[w] >= avg):
                resultant_keywords[sol_id][w] = words[w]

    return resultant_keywords

def reorder_keywords(keywords_map):
    reorder_map = {}

    for sol_id in keywords_map:
        for w in keywords_map[sol_id]:
            if w in list(reorder_map.keys()):
                reorder_map[w][sol_id] = keywords_map[sol_id][w]
            else:
                reorder_map[w] = {}
                reorder_map[w][sol_id] = keywords_map[sol_id][w]
    
    return reorder_map

def main():
    tf_set = {}
    idf_set = {}
    word_to_doc = {}

    for sol in solutions_data:
        tf_set[sol['solutionID']] = calculate_tf_value(sol['descp'])
        idf_set[sol['solutionID']] = calculate_idf_value(sol['descp'], solutions_data, word_to_doc)

    tf_idf_values = calculate_tf_idf(tf_set, idf_set)

    keywords_map = select_keywords(tf_idf_values)
    reorder_map = reorder_keywords(keywords_map)

    pprint(reorder_map)

    with open('tags.json', 'w') as tags:
        json.dump(reorder_map, tags)


if __name__ == "__main__":
    main()
