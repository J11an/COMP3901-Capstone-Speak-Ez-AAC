<script>
import Phrase from "./Phrase.vue";

export default {
  name: "PhraseCategory",

  components: { Phrase },
  props: ["category", "phrase"],

  data() {
    return {
      currentScreen: "PHRASEVIEW",
    };
  },
  mounted() {},
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
    test() {
      return true;
    },
    updateBody(screen) {
      this.currentScreen = screen;
    },
  },
};
</script>

<template>
  <div class="container phrases-con">
    <h2>SELECT FROM YOUR SAVED PHRASES</h2>
    <div>
      <button class="btn-container"  @click="test">
        <img class="folder-btn" src="folder.png" alt=""/>
        <p class="centered">{{ category.toUpperCase() }}</p>
      </button>
    </div >
      <Phrase :phrases="phrase" :category="category" />
  </div>
  
</template>

<style scoped>

.add-icon{
  width: 100%;
  height: 20%;
}

.btn-container {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: transparent;
  border: none;
  cursor: pointer;
  text-align: center;
  flex-direction: column;
  height: 100%;
}

 .folder-btn{
  max-width: 50%;
  max-height:50%;
}
.phrases-con {
    display: flexbox;
    text-align: center;
}

</style>
