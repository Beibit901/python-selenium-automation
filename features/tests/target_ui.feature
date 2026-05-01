Feature: verify Target Help UI contain following elements
    Scenario Outline: Target UI page contain Following <paragraph>
        Given Target Help page
        Then Verify that it is correct Correct <paragraph>
        Examples:
        |paragraph                      |
        |Help                           |
        |Have a question?               |
        |Popular Pages                  |
        |What would you like help with? |

    Scenario: Find number of links with what would you like help with
        Given Target Help page
        Then verify 9 help categories under 'What would you like help with?'

    Scenario: Find number of links with Popular pages
        Given Target Help page
        Then verify 8 categories under 'Popular Pages'

    Scenario: Find What I thought lazy to put in separate categories because I am lazy
        Given Target Help page
        Then verify Search bar
        And verify Search button
        And verify 'Browse all help' button