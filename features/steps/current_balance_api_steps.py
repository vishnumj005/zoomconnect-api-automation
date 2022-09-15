from behave import step

from features.services.api_commons import create_headers
from features.services.api_requests import get_request_service, verify_response_code, verify_response_message

from features.service_constants.api_config import ENDPOINTS
from features.service_constants.authorization_enum import AuthorizationEnum


@step("GET request is sent to view the balance")
def step_impl(context):
    header = create_headers(auth_token=AuthorizationEnum.AUTH_TOKEN.value,
                            auth_email=AuthorizationEnum.AUTH_EMAIL.value)
    get_request_service(context,
                        url=ENDPOINTS.CURRENT_BALANCE,
                        headers=header)


@step("GET request is sent to view current balance with invalid {token}")
def step_impl(context, token):
    header = create_headers(auth_token=token,
                            auth_email=AuthorizationEnum.AUTH_EMAIL.value)
    get_request_service(context,
                        url=ENDPOINTS.CURRENT_BALANCE,
                        headers=header)


@step("verify error {message} is displayed")
def step_impl(context, message):
    verify_response_message(context, message)
