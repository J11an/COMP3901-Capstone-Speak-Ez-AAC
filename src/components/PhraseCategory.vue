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
      return console.log("click");
    },
    updateBody(screen) {
      this.currentScreen = screen;
    },
  },
};
</script>

<template>
      <button class="btn-container" @click="test">
        <div class="folder-btn">
          <p class="centered">{{ category.toUpperCase() }}</p>
          <!--<img class="folder-btn" src="folder.png" alt=""/>-->
        </div>
      </button>
      <Phrase :phrases="phrase" :category="category" />
</template>

<style scoped>

.add-icon{
  width: 100%;
  height: 20%;
}

.btn-container {
  background-color: transparent;
  border: none;
  cursor: pointer;
  margin:auto;
}

.folder-btn{
  padding: 70px 0;
  text-align: center;
  height: 200px;
  width:200px;
  background-image: url("folder.png");
  background-size: 100% 100%;
}
.centered{
  margin-top: 50px;
}

</style>
