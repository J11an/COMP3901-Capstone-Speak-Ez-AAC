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
      currentMessage: [],
      messageList: []
    };
  },
  methods: {
    updateBody(screen) {
      this.currentScreen = screen;
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
      console.log(this.messageList);
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
      v-if="currentScreen === 'LISTENING'"
    />

    <MessageBar
        :current-sentence="currentMessage"
        @updateScreen="updateBody"
        @updateSentence="updateMessage"
        @updateMessages="updateMessageList"
        v-if="
        currentScreen === 'SPEAKING' ||
        currentScreen === 'LISTENING' ||
        currentScreen === 'PINNED'
      "
    />

    <PinnedWordsContainer v-if="currentScreen === 'PINNED'" />

    <SpeakingBoardContainer @updateSentence="updateMessage" v-if="currentScreen === 'SPEAKING'" />

    <PhrasesContainer v-if="currentScreen === 'PHRASES'" />
  </main>
</template>

<style></style>
