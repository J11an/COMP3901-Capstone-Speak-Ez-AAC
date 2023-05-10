<script>
import SearchBar from "../components/SearchBar.vue"
import WordPictureTile from "./WordPictureTile.vue";

export default {
  components: {WordPictureTile, SearchBar},
  props:{
    currentMessage:Array
  },
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
    },
    addWord(id, word, symbol, partOfSpeech){
      console.log(id, word, symbol, partOfSpeech);
      this.$emit("updateSentence", ['add',{
        id: id,
        word: word,
        symbol: symbol,
        partOfSpeech: partOfSpeech
      }])
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
        <img class="search-icon" src="/search.png" />
      </button>
      <SearchBar v-if="searchOn" />
    </div>

    <!--Linear-->
    <div v-if="searchOn" class="linear-container">
      <div class="search-section d-flex flex-wrap"></div>
    </div>

    <!--Dynamic-->
    <div v-if="!searchOn" class="dynamic-container">
      <div>
        <hr /><p>See suggested words here</p><hr />
        <div v-if="!searchOn" class="board-container d-flex justify-content-between mt-3">
          <div v-for="(words,partOfSpeech) in columns">
            <div v-for="word in words">
              <WordPictureTile :word="word.word.toUpperCase()"
                               :symbol="word.symbol"
                                @click="addWord(word.id, word.word, word.symbol, partOfSpeech)"/>
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
.search-icon {
  width: 50px;
}
</style>
