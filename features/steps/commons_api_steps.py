from behave import step
from features.services.api_requests import  verify_response_code


@step("verify the response code {status_code}")
def step_impl(context, status_code):
    verify_response_code(context, status_code)
