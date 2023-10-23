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
* loop_count: How many times to play the audio file.  0 means once, -1 will loop infinitely (until stop() is called). Default 0.
* maxtime_ms: How long to play the audio for.  0 means no maxtime. Note that some file types like .wav do not support time indexing so this will fail. Default 0.
* fadein_ms: If non-zero, will make the sound start playing at 0 volume and fade up to full volume over the time given. The sample may end before the fade-in is complete.  Default 0.
* block: If False, will play sound async.  If true, will not return until sound is complete.  Default False.

This method returns a string response, which is the file_path that was passed in to the *play()* request.

### stop()

The *stop()* command will stop sound playback on any active channels.

If successful, will return the string "OK".

## Viam Service Configuration

There are currently no attributes available to configure for this module.

## Using audioout with the Python SDK

Because this module uses a custom protobuf-based API, you must include this project in your client code.  One way to do this is to include it in your requirements.txt as follows:

```
audioout @ git+https://github.com/viam-labs/audioout.git@main
```

You can now import and use it in your code as follows:

```
from audioout import Audioout
ao = Audioout.from_robot(robot, name="audioout")
ao.play(...)
```

## Troubleshooting

When using a USB audio device, it may sometimes come up as the default, sometimes not.  To ensure that it comes up consistently as the default:

1. check the existing alsa modules:

```
cat /proc/asound/modules
```

This will output something like:

```
 0 snd_usb_audio
 2 snd_soc_meson_card_utils
 3 snd_usb_audio
```

2. ensure the USB device comes up first by editing /etc/modprobe.d/alsa-base.conf, adding content similar to:

```
options snd slots=snd-usb-audio,snd_soc_meson_card_utils
```
