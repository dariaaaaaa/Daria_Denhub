Feature: Modify job title

  Background:
    Given the user logging in with username and password given on the page
    And navigates to Admin
    And navigates to to Job - Job Titles

  Scenario: Modify job title
    Given the following existing record
    | job_title |
    | Student   |
    And user select "Student" record
    And click on Edit button
    And refill Job Description with "NewDescription"
    When the user click on Save
    Then following changes is visible on the grid
    | new_description |
    | NewDescription  |
