@api_current_balance
Feature: To test the get balance API for Zoom Connect

    Scenario: Testing the get balance API response
        When GET request is sent to view the balance
        Then verify the response code 200

    Scenario Outline: Testing the get balance API response for authentication scenarios
        When GET request is sent to view current balance with invalid <token>
        Then verify the response code <status_code>
        And verify error <message> is displayed
        Examples:
        | token        | status_code | message               |
        | None         | 401         | Reason: Unauthorized  |
        | 1234         | 401         | Reason: Unauthorized  |
