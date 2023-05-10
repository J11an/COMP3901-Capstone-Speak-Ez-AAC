<script>
import Phrase from "./Phrase.vue";
export default {
  name: "PhraseCategory",

  components: { Phrase },
  props: ["category", "phrase"],

  data() {
    return {};
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
      console.log("test");
    },
  },
};
</script>

<template>
  <div>
    <Button @click="test">{{ category }}</Button>
    <Phrase :phrases="phrase" />
  </div>
</template>

<style scoped></style>
