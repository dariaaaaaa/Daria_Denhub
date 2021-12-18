# Created by daria at 13.12.21
Feature: Get File Metadata

  Scenario: Request existing file
    Given dropbox url "https://api.dropboxapi.com/2/sharing/get_file_metadata"
    And we want to request file "picture.png" from directory "/webAPI_home_task/"
    When we consume the endpoint
    Then json response is retrieved with right data and 200 as status code
