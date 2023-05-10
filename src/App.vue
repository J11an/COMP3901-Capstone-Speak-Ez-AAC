<script>
import AppHeader from "@/components/AppHeader.vue";
import MessageBar from "./components/MessageBar.vue"
import ListeningMessageContainer from "./components/ListeningMessageContainer.vue";
import SpeakingBoardContainer from "./components/SpeakingBoardContainer.vue";
import PinnedWordsContainer from "./components/PinnedWordsContainer.vue";
import PhrasesContainer from "./components/PhrasesContainer.vue";

export default {
  components : {
    PhrasesContainer,
    PinnedWordsContainer, SpeakingBoardContainer, AppHeader, ListeningMessageContainer, MessageBar},
  data() {
    return {
      currentMessage: [],
      messageList: [],
      currentScreen:"SPEAKING"
    }
  },
  methods : {
    updateBody(screen){
      this.currentScreen = screen
    }
  },
  mounted() {
    this.columns = {
      noun: [1, 1, 1, 1],
      verb: [2, 2, 2, 2],
      adjective: [3, 3, 3, 3],
      article: [4, 4, 4, 4],
    };
    this.currentSetence = ["I", "eat"];
    const fromArr = ["SPEAKER","LISTENER"];
    for (let i = 0; i < 15; i++) {
        const from = fromArr[Math.round(Math.random())];
        this.messageList.push({
          id: i,
          msg:`This is a test message from the ${from}`,
          from: from,
        })
    }
  }
}
</script>

<template>

  <AppHeader @updateScreen="updateBody"/>

  <main>

    <ListeningMessageContainer :message-list="messageList" v-if="currentScreen==='LISTENING'"/>

    <MessageBar @updateScreen="updateBody" v-if="currentScreen==='SPEAKING' || currentScreen==='LISTENING' || currentScreen==='PINNED'"/>

    <PinnedWordsContainer v-if="currentScreen==='PINNED'" />

    <SpeakingBoardContainer v-if="currentScreen==='SPEAKING'"/>

    <PhrasesContainer v-if="currentScreen==='PHRASES'"/>

  </main>

</template>

<style>

</style>
