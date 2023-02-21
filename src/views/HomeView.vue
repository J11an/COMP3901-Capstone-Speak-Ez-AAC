<script>
import AACTile from "../components/AACTile.vue";

export default {
  components: { AACTile },
  data() {
    return {
      message: "Group 1",
    };
  },
};
</script>

<template>
  <link
    href="https://fonts.googleapis.com/css?family=DM Sans"
    rel="stylesheet"
  />
  <div class="container">
    <div class="text-center">
      <h1 class="mode-title-text pd-3">Select the Mode you wish to use</h1>
      <div class="row">
        <div class="col">
          <AACTile title="SPEAKING" image-url="/SpeakingScreen.png"></AACTile>
        </div>
        <div class="col">
          <AACTile title="TYPING" image-url="/TypingScreen.png"></AACTile>
        </div>
        <div class="col">
          <AACTile title="LISTENING" image-url="/ListeningScreen.png"></AACTile>
        </div>
      </div>
      <div class="row">
        <div class="col">
          <AACTile
            title="NEW/EDIT WORD"
            image-url="/NewEditScreen.png"
          ></AACTile>
        </div>
        <div class="col">
          <AACTile
            title="SAVED PHRASES"
            image-url="/SavedPhrasesScreen.png"
          ></AACTile>
        </div>
        <div class="col">
          <AACTile title="LEARNING" image-url="/LearningScreen.png"></AACTile>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.mode-title-text {
  font-family: "DM Sans";
  font-style: normal;
  font-weight: 700;
  font-size: 48px;
  line-height: 62px;
  text-transform: uppercase;
}
</style>
