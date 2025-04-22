<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>CLASSIFIED: SECURE CONSOLE</title>
  <style>
    html, body {
      margin: 0;
      padding: 0;
      height: 100%;
      width: 100%;
      overflow: hidden;
      font-family: 'Courier New', monospace;
      background: #0a0a0a;
      color: #00ff00;
      display: flex;
      justify-content: center;
      align-items: center;
      box-sizing: border-box;
    }
    #backgroundVideo {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      z-index: -1;
      opacity: 0.1;
      filter: grayscale(100%);
    }
    .wrapper {
      width: 95%;
      max-width: 1200px;
      height: 90vh;
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      align-items: stretch;
      padding: 10px;
      position: relative;
      z-index: 1;
      box-sizing: border-box;
      border: 2px solid #00ff00;
      box-shadow: 0 0 15px rgba(255, 0, 0, 0.5);
    }
    .main-console {
      flex: 3;
      display: flex;
      flex-direction: column;
      padding: 10px;
    }
    .sidebar {
      flex: 1;
      background: rgba(10, 0, 0, 0.8);
      padding: 10px;
      border-left: 1px solid #00ff00;
      display: flex;
      flex-direction: column;
      align-items: center;
      overflow-y: auto;
    }
    .media-panel {
      width: 100%;
      margin-bottom: 10px;
      text-align: center;
    }
    .media-panel img, .media-panel video {
      max-width: 100%;
      max-height: 150px;
      object-fit: contain;
      border: 1px solid #00ff00;
      box-shadow: 0 0 10px rgba(255, 0, 0, 0.3);
      cursor: pointer;
    }
    #videoContainer {
      width: 100%;
      max-width: 300px;
      aspect-ratio: 1/1;
      margin: 0 auto 10px;
      overflow: hidden;
      border: 2px solid #00ff00;
      box-shadow: 0 0 15px rgba(255, 0, 0, 0.5);
      display: flex;
      align-items: center;
      justify-content: center;
      background: #000;
    }
    #videoContainer video, #videoContainer img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center;
      filter: contrast(1.2) brightness(1.1);
    }
    #chatContainer {
      flex: 1;
      width: 100%;
      padding: 10px;
      background: rgba(10, 0, 0, 0.8);
      border: 1px solid #00ff00;
      margin-top: 10px;
      display: flex;
      flex-direction: column;
    }
    #chatContainer h2 {
      margin: 0 0 10px;
      font-size: 1.8em;
      color: #00ff00;
      text-shadow: 0 0 10px rgba(255, 0, 0, 0.9);
      letter-spacing: 2px;
      text-transform: uppercase;
      text-align: center;
      animation: blink 1.5s infinite;
    }
    #chatbox {
      flex: 1;
      max-height: 200px;
      overflow-y: auto;
      margin-bottom: 10px;
      background: #000;
      border: 1px solid #00ff00;
      padding: 8px;
      box-shadow: inset 0 0 10px rgba(255, 0, 0, 0.1);
      font-size: 0.95em;
    }
    .message {
      padding: 6px;
      margin-bottom: 6px;
      border-radius: 3px;
      text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.8);
    }
    .user {
      background: linear-gradient(90deg, #330000, #220000);
      text-align: right;
      color: #00ff00;
    }
    .bot {
      background: linear-gradient(90deg, #110000, #080000);
      text-align: left;
      color: #00ff00;
    }
    input, button {
      padding: 10px;
      font-size: 0.95em;
      width: 100%;
      border: none;
      outline: none;
      border-radius: 3px;
      margin-bottom: 8px;
      transition: all 0.3s ease;
      box-sizing: border-box;
      font-family: 'Courier New', monospace;
    }
    input {
      background: #000;
      color: #00ff00;
      border: 1px solid #00ff00;
      box-shadow: 0 0 10px rgba(255, 0, 0, 0.2);
      text-align: left;
    }
    input::placeholder {
      color: #cc0000;
      text-transform: uppercase;
    }
    button {
      background: linear-gradient(90deg, #ff0000, #cc0000);
      color: #00ff00;
      cursor: pointer;
      font-weight: bold;
      text-transform: uppercase;
      box-shadow: 0 0 15px rgba(0, 255, 0, 0.5);
    }
    button:hover {
      background: linear-gradient(90deg, #cc0000, #990000);
      box-shadow: 0 0 20px rgba(0, 255, 0, 0.7);
    }
    .modal {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.9);
      z-index: 1000;
      justify-content: center;
      align-items: center;
    }
    .modal-content {
      max-width: 80%;
      max-height: 80%;
      object-fit: contain;
      border: 2px solid #00ff00;
      box-shadow: 0 0 20px rgba(255, 0, 0, 0.5);
    }
    .modal-close {
      position: absolute;
      top: 20px;
      right: 20px;
      color: #ff0000;
      font-size: 2em;
      cursor: pointer;
    }
    @keyframes pulse {
      0% { box-shadow: 0 0 10px rgba(0, 255, 0, 0.3), 0 0 5px rgba(255, 0, 0, 0.3); }
      50% { box-shadow: 0 0 20px rgba(0, 255, 0, 0.6), 0 0 10px rgba(255, 0, 0, 0.6); }
      100% { box-shadow: 0 0 10px rgba(0, 255, 0, 0.3), 0 0 5px rgba(255, 0, 0, 0.3); }
    }
    @keyframes blink {
      0% { opacity: 1; }
      50% { opacity: 0.5; }
      100% { opacity: 1; }
    }
    #videoContainer, button, .media-panel img, .media-panel video {
      animation: pulse 3s infinite ease-in-out;
    }
    @media (max-width: 768px) {
      .wrapper {
        flex-direction: column;
        width: 98%;
        height: 95vh;
      }
      .sidebar {
        flex: none;
        height: 150px;
        flex-direction: row;
        overflow-x: auto;
        border-left: none;
        border-top: 1px solid #00ff00;
      }
      .media-panel {
        flex: 0 0 auto;
        margin-right: 10px;
      }
      .media-panel img, .media-panel video {
        max-width: 100px;
        max-height: 100px;
      }
      #videoContainer {
        max-width: 200px;
      }
      #chatContainer h2 {
        font-size: 1.5em;
      }
      #chatbox {
        max-height: 150px;
        font-size: 0.9em;
      }
    }
    @media (max-width: 500px) {
      #videoContainer {
        max-width: 150px;
      }
      #chatContainer h2 {
        font-size: 1.2em;
      }
      input, button {
        padding: 8px;
        font-size: 0.9em;
      }
    }
  </style>
</head>
<body>
  <video id="backgroundVideo" playsinline autoplay loop muted>
    <source src="background.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="wrapper">
    <div class="main-console">
      <div id="videoContainer"></div>
      <div id="chatContainer">
        <h2>SECURE CONSOLE: ACCESS GRANTED</h2>
        <div id="chatbox"></div>
        <input id="userInput" type="text" placeholder="ENTER QUERY [CLASSIFIED]">
        <button id="sendButton">TRANSMIT</button>
      </div>
    </div>
    <div class="sidebar">
      <div class="media-panel">
        <img src="console_screenshot.png" alt="Console Screenshot" onclick="openModal('console_screenshot.png')">
        <p>System Log</p>
      </div>
      <div class="media-panel">
        <video loop muted onclick="openModal('code_execution.mp4')">
          <source src="code_execution.mp4" type="video/mp4">
        </video>
        <p>Code Execution</p>
      </div>
    </div>
  </div>
  <div id="modal" class="modal">
    <span class="modal-close" onclick="closeModal()">×</span>
    <img id="modal-content" class="modal-content">
  </div>

  <script>
    const inputField = document.getElementById("userInput");
    const sendButton = document.getElementById("sendButton");
    const chatbox = document.getElementById("chatbox");
    const videoContainer = document.getElementById("videoContainer");
    const modal = document.getElementById("modal");
    const modalContent = document.getElementById("modal-content");

    // Detect mobile devices
    const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);

    // Set up video or image based on device
    let ugaVideo = null;
    if (!isMobile) {
      ugaVideo = document.createElement("video");
      ugaVideo.id = "ugaVideo";
      ugaVideo.loop = true;
      ugaVideo.muted = true;
      ugaVideo.innerHTML = `<source src="348910056580788233.mp4" type="video/mp4">`;
      videoContainer.appendChild(ugaVideo);
    } else {
      const ugaImage = document.createElement("img");
      ugaImage.id = "ugaImage";
      ugaImage.src = "StillImage.png";
      ugaImage.alt = "Secure Console Still";
      videoContainer.appendChild(ugaImage);
    }

    // Function to get the best elderish voice
    function getElderVoice() {
      const voices = speechSynthesis.getVoices();
      const preferredVoices = voices.filter(voice => 
        (voice.lang === "en-GB" || voice.lang === "en-US") &&
        (voice.name.toLowerCase().includes("male") || 
         voice.name.includes("Daniel") || 
         voice.name.includes("David") || 
         voice.name.includes("Mark"))
      );
      return preferredVoices[0] || voices.find(voice => voice.default) || voices[0] || null;
    }

    // Ensure voices are loaded before using
    let voicesLoaded = false;
    speechSynthesis.onvoiceschanged = () => {
      voicesLoaded = true;
    };
    speechSynthesis.getVoices();

    sendButton.addEventListener("click", sendMessage);
    inputField.addEventListener("keydown", function(e) {
      if (e.key === "Enter") sendMessage();
    });

    async function sendMessage() {
      const userText = inputField.value.trim();
      if (!userText) return;

      chatbox.innerHTML = "";
      chatbox.innerHTML += `<div class="message user">OPERATOR: ${userText}</div>`;
      inputField.value = "";

      try {
        const response = await fetch("https://elderugachatbot.onrender.com/chat", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ message: userText })
        });

        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

        const data = await response.json();
        chatbox.innerHTML += `<div class="message bot">SYSTEM: ${data.reply}</div>`;
        chatbox.scrollTop = chatbox.scrollHeight;

        // Play response with Web Speech API
        if ('speechSynthesis' in window) {
          const utterance = new SpeechSynthesisUtterance(data.reply);
          utterance.pitch = 0.8;
          utterance.rate = 0.7;
          utterance.volume = 1.0;
          const elderVoice = getElderVoice();
          if (elderVoice) {
            utterance.voice = elderVoice;
          }

          // Play video synced with voice on non-mobile devices
          if (!isMobile && ugaVideo) {
            ugaVideo.playbackRate = 1.5;
            ugaVideo.currentTime = 0;
            ugaVideo.play().catch(error => console.error("Video playback failed:", error));
            utterance.onend = () => {
              ugaVideo.pause();
              ugaVideo.currentTime = 0;
            };
          }

          speechSynthesis.speak(utterance);
        } else {
          console.warn("Web Speech API not supported in this browser.");
        }
      } catch (error) {
        console.error('Console response error:', error);
        chatbox.innerHTML += `<div class="message bot">SYSTEM ERROR: ${error.message}</div>`;
      }
    }

    // Modal functions for media
    function openModal(src) {
      modalContent.src = src;
      modal.style.display = "flex";
      if (src.endsWith('.mp4')) {
        modalContent.outerHTML = `<video id="modal-content" class="modal-content" autoplay loop muted><source src="${src}" type="video/mp4"></video>`;
     /keys/fake_key.pem
      } else {
        modalContent.outerHTML = `<img id="modal-content" class="modal-content" src="${src}">`;
      }
    }

    function closeModal() {
      modal.style.display = "none";
      const video = modal.querySelector('video');
      if (video) video.pause();
    }

    // Close modal on click outside
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeModal();
    });
  </script>
</body>
</html>