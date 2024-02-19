Feature: login page
  Background: common steps
    Given that i launch the browser.
    When I enter the login page.

  Scenario Outline:Login with valid parameters
    And insert a "<username>" and "<password>"
    And click the button login.
    Then It should display the products catalog.

    Examples:
      | username       | password     |
      | standard_user  | secret_sauce |
      | problem_user   | secret_sauce |
      | error_user     | secret_sauce |
      | visual_user    | secret_sauce |

  # Scenario: Login with invalid parameters
  #   And insert a username "locked_out_user" and "secret_sauce"
  #   Then it should display an error. 