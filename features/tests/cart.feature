Feature: Cart test cases

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open Target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown

  Scenario: Create a test case to add Target’s product into the cart, and make sure it’s there
    Given Open Target main page
    When Add Item to cart
    And Close adding item
    And Click on Cart icon
    Then Verify Item in cart or total prices
