# Battleships Game

Battleships is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.
Users can try to beat the computer by finding all the computer's battleships before the computer finds theirs. Each Battleship occupies one square on the board. One can find more info on the rules and the history of the game here on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))

<div align="center"><img src="/assets/images/battleships-python-pp3.jpg" alt="battleships welcome screen"></div>


Click on me [Battleships](https://battleships-joe-yip-a6b915940e04.herokuapp.com/) to be taken to the final deployment of the project.

## Table of Contents 

1. [How to play](#how-to-play)
    
2. <details open>
    <summary><a href="#features">Existing Features</a></summary>

    - [Welcome Screen](#welcome-screen)
    - [Instructions](#instructions)
    - [Play](#play)
    - [Enter Username](#enter-username)
    - [Coin Toss](#coin-toss)
    - [Random Board Generator](#random-board-generator)
    - [Player Feedback](#player-feedback)
    - [Score Count](#score-count)
    - [Number of Turns](#number-of-turns)
    - [Play Again](#play-again)
    - [Goodbye](#goodbye)
    </details></li>
    </ul>
</details>

3. <summary><a href="#future-features">Future Features</a></summary>

4. <summary><a href="#design">Design</a></summary>

5. <summary><a href="#data-model">Data Model</a></summary>

6. <summary><a href="#technologies">Technologies</a></summary>

7. <details open>
    <summary><a href="#testing">Testing</a></summary>

    - [Validation](#validation)
    - [General Testing](#general-testing)
    </details>

8. <details open>
    <summary><a href="#deployment">Deployment</a></summary>

    - [Heroku](#heroku)
    </details>

9. <details open>
    <summary><a href="#credits">Credits and Contact</a></summary>

    - [Credit](#credit)
    </details>

----

## How to Play
A single player game against the computer. 

Gameplay;
- Enter your username and the game will begin.
- A coin toss is determine who will guess first. 
- Player's board and opponent board will automatically generate five random ship spaces for the user
and computer.
- Both game boards will be dsplayed. Player's and Computer's.
- Enter your X and Y co-ordinates.
- Game objectives is to sink the opponents ship.
- Winner is first to sink all opponents ships.
- 'X' marks a miss on the board. '*' Marks a hit on board.

## Features
### Welcome Screen
For the welcome screen, the user is first introduced to a battleships title in. Taken from this source: [ASCII Art](https://ascii.co.uk/art/battleship)<br> The user is has access to two options.
- Enter 'P' to play game,
- Enter 'I' for instructions
<div><img src="/assets/images/welcome-screen.jpg" alt="battleships welcome screen"></div>

### Instructions
If the user enters 'i' the game instructions on how to play will be presented. 
<div><img src="/assets/images/game-instructions.jpg" alt="battleships instructions"></div>

### Play
If the user enters 'p' the game will print a message "Starting game..." for user feedback and will be prompt a input to the user to enter a 'username'.
<div><img src="/assets/images/enter-p.jpg" alt="battleships play game"></div>

### Enter Username
Once the user enters a desirable username, they will be prompt a welcome message to the game and highlighted is their username input.  
<div><img src="/assets/images/enter-username.jpg" alt="battleships entering username"></div>

### Coin Toss
The coin toss is to determine who gets to guess first. Feedback if you win
<div><img src="/assets/images/heads-or-tails-after-p.jpg" alt="battleships coin toss"></div>
<br>Feedback if you lose<br>
<div><img src="/assets/images/heads-or-tails-after-p-lose.jpg" alt="battleships coin toss"></div>

### Random Board Generator
Ships are randomly placed on both the player and the computer boards. The player cannot see where the computer ship's are.
<div><img src="/assets/images/game-board.jpg" alt="battleships board"></div>

### Player Feedback 
Entering X co-ordinate
<div><img src="/assets/images/enter-x.jpg" alt="enter x feedback"></div>
Entering nothing feedback
<div><img src="/assets/images/no-input-x.jpg" alt="no input feedback"></div>

Entering Y co-ordinate
<div><img src="/assets/images/enter-y.jpg" alt="enter y feedback"></div>

Entering nothing on Y will loop over to input X co-ordinate again
<div><img src="/assets/images/no-input-y.jpg" alt="no input feedback"></div>

If player enters the same co-ordinates already guessed before
<div><img src="/assets/images/repeated-guess.jpg" alt="already guessed feedback"></div>

User feedback from entering given X and Y co-ordinates. This prints the user's username and where they have guessed at the opponents board. 'X' marks the location on the board. If its a miss it prints out 'MISS' if its a hit it prints out a HIT!
<br> The feedback also prints out where the computer has randomly guessed on the players board and shows the location where they have hit. 
<div><img src="/assets/images/game-turn-1.jpg" alt="game-turn-1"></div>

### Score Count
Score count keeps track and displays the score for the player and computer. For every ship sunk it is incremented by one.
<div><img src="/assets/images/score-count.jpg" alt="score-count"></div>

### Number of Turns
Number of turns keep track of the current amount of turns
<div><img src="/assets/images/score-count.jpg" alt="score-count"></div>

### Play Again
- When the player or the computer has sunk all the opponents ship the game will end.
- Once game has ended, the player will be asked if they want to play again. The player will need to input Y for yes or N for no.
- If the player decides to play again, the game will reload.

<div><img src="/assets/images/win-feedback.jpg" alt="play-again"></div>

### Goodbye 
- If the player decides against playing again, they will get a goodbye message.
<div><img src="/assets/images/goodbye.jpg" alt="goodbye"></div>

[Back to top](#table-of-contents)

----

## Future Features

- In the future, I would like to add more features such as;
    - Add rounds should the player wishes to play again. 
    - Different levels of difficulty. Have the user input a X and Y for the size of the board and thus increases the length / size of the ships on the board.
    - Allow the player to place the ships on the board themselves. 
    - Add more visual feedback into the game. Maybe audio.
    - The ability to play online with another friend or on the same screen. 

----

## Design

- When approaching for the design model for this project, I took the Code Institute Ultimate Battleships from the Python Essentials as a great base for what I planned to create. As it was going to be a game on a terminal which consists of a black background and white text, I wanted to keep it quite simple too but add some color to the terminal for a better UX.
- I wanted a big bold welcome message so immediately it draws the user to the screen and the battleships title in ASCII art was the ideal choice.
- I imported colorama as my main colours. Very simple colours and I used them throughout my python code to print a much cleaner and better display. 

----

## Data Model

Lucidchart was used in the development stages of this project. This was a simple but effective logic flow to follow which helped me structure what functions, output and error handling i'll be needing to create. 
<div><img src="/assets/images/lucidchart.jpg" alt="lucidchart"></div>

[Back to top](#table-of-contents)

----

## Testing 
## Validation
- Pass Python script through Code Institutes Python Linter.
- No errors found on run script file
<div><img src="/assets/images/run-ci-linter.jpg" alt="run ci linter"></div>

- Errors mostly from the intro script file is the ASCII art title. This does not cause the code to break.
<div><img src="/assets/images/intro-ci-linter.jpg" alt="intro ci linter"></div>


## General Testing

- I carried out most the testing myself. I did post my code into the Slack community in the #peer-code-review in hopes for another person to test it but I had no reply.
- I also had a family member to play on the game once I introduced new features to find any bugs.
- Some errors found and fixed during my testing. These errors happened if the player was to enter two or more characters in the X or Y co-ordinates that are in the scope of the X and Y axis, i.e input "ab" for X or "12" for Y. It would cause the error.
<div><img src="/assets/images/x-error.jpg" alt="x input error"></div>
<div><img src="/assets/images/y-error.jpg" alt="y input error"></div>

- Another issue found was the once randomly generated and placed on the board, some of the ships was able to over lap. So you could potentially have more than one ship on a single square.
<div><img src="/assets/images/testing-ships-over-lapping-ontop.jpg" alt="ships overlapping"></div>

- A error where the computer would win but it would not end the game on that particular turn. I would have to play another turn before the game would end.
<div><img src="/assets/images/testing-computer-wins-error.jpg" alt="computer win error"></div>

- All errors fixed during testing 

[Back to top](#table-of-contents)

----

## Deployment
### Heroku

The app was deployed via Heroku and the live link can be found here [Battleships Game](https://battleships-joeyip13.herokuapp.com/)
- To deploy the project through Heroku, the following steps were taken:
- Sign up / Log in to [Heroku](https://www.heroku.com/)
- From the main Heroku Dashboard, press the 'New' button and then press on the 'Create New App' button.
- Give the project a name (Needs to be a unique name) and then select the region that is suitable to you. After this is done, press on the 'Create App' button.
- Once the app has been created, you will be redirected to the deploy section. Using the submenu at the top, press on the settings button.
- Once on the settings page, scroll down a to the 'Config vars' section. Once located, press on the 'Reveal congfig vars' button. This will reveal the current config vars for the app. There should not be any vars configured beforehand.
- In the KEY input field, input PORT in capital letters and in the VALUE field, input 8000. Then click on the 'Add' button. This needs to be done for the Code Institute template. If you are not using the CI template, you may not need to do this.
- Next, you need to click on the 'Add buildpack' button below. This should trigger a popup. Select Python as your first buildpack and press on the 'save changes' button.
- Repeat the above step but this time select Node.js as the buildpack. The order of the buildpacks is important. Python should be first and Node.js second. If you accidently do them in the wrong order, you can click on either buildpacks and drag them to put them in the correct order.
- Next, you need to navigate to the deploy page which you can do from the submenu at the top of the page.
- Once on the deploy page, look for the deployment method section and press on the Github logo. Once done, a small section should appear underneath. Click on the 'Connect to GitHub' button. On your first time doing this, you may be promted to follow some steps which you should do.
- Once done, a 'Connect to GitHub section should appear. Here you will need to search for the repository you want to connect to. You can either type in the repository name in the input field and press search or you can just press search right away and a list of all your repositories should appear and you can press on the one you would like to connect to. Once you have have found the repository you would like to connect to, press on the 'Connect' button on the right hand side.
- Now that your app has been connected to GitHub, double check the 'Choose a branch deploy' drop down menu is deploying the correct branch from your GitHub Repository. Once you are sure, you need to decide if you would like to enable automatic deploys via the 'Enable Automatic Deploys' button below or if you would like to deploy it manually everytime. The difference is, with automatic deploy, your app will be updated automatically everytime you push the changes in GitHub where as with manual deploy, you will need to go back to the deploy page everytime you want to update the app with the changes. I prefer for it to be automatically done but it is entirely upto you.
- Once you have decided how you want the deploys to be, press on the deploy branch below. Heroku will now build the app for you. Once it has been completed, a 'Your App Was Successfully Deployed' message will appear with a link the live site.
- I needed to remove some dependencies from the requirements.txt file. Having switching to Code Anywhere IDE. Certain depandancies was not working with Code Anywhere. 

<div><img src="/assets/images/remove-dependencies.jpg" alt="remove dependencies"></div>


[Back to top](#table-of-contents)

---- 

# Credits 

- Code Institute - [Code Institute](https://github.com/Code-Institute-Org/python-essentials-template)
I used Code Institute gitpod full template and Python Essentials in the Full Stack Development course.
- W3 Schools - [W3 Schools](https://www.w3schools.com/)
- README.md for the template - https://github.com/Code-Institute-Solutions/readme-template
- I used my own template from my previous project 2 - https://github.com/JoeYip13/Project-2-JavaScript/blob/main/README.md
- Rory Patrick Sheridan README.md to help with structure content in my README.md - https://github.com/Ri-Dearg/horizon-photo/blob/master/README.md#page-elements
- Rory Patrick Sheridan for all his knowledgable guidance throughout my learning.
- My family for their continued support
- Kevin Powell on YouTube - [Kevin Powell](https://www.youtube.com/@KevinPowell)
- Web Dev Simplified on YouTube - [Web Dev Simplified](https://www.youtube.com/@WebDevSimplified)
- Slack community for all the technical issues and learning of IDE's, VS Code.
- Code Institute Tutor Legends. Always there to guide me and teach me. 

[Back to top](#table-of-contents)

----

# Other Comments
Overall I enjoyed this project 3 python essentials. I found this to be much smoother in terms of learning curve compared to Javascript in the previous project 2. Having said that, learning Python has made me uderstand more of the Javascript syntax and language as I compared the very similar function syntax and to one and other. I do believe my commits have been a lot more concise and structured in this project compared to my last project. Learning to use branches in this project for the first time has been a great learning curve. # Battleships Game

