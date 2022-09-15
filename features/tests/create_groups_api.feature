@create_groups
Feature: To test the get create group API for Zoom Connect

    Scenario: Testing the create group API response
        When POST request is sent to create group name test
        Then verify the response code 201

    Scenario Outline: Testing the create group with different group name
        When POST request is sent to create group name <name>
        Then verify the response code <status_code>
        Then verify the <response> is displayed
        Examples:
        | name       | status_code | response   |
        | 123        | 201         | 123        |
        | r%$E$%#$%# | 201         | r%$E$%#$%# |

    Scenario Outline: Testing the create group with empty group name
        When POST request is sent to create group name <name>
        Then verify the response code <status_code>
        Then verify the <response> is displayed
        Examples:
        | name         | status_code | response                          |
        | None         | 400         | Group name us required            |
