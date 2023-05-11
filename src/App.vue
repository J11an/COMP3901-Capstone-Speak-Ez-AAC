<script>
import AppHeader from "./components/AppHeader.vue";
import MessageBar from "./components/MessageBar.vue";
import ListeningMessageContainer from "./components/ListeningMessageContainer.vue";
import SpeakingBoardContainer from "./components/SpeakingBoardContainer.vue";
import PinnedWordsContainer from "./components/PinnedWordsContainer.vue";
import PhrasesContainer from "./components/PhrasesContainer.vue";

export default {
  components: {
    PhrasesContainer,
    PinnedWordsContainer,
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
      messageList: []
    };
  },
  methods: {
    updateBody(screen) {
      if ((screen==='SPEAKLISTEN' || screen==='PINNED') && (this.currentScreen==='SPEAKLISTEN' || this.currentScreen==='PINNED')){
        this.currentScreen = this.previousScreen;
        this.previousScreen = "";
      } else if (screen==='SPEAKLISTEN' || screen==='PINNED') {
        this.previousScreen = this.currentScreen;
        this.currentScreen = screen;
      } else {
        this.currentScreen = screen;
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
      this.messageList.push({
        id: this.messageList.length!==0 ? this.messageList[this.messageList.length-1].id+1 : 0,
        msg: msg,
        from: from
      })
    }
  },
  mounted() {
  },
};
</script>

<template>
  <AppHeader @updateScreen="updateBody" />

  <main>
    <ListeningMessageContainer
      :message-list="messageList"
      :current-screen="currentScreen"
      v-if="currentScreen === 'LISTENING' || currentScreen==='SPEAKLISTEN'"
    />

    <MessageBar
        :current-sentence="currentMessage"
        @updateScreen="updateBody"
        @updateSentence="updateMessage"
        @updateMessages="updateMessageList"
        v-if="
        currentScreen === 'SPEAKING' ||
        currentScreen === 'LISTENING' ||
        currentScreen === 'PINNED' ||
        currentScreen==='SPEAKLISTEN'
      "
    />

    <PinnedWordsContainer v-if="currentScreen === 'PINNED'" />

    <SpeakingBoardContainer :current-message="currentMessage" @updateSentence="updateMessage" v-if="currentScreen === 'SPEAKING' || currentScreen==='SPEAKLISTEN'" />

    <PhrasesContainer v-if="currentScreen === 'PHRASES'" />
  </main>
</template>

<style>
*{
  transition: 200ms;
}
</style>
