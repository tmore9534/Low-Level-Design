from abc import ABC, abstractmethod

# Subject Interface
class YouTubeService(ABC):
    @abstractmethod
    def fetch_video(self, video_id: str) -> str:
        pass

# Real Object
class YouTubeAPI(YouTubeService):
    def fetch_video(self, video_id: str) -> str:
        print(f"Fetching video from YouTube: {video_id}")
        return f"Video Data of {video_id}"

# Proxy Object (Caching Proxy)
class CachedYouTubeProxy(YouTubeService):
    def __init__(self, real_service: YouTubeAPI):
        self.real_service = real_service
        self.cache = {}

    def fetch_video(self, video_id: str) -> str:
        if video_id in self.cache:
            print("Cache hit: Returning cached video data...")
            return self.cache[video_id]
        
        print("Cache miss: Fetching video from YouTube...")
        self.cache[video_id] = self.real_service.fetch_video(video_id)
        return self.cache[video_id]

# Client Code
if __name__ == "__main__":
    real_service = YouTubeAPI()
    proxy_service = CachedYouTubeProxy(real_service)
    
    # client doesn't have to bother which object is is calling.
    # First fetch - Cache miss
    print(proxy_service.fetch_video("abc123"))  # will only call the real_service if the doesn't contain in cache, so saves the computational time and resource

    # Second fetch - Cache hit
    print(proxy_service.fetch_video("abc123"))

    # Fetching a different video - Cache miss
    print(proxy_service.fetch_video("xyz789"))
