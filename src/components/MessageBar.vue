<script>
import WordPictureTileMessage from "./WordPictureTileMessage.vue";

export default {
  components:{WordPictureTileMessage},
  props:{
    currentSentence: Array
  },
  data(){
    return {
      tts: window.speechSynthesis,
      micActive: false
    }
  },
  methods:{
    handleBackspace() {
      this.$emit("updateSentence", ['backspace',{}]);
    },
    handleClear() {
      this.$emit("updateSentence", ['clear',{}]);
    },
    handleSpeaker() {
      this.tts.speak(new SpeechSynthesisUtterance(this.currentSentence.map((wordObj)=>wordObj.word).join(" ")));
      this.$emit("updateMessages",["LISTENER",this.currentSentence]);
    },
    updateScreen(screen) {
      this.$emit("updateScreen",screen);
    },
    toggleListening(){
      this.micActive = !this.micActive;
      this.$emit("updateMicState",this.micActive);
    }
  }
}


</script>
<template>
  <div class="container msg-container">
    <div id="message" class="msg-display d-flex flex-wrap" @click="updateScreen('SPEAKLISTEN')">
      <div class="word-tile" v-for="word in currentSentence" v-bind:key="word.id">
              <WordPictureTileMessage :word="word.word.toUpperCase()"
                               :symbol="word.symbol"/>
      </div>
    </div>

    <div class="btn-group btn-group-md options">
      <button class="btn" @click="handleBackspace">
        <img src="/Backspace.png" alt="Backspace Icon" />
      </button>
      <button class="btn" @click="handleClear">
        <img src="/clear.png" alt="Clear Icon" />
      </button>
      <button class="btn" @click="handleSpeaker">
        <img src="/SpeakerIcon.png" alt="Speaker Icon" />
      </button>
      <button class="btn" @click="toggleListening">
        <img src="/micOff.png" alt="Mic Off" v-if="!this.micActive"/>
        <img src="/micOn.png" alt="Mic On" v-else/>
      </button>
      <button class="btn" @click="updateScreen('PINNED')">
        <img src="/pinned_folder.png" alt="Speaker Icon" />
      </button>
    </div>

  </div>
</template>

<style scoped>
#message{
  cursor: pointer;
  width: 100vw;
  height: 100px;
}
#message:hover{
  background-color: lightblue;
}

.msg-container {

  margin-top: 10px;
  padding: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: row;
  @media (max-width: 1200px) {
    flex-wrap: wrap;
  }
}

.msg-display {
  height: 100%;
  width: 90%;
  display: flex;
  background: #ffffff;
  border: 2px solid black;
  border-radius: 20px;
}

.btn-group .options {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  margin: auto;
}

.btn img {
  width: 70px;
  height: 70px;
}
</style>
