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
      console.log(message);
      let utterance = new SpeechSynthesisUtterance(message);
      tts.speak(utterance);
    },
  },
};
</script>

<template>
  <div class="container">
    <h1 id="title">{{ category }}</h1>
    <h3 id="title">Tap the phrase you want them to hear!</h3>
    <br />
    <div class="d-grid gap-2 col-6 mx-auto">
      <button
        v-for="(item, index) in phrases"
        :key="index"
        type="button"
        class="btn btn-primary btn-lg"
        @click="texttospeech($event)"
      >
        {{ item }}
      </button>
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
</style>
