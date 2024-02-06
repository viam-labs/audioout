# `audioout` modular service

This module implements the [`viam-labs:audioout` API](https://github.com/viam-labs/audioout-api) in a `pygame` model.
This modular service provides audio output capabilities via the Python [pygame mixer library](https://www.pygame.org/docs/ref/mixer.html).

## Requirements

If you want to run this module on a Linux-based machine, install prerequisites with the following commands:

``` bash
sudo apt update && sudo apt upgrade -y
sudo apt-get install python3
sudo apt install python3-pip python3-venv
sudo apt install python3-pyaudio
sudo apt-get install alsa-tools alsa-utils
sudo apt-get install flac
```

## Build and Run

To use this module, follow these instructions to [add a module from the Viam Registry](https://docs.viam.com/registry/configure/#add-a-modular-resource-from-the-viam-registry) and select the `viam-labs:audioout:pygame` model from the [`audioout` module](https://app.viam.com/module/viam-labs/audioout).

## Configure your `audioout:pygame` service

> [!NOTE]  
> Before configuring your service, you must [create a machine](https://docs.viam.com/manage/fleet/machines/#add-a-new-machine).

Navigate to the **Config** tab of your machine’s page in [the Viam app](https://app.viam.com/).
Click on the **Components** subtab and click **Create component**.
Select the `audioout` type, then select the `pygame` model. 
Enter a name for your service and click **Create**.

> [!NOTE]  
> For more information, see [Configure a Machine](https://docs.viam.com/manage/configuration/).

## Attributes

There are no attributes available for configuration with this service.

## Example Configuration

```json
{
  "services": [
    {
      "name": "my-audioout",
      "type": "audioout",
      "namespace": "viam-labs",
      "model": "viam-labs:audioout:pygame"
    }
  ],
  "modules": [
    {
      "type": "registry",
      "name": "viam-labs_audioout",
      "module_id": "viam-labs:audioout",
      "version": "0.0.6"
    }
  ],
  "packages": []
}
```

## API Usage

This service implements the [`viam-labs:audioout` API](https://github.com/viam-labs/audioout-api).

Please reference the API codebase to interact with your configured service through a Viam SDK.
Follow the instructions in [Using Audioout-api with the Python SDK](https://github.com/viam-labs/audioout-api?tab=readme-ov-file#using-audioout-api-with-the-python-sdk) to get started.

## Troubleshooting

When using a USB audio device, it may sometimes come up as the default, sometimes not.
To ensure that it comes up consistently as the default:

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

2. Ensure the USB device comes up first by editing /etc/modprobe.d/alsa-base.conf. 
Add content similar to:

```
options snd slots=snd-usb-audio,snd_soc_meson_card_utils
```
