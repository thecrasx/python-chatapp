from client.Window.UI.Animations.friends_container_animation import FriendsContainerAnimation
from client.Window.UI.Animations.message_animation import MessageAnimation
from client.Window.UI.Animations.loading_animation import LoadingAnimation



class Animations:
    def __init__(self, friendsContainer) -> None:
        self.friendsContainerAnimation = FriendsContainerAnimation(friendsContainer, b"maximumWidth")
        self.loadingAnimation = LoadingAnimation