<script>
export default {
  props: {
    currentScreen: String,
  },
  methods: {
    updateScreen(screen) {
      this.$emit("updateScreen", screen);
    },
  },
};
</script>

<template>
  <header>
    <nav class="navbar navbar-expand navbar-light bg-light">
      <div
        class="navbar-collapse justify-content-center collapse show"
        id="navbarsExample08"
        style=""
      >
        <ul class="navbar-nav">
          <li :class="this.currentScreen==='SPEAKING' || this.currentScreen==='SPEAKLISTEN' ? 'nav-item active' : 'nav-item'">
            <a class="nav-link" v-on:click="updateScreen('SPEAKING')"
              >SPEAKING <img src="/SpeakingScreen.png" class="nav-img"
            /></a>
          </li>
          <li :class="this.currentScreen==='LISTENING' || this.currentScreen==='SPEAKLISTEN' ? 'nav-item active' : 'nav-item'">
            <a class="nav-link" v-on:click="updateScreen('LISTENING')"
              >LISTENING <img src="/ListeningScreen.png" class="nav-img"
            /></a>
          </li>
          <li :class="this.currentScreen==='PHRASES' ? 'nav-item active' : 'nav-item'">
            <a class="nav-link" v-on:click="updateScreen('PHRASES')"
              >PHRASES <img src="/SavedPhrasesScreen.png" class="nav-img"
            /></a>
          </li>
          <li :class="this.currentScreen==='WORDS' ? 'nav-item active' : 'nav-item'">
            <a class="nav-link" v-on:click="updateScreen('WORDS')"
              >WORDS <img src="/SavedPhrasesScreen.png" class="nav-img"
            /></a>
          </li>
          <li :class="this.currentScreen==='SETTINGS' ? 'nav-item active' : 'nav-item'">
            <a class="nav-link" v-on:click="updateScreen('SETTINGS')"
              >SETTINGS <img src="/settings.png" class="nav-img"
            /></a>
          </li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<style scoped>
/* Add any component specific styles here */
.active {
  border-bottom: 5px solid black;
}

.nav-item {
  cursor: pointer;
}

.nav-item:hover{
  background-color: #9bb8e3;
  font-weight: bolder;
}

.nav-img {
  width: 50px;
  height: 50px;
}
.nav-img:hover{
  width: 80px;
  height: 80px;
}

.nav-link {
  padding: 0;
  margin: 0 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

p {
  margin: 0;
  padding: 0;
  font-size: 1rem;
}
</style>
