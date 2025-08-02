import os, time
from googleapiclient.discovery import build
import yt_dlp
from moviepy.editor import VideoFileClip, concatenate_videoclips
from upload_script import upload_video
import config

def get_top_videos():
    yt = build("youtube", "v3", developerKey=config.YT_API_KEY)
    resp = yt.videos().list(
        part="snippet,statistics",
        chart="mostPopular",
        regionCode=config.REGION,
        maxResults=config.NUM_VIDEOS
    ).execute()
    return resp.get("items", [])

def download_cc(video_id):
    opts = {'outtmpl': f"{video_id}.%(ext)s", 'format': 'best'}
    opts['match_filter'] = yt_dlp.utils.match_filter_func("license==cc")
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([f"https://www.youtube.com/watch?v={video_id}"])

def add_intro(video_id):
    clip = VideoFileClip(f"{video_id}.mp4")
    intro = VideoFileClip("intro.mp4")
    final = concatenate_videoclips([intro, clip])
    out = f"{video_id}_final.mp4"
    final.write_videofile(out, codec="libx264")
    return out

def main():
    videos = get_top_videos()
    for vid in videos[:config.NUM_VIDEOS]:
        vid_id = vid['id']
        title = "REUPLOAD: "+vid['snippet']['title']
        desc = vid['snippet']['description']
        download_cc(vid_id)
        filepath = add_intro(vid_id) if os.path.exists("intro.mp4") else f"{vid_id}.mp4"
        upload_video(filepath, title, desc)
        time.sleep(5)

if __name__ == "__main__":
    main()
