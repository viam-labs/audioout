# audioout modular service

*audioout* is a Viam modular service that provides audio output capabilities via the Python [pygame mixer library](https://www.pygame.org/docs/ref/mixer.html)

## Prerequisites

``` bash
sudo apt update && sudo apt upgrade -y
sudo apt-get install python3
sudo apt install python3-pip
sudo apt install python3-pyaudio
sudo apt-get install alsa-tools alsa-utils
sudo apt-get install flac
```

## API

The audioout resource provides the following API:

### play(file_path=*string*, loop_count=*int*(0), maxtime_ms=*int*(0), fadein_ms=*int*(0), block=*bool*)

The *play()* command takes:

* file_path: The audio file on device to play
* loop_count: How many times to play the audio file.  0 means once, -1 will loop infinitely (until stop() is called).
* maxtime_ms: How long to play the audio for.  Note that some file types like .wav do not support time indexing so this will fail.
* fadein_ms: If non-zero, will make the sound start playing at 0 volume and fade up to full volume over the time given. The sample may end before the fade-in is complete.
* block: If False, will play sound async.  If true, will not return until sound is complete.

This method returns a string response, which is the file_path that was passed in to the *play()* request.

### stop()

The *stop()* command will stop sound playback on any active channels.

If successful, will return the string "OK".

## Viam Service Configuration

The following attributes may be configured as speech service config attributes.
For example: the following configuration would set up listening mode, use an ElevenLabs voice "Antoni", make AI completions available, and use a 'Gollum' persona for AI completions:

``` json
{
   "mic_device_name": "myMic"
}
```

### mic_device_name

*string (default: "")*

If not set, will attempt to use the first available microphone device.
Available microphone device names will logged on module startup.
