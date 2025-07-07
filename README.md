# Overview

- Inspiration for this project came from tinkering with the NVIDIA Jetson Nano (https://github.com/mpromonet/webrtc-streamer) and similar open-source projects.
- Key Takeaways:
    * uses of SDP munging to force the use of specific codecs.
    * response latency of video streaming/use cases webrtc-internals

# Setup 

- Node.js (v22.14.0)
- Install package dependencies
- Setup OpenSSL certificate (HTTPS) localhost 
- Start server and begin application

```bash
npm run start:basic-p2p
```
<details>
    <summary>Install Node.js</summary>

Link: https://nodejs.org/en/download/ 

Download and install nvm (MacOS/Linux):

```bash
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.2/install.sh | bash

    \. "$HOME/.nvm/nvm.sh"

    nvm install 22

    node -v # Should print "v22.14.0".
    nvm current # Should print "v22.14.0".

    npm -v # Should print "10.9.2".
```

- Start server and run application
```bash
npm run start:basic-p2p
```

</details>

# Documentation 

- Descriptions below include diagrams and explanations for ```basic-p2p/js/main.js``` and ```p2pwebrtc/server.js```.

### Signaling Server

<details>
    <summary>Socket.IO</summary> 
   
- Update description Socket.IO
- Include description of signaling channel setup and event process
- Connecting to the signaling channel
- Description of signal callbacks ```registerScCallbacks()``` and placeholder functions for channel events


   
</details>

#### Namespace Utility

<details>
    <summary>Flowchart Diagram</summary>

##### Flowchart Diagram

   ![webrtc-signaling_channel_setup](https://github.com/user-attachments/assets/c5dd22af-572e-4d25-8f03-ca168972feca)

</details>


### Starting P2P Connection

- User-media permissions
- User-media functional setup
- Window: self property, read only property returns the window itself. [^1]

Basic media constraints for requesting access to the user's microphone and video. User must respond to the dialog box prompted by the browser to grant permissions.

```js
const $self = {
mediaConstraints: { audio: false, video: true },
};
```
[^1]: https://developer.mozilla.org/en-US/docs/Web/API/Window/self 


<details>
    <summary>Functions and Callback</summary>
   
##### Sequence Diagram

   ![peer-to-peer](https://github.com/user-attachments/assets/abe3c762-8596-4caf-a89f-464bc61ff1f1)

</details>



