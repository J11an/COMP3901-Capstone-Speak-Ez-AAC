<script setup>
//import { ref } from 'vue';

var tts = window.speechSynthesis;


function handleBackspace(){
  const word = document.getElementById('tile');
  word.remove()
  
}  

function handleClear(){
  const message = document.getElementById('message');
  message.innerHTML = '';
}  

</script>


<template>
  <div class="container msg-container">
    <div id="message" class="msg-display">
    </div>
    <!--<input id="input" class="msg-display"/>-->
      <!--<input type="text" class="mt-4 msg-bar ml-5" />-->
      <div class="btn-group btn-group-md options">
        <button class="btn"  @click="handleBackspace">
          <img src="/Backspace.png" alt="Backspace Icon" />
        </button>
        <button class="btn" @click="handleClear"><img src="/clear.png" alt="Clear Icon" /></button>
        <button class="btn" @click="somefunc"><img src="/SpeakerIcon.png" alt="Speaker Icon" /></button>
        <!---<img src="/Backspace.png" alt="Backspace Icon" />
        <img src="/SpeakerIcon.png" alt="Speaker Icon" />-->
      </div>
  </div>
</template>


<style>
.msg-container {
  width:100vw;
  height: 100px; /*maybe the size of whatver the title is set to here*/
  margin:10px;
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
