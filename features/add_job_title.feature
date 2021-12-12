# Created by daria at 12.12.21
Feature: Add job title

  Background:
    Given the user logging in with username and password given on the page
    And navigates to Admin
    And navigates to to Job - Job Titles

  Scenario: Add new unique job title
    Given there is no "Student" record on the grid
    And user click on the Add button
    And fill the fields with following
    | job_title | description | notes     |
    | Student   | someText    | someNotes |
    When user click on Save
    Then newly added title "Student" is visible on the grid

  Scenario: Add existing job title
    Given user has already created job title "Student"
    And user click on the Add button
    When user fills the Job Title field with "Student"
    Then error message "Already exist" appear

