<script>
import MessageBar from "../components/MessageBar.vue";
import WordPictureTile from "../components/WordPictureTile.vue";

export default {
  components: { WordPictureTile, MessageBar },

  data() {
    return {};
  },
  methods: {},
};
</script>
<template>
  <div>
    <MessageBar />
    <div class="d-flex flex-wrap justify-content-between mt-3">
      <WordPictureTile image-url="/HelpIcon.png" word="I" />
      <WordPictureTile image-url="/HelpIcon.png" word="I" />
      <WordPictureTile image-url="/HelpIcon.png" word="I" />
      <WordPictureTile image-url="/HelpIcon.png" word="I" />
      <WordPictureTile image-url="/HelpIcon.png" word="I" />
      <WordPictureTile image-url="/HelpIcon.png" word="I" />
      <WordPictureTile image-url="/HelpIcon.png" word="I" />
      <WordPictureTile image-url="/HelpIcon.png" word="I" />
      <WordPictureTile image-url="/HelpIcon.png" word="I" />
      <WordPictureTile image-url="/HelpIcon.png" word="I" />
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
