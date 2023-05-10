<script>
export default {
  methods:{
    updateScreen(screen){
      this.$emit('updateScreen', screen);
    }
  }
}
</script>

<template>
  <header>
    <nav class="navbar navbar-expand navbar-light bg-light">
      <div class="navbar-collapse justify-content-center collapse show" id="navbarsExample08" style="">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link" v-on:click="updateScreen('SPEAKING')" >SPEAKING <img src="/SpeakingScreen.png" class="nav-img"></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" v-on:click="updateScreen('LISTENING')">LISTENING <img src="/ListeningScreen.png" class="nav-img"></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" v-on:click="updateScreen('PHRASES')">PHRASES <img src="/SavedPhrasesScreen.png" class="nav-img"></a>
          </li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<style scoped>
/* Add any component specific styles here */
.nav-item{
  cursor: pointer;
}

.nav-img{
  width: 35px;
  height: 35px;
}

.nav-link{
  padding: 0;
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
