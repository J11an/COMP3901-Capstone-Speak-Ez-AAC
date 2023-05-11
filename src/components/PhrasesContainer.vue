<script>
import AddPhrase from "../components/AddPhrase.vue";
import PhraseCategory from "./PhraseCategory.vue";
import Phrase from "./Phrase.vue";

export default {
  name: "PhrasesContainer",
  components: { AddPhrase, PhraseCategory, Phrase },

  data() {
    return {
      phrases: {},
      currentCategory:'',
      currentPhrases:{},
      toggleExpandedPhrase: false,
      showForm: false,
      update: false,
    };
  },
  mounted() {
    this.getPhrases();
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
          console.log(self.phrases);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    expandPhrase(category,phrases){
      this.toggleExpandedPhrase = true;
      this.currentCategory = category;
      this.currentPhrases = phrases;
    },
    hidePhrases(){
      this.toggleExpandedPhrase = false;
      this.currentCategory = "";
      this.currentPhrases = {};
    }
  },
};
</script>

<template>
  <div class="container phrase-container">
  <div class="phrase-header">
      <h2>ADD PHRASE</h2>
      <button class="toggle-container btn" @click="showForm = true">
      <img class="search-icon" src="Add.png" />
    </button>
    
    <addPhrase 
      v-show="showForm"
      @close-modal="showForm = false"
      @update-page="update = true"
    />
  </div>

    <div>
      <!-- Folders -->
      <div v-if="!toggleExpandedPhrase" v-for="(phrases, category) in phrases" :key="category">
        <PhraseCategory :category="category" @click="expandPhrase(category,phrases)"/>
      </div>

      <!-- Expanded Phrases -->
      <div v-if="toggleExpandedPhrase">
        <button class="btn btn-dark" @click="hidePhrases">BACK</button>
        <Phrase :phrases="currentPhrases" :category="currentCategory" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.search-icon {
  width: 50px;
  margin:auto;
}

.phrase-container{
  display: flex;
  flex-direction: column;
}

.phrase-header{
  display: flex;
  align-items: center;
  justify-content: center;
  width:90%;
}

</style>
