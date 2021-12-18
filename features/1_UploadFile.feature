# Created by daria at 13.12.21
Feature: Upload file
  # Enter feature description here

  Scenario: Valid request
    Given dropbox url "https://content.dropboxapi.com/2/files/upload"
    And we want to upload file "/features/lib/img/picture.png" to dropbox with path "/webAPI_home_task/picture.png"
    When we consume the endpoint
    Then json response is retrieved with right data and 200 as status code
