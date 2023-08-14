#!/bin/bash

images_folder="images"
audio_folder="output_phrases"
output_folder="output_videos"

mkdir -p "$output_folder"

# Create an array to store the video paths
video_paths=()

for audio_file in "$audio_folder"/*.wav; do
    if [[ -f "$audio_file" ]]; then
        audio_filename=$(basename "$audio_file")
        image_number="${audio_filename%.*}"
        image_file="${image_number}.png"
        image_path="${images_folder}/${image_file}"
        output_file="${image_number}.mp4"
        output_path="${output_folder}/${output_file}"

        ffmpeg -loop 1 -i "$image_path" -i "$audio_file" -c:v libx264 -tune stillimage -c:a aac -b:a 192k -vf "scale=1920:1080,setsar=1:1" -pix_fmt yuv420p -shortest -strict -2 "$output_path"

        # Add the video path to the array
        video_paths+=("file '$output_file'")
    fi
done

# Sort the video paths based on numeric filenames
IFS=$'\n' sorted_video_paths=($(sort -V <<<"${video_paths[*]}"))
unset IFS

# Create a text file containing the list of sorted video files
list_file="${output_folder}/video_list.txt"
printf "%s\n" "${sorted_video_paths[@]}" > "$list_file"

# Concatenate all generated videos into one
concatenated_videos="${output_folder}/all_generated_videos.mp4"
ffmpeg -f concat -safe 0 -i "$list_file" -c copy "$concatenated_videos"

# Remove the temporary text file
rm "$list_file"
