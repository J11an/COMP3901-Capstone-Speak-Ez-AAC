<script>
import Message from "./Message.vue";

export default {
  components: { Message },
  props: {
    messageList: Array,
    currentScreen: String,
    micState: Boolean,
    recognizer: Object,
    tts: Object,
  },
  data() {
    return {
      currentClass: "",
      listeningActive: false,
      cachedRecognizedWord: [],
    };
  },
  watch: {
    micState: {
      handler() {
        this.toggleListening();
      },
      deep: true,
    },
  },
  mounted() {
    this.scrollToBottom();
    if (this.micState) {
      this.toggleListening();
    }
  },
  updated() {
    this.scrollToBottom();
  },
  unmounted() {
    this.$emit("sendMicState", this.micState);
    this.recognizer.abort();
  },
  methods: {
    toggleListening() {
      if (!this.listeningActive) {
        this.recognizer.start();
        console.log("Ready to receive audio");
      } else {
        this.recognizer.abort();
        console.log("Audio Off");
      }
      this.listeningActive = !this.listeningActive;
    },
    scrollToBottom() {
      const container = document.querySelector("#con-container");
      container.scrollTop = container.scrollHeight;
    },
    sendTileAudio(word) {
      this.$emit("playAudio",word);
    }
  },
};
</script>

<template>
  <!-- Messages container at top -->
  <div
    :class="
      this.currentScreen !== 'SPEAKLISTEN'
        ? 'conversation-container'
        : 'mixed-conversation-container'
    "
    id="con-container"
  >
    <!-- Go through all messages -->
    <div
      class="msg-body-container"
      v-for="message in messageList"
      v-bind:key="message.id"
    >
      <Message :msg="message.msg" :from="message.from" @playMessageTile="sendTileAudio" />
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

  @media (max-width: 1200px) {
    min-height: 67vh;
    max-height: 67vh;
  }

  @media (max-width: 1200px) and (max-height:984px) {
    min-height: 60vh;
    max-height: 60vh;
  }

  @media (max-width: 1200px) and (max-height:814px) {
    min-height: 55vh;
    max-height: 55vh;
  }
}

.conversation-container {
  overflow-y: scroll;
}
.conversation-container::-webkit-scrollbar {
  width: 5px;
}
.conversation-container::-webkit-scrollbar-track {
  background: #eee;
}
.conversation-container::-webkit-scrollbar-thumb {
  border-radius: 1rem;
  background-color: #3a7bd5;
  background-image: linear-gradient(to top, #3a7bd5 0%, #3a7bd5 100%);
}

.mixed-conversation-container {
  /*border: solid red 1px;*/
  margin: 10px;
  padding: 10px;
  overflow: auto;
  min-height: 30vh;
  max-height: 30vh;
}

.mixed-conversation-container {
  overflow-y: scroll;
}
.mixed-conversation-container::-webkit-scrollbar {
  width: 5px;
}
.mixed-conversation-container::-webkit-scrollbar-track {
  background: #eee;
}
.mixed-conversation-container::-webkit-scrollbar-thumb {
  border-radius: 1rem;
  background-color: #3a7bd5;
  background-image: linear-gradient(to top, #3a7bd5 0%, #3a7bd5 100%);
}

.msg-body-container {
  display: flex;
  margin: 1vw;
}
</style>
