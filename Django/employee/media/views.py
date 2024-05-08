from django.shortcuts import render

# Create your views here.
from .models import Media

def media_list(request):
    # Retrieve all audio files
    audio_files = Media.objects.audio()

    # Retrieve all video files
    video_files = Media.objects.video()

    # Retrieve all image files
    image_files = Media.objects.images()

    return render(request, 'media_list.html', {'audio_files': audio_files, 'video_files': video_files, 'image_files': image_files})
