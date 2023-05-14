<script>
import AppHeader from "./components/Layout/AppHeader.vue";
import MessageBar from "./components/MessageBar/MessageBar.vue";
import ListeningMessageContainer from "./components/Listening/ListeningMessageContainer.vue";
import SpeakingBoardContainer from "./components/Speaking/SpeakingBoardContainer.vue";
import PhrasesContainer from "./components/PhrasesContainer.vue";
import WordDisplay from "./components/WordDisplay.vue";
import SettingsDisplay from "./components/Settings/SettingsDisplay.vue";

export default {
  components: {
    PhrasesContainer,
    SpeakingBoardContainer,
    AppHeader,
    ListeningMessageContainer,
    MessageBar,
    WordDisplay,
    SettingsDisplay
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
    filterSentence(sentence){
      return fetch(`/api/filter_words?message=${sentence}`, {
        method: "GET",
        headers: {
          "X-CSRFToken": this.csrf_token,
        },
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          return data;
        })
        .catch(function (error) {
          return error;
        });
    },
    configureRecognizer(){
      if (this.recognizer){
        this.recognizer.continuous = true;
        this.recognizer.lang = "en-US";
        this.recognizer.interimResults = false;
        this.recognizer.maxAlternatives = 1;
        this.recognizer.onresult = (event) => {
          const msg = event.results[event.results.length-1][0].transcript;
          this.filterSentence(msg)
              .then((filteredSentence)=>{
                this.updateMessageList(
                    ["SPEAKER",
                      filteredSentence.map(
                          (val)=>{
                            return {
                              id: 0,
                              word: val,
                            }
                          }
                      )
                    ]
                )
              })
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
    <Transition name="fade" appear>
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
    </Transition>


    <Transition name="fade" appear>
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
    </Transition>

    <Transition name="fade" appear>
      <SpeakingBoardContainer
          :current-message="currentMessage"
          :current-screen="currentScreen"
          @updateScreen="updateBody"
          @updateSentence="updateMessage"
          v-if="currentScreen === 'SPEAKING' || currentScreen==='SPEAKLISTEN'" />
    </Transition>

    <Transition name="fade" appear>
      <PhrasesContainer v-if="currentScreen === 'PHRASES'" />
    </Transition>
    <Transition name="fade" appear>
      <WordDisplay v-if="currentScreen === 'WORDS'" />
    </Transition>

    <Transition name="fade" appear>
      <SettingsDisplay v-if="currentScreen === 'SETTINGS'" />
    </Transition>
  </main>
</template>

<style>
*{
  transition: 200ms;
}

.fade-enter-active {
  transition: all 0.5s ease-out;
}

.fade-leave-active {
  transition: all 0.5s cubic-bezier(1, 0.5, 0.8, 1);
}

.fade-enter-from{
  opacity: 0;
}
.fade-leave-to {
  opacity: 0;
}
</style>
