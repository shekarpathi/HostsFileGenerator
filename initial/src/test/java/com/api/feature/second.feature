Feature: fetching User Details 3

  Scenario: testing the get call for User Details

    Given url 'https://reqres.in/api/users/3'
    When method GET
    Then status 200