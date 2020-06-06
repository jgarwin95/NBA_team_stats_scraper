# NBA_team_stats_scraper
  ---
## About
NBA_team_stats_scraper is a webscraping application that accesses Basketball-Reference's NBA & ABA League Index located at https://www.basketball-reference.com/leagues/ and returns team's season averages including: Year, Team, G, MP, FG, FGA, FG%, 3P, 3PA, 3P%, 2P, 2PA, 2P%, FT, FTA, FT%, ORB, DRB, TRB, AST, STL, BLK, TOV, PF, PTS, W, L, W/L%, GB, PS/G, PA/G, SRS. After scraping, the application returns the data in the form of comma-seperated-value (csv) table.

What makes this application special is simplicity of the code that it is written in and the ease in which it is used. You are able to grab a single year of team data or a range of years by simply specifiying the desired range (i.e. '2012-2020').

---
## How-To-Use
#### Installation
This game was written using Python version 3.8.2 and pygame version 1.9.6. In order to install this version of pygame, type within your command prompt:
```bash
    pip install pygame==1.9.6
```
If you already have another pygame version installed, the code may run fine, but backwards compatibility has not been tested. 

After installation, download or clone this repository to your own machine.

#### Scrapin'
In order to start playing the game you need to be running python in the directory within which the game is located (be sure to have all the auxillary files containing the sound, etc. in that location as well). Simply import the module and use:

Operating from the command simply type:
```python
>>> python main.py
```
NOTE: Your python command may vary. In some cases it may be "python3" rather than just "python"

#### Keys
This highly complex game is not for the feable-minded. So tred carefully while glancing over the following game-play instructions...
| Action | Key |
|--------|-----|
| jump | spacebar |

And that's it! Stunningly easy, I know...

A few things to note; 1) The spacebar does have a time-sensitive aspect (all jumps are not created equal). The longer you hold the spacebar the more lasting your jump will be until gravity completely overtakes you. 2) The space bar is on auto-jump. If you don't cease holding down the spacebar, your player will jump again automatically. 

Both of these features were present in the original T-Rex Run!

#### Settings
##### Game Constanst
All constant game settings are located in settings.py. The three constants, located in this file, that will impact the game the most upon altering are:
* PLAYER_JUMP - decrease this to increase the player's jumping height
* GRAVITY - increase this to accelrate faster to the ground
* ANTI_GRAVITY - This is the spacebar feature mentioned above. Decreasing will allow holding the spacebar to have a greater effect and will increase the feeling of floating. Careful though... if you exceed the magnitude of gravity then there will be no coming back down to earth
##### In-Game variable settings
The most important variables in terms of altering difficulty are:
* self.obs_gen_time (located in main.py) This variable is steadly diminished over time in the update() section of the game loop
* self.velocity & self.vel_chng_rt variables located in sprites.py, under the Obstacles class. These variables control the obstacles speed and rate of change respectively. 