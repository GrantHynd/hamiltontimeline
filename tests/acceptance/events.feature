Feature: Test that events can be created
  Scenario: User can create new events
    Given I am on the create event page
    When I enter "Birth of a Legend" in the "title" field
    And I enter "Alexander Hamilton was born and spent part of his childhood in Charlestown." in the "description" field
    And I enter "11-01-1757" in the "occurred_on" field
    And I press the submit button
    Then I am on the create event page
    Given I wait for the status message to appear
    Then I see a status message "Event Created: 'Birth of a Legend'"

  Scenario: User is displayed with an error message when form is incomplete
    Given I am on the create event page
    When I enter "" in the "title" field
    And I enter "Alexander Hamilton was born and spent part of his childhood in Charlestown." in the "description" field
    And I enter "11-01-1757" in the "occurred_on" field
    And I press the submit button
    Then I am on the create event page
    Given I wait for the status message to appear
    Then I see a status message "Title must not be blank"