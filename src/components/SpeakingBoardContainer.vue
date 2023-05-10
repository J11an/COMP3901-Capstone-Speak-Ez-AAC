<script>
import SearchBar from "../components/SearchBar.vue";

export default {
  components: { SearchBar },
  data() {
    return {
      searchOn: false,
      columns: [],
    };
  },
  methods: {
    toggleSwitch() {
      this.searchOn = !this.searchOn;
    },
  },
  mounted() {
    this.columns = {
      noun: [1, 1, 1, 1],
      verb: [2, 2, 2, 2],
      adjective: [3, 3, 3, 3],
      article: [4, 4, 4, 4],
    };
  },
};
</script>

<template>
  <!--Toggle-->
  <div class="speaking-container container">
    <div class="toggle-wrapper">
      <button class="toggle-container btn" @click="toggleSwitch">
        <img class="search-icon" src="/search.png" />
      </button>
      <SearchBar v-if="searchOn" />
    </div>

    <!--Linear-->
    <div v-if="searchOn" class="linear-container">
      <div class="search-section"></div>
    </div>

    <!--Dynamic-->
    <div v-if="!searchOn" class="dynamic-container">
      <!--suggestions section-->
      <div>
        <hr />
        <p>See suggested words here</p>
        <hr />
      </div>
      <AACBoard :currentSentence="currentMessage" />
    </div>
  </div>
</template>

<style scoped>
.toggle-wrapper {
  display: flex;
  flex-direction: row;
}
.search-icon {
  width: 50px;
}
</style>
