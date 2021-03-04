import re


def translate(text):
    splited = re.split('[;\t\n.]', text)
    splited = [x for x in splited if len(x) > 5]
    print(splited)
    res = "\n".join(translation_model.test(x)[0] for x in splited)
    dbconnection.add_history(inp['text'], res, inp['session_id'])
    return jsonify({'text': res,
                    'result': 'OK'}), 201


def get_history():
    print(request.json)
    if not request.json:
        abort(400)

    json_req = json.loads(request.json)
    print(json_req)
    if not 'position' in json_req or not 'session_id' in json_req:
        abort(400)

    result = dbconnection.get_history(int(json_req['position']), int(json_req['session_id']))
    if not result:
        abort(400)

    result['result'] = 'OK'
    return result


def login():
    print(request.json)
    if not request.json:
        abort(400)

    json_req = json.loads(request.json)
    print(json_req)

    if 'login' not in json_req or 'password' not in json_req:
        abort(400)

    result = dbconnection.login_user(json_req['login'], json_req['password'])
    if result is False:
        return jsonify({'result': 'Wrong id or password',
                        'session_id': '0'}), 404

    # TODO generate session key here
    return jsonify({'result': 'OK',
                    'session_id': str(result)}), 201
