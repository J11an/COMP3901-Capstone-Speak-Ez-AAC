<script>
import Message from "../components/Listening/Message.vue";

export default {
  components: { Message },
  props: {
    messageList: Array,
    currentScreen: String,
    micState: Boolean,
    recognizer: Object,
    tts: Object,
  },
  data(){
    return {
      currentClass: '',
      listeningActive: false,
      cachedRecognizedWord: []
    }
  },
  watch: {
    micState : {
      handler(){
        this.toggleListening();
      },
      deep: true
    }
  },
  mounted() {
    this.scrollToBottom();
    if (this.micState){
      this.toggleListening()
    }
  },
  updated() {
    this.scrollToBottom();
  },
  unmounted() {
    this.$emit('unloadMic',false);
  },
  methods:{
    toggleListening(){
      if (!this.listeningActive){
        this.recognizer.start();
        console.log("Ready to receive audio");
      } else {
        this.recognizer.abort();
        console.log("Audio Off");
      }
      this.listeningActive = !this.listeningActive;
    },
    scrollToBottom(){
        const container = document.querySelector('#con-container');
        container.scrollTop = container.scrollHeight;
    },
  },
};
</script>

<template>
  <!-- Messages container at top -->
  <div :class="this.currentScreen!=='SPEAKLISTEN' ? 'conversation-container' : 'mixed-conversation-container'" id="con-container">
    <!-- Go through all messages -->
    <div class="msg-body-container" v-for="message in messageList" v-bind:key="message.id">
      <Message :msg="message.msg" :from="message.from" :tts="tts"/>
    </div>


    <div id="anchor"></div>
  </div>
</template>

<style>
.conversation-container {
  /*border: solid red 1px;*/
  margin: 10px;
  padding: 10px;
  overflow: auto;
  min-height: 73vh;
  max-height: 73vh;

  @media (max-height: 1040px) {
    min-height: 66vh;
    max-height: 66vh;
  }

  @media (max-height: 876px) {
    min-height: 60vh;
    max-height: 60vh;
  }

  @media (max-height: 738px) {
    min-height: 49vh;
    max-height: 49vh;
  }
}

.mixed-conversation-container {
  /*border: solid red 1px;*/
  margin: 10px;
  padding: 10px;
  overflow: auto;
  min-height: 30vh;
  max-height: 30vh;
}

.msg-body-container {
  display: flex;
  margin: 1vw;
}
</style>
