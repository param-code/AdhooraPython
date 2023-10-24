# from pytube import Playlist
# Play_list = Playlist("https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME")
# print(len(Play_list))
# for link in Play_list:
#     print(link)
# for video in Play_list.videos:
#     print(video.title)
# from pytube import YouTube

# def Download(link):
#     youtubeObject = YouTube(link)
#     youtubeObject = youtubeObject.streams.get_highest_resolution()
#     try:
#         youtubeObject.download()
#     except:
#         print("An error has occurred")
#     print("Download is completed successfully")


# link = input("Enter the YouTube video URL: ")
# Download(link)
# from pytube import Playlist
# Play_list = Playlist("https://youtube.com/playlist?list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz&feature=shared")
# stream = Play_list.get_highest_resolution()
# stream.download()