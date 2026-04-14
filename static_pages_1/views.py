from django.http import HttpResponse

nav = """
<nav>
    <a href='/'>Home</a> |
    <a href='/contact/'>Contact</a> |
    <a href='/about/'>About Us</a> |
    <a href='/store/'>Store</a>
</nav>
"""


nickname = "Balakudra"  
level = 79.5             
kills = 4232          

top_players = ["Alex", 120, 99.5, True, None, {"rank": "A+"}]


server_info = {
    "name": "Game-Server x10 low state",
    "year": 2019,
    "online": 1500,
    "anti_cheat": True,
    "region": "EU"
}


def render_variables():
    return f"""
    <h2>Player Info</h2>
    <ol>
        <li>Nickname: {nickname}</li>
        <li>Level: {level}</li>
        <li>Kills: {kills:.2f}</li>
    </ol>
    """

def render_list():
    items = "".join([f"<li>{i}</li>" for i in top_players])
    return f"""
    <h2>Top Players (List)</h2>
    <ul>
        {items}
    </ul>
    """

def render_dict():
    items = "".join([f"<li>{k}: {v}</li>" for k, v in server_info.items()])
    return f"""
    <h2>Server Info (Dict)</h2>
    <ul>
        {items}
    </ul>
    """

def home(request):
    content = """
    <h1>Welcome to Game-Server x10 low state</h1>
    <h2>Main Menu</h2>
    <p>Top gamers section</p>
    """
    return HttpResponse(nav + content + render_variables() + render_list())


def contact(request):
    content = """
    <h1>Contact</h1>
    <h2>Social Media</h2>
    <p>LinkedIn / Facebook / Instagram</p>
    """
    return HttpResponse(nav + content + render_variables())


def about(request):
    content = """
    <h1>About</h1>
    <h2>Server History</h2>
    <p>Started in 2019, stable gameplay, anti-cheat system active.</p>
    """
    return HttpResponse(nav + content + render_dict())


def store(request):
    content = """
    <h1>Store</h1>
    <h2>Donate Shop</h2>
    <p>Exchange system and premium items</p>
    """
    return HttpResponse(nav + content)