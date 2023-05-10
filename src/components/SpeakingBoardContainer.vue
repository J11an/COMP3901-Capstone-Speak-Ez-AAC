<script>
import SearchBar from "../components/SearchBar.vue"
import WordPictureTile from "./WordPictureTile.vue";

export default {
  components: {WordPictureTile, SearchBar},
  data() {
    return {
      searchOn: false,
      columns: [],
    }
  },
  methods: {
    toggleSwitch() {
      this.searchOn = !this.searchOn;
    },
    fetchInitColumns() {
      return fetch("api/inital_tree_setting", {
        method: "GET",
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          console.log("Received Initial Columns : ",data);
          return data;
        })
        .catch(function (error) {
          console.log(error);
          return error
        });
    }
  },
  mounted() {
    this.fetchInitColumns().then((columns)=>this.columns=columns);
  }
}
</script>

<template>
  <!--Toggle-->
  <div class="speaking-container container">

    <div class="toggle-wrapper">
      <button class="toggle-container btn" @click="toggleSwitch">
        <img class="search-icon" src="/search.png"/>
      </button>
      <SearchBar v-if="searchOn"/>
    </div>

    <!--Linear-->
    <div v-if="searchOn" class="linear-container">
      <div class="search-section">

      </div>
    </div>

    <!--Dynamic-->
    <div v-if="!searchOn" class="dynamic-container">
      <div>
        <hr /><p>See suggested words here</p><hr />
        <div v-if="!searchOn" class="d-flex flex-wrap justify-content-between mt-3">
          <div v-for="(words,partOfSpeech) in columns" v-bind:key="column">
            <div v-for="word in words">
              <WordPictureTile :word="word" symbolURL="/HelpIcon.png" :part-of-speech="partOfSpeech" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<style scoped>
.speaking-container {
  display: flex;
  flex-direction: column;
}

.toggle-wrapper{
  display: flex;
  flex-direction: row;
}
.search-icon{
  width: 50px;
}
</style>