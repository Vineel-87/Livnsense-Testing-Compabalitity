Feature: VICAS Login Functionality with CSV Data

  @Test
  Scenario: Verify login page elements are displayed
    Given I am on the VICAS login page
    Then I should see the "Welcome to VICAS" header
    And I should see the username input field
    And I should see the password input field
    And I should see the "Forgot Password?" link
    And I should see the "Sign in" button

  @Test
  Scenario: Sign in button remains disabled with empty credentials
    Given I am on the VICAS login page
    When I leave the username field empty
    And I leave the password field empty
    Then the "Sign in" button should be disabled

  @Test
  Scenario: Test login with multiple credentials from CSV
    Given I am on the VICAS login page
    And I read login data from CSV file
    When I test login for each user from the CSV
    Then I should see appropriate results for each login attempt

  @Test
  Scenario: Verify button state with valid credentials
    Given I am on the VICAS login page
    And I read login data from CSV file
    When I enter valid credentials from CSV
    Then the "Sign in" button should be enabled

  @Test
  Scenario: Verify error messages for invalid logins
    Given I am on the VICAS login page
    And I read login data from CSV file
    When I attempt login with invalid credentials from CSV
    Then I should see an error message for invalid login

  Scenario: Sign in button remains disabled with only password
      Given I am on the VICAS login page
        When I leave the username field empty
        And I enter "Test@123" in the password field
        Then the "Sign in" button should be disabled

    Scenario: Sign in button enables when both fields are filled
        Given I am on the VICAS login page
        When I enter "valid_user" in the username field
        And I enter "Valid@123" in the password field
        Then the "Sign in" button should be enabled

    Scenario: Access password recovery via Forgot Password link
        Given I am on the VICAS login page
        When I click the "Forgot Password?" link
        Then I should be redirected to the password recovery page

    Scenario: Attempt login with invalid credentials
        Given I am on the VICAS login page
        When I enter "invalid_user" in the username field
        And I enter "wrong_password" in the password field
        And I click the "Sign in" button
        Then I should see an error message "Invalid credentials"

    Scenario: Password field masks input characters
        Given I am on the VICAS login page
        When I enter "secret" in the password field
        Then the password field should mask the input characters