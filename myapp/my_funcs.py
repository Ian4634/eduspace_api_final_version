def move_forward(videos, original, new):
    new = int(new)
    original = int(original)
    # videos is a list of Video objects
    affected_videos = []
    for video in videos:
        if int(video.position) >= new and int(video.position) <= original:
            affected_videos.append(video)
        else:
            continue
    # actual works
    count = 0
    affected_videos.reverse()
    print(affected_videos)
    for video in affected_videos:
        if count == 0: 
            video.position = new
            video.save()
            count += 1
        else:
            video.position = int(video.position) + 1
            video.save()
    

def move_backward(videos, original, new):
    pass

def move(videos, original, new):
    if original > new:
        move_forward(videos, original, new)
    else:
        move_backward(videos, original, new)


v = [0,1,2,3]
v.reverse()
print(v)