Feature: fetching User Details 3

  Scenario: testing the get call for User Details 3

    Given url 'https://reqres.in/api/users/3'
    When method GET
    Then status 200



  Scenario: testing the get call for User Details 4

    Given url 'https://reqres.in/api/users/4'
    When method GET
    Then status 200

