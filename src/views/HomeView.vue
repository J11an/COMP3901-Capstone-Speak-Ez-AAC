<script>
export default {
  components: {},
  data() {
    return {
      isSpeaking: true,
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
    <!--
    <div class="text-center">
      <h1 class="mode-title-text pd-3 mt-4">Select the Mode you wish to use</h1>
      <div class="d-flex flex-wrap justify-content-center">

        <RouterLink :to="{ name : 'speaking' }">
          <AACTile title="SPEAKING" image-url="/SpeakingScreen.png" />
        </RouterLink>

        <RouterLink :to="{ name : 'listening' }">
          <AACTile title="LISTENING" image-url="/ListeningScreen.png" />
        </RouterLink>

      </div>
    </div>-->
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
