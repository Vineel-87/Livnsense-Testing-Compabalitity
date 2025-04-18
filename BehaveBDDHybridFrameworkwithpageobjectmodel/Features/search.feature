Feature: Search functionality

  @completed
  Scenario: Search for a valid product
    Given I got navigated to Home page
    When I enter valid product into the Search box field
    And I click on Search product
    Then Valid product should get displayed in Search results

  Scenario: Search for an invalid product
    Given I got navigated to Home page
    When I enter invalid product into Search box field
    And I click on Search product
    Then Proper message should be displayed in Search results

  Scenario: Search without entering any product
    Given I got Navigated to Home page
    When I dont enter anything into Search box field
    And I click on Search button
    Then Proper message should be displayed in Search results
