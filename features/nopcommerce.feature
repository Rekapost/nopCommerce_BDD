Feature: nopCommerce Login

  Scenario: Login to nopCommerce with valid parameters
    Given Launch Chrome browser
    When Open nopCommerce page
    And Enter username "admin@yourstore.com" and password "admin"
    And Click on login button
    Then User must be successfully able to login to dashboard page
    And Close browser

  Scenario Outline: Login to nopCommerce with valid parameters
    Given Launch Chrome browser
    When Open nopCommerce page
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must be successfully able to login to dashboard page
    Examples:
      | username            | password |
      | admin@yourstore.com | admin    |
      | adm@yourstore.com   | admin123 |
      | admin@yourso.com    | adminxyz |
      | admin@yourstore.com | admin&*  |






