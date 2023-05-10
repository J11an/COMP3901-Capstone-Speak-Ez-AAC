<script>
const tts = window.speechSynthesis;

export default {
  name: "PhraseCategory",

  props: ["phrases"],

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
  <li v-for="(item, index) in phrases" :key="index">
    <button
      type="button"
      class="btn btn-primary btn-lg"
      @click="texttospeech($event)"
    >
      {{ item }}
    </button>
  </li>
</template>

<style scoped></style>
