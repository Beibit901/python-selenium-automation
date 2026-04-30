Feature: Test cases for target4

  Scenario: Open target.com, click on cart icon, and verify empty cart message
    Given Open target.com
    When Click on Cart icon
    Then Verify "Your cart is empty" message is shown

  Scenario: Logged out user can navigate to Sign In
    Given Open target.com
    When Click Sign In
    Then Verify Sign In form opened

  Scenario: Search for product on Target
    Given  Open target.com
    When Search for <product>
    Then verify that search worked for <expected_product>
    Examples:
    |product    | expected_product  |
    |coffee    | coffee  |
    |ice cream    | ice cream  |
    |nintendo  | nintendo  |

  Scenario: Open the Target Circle page and verify there are 2 story cards under “Unlock added value”
    Given Open the Target Circle page
    Then verify there are 2 story cards under “Unlock added value”
