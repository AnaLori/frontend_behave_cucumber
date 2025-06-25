# language: en
Feature: Order Flow ecommerce-playground.lambdatest.io

  Background: ecommerce-playground.lambdatest.io
    Given that I am on the website's home page

  @login
  Scenario Outline: Log in with different valid credentials
    When I fill in the email "<email>" and password "<password>"
    And click on the submit button
    Then Validate the title after login
    And Validate the search products field after login

    Examples:
      | email                         | password          |
      | anatestedesafio@gmail.com     | senhaenjoeiteste  |

  @search
  Scenario Outline: Search for different items
    Given I am logged in on the site
    When I search for the product "<product>"
    Then search results must be shown

    Examples:
      | product         |
      | Canon EOS 5D    |
      | HTC Touch HD    |

  @search_no_results
  Scenario: Search for non-existent product
    Given I am logged in on the site
    When I search for the product "Produto inexistenmte723457"
    Then no results message should be shown
  
  @cart
  Scenario: Add products to cart
    Given I am logged in on the site
    When I search for the product "iPod Nano"
    And I click in the product "iPod Nano"
    And add it to cart
    Then the product must be in the cart

