<script>
import AddPhrase from "../components/AddPhrase.vue";
import Phrase from "./Phrase.vue";
import WordPictureTile from "./WordPictureTile.vue";
import WordPictureTileMessage from "./WordPictureTileMessage.vue";

const tts = window.speechSynthesis;

export default {
  name: "PhrasesContainer",
  components: { AddPhrase, Phrase, WordPictureTile, WordPictureTileMessage },

  data() {
    return {
      phrases: {},
      toggleExpandedPhrase: false,
      showForm: false,
      toggleEditPhraseForm: false,
      toggleAddPhraseForm: false,
      categories: [],
      currentCategory: "",
    };
  },
  mounted() {
    this.getPhrases();
    this.getCategories();
  },
  methods: {
    getPhrases(category) {
      let self = this;
      fetch(`/api/saved_phrases?category=${category}`, {
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
          console.log("phrases", self.phrases);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    expandPhrase(category) {
      let self = this;
      this.toggleExpandedPhrase = true;
      self.currentCategory = category;
      this.getPhrases(category);
      console.log(category);
    },
    hidePhrases() {
      this.toggleExpandedPhrase = false;
    },
    expandEditForm() {
      this.toggleEditPhraseForm = true;
    },
    hideEditForm() {
      this.toggleEditPhraseForm = false;
    },
    expandAddForm() {
      this.toggleEditPhraseForm = true;
    },
    hideAddForm() {
      this.toggleEditPhraseForm = false;
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
    updatePhrase(id, saved_phrases, category) {
      fetch(
        `/api/saved_phrases?id=${id}&saved_phrases=${saved_phrases}&category=${category}`,
        {
          method: "PUT",
          headers: {
            "X-CSRFToken": this.csrf_token,
          },
        }
      )
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
    getCategories() {
      let self = this;
      fetch("/api/get_phrase_categories", {
        method: "GET",
        headers: {
          "X-CSRFToken": this.csrf_token,
        },
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          self.categories = data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    AutoDelete(id, category) {
      let self = this;
      this.deletePhrase(id);
      this.hidePhrases();
      this.expandPhrase(category);
    },
    texttospeech(phrase) {
      console.log(phrase);
      let utterance = new SpeechSynthesisUtterance(phrase);
      tts.speak(utterance);
    },
  },
};
</script>

<template>
  <div class="container">
    <div class="phrase-header">
      <h2>SELECT FROM OR ADD ONE OF YOUR PHRASES</h2>
      <!-- <button class="toggle-container btn" @click="showForm = true">
        <img class="add-icon" src="Add.png" />
        <p>ADD PHRASE</p>
      </button> -->

      <!--  -->
      <addPhrase v-show="showForm" @close-modal="showForm = false" />
      <button class="toggle-container btn" @click="toggleAddForm">
        <img class="add-icon" src="Add.png" />
        <p>ADD PHRASE</p>
      </button>
    </div>

    <div v-if="toggleAddForm">
      <Transition name="modal">
        <div v-if="show" class="modal-mask">
          <div class="modal-container">
            <div class="modal-header">
              <button class="btn btn-dark" @click="hideAddForm">BACK</button>
              <slot name="header">default header</slot>
            </div>

            <div class="modal-body">
              <slot name="body">default body</slot>
            </div>
          </div>
        </div>
      </Transition>
    </div>

    <div v-if="toggleEditForm">
      <Transition name="modal">
        <div v-if="show" class="modal-mask">
          <div class="modal-container">
            <div class="modal-header">
              <button class="btn btn-dark" @click="hideEditForm">BACK</button>
              <slot name="header">default header</slot>
            </div>

            <div class="modal-body">
              <slot name="body">default body</slot>
            </div>
          </div>
        </div>
      </Transition>
    </div>

    <div>
      <!-- Folders -->
      <div class="category-container">
        <div
          v-for="(category, index) in categories"
          v-if="!toggleExpandedPhrase"
          :key="index"
          class="category"
        >
          <WordPictureTile
            :word="category.toUpperCase()"
            :symbol="category.symbol"
            @click="expandPhrase(category)"
          />
        </div>
      </div>

      <!-- Expanded Phrases -->
      <div v-if="toggleExpandedPhrase">
        <button class="btn btn-dark" @click="hidePhrases">BACK</button>
        <div class="phrase-container">
          <div v-for="phrase in phrases" :key="phrase.id">
            <div class="phrase" @click="texttospeech(phrase.word)">
              <div v-for="(item, index) in phrase.word.split(' ')" :key="index">
                <WordPictureTileMessage :word="item" :tts="tts" />
              </div>
            </div>
            <div class="phrase-opts">
              <button
                type="button"
                class="btn delete-btn"
                @click="AutoDelete(phrase.id, currentCategory)"
              >
                <img src="delete.png" alt="" />
                <p>Delete</p>
              </button>
              <button
                type="button"
                class="btn delete-btn"
                @click="expandEditForm"
              >
                <img src="edit.png" alt="" />
                <p>Edit</p>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
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

.phrase {
  display: flex;
  flex-direction: row;
  border: 2px solid black;
  justify-content: center;
  align-items: center;
  padding: 5px;
  height: auto;
  min-width: 80%;
  border-radius: 10px;
  margin: 20px;
  float: left;
}

.phrase-container {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.phrase-opts {
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding-top: 30px;
}

.delete-btn {
  height: 50%;
  width: 80px;
  margin: 5px
}

.delete-btn img {
  height: 100%;
  max-width: 100%;
}
</style>
