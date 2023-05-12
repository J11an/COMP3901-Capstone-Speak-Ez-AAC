<script>
import EditPhrase from "./EditPhrase.vue";

const tts = window.speechSynthesis;

export default {
  components: { EditPhrase },

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
    texttospeech(e) {
      let message = e.target.firstChild.data;
      console.log(message);
      let utterance = new SpeechSynthesisUtterance(message);
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
    <div class="d-grid gap-2 col-6 mx-auto" role="group">
      <div class="btn-group" v-for="(item, index) in phrases" :key="index">
        <button
          type="button"
          id="phrase"
          class="btn btn-primary btn-block"
          @click="texttospeech($event)"
        >
          {{ item.word }}
        </button>
        <button
          type="button"
          class="btn btn-secondary delete-btn"
          @click="deletePhrase(item.id)"
        >
          <img src="delete.png" alt="" />
        </button>
        <button type="button" class="btn btn-secondary delete-btn">
          <img src="edit.png" alt="" @click="showForm" />
        </button>

        <!-- <EditPhrase v-show="showForm" @close-modal="showForm = false" /> -->
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
  height: 50px;
  width: 50px;
}

.delete-btn img {
  height: 100%;
  max-width: 100%;
}

.phrase {
  width: 100opx;
}
</style>
