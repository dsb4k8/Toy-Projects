# Toy Projects
### Includes:
##### Black Jack:
###### Pseudocode:
      - When the game starts, the player and dealer receive 2 cards each
      - The player's cards are both exposed while the dealer's hand consists of one face up card and one face down card
      - At this point the player sees their total hand score but only sees the potential hand score of the dealer.
            - example output: 
              Player's Hand: [5 of Hearts, 10 of clubs] Total:       15
              Dealer's Hand: [J of Spades, ***********] Potential:   21
      - Player is then given the option to "hit" (get delt a new card from the game deck) in order to maximize hand score
            - If player's score exceeds 21 or if player decides not to hit:
                  - If score exceeds 21: Player loses
                  - Player's turn is over and the Dealer's turn begins
                  - pass out of this process
            - If player's score == 21:
                  - Player's turn is over and the Dealer's turn begins
                        - Note that if this happens, Player can only Win or Draw
                  - pass out of this process
            - Else:
                  - Continue this process
      - While dealer's hand total <= 17:
            - Dealer hits
            - If Dealers's score exceeds 21
                  - Player Wins
                  - pass out of this process
            - If Dealer's score == 21:
                  - pass out of this process          
      - if Player score > 21:
            - if Dealer's score > 21:
                  - Draw Game
            - else: Dealer wins
      - if Dealer score > 21:
            - if Player's score > 21:
                  - Draw Game
            - else: Player Wins
      - if Dealer score == Player score:
            - Draw Game
      - if Player's hand score is > dealers hand score
            -Player Wins
      - else: 
            -Dealer Wins
      Ask if player would like to play another hand
      if yes: continue game
      if no:  greet player and break
##### Face Detection Alerts
###### Quick Definition:
           - A Haar Cascade is basically a classifier which is used to detect particular objects from the source. The haarcascade_frontalface_default.xml is a haar cascade designed by OpenCV to detect the frontal face. This haar cascade is available on their github.
###### High Level Logic:
            - Feature recognition can be achieved very easily with OpenCV's built in methods
            - If a face is detected:
                  - Save file locally
                  - connect to smtp server
                  - authenticate through provider
                  - Send email with file attachment to specified email
                  - alert owner that face has been detected in device

            

      

