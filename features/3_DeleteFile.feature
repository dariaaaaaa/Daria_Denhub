# Created by daria at 13.12.21
Feature: Delete File

  Scenario: Requesting existing file
    Given dropbox url "https://api.dropboxapi.com/2/files/delete_v2"
    And we want to delete file "/webAPI_home_task/picture.png"
    When we consume the endpoint
    Then json response is retrieved with right data and 200 as status code
