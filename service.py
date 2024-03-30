from moviepy.editor import *
import os

video_types = ['avi','mov','mp4']
START_URL = 'before'
END_URL = 'after'

def compression_and_thumbnail(starturl,endurl,comp_size):
    for filename in os.listdir(starturl):
        if filename.split(".")[1] not in video_types:
            continue
        clip = VideoFileClip(starturl + str('/') + str(filename))
        height = clip.h
        width = clip.w
        min_dim = min(width,height)
        image_url = 'thumbnails/'
        if min_dim <=comp_size:
            clip = clip
        elif min_dim>comp_size:
            if min_dim == height:
                clip = clip.resize(height=comp_size)
            elif min_dim == width:
                clip = clip.resize(width=comp_size)
        final_vid = endurl+'/'+filename.split(".")[0] + '.mp4'
        img = clip.get_frame(1)
        clip.save_frame(image_url + filename.split(".")[0] + '.jpg',t=1)
        clip.write_videofile(final_vid)
compression_and_thumbnail(START_URL,END_URL,720)