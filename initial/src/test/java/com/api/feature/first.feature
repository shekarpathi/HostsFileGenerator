Feature: fetching User Details 2

  Scenario: testing the get call for User Details 2

    Given url 'https://reqres.in/api/users/2'
    When method GET
    Then status 200