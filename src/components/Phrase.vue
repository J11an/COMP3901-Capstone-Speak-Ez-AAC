<script>
const tts = window.speechSynthesis;

export default {
  name: "PhraseCategory",

  props: ["phrases", "category"],

  data() {
    return {};
  },
  mounted() {},
  methods: {
    texttospeech(e) {
      let message = e.target.firstChild.data;
      let utterance = new SpeechSynthesisUtterance(message);
      tts.speak(utterance);
    },
  },
};
</script>

<template>
  <div class="container">
  <h1>{{ category }}</h1>
    <div class="d-grid gap-3 col-6 mx-auto">
      <button v-for="(item, index) in phrases" :key="index" 
        type="button"
        class="btn btn-primary"
        @click="texttospeech($event)"
      >
        {{ item }}
      </button>
    </div>
  </div>
</template>

<style scoped>

</style>
