Feature: Job

  Background:
    Given the user logging in with username and password given on the page
    And navigates to Admin
    And navigates to to Job - Job Titles

  Scenario: Delete job title
    Given user select the following existing record
    | job_title |
    | Student   |
    When user click on Delete button
    Then Student record no longer visible on the grid