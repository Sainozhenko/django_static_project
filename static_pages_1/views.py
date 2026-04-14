from django.shortcuts import render
from django.http import HttpResponse


nav = """
    <nav>
        <a href='/'>Home</a> |
        <a href='/contact/'>Contact</a> |
        <a href='/about/'>About Us</a> |
        <a href='/store/'>Store</a> |
    </nav>
"""

nickname = "Balakudra"
level = 80
kills = 789.0


home_body = f"""
    <ol>
    <h3>1</h3>
        <li>Nickname: {nickname}</li>
        <li>Level: {level}</li>
        <li>Kills: {kills:.2f}</li>
    </ol>
"""



def home(request):
    content= """
            <h1>Welcome to Game-Server x10 low state</h1>
            <h2><a href='/store/'>Store</a></h2>
            <h2><a href='/about/'>About</a></h2>
            <h2><a href='/contact/'>Contact</a></h2>
            <p>Top gamers:</p>
            
    """
    
    return HttpResponse(nav + content + home_body)

def contact(request):
    content = """
    <p>Our LinkedIn:</p>
    <p>Our Facebook:</p>
    <p>Our Instagram:</p>
    <p>Phone:</p>
    <p>Careers:</p>
    <p>Support:</p>
    """
    return HttpResponse(nav +  content)

def about(request):
    content ="""
    <p>Our server is started in 2019. During this time no wipes,</p>
    <p>Stable game, online, no bots, cheats avoid.</p>
    Anti-cheat protection!
    """
    return HttpResponse(nav + content)

def store(request):
    content ="""
    <p>Donate shop:</p>
    <p>Exchange:</p>
    <h3>Request to migrate to different server.</h3>
    """
    return HttpResponse(nav +content)