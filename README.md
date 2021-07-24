## Bingo Bango Bongo

#### 1. install python and visual studio code
  * https://www.python.org/downloads/
  * https://code.visualstudio.com/download/
  
#### 2. install prerequisites
  * from the command line: "pip install image"

#### 3. create blank bango cards
  * cards should be 1080x1920
  * design however you want as long as you have enough room for bango squares
  * you may want to design the cards so that the round number is written on them -- if you want to do 4 rounds, make 4 different blank cards
  * example card: https://imgur.com/a/yqT8805 (or scroll down to the bottom of the instructions)
  
#### 4. get emojis ready
  * move emojis to a single folder and convert to 128x128 PNGs with colored background and padding: https://bulkresizephotos.com/en
  * separate emojis into folders for each round
    * you need at least 25 emojis per round
    
#### 5. load folders with emojis and blank cards
  * the folder structure should look something like this:
  ```
  \bango\bango.py
  \bango\images\
  \bango\images\background\
  \bango\images\squares\
  \bango\result\
 ```
 * bango.py is the python script
 * the \images\background\ folder is where you put the blank cards
    * replace the image in the background folder for each round
 * the \images\squares\ folder is where you put the emojis (at least 25 per round)
    * replace the emojis in the squares folder for each round
 * the \result\ folder is where the cards will be saved

#### 6. run the script
 * edit output filename in bango.py:
    * edit the filename with the format "BangoTitle-R#C{}.png":
    ```
    result.save(
        outImages + 'FuckoBango-R1C{}.png'.format(cardNum), "PNG")
    ```
    
      * the script will output starting from FuckoBango-R1C0.png
      * make sure to change this per round
  * edit number of cards in bango.py:
  ```
  nbCards = 1
  ```
  
   * do a test run with 1 card before creating hundreds
  * edit pixel offset in bango.py:
  ```
  y_offset = -145
  x_offset = 10
  ```
  
   * if you need to align the emojis, adjust this pixel offset.  

#### 7. run the script with a shitload of cards
  * cards will be in the results folder

![https://imgur.com/a/yqT8805](https://i.imgur.com/9kC5svi.png)
