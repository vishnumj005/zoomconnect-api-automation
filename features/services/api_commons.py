import xmltodict
import json


def verify_status(response, expected_code):
    assert response.status_code == int(expected_code), \
        f'Expected status code:{expected_code},' \
        f' but was: {response.status_code} with body: {response.text} for {response.request.method} {response.url}'
    if response.status_code != int(expected_code):
        print(response)


def verify_message(response, expected_message):
    try:
        if "Unauthorized" in expected_message or "Group name us required" in expected_message:
            message = xmltodict.parse(response.text)['error']['message']
        else:
            message = xmltodict.parse(response.text)['group']['name']
    except KeyError as key:
        assert False, f"Key not found, {key}"
    assert message == expected_message


def create_headers(auth_token=None, auth_email=None):
    return {
        'Content-Type': "application/json",
        'token': auth_token,
        'email': auth_email
    }


def build_api_key_payload(name):
    return json.dumps({
        "name": name
    })
