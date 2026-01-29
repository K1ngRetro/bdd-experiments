Feature: Basic arithmetic

    Scenario: Add two numbers
        Given I have numbers 3 and 5
        When I add them
        Then the result should be 8

    Scenario: Add two negative numbers
        Given I have numbers -2 and -7
        When I add them
        Then the result should be -9

    Scenario: Subtract two numbers
        Given I have numbers 10 and 4
        When I subtract them
        Then the result should be 6

    Scenario: Multiply two numbers
        Given I have numbers 6 and 7
        When I multiply them
        Then the result should be 42

    Scenario Outline: Add many pairs
        Given I have numbers <a> and <b>
        When I add them
        Then the result should be <sum>

        Examples:
            | a | b | sum |
            | 0 | 0 | 0   |
            | 1 | 9 | 10  |
            | 5 | -3| 2   |

    Scenario: Compare two JSON objects
        Given I have JSON object A:
            """
            {"name": "Ada", "age": 36, "skills": ["math", "logic"]}
            """
        And I have JSON object B:
            """
            {"skills": ["math", "logic"], "age": 36, "name": "Ada"}
            """
        Then the JSON objects should be equal
