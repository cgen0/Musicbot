# Musicbot
## Upload your music library on Telegram

Requires python3 and FLAC files (with metadata) ordered in this way: 

<i>./Artist/Year - Album/Track - Title</i>.flac


## Installation
<ul>
<li> git clone https://github.com/genox997/Musicbot.git </li>
<li> cd Musicbot </li>
<li> pip3 install --user -r requirements.txt</li>
</ul>

## Usage
<ul>
<li> go to https://my.telegram.org/auth log in with your number and get your api_id and api_hash.</li>
<li> change the example values in main.py with yours.</li>
<li> copy main.py and Metadata.py in your music library directory.</li>
<li> run python3 main.py.</li>
<li> open your telegram app or desktop client.</li>
<li> send yourself a messagge with /add command before the name of the artist (Example: /add Pink Floyd)</li> 
</ul>

