<script>
import SearchBar from "../components/SearchBar.vue"

export default {
  components: {SearchBar},
  data() {
    return {
      toggleVal: true
    }
  },
  methods: {
    toggleSwitch() {
      this.toggleVal = !this.toggleVal;
    },
  },
}
</script>

<template>
  <!--Toggle-->
  <div class="speaking-container container">
    <div class="toggle-wrapper">
      <button class="toggle-container btn" @click="toggleSwitch">
        <img class="search-icon" src="/search.png"/>
      </button>
      <SearchBar />
    </div>

    <!--Linear-->
    <div v-if="!toggleVal" class="linear-container">
      <div class="search-section">

      </div>
    </div>

    <!--Dynamic-->
    <div v-if="toggleVal" class="dynamic-container">
      <!--suggestions section-->
      <div>
        <hr /><p>See suggested words here</p><hr />
      </div>
      <AACBoard :currentSentence="currentMessage" />
    </div>
  </div>

</template>

<style scoped>
.speaking-container{

}
.search-icon{
  width: 50px;
}
</style>