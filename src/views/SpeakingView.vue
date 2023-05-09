<script>
import MessageBar from "../components/MessageBar.vue";
import WordPictureTile from "../components/WordPictureTile.vue";
import AACBoard from "../components/AACBoard.vue";
import SearchBar from "../components/SearchBar.vue";

export default {
  components: { MessageBar, AACBoard, SearchBar },

  data() {
    return {
      columns: {},
      currentSetence: [],
      lastWord: "",
      toggleVal: false,
    };
  },

  mounted() {
    this.columns = {
      noun: [1, 1, 1, 1],
      verb: [2, 2, 2, 2],
      adjective: [3, 3, 3, 3],
      article: [4, 4, 4, 4],
    };
    this.currentSetence = ["I", "eat"];
  },

  methods: {
    toggleSwitch() {
      this.toggleVal = !this.toggleVal;
    },
  },
};
</script>

<template>
  <div class="container">
    <MessageBar/>

    <!--Toggle-->
    <div class="toggle-wrapper">
      <button class="toggle-container" @click="toggleSwitch">
        <h5>Dynamic</h5>
        <h5>|</h5>
        <h5>Linear</h5>
      </button>
    </div>

    <!--Linear-->
    <div v-if="!toggleVal" class="">
      <h5>Linear Search Active</h5>

      <div class="search-section">
        <SearchBar />
      </div>
      <!--<AACBoard />-->
    </div>

    <!--Dynamic-->
    <div v-if="toggleVal" class="d-flex flex-wrap justify-content-between mt-3">
      <!--suggestions section-->
      <div>
        <hr />
        <p>See suggested words here</p>
        <hr />
      </div>
      <AACBoard props.currentSentence="currentSentence" />
    </div>
  </div>
</template>

<style>
.pinned-words-text {
  font-size: 32px;
  font-weight: bold;
}

.search-section {
  display: flex;
  flex-direction: row;
}

.toggle-container {
  display: flex;
  flex-direction: row;
  margin-top: 10px;
  justify-content: center;
  align-content: center;
}
</style>
