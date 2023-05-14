<script>
import EditPhrase from "./EditPhrase.vue";
import WordPictureTileMessage from "./WordPictureTileMessage.vue";

const tts = window.speechSynthesis;

export default {
  components: { WordPictureTileMessage, EditPhrase },

  name: "PhraseCategory",

  props: ["phrases", "category"],

  emits: ["phrase-added", "phrase-edited"],

  data() {
    return { csrf_token: "", showForm: false };
  },
  mounted() {},
  created() {
    this.getCsrfToken();
  },
  methods: {
    texttospeech(phrase) {
      // let message = e;
      // console.log(message);
      console.log(phrase);
      let utterance = new SpeechSynthesisUtterance(phrase);
      tts.speak(utterance);
    },
    deletePhrase(id) {
      let self = this;
      fetch(`/api/saved_phrases?id=${id}`, {
        method: "DELETE",
        headers: {
          "X-CSRFToken": this.csrf_token,
        },
      })
        .then(function (response) {
          self.$emit("phrase-added");
          return response.json();
        })
        .then(function (data) {
          console.log(data);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    updatePhrase(id) {
      let uploadForm = document.getElementById("edit-form");
      let form_data = new FormData(uploadForm);
      fetch(`/api/saved_phrases?id=${id}`, {
        method: "PUT",
        body: form_data,
        headers: {
          "X-CSRFToken": this.csrf_token,
        },
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          console.log(data);
        })
        .catch(function (error) {
          console.log(error);
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
};
</script>

<template>
  <div class="container">
    <h1 id="title">{{ category }}</h1>
    <h3 id="title">Tap the phrase you want them to hear!</h3>
    <br />
    <div class="d-grid gap-2 col-7 mx-auto" role="group">
      <div
        v-for="(phrase, index) in phrases"
        :key="index"
        class="phrase-container"
      >
        <div class="phrase" @click="texttospeech(phrase.word)">
          <div
            v-if="phrase.word"
            v-for="word in phrase.word.split(' ')"
            :key="word.id"
          >
            <div class="row-6 word">
              <WordPictureTileMessage
                :word="word"
                :symbol="word.symbol"
                :tts="tts"
              />
            </div>
          </div>
        </div>
        <div class="phrase-opts">
          <button
            type="button"
            class="btn delete-btn"
            @click="deletePhrase(phrase.id)"
          >
            <img src="delete.png" alt="" />
            <p>Delete</p>
          </button>

          <button type="button" class="btn delete-btn" @click="showForm = true">
            <img src="edit.png" alt="" />
            <p>Edit</p>
          </button>
          <editPhrase
            v-show="showForm"
            @close-modal="showForm = false"
            @phrase-edited="updatePhrase(phrase.id)"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
}

#title {
  text-align: center;
}

.delete-btn {
  margin: 0;
  height: 50%;
  width: 80px;
}

.delete-btn img {
  height: 100%;
  max-width: 100%;
}

.phrase {
  display: flex;
  flex-direction: row;
  border: 2px solid black;
  justify-content: center;
  align-items: center;
  padding: 5px;
  height: 100%;
  max-width: 100%;
  border-radius: 10px;
}

.phrase-container {
  display: flex;
}

.phrase {
  flex: 1;
}

.phrase-opts {
  display: flex;
  align-items: center;
}
</style>
