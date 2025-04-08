from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import ImageClip
import os


def create_video(image_path, audio_path, output_path):
    try:
        # Verify input files exist
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio file not found: {audio_path}")

        # Load the audio first to get its duration
        audio_clip = AudioFileClip(audio_path)

        # Load the image with the audio duration
        image_clip = ImageClip(image_path, duration=audio_clip.duration)

        # Create video clip with audio
        video_clip = image_clip
        video_clip.audio = audio_clip

        # Write the result to a video file
        video_clip.write_videofile(output_path, fps=24)

        print(f"Video successfully created at: {output_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Clean up resources
        try:
            audio_clip.close()
            image_clip.close()
            video_clip.close()
        except:
            pass


if __name__ == "__main__":
    # Replace these with your actual file paths
    image_path = "image.png"  # or "image.png"
    audio_path = "audio.wav"
    output_path = "output.mp4"

    create_video(image_path, audio_path, output_path)
