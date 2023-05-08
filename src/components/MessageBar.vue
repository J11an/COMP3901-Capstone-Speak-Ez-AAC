<script setup>
import { ref } from 'vue';

let tts = window.speechSynthesis;
/*let voice = tts.getVoices().filter(function (voice) {return voice.lang === 'en';})[0];*/


function handleBackspace(){
  const message = document.getElementById('message');
  message.lastChild.remove()
}  

function handleClear(){
  const message = document.getElementById('message');
  message.innerHTML = '';
}  

function handleSpeaker(){
  const sentence = ref(document.querySelectorAll("div#word p"))
  var utterance
  sentence.value.forEach(word => {
    console.log("word:", word.textContent) 
    utterance = new SpeechSynthesisUtterance(word.textContent);
    // Speak the utterance
    tts.speak(utterance);
  });
}

</script>


<template>
  <div class="container msg-container">
    <div id="message" class="msg-display" @input="handleSpeaker">
    </div>
    <!--<input id="input" class="msg-display"/>-->
      <!--<input type="text" class="mt-4 msg-bar ml-5" />-->
      <div class="btn-group btn-group-md options">
        <button class="btn"  @click="handleBackspace">
          <img src="/Backspace.png" alt="Backspace Icon" />
        </button>
        <button class="btn" @click="handleClear"><img src="/clear.png" alt="Clear Icon" /></button>
        <button class="btn" @click="handleSpeaker"><img src="/SpeakerIcon.png" alt="Speaker Icon" /></button>
        <!---<img src="/Backspace.png" alt="Backspace Icon" />
        <img src="/SpeakerIcon.png" alt="Speaker Icon" />-->
      </div>
  </div>
</template>


<style>
.msg-container {
  width:100vw;
  height: 100px; /*maybe the size of whatver the title is set to here*/
  margin-top:10px;
  padding: 10px;
  display:flex;
  flex-direction: row;
}

.msg-display{
  height: 100%;
  width: 90%;
  display: flex;
  background: #ffffff;
  border: 2px solid black;
  border-radius: 20px;
}

 .btn-group .options{
  display: flex;
  flex-direction: row;
}

button img {
  width: 100%;
  height: 100%;
}
</style>
