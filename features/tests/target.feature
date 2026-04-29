Feature: Test cases for target4

  Scenario: Open target.com, click on cart icon, and verify empty cart message
    Given Open target.com
    When Click on Cart icon
    Then Verify "Your cart is empty" message is shown

  Scenario: Logged out user can navigate to Sign In
    Given Open target.com
    When Click Sign In
    Then Verify Sign In form opened