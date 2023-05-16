<script>
import WordPictureTileMessage from "../WordPictureTileMessage.vue";
import WordPictureTileCategory from "../WordPictureTileCategory.vue";
import SavedPhraseModal from './SavedPhraseModal.vue'

export default {
  components:{WordPictureTileMessage, WordPictureTileCategory, SavedPhraseModal},
  props:{
    currentSentence: Array,
    tts: Object,
    utterance: Object
  },
  data(){
    return {
      micActive: false,
      showSavePhraseModal: false,
      phraseAdded: false,
      phraseExists: false,
      success: false,
      errorMsg: '',
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
      const sentence = this.currentSentence.map((wordObj)=>wordObj.word).join(" ");
      this.$emit("playAudio",sentence);
      this.$emit("updateMessages",["LISTENER",this.currentSentence]);
    },
    playTile(word){
      this.$emit("playAudio",word);
    },
    toggleListening(){
      if (!this.micActive) {
          this.$emit("playAudio","I am listening");
      } else {
          this.$emit("playAudio","Goodbye");
      }
      this.micActive = !this.micActive;
      this.$emit("updateMicState",this.micActive);
    },
    updateScreen(screen){
      this.$emit("updateScreen",screen)
    },
    sendPhraseRequest(category,phrase){
      return fetch(`/api/saved_phrases?saved_phrases=${phrase.map((p)=>p.word).join(" ")}&category=${category}`, {
          method: "POST",
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
            .then((data)=>{
              console.log(data)
              this.success = true;
              if (data.error){
                this.success = false
                this.errorMsg = data.error;
              } else {
                this.phraseExists = true
              }
              this.phraseAdded = true;
              setTimeout(()=>{
                this.showSavePhraseModal = false;
                setTimeout(()=>{this.phraseAdded=false},100);
              },3000)
            })
            .catch((error)=>{
              this.success = false;
              this.errorMsg = error;
              this.phraseAdded = true;
              setTimeout(()=>{
                this.showSavePhraseModal = false;
                setTimeout(()=>{this.phraseAdded=false},100);
              },1000)
            })
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
      checkPhrase(phrase) {
        return fetch(`/api/check_message?saved_phrases=${phrase.map((p)=>p.word).join(" ")}`, {
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
      this.fetchCategories().then((categories)=>this.categories=categories);
      this.getCsrfToken();
    },
    watch:{
      currentSentence:{
        handler(oldVal,newVal){
          this.checkPhrase(newVal).then((data)=>{
            const msg = data.message;
            console.log(msg)
            if (msg==='Phrase exists'){
              this.phraseExists = true;
            } else {
              this.phraseExists = false;
            }
          });
        },
        deep: true
      }
    }
}


</script>
<template>
  <div class="container msg-container">
    <div id="message" class="msg-display d-flex flex-wrap" @click="updateScreen('SPEAKLISTEN')">
      <div class="word-tile" v-for="word in currentSentence" v-bind:key="word.id">
              <WordPictureTileMessage :word="word.word.toUpperCase()"
                               :symbol="word.symbol" @tileSpeech="playTile"/>
      </div>
    </div>

    <div class="btn-group btn-group-md options">
      <button class="btn" @click="handleBackspace">
        <img class="btn-img" src="/Backspace.png" alt="Backspace Icon" />
        <p>Delete</p>
      </button>
      <button class="btn" @click="handleSpeaker">
        <img  class="btn-img" src="/SpeakerIcon.png" alt="Speaker Icon" />
        <p>Speak</p>
      </button>

      <button class="btn" @click="showSavePhraseModal = true">
        <img v-if="!phraseExists" src="/saveIconOff.png" class="btn-img">
        <img v-else src="/saveIconOn.png" class="btn-img">
        <p>Save</p>
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
            <div v-if="!phraseAdded" class="phrase-section d-flex flex-wrap">
              <div
                  v-for="category in categories"
                  @click="addPhrase(category)">
                  <WordPictureTileCategory
                    :id="-2"
                    :word="category.toUpperCase()"
                  />
              </div>
            </div>
            <div class="d-flex flex-wrap success-wrapper" v-else>
              <div v-if="success">
                <img class="success-wrapper-btn" src="/checked.png"/>
              </div>
              <div class="d-flex flex-wrap success-wrapper" v-else>
                <img class="success-wrapper-btn" src="/error.png"/>
                <p class="text-center error-msg">{{ errorMsg }}</p>
              </div>

            </div>
          </template>
        </SavedPhraseModal>
      </Teleport>

      <button class="btn" @click="toggleListening">
        <img class="btn-img" src="/micOff.png" alt="Mic Off" v-if="!this.micActive"/>
        <img class="btn-img" src="/micOn.png" alt="Mic On" v-else/>
        <p>Listen</p>
      </button>
      <button class="btn" @click="handleClear">
        <img class="btn-img" src="/clear.png" alt="Clear Icon" />
        <p>Clear</p>
      </button>
    </div>

  </div>
</template>

<style scoped>
.success-wrapper{
  align-items: center;
  justify-content: center;
  display: flex;
  flex-direction: column;
}
.success-wrapper-btn{
  width: 150px;
  height: 150px;
}
.error-msg{
  font-size: 26px;
  font-weight: bolder;
  color: crimson;
}

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
  width: 60px;
  height: 60px;
  margin: 0 10px;
}

.btn-img:hover{
  width: 75px;
  height: 75px;
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
