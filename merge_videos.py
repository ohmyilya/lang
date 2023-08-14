import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

def is_numeric_filename(filename):
    return filename[:-4].isdigit() and filename.endswith(".mp4")

def merge_videos(input_folder, output_file):
    video_clips = []
    all_files = os.listdir(input_folder)
    sorted_files = sorted(filter(is_numeric_filename, all_files), key=lambda x: int(x.split('.')[0]))
    
    for file_name in sorted_files:
        video_path = os.path.join(input_folder, file_name)
        video_clip = VideoFileClip(video_path)
        video_clip = video_clip.set_audio(video_clip.audio)  # Ensure the audio is included
        video_clips.append(video_clip)
    
    final_clip = concatenate_videoclips(video_clips)
    final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    input_folder = "output_videos"
    output_file = "merged_video.mp4"
    merge_videos(input_folder, output_file)
