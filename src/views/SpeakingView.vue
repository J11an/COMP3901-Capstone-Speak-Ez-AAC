<script>
import MessageBar from "../components/MessageBar.vue";
import WordPictureTile from "../components/WordPictureTile.vue";
import AACBoard from '../components/AACBoard.vue'

export default {
  components: {MessageBar, AACBoard},

  data() {
    return {
      columns: {},
      currentMessage: "",
      lastWord: "",
      toggleVal: false,
    };
  },

  mounted() {
    this.columns = {
      "noun" : [1,1,1,1],
      "verb" : [2,2,2,2],
      "adjective" : [3,3,3,3],
      "article" : [4,4,4,4]
    }
  },

  methods: {
    toggleSwitch(){
      this.toggleVal = !this.toggleVal;
    }
  },
};
</script>
<template>
  <div>
    <MessageBar/>

    <!--Toggle-->
    <div class="toggle-wrapper">
      <button class="toggle-container" @click="toggleSwitch">
        <h1>Dynamic</h1>
        <h1>|</h1>
        <h1>Linear</h1>
      </button>
    </div>

    <!--Linear-->
    <div v-if="!toggleVal" class="d-flex flex-wrap justify-content-between mt-3">
      <h1>Linear Search Active</h1>
      <!--<WordPictureTile image-url="/HelpIcon.png" :word="word"/>-->
    </div>

    <div><AACBoard /></div>

    <!--Dynamic-->
    <!--<div v-if="toggleVal" class="d-flex flex-wrap justify-content-between mt-3">
      <div class="column" v-for="column in columns">
        <div v-for="word in column">
          <WordPictureTile image-url="/HelpIcon.png" :word="word"/>
        </div>
      </div>
    </div>-->

    <!--<hr />
    <div class="pinned section">
      <div class="d-flex justify-content-center align-items-center">
        <img
          class="pinned-icon-section"
          src="/PinnedIcon.png"
          alt="Pinned Icon"
        />
        <p class="text-center pinned-words-text">Pinned Words</p>
      </div>
      <div class="d-flex justify-content-center align-items-center">
        <WordPictureTile image-url="/HelpIcon.png" word="I" />
        <WordPictureTile image-url="/HelpIcon.png" word="I" />
        <WordPictureTile image-url="/HelpIcon.png" word="I" />
      </div>
    </div>-->
  </div>
</template>

<style>
.pinned-words-text {
  font-size: 32px;
  font-weight: bold;
}

.toggle-container {
  display: flex;
  flex-direction: row;
  margin: auto;
  justify-content: center;
  align-content: center;
}
</style>
