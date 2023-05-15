<script>
import WordPictureTileMessage from "../WordPictureTileMessage.vue";
export default {
  components: {WordPictureTileMessage},

  props: {
    msg: Array,
    from: String,
  },
  methods: {
    playTile(word){
      this.$emit("playMessageTile",word);
    },
  }
};
</script>

<template>
  <!-- Section for messages -->
  <section v-if="from === 'SPEAKER'">
    <div class="speaker-msg">
      <div v-for="word in msg" v-bind:key="word.id">
        <WordPictureTileMessage :word="word.word" :symbol="word.symbol" :tts="tts"  v-if="word.word" @tileSpeech="playTile"/>
      </div>
    </div>
  </section>

  <section v-else class="listener-msg">
      <div v-for="word in msg" v-bind:key="word.id">
        <WordPictureTileMessage :word="word.word" :symbol="word.symbol" :tts="tts" @tileSpeech="playTile"/>
      </div>
  </section>
</template>

<style scoped>
.speaker-msg,
.listener-msg {
  font-size: 2vw;
  padding: 1vw;
  border-radius: 25px;
}

.speaker-label {
  margin-left: 20px;
}

.speaker-msg {
  margin-right: auto;
  background-color: #9bb8e3;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

.listener-msg {
  margin-left: auto;
  background-color: #8eff9a;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
</style>
