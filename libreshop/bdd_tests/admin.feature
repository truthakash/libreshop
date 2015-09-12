Feature: admin
  As a staff member
  I want to use the admin panel
  So that I can manage the website effectively

  Scenario: access the admin login page
     Given I am a staff member
      When I visit the admin login page
      Then I will see "Log in | Django site admin" in the browser title

  Scenario: log in to the admin panel
     Given I am a staff member
      When I visit the admin login page
       And I log in to the site admin page
      Then I will see "Site administration | Django site admin" in the browser title

  Scenario: add a user via the admin panel
     Given I am a staff member
      When I visit the admin login page
       And I log in to the site admin page
       And I click the "Add" link next to "Users"
       And I add a user named "new_user"
      Then I will see a link for "new_user"

  Scenario: add a product via the admin panel
     Given I am a staff member
      When I visit the admin login page
       And I log in to the site admin page
       And I click the "Add" link next to "Products"
       And I add a product called "new_product"
      Then I will see a link for "new_product"

  Scenario: add a product via the change user page
     Given I am a staff member
      When I visit the admin login page
       And I log in to the site admin page
       And I click the "Add" link next to "Users"
       And I add a user named "new_user"
       And I click the "new_user" link
       And I click the plus icon next to the "Selected products" field
       And I switch to the popup window
       And I enter "thing" in the "Name" field
       And I click the "Save" button
       And I switch to the main window
      Then I will see "thing" in the "Selected products" select box
