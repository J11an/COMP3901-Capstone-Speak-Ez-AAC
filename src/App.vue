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
        console.log(this.currentMessage);
      }
      if (requestType==='backspace' && this.currentMessage){
        this.currentMessage.pop();
      }
      if (requestType==='clear'){
        this.currentMessage = [];
      }
    }
  },
  mounted() {

    const fromArr = ["SPEAKER", "LISTENER"];
    for (let i = 0; i < 15; i++) {
      const from = fromArr[Math.round(Math.random())];
      this.messageList.push({
        id: i,
        msg: `This is a test message from the ${from}`,
        from: from,
      });
    }
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
