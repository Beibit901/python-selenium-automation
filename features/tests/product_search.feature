Feature: Test cases for Product Search on Target

  Scenario Outline: User can search for products
    Given Open Target main page
    When Search for <search_query>
    Then Verify search results for <product> shown
    Examples:
    |search_query   |product      |
    |Coffee         |Coffee       |
    |coffee cup     |coffee cup   |
    |sugar          |sugar        |
    |tea            |tea          |
#    |茶             |茶           |

  Scenario: Verify that user can see product names and images
    Given Open Target main page
    When Search for AirPods
    Then Verify that every product has a name and an image


