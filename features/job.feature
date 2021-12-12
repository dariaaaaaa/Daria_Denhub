# Created by daria at 08.12.21
Feature: Job

  Background:
    Given the user logging in with username and password given on the page
    And navigates to Admin
    And navigates to to Job - Job Titles

  Scenario: Add new job title
    Given user click on the Add button
    And fill the fields with following
    | job_title | description | notes     |
    | Student   | someText    | someNotes |
    When user click on Save
    Then newly added title "Student" is visible on the grid

  Scenario: Modify job title
    Given user go to the following existing record
    | job_title |
    | Student   |
    And click on Edit button
    And refill Job Description with "NewDescription"
    When the user click on Save
    Then following changes is visible on the grid
    | new_description |
    | NewDescription  |

  Scenario: Delete job title
    Given user select the following existing record
    | job_title |
    | Student   |
    When user click on Delete button
    Then Student record no longer visible on the grid