Feature: New users

    Background:
        Given The web app is opened


    @UI @ADD_USER @GET_USERS @SMOKE
    Scenario: A successfully submitted user is shown in all user tab
        When I click on "New User" option
        And I complete all user information for a user
        And I click on submit user button
        Then I see a "Success" feedback message
        When I click on "All Users" option
        Then The recent submitted user is shown


    @UI @ADD_USER @GET_USERS
    Scenario: Multiple successfully submitted users are shown in all user tab
        Given I click on "New User" option
        And I submit "3" users
        When I click on "All Users" option
        Then All the users are shown


    @UI @ADD_USER @GET_USERS
    Scenario: A user which birthday is incorrect is not submitted
        When I click on "New User" option
        And I complete all user information for a user which "birthday" is "25/25/1995"
        And I click on submit user button
        Then I see a "Warning" feedback message
        When I click on "All Users" option
        Then The user is not shown


    @UI @ADD_USER @GET_USERS
    Scenario: A user which information is incomplete is not submitted
        When I click on "New User" option
        And I complete all user information except "surname"
        And I click on submit user button
        Then I see a "Warning" feedback message
        When I click on "All Users" option
        Then The user is not shown
