<script>
import MessageBar from "../components/MessageBar.vue";
import WordPictureTile from "../components/WordPictureTile.vue";

export default {
  components: { WordPictureTile, MessageBar },

  data() {
    return {
      columns: {},
      currentMessage: "",
      lastWord: ""
    };
  },

  methods: {
  },

  mounted() {
    this.columns = {
      "noun" : [1,2,3,4],
      "verb" : [1,2,3,4],
      "adjective" : [1,2,3,4],
      "article" : [1,2,3,4]
    }
  }

};
</script>
<template>
  <div>
    <MessageBar />

    <div class="d-flex flex-wrap justify-content-between mt-3">
      <div class="column" v-for="column in columns">
        <WordPictureTile v-for="word in column" image-url="/HelpIcon.png" word="I"/>
      </div>
    </div>

    <hr />
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
    </div>
  </div>
</template>

<style>
.pinned-words-text {
  font-size: 32px;
  font-weight: bold;
}
</style>
