import json

from behave import step

from features.services.api_commons import build_api_key_payload, create_headers
from features.services.api_requests import verify_response_message, \
    post_request_service
from features.service_constants.api_config import ENDPOINTS
from features.service_constants.authorization_enum import AuthorizationEnum


@step("POST request is sent to create group name {group_name}")
def step_impl(context, group_name):
    header = create_headers(auth_token=AuthorizationEnum.AUTH_TOKEN.value,
                            auth_email=AuthorizationEnum.AUTH_EMAIL.value)

    if group_name == "None": group_name = ""
    api_payload = build_api_key_payload(group_name)
    post_request_service(context,
                         url=ENDPOINTS.CREATE_GROUPS,
                         payload=api_payload,
                         headers=header)


@step("verify the {response} is displayed")
def step_impl(context, response):
    verify_response_message(context, response)
