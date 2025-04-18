Feature: Register Account Functionality

  Scenario: Register with mandatory fields
    Given I navigate to Register page
    When I enter details into mandatory fields
    And I click on Continue button
    Then Account should get created

  Scenario: Register with all fields
    Given I navigate to Register page
    When I enter details into all fields
    And I click on Continue button
    Then Account should get created

  Scenario: Register with a duplicate email address
    Given I navigate to Register page
    When I enter details into all fields expect email field
    And I enter existing accounts email into email field
    Then Proper warning message informing about duplicate account should be displayed

  Scenario:  Register without providing any details
    Given I navigate to Register page
    When I dont enter anything into the fields
    And I click on Continue button
    Then Proper warning messages for every mandatory fields should be displayed


