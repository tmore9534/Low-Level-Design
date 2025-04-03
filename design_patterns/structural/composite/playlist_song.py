from abc import ABC, abstractmethod

class IComponent(ABC):
    @abstractmethod
    def play(self):
        pass
    
    @abstractmethod
    def setPlaybackSpeed(self, speed: float):
        pass

    @abstractmethod
    def getName(self):
        pass


#composite class
class Playlist(IComponent):

    def __init__(self, playlistName, speed=1):
        self.playlist = []
        self.playlistName = playlistName
        self.speed = speed #default playblackSpeed for all songs

    def play(self):
        print(f"starting to play {self.playlist[0]} songs from {self.getName}")
    
    #IMP, work as a unifomely without checking the individual type, 
    # traverse through the leafs and change playblack speed uniof
    def setPlaybackSpeed(self, speed: float):
        for component in self.playlist:
            component.setPlaybackSpeed(speed)

    def getName(self):
        return self.playlistName

    def add(self, component: IComponent):
        print(f"Added the {component.getName()} in {self.getName()}")
        self.playlist.append(component)
        return len(self.playlist) - 1

    def remove(self, component: IComponent):
        self.playlist.remove(component)
        print(f"{component.getName()} removed successfully: ")


# leaft class
class Song(IComponent):
    def __init__(self, songName, artist, speed=1):
        self.songName = songName
        self.artist = artist
        self.speed = speed
    
    def play(self):
        print(f"Started playling {self.getName()}")
        pass
    
    def setPlaybackSpeed(self, speed: float):
        self.speed = speed
        print(f"The playblack speed of {self.getName()} has been set to {self.speed}")
        pass

    def getName(self):
        return self.songName
    
    def getArtist(self):
        return self.artist


#build structure layer by layer
playlist1 = Playlist("MySongs")

#playlist can contain now another playlist or song - recursive composition
studyPlaylist = Playlist("Study")

# add two songs into study by creating the objects.
song1 = Song("ABC_study", "xyz1_art")
song2 = Song("PQR_study", "lmn_art")

studyPlaylist.add(song1)
studyPlaylist.add(song2)

# add the studyPlaylist in Playlist1
playlist1.add(studyPlaylist)

# set the speed of son1 to 1.5
song1.setPlaybackSpeed(1.5)

# create a new song in Main MySongs
song3 = Song("HJI_mysongs", "xyz")
song3_index = playlist1.add(song3)

# remove song3 from playlist1
playlist1.remove(song3)

# change the playspeed of all songs in study
studyPlaylist.setPlaybackSpeed(1)





        




