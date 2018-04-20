Feature: Test that the home page timeline contains the correct content
  Scenario: Home Page's timeline displays a single event
    Given I am on the home page
    Then I see an event with the title "Birth of a Legend"