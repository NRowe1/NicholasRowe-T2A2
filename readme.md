## R1	
### Identification of the problem you are trying to solve by building this particular app.

My idea for this app is to make it easily accesible to see the points a player gets from playing in an afl game. Previous methods used can be overwhelming by showing the other statitics a player can obtain during a match 

## R2	
### Why is it a problem that needs solving?
This problem needs solving as it will help users to define what goals and points a player has scored in a match. To help refine the search I have added the players team they play for and what time the match start and the date

## R3  
### Why have you chosen this database system. What are the drawbacks compared to others?

I've chosen postgres as its open source and free, with this there are multiple features that allows for advanced SQL queries.

Being free the community support is large and active, having multiple developers providing support by sharing knowledge through forums.

The drawbacks of using PostgreSQL including

PostgreSQL is much more complex that other commonly used database systems to set up and manage. 

Finally the performance isnt as fast as other database systems and is not ideal for bigger files and for more scripts to write.

## R4	
### Identify and discuss the key functionalities and benefits of an ORM

An ORM simplifies database interactions by abstracting away SQL complexities, mapping object-oriented models to relational databases.

It streamlines database schema management, and provides tools for data validation and type conversion. ORM libraries optimize performance with lazy loading and query caching while promoting the object-oriented programming paradigm. 

They facilitate rapid application development by minimizing low-level database tasks, allowing developers to focus on business logic. 

Overall, ORMs enhance code quality, developer productivity, and the development of scalable, maintainable applications.


## R5	
### Document all endpoints for your API

Most of my endpoints were all GET and POST methods

To keep my code consistent I kept the same URL's with all controllers but changed the names in relation to what data needs to be found. 

Integer and string were used with all JSON - POST methods.

I did yuse a date and time module for the games table.

## R6	
### An ERD for your app

My ERD of the app is a very simple and clean layout having most tables linking to my player table. 

![ERD](images/download.png)

## R7	
### Detail any third party services that your app will use

I would use API's like good maps or mapbox to help users find where the games are being played

Social media API's, facebook and twitter can be helpful for uses to share content or fetching user data from social profiles

## R8
### Describe your projects models in terms of the relationships they have with each other

The player belongs to a team by having a team_id as a foriegn key, this is referenced the team_id primary key in the Team model. Finally in the player model, a single player can have multiple scores. This is done by a player_id forieng key in the Score model

A game belongs to a team, this is represented through a forieng key team_id in the Games model.

## R9	
### Discuss the database relations to be implemented in your application

My relationships between tables are all one to many relationships mainly between the teams table

Teams table has a one to many relation between the Players table, while also have a one to many relationship between the games table 

Players has a one to many relationships between the goal table

The games table has a one to many relationship with the games table '

and finally the states table has a one to many relationship with the Teams table

## R10	
### Describe the way tasks are allocated and tracked in your project

Using trello allowed me to keep on track on what files i need to complete, when I complete a models i would copy the code and put it in the comment card for in trello

Another method I have used is commiting my code on GitHub. This allowed me to keep previous saves in case my code doesnt work as I hoped.

I 