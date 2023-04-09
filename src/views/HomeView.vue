<script>
import MenuTile from "../components/MenuTile.vue";

export default {
  components: { AACTile: MenuTile },
  data() {
    return {
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
      <div class="d-flex flex-wrap justify-content-between">
        <RouterLink to="/speaking">
          <AACTile title="SPEAKING" image-url="/SpeakingScreen.png" />
        </RouterLink>

        <!--<RouterLink to="/typing">
          <AACTile title="TYPING" image-url="/TypingScreen.png" />
        </RouterLink>-->

        <RouterLink to="/listening">
          <AACTile title="LISTENING" image-url="/ListeningScreen.png" />
        </RouterLink>

        <!--<RouterLink to="/neweditword">
          <AACTile
            title="NEW/EDIT WORD"
            image-url="/NewEditScreen.png"
          ></AACTile>
        </RouterLink>-->

        <!--<RouterLink to="/savedphrases">
          <AACTile
            title="SAVED PHRASES"
            image-url="/SavedPhrasesScreen.png"
          ></AACTile>
        </RouterLink>-->
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

a {
  text-decoration: none;
  color: inherit;
  border-radius: 100px;
  margin: 10px;
}
</style>
