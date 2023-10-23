# Generate Videos Script

![MIT License](https://img.shields.io/badge/license-MIT-blue)

A Bash script for creating videos from a sequence of images using FFmpeg.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Introduction

The `generate_videos.sh` script is a convenient tool for creating videos from a series of images. It utilizes the FFmpeg multimedia framework to combine a collection of images into a video file. This script is particularly useful for creating time-lapse videos or animations from a sequence of image frames.

Key features and highlights:
- Simple to use: Just provide the script with a directory containing image frames, and it will generate a video for you.
- Customizable: You can easily adjust the frame rate and output format according to your needs.
- Requires FFmpeg: Ensure that FFmpeg is installed on your system before using the script.

## Prerequisites

Before using the `generate_videos.sh` script, you must have FFmpeg installed on your system. You can download and install FFmpeg from the official website: [FFmpeg](https://www.ffmpeg.org/download.html).

## Usage

1. Place your image frames in a directory (e.g., `frames/`) in sequential order, such as `image_0001.png`, `image_0002.png`, etc.

2. Open a terminal and navigate to the directory containing the script.

3. Run the script using the following command, specifying the input and output directories:

   ```bash
   ./generate_videos.sh

