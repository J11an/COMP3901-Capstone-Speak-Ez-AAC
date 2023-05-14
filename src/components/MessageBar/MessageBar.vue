<script>
import WordPictureTileMessage from "../WordPictureTileMessage.vue";
import WordPictureTileCategory from "../WordPictureTileCategory.vue";
import SavedPhraseModal from './SavedPhraseModal.vue'

export default {
  components:{WordPictureTileMessage, WordPictureTileCategory, SavedPhraseModal},
  props:{
    currentSentence: Array,
    tts: Object,
  },
  data(){
    return {
      micActive: false,
      showSavePhraseModal: false,
      categories: [],
      csrf_token: ''
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
    toggleListening(){
      if (!this.micActive) {
        this.tts.speak(new SpeechSynthesisUtterance("I am listening"));
      } else {
        this.tts.speak(new SpeechSynthesisUtterance("Goodbye"));
      }
      this.micActive = !this.micActive;
      this.$emit("updateMicState",this.micActive);
    },
    updateScreen(screen){
      this.$emit("updateScreen",screen)
    },
    sendPhraseRequest(category,phrase){
      return fetch(`/api/saved_phrases`, {
          method: "PUT",
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
      addPhrase(category){
        this.sendPhraseRequest(category,this.currentSentence)
            .then((data)=>console.log(data))
            .catch((error)=>console.log(error))
      },
      fetchCategories() {
        return fetch(`/api/get_phrase_categories`, {
          method: "GET",
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
      getCsrfToken() {
          let self = this;
          fetch("/api/csrf-token")
            .then((response) => response.json())
            .then((data) => {
              console.log(data);
              self.csrf_token = data.csrf_token;
            });
        },
    },
    mounted() {
    this.fetchCategories().then((categories)=>this.categories=categories)
    }
}


</script>
<template>
  <div class="container msg-container">
    <div id="message" class="msg-display d-flex flex-wrap" @click="updateScreen('SPEAKLISTEN')">
      <div class="word-tile" v-for="word in currentSentence" v-bind:key="word.id">
              <WordPictureTileMessage :word="word.word.toUpperCase()"
                               :symbol="word.symbol" :tts="tts"/>
      </div>
    </div>

    <div class="btn-group btn-group-md options">
      <button class="btn" @click="handleBackspace">
        <img class="btn-img" src="/Backspace.png" alt="Backspace Icon" />
      </button>
      <button class="btn" @click="handleSpeaker">
        <img  class="btn-img" src="/SpeakerIcon.png" alt="Speaker Icon" />
      </button>

      <button class="btn" @click="showSavePhraseModal = true">
        <img src="/saveIconOff.png" class="btn-img">
      </button>
      <Teleport to="body">

        <SavedPhraseModal :show="showSavePhraseModal">
          <template #header>
            <h3>Saving Phrase</h3>
            <button class="btn" @click="showSavePhraseModal = false">
              <img src="/clear.png" class="btn-modal"/>
            </button>
          </template>
          <template #body>
            <div class="phrase-section d-flex flex-wrap">
              <div
                  v-for="category in categories"
                  @click="addPhrase(category)">
                  <WordPictureTileCategory
                    :id="-2"
                    :word="category.toUpperCase()"
                  />
              </div>
            </div>
          </template>
        </SavedPhraseModal>
      </Teleport>

      <button class="btn" @click="toggleListening">
        <img class="btn-img" src="/micOff.png" alt="Mic Off" v-if="!this.micActive"/>
        <img class="btn-img" src="/micOn.png" alt="Mic On" v-else/>
      </button>
      <button class="btn" @click="handleClear">
        <img class="btn-img" src="/clear.png" alt="Clear Icon" />
      </button>
    </div>

  </div>
</template>

<style scoped>
#message{
  cursor: pointer;
  width: 100vw;
  min-height: 100px;
}
#message:hover{
  background-color: lightblue;
}

.phrase-section{
  max-width: 50vw;
  max-height: 50vh;
  justify-content: center;
  align-items: center;
  overflow: auto;
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

.btn-img {
  width: 70px;
  height: 70px;
}

.btn-img:hover{
  width: 85px;
  height: 85px;
}

.btn-modal{
  width: 30px;
  height: 30px;
}

p{
  margin: 0;
  padding: 0;
}
</style>
