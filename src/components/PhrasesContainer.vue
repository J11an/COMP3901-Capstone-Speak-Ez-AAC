<script>
import AddPhrase from "../components/AddPhrase.vue";
import Phrase from "./Phrase.vue";
import WordPictureTile from "./WordPictureTile.vue";

export default {
  name: "PhrasesContainer",
  components: { AddPhrase, Phrase, WordPictureTile },

  data() {
    return {
      phrases: {},
      words: {},
      currentCategory: "",
      currentPhrases: {},
      toggleExpandedPhrase: false,
      showForm: false,
    };
  },
  mounted() {
    this.getPhrases();
    this.getWords();
  },
  methods: {
    getPhrases() {
      let self = this;
      fetch("/api/saved_phrases", {
        method: "GET",
        headers: {
          "X-CSRFToken": this.csrf_token,
        },
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          self.phrases = data;
          self.currentPhrases = data;
          console.log(self.phrases);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    expandPhrase(category, phrases) {
      this.toggleExpandedPhrase = true;
      this.currentCategory = category;
      this.currentPhrases = phrases;
    },
    hidePhrases() {
      this.toggleExpandedPhrase = false;
      this.currentCategory = "";
      this.currentPhrases = {};
    },
    deletePhrase(id) {
      fetch(`/api/saved_phrases?id=${id}`, {
        method: "DELETE",
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
    updatePhrase(id) {
      let uploadForm = document.getElementById("registrationform");
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
    getWords() {
      let self = this;
      fetch("/api/word", {
        method: "GET",
        headers: {
          "X-CSRFToken": this.csrf_token,
        },
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          self.words = data;
          console.log(self.words);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    deleteWord(id) {
      fetch(`/api/word?id=${id}`, {
        method: "DELETE",
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
    updateWord(id) {
      let uploadForm = document.getElementById("registrationform");
      let form_data = new FormData(uploadForm);
      fetch(`/api/word?id=${id}`, {
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
    saveWord() {
      let self = this;
      let uploadForm = document.getElementById("registrationform");
      let form_data = new FormData(uploadForm);
      fetch("/api/word", {
        method: "POST",
        body: form_data,
        error: false,
        errors: [],
        headers: {
          "X-CSRFToken": this.csrf_token,
        },
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          // self.$emit("phrase-added");
          console.log(data);
          if ("error" in data) {
            self.errors = data.error;
            self.error = true;
            console.log(self.error);
          } else {
            self.error = false;
            document.getElementById("registrationform").reset();
          }
        })
        .catch(function (error) {
          console.log(error);
          console.log(form_data);
        });
    },
  },
};
</script>

<template>
  <div class="container">
    <div class="phrase-header">
      <h2>SELECT FROM OR ADD ONE OF YOUR PHRASES</h2>
      <button class="toggle-container btn" @click="showForm = true">
        <img class="add-icon" src="Add.png" />
        <p>ADD PHRASE</p>
      </button>

      <addPhrase
        v-show="showForm"
        @close-modal="showForm = false"
        @phrase-added="getPhrases()"
      />
    </div>
    <div class="category-container">
      <!-- Folders -->
      <div
        v-if="!toggleExpandedPhrase"
        v-for="(phrases, category) in phrases"
        :key="category"
      >
        <WordPictureTile
          :word="category.toUpperCase()"
          :symbol="category.symbol"
          @click="expandPhrase(category, phrases)"
        />
        <!-- <PhraseCategory
          :category="category"
          @click="expandPhrase(category, phrases)"
        /> -->
      </div>

      <!-- Expanded Phrases -->
      <div v-if="toggleExpandedPhrase">
        <button class="btn btn-dark" @click="hidePhrases">BACK</button>
        <Phrase
          :phrases="currentPhrases"
          :category="currentCategory"
          @phrase-added="getPhrases()"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  height: 100vh;
  width: 100vw;
}
.category-container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  flex: auto;
  align-items: center;
  justify-content: center;
}

.add-icon {
  width: 80%;
  height: auto;
  margin: auto;
}

.phrase-header {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
</style>
