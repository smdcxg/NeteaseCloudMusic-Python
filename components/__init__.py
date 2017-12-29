
from .discover import load_discover
from .login import load_login
from .comments import load_comments
from .search import load_search
from .playlist import load_playlist

def load_components(obj):
    load_comments(obj)
    load_login(obj)
    load_search(obj)
    load_discover(obj)
    load_playlist(obj)
