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

The audioout resource implements the [viam-labs audioout API](https://github.com/viam-labs/audioout-api).

Please also use the API codebase to interact with a configured version of this service via Viam SDK.

## Viam Service Configuration

There are currently no attributes available to configure for this module.

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
