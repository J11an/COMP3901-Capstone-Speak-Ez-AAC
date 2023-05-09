<script>
import MessageBar from "../components/MessageBar.vue";
import WordPictureTile from "../components/WordPictureTile.vue";
import AACBoard from '../components/AACBoard.vue';
import SearchBar from "../components/SearchBar.vue";

export default {
  components: { MessageBar, AACBoard, SearchBar },

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
  <div class="container">
    <MessageBar/>
    <div class="search-section">
      <SearchBar/>
      <!--Toggle-->
      
      <div class="toggle-wrapper">
        <button class="toggle-container" @click="toggleSwitch">
          <h5>Dynamic</h5>
          <h5>|</h5>
          <h5>Linear</h5>
        </button>
      </div>

    </div>
      <!--Linear-->
      <div v-if="!toggleVal" class="d-flex flex-wrap justify-content-between mt-3">
        <h5>Linear Search Active</h5>
        <!--<WordPictureTile image-url="/HelpIcon.png" :word="word"/>-->
    
    <!--suggestions section-->
    </div>
    <hr/>
    <p>See suggested words here</p>
    <hr/>
    <div>
    </div>
    <AACBoard />

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

.search-section{
  display:inline-flex;
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
