<script>
import AddPhrase from "../components/AddPhrase.vue";
import PhraseCategory from "./PhraseCategory.vue";

export default {
  name: "PhrasesContainer",
  components: { AddPhrase, PhraseCategory },

  data() {
    return {
      phrases: {},
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
  },
};
</script>

<template>
  <button class="toggle-container btn" @click="showForm = true">
    <img class="search-icon" src="Add.png" />
  </button>
<<<<<<< Updated upstream
  <addPhrase
    v-show="showForm"
    @close-modal="showForm = false"
    @phrase-added="getPhrases"
  />
=======
  <addPhrase 
    v-show="showForm"
    @close-modal="showForm = false"
    @update-page="update = true"
  />

>>>>>>> Stashed changes
  <div v-for="(phrase, category) in phrases" :key="category">
    <PhraseCategory :category="category" :phrase="phrase" />
    <!-- <ul>
      <li v-for="value in values" :key="value">{{ value }}</li>
    </ul> -->
  </div>
</template>

<style scoped>
.search-icon {
  width: 50px;
}

</style>
