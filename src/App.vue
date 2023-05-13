<script>
import AppHeader from "./components/AppHeader.vue";
import MessageBar from "./components/MessageBar.vue";
import ListeningMessageContainer from "./components/ListeningMessageContainer.vue";
import SpeakingBoardContainer from "./components/SpeakingBoardContainer.vue";
import PhrasesContainer from "./components/PhrasesContainer.vue";

export default {
  components: {
    PhrasesContainer,
    SpeakingBoardContainer,
    AppHeader,
    ListeningMessageContainer,
    MessageBar,
  },
  data() {
    return {
      currentScreen: "SPEAKING",
      previousScreen: "",
      currentMessage: [],
      messageList: [],
      micActive: false,
      recognizer: new webkitSpeechRecognition() ? new webkitSpeechRecognition() : null,
      tts: window.speechSynthesis,
    };
  },
  methods: {
    updateBody(screen) {
      if (!(this.currentScreen==='SPEAKING' && screen==='SPEAKLISTEN')){
        if ((screen==='SPEAKLISTEN' || screen==='PINNED') && (this.currentScreen==='SPEAKLISTEN' || this.currentScreen==='PINNED')){
          this.currentScreen = this.previousScreen;
          this.previousScreen = "";
        } else if (screen==='SPEAKLISTEN' || screen==='PINNED') {
          this.previousScreen = this.currentScreen;
          this.currentScreen = screen;
        } else {
          this.currentScreen = screen;
        }
      }

    },
    updateMessage(request) {
      const requestType = request[0];
      const requestBody = request[1];
      if (requestType==='add'){
        this.currentMessage.push(requestBody);
      }
      if (requestType==='backspace' && this.currentMessage){
        this.currentMessage.pop();
      }
      if (requestType==='clear'){
        this.currentMessage = [];
      }
    },
    updateMessageList(request) {
      const from = request[0];
      const msg = request[1];
      if (from==='SPEAKER') {
        this.messageList.push({
          id: this.messageList.length!==0 ? this.messageList[this.messageList.length-1].id+1 : 0,
          msg: [...msg],
          from: from
        })
      } else {
        this.messageList.push({
          id: this.messageList.length!==0 ? this.messageList[this.messageList.length-1].id+1 : 0,
          msg: [...msg],
          from: from
        })
      }
    },
    updateMicState(newState){
      this.micActive = newState;
    },
    configureRecognizer(){
      if (this.recognizer){
        this.recognizer.continuous = true;
        this.recognizer.lang = "en-US";
        this.recognizer.interimResults = false;
        this.recognizer.maxAlternatives = 1;
        this.recognizer.onresult = (event) => {
          this.updateMessageList(["SPEAKER",event.results[event.results.length-1][0].transcript.split(" ").map(
              (val)=>{
                return {
                  id: -1,
                  word: val,
                }
              }
          )])
        };
      }

    },
  },
  mounted() {
    this.configureRecognizer();
  }
};
</script>

<template>
  <AppHeader @updateScreen="updateBody" :current-screen="currentScreen" />

  <main>
    <ListeningMessageContainer
      :message-list="messageList"
      :current-screen="currentScreen"
      :mic-state="micActive"
      :recognizer="recognizer"
      :tts="tts"
      v-if="currentScreen === 'LISTENING' || currentScreen==='SPEAKLISTEN'"
      @updateMessages="updateMessageList"
      @sendMicState="updateMicState"
    />

    <MessageBar
        :current-sentence="currentMessage"
        :tts="tts"
        @updateSentence="updateMessage"
        @updateMessages="updateMessageList"
        @updateMicState="updateMicState"
        @updateScreen="updateBody"
        v-if="
        currentScreen === 'SPEAKING' ||
        currentScreen === 'LISTENING' ||
        currentScreen === 'PINNED' ||
        currentScreen==='SPEAKLISTEN'
      "
    />

    <SpeakingBoardContainer :current-message="currentMessage" @updateScreen="updateBody" @updateSentence="updateMessage" v-if="currentScreen === 'SPEAKING' || currentScreen==='SPEAKLISTEN'" />

    <PhrasesContainer v-if="currentScreen === 'PHRASES'" />
  </main>
</template>

<style>
*{
  transition: 200ms;
}
</style>
