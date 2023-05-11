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
      searchTerm: "",
      searchResults: []
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
          return data;
        })
        .catch(function (error) {
          console.log(error);
          return error
        });
    },
    fetchColumnsFromWord(word){
      return fetch(`/api/word_associated/?word=${word}`, {
        method: "GET",
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          return data;
        })
        .catch(function (error) {
          console.log(error);
          return error
        });
    },
    fetchSearchedWord(word) {
      return fetch(`api/search/${word}`, {
        method: "GET",
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          console.log(data);
          return data
        })
        .catch(function (error) {
          console.log(error);
          return error
        });
    },
    addWord(id, word, symbol, partOfSpeech){
      this.$emit("updateSentence", ['add',{
        id: id,
        word: word,
        symbol: symbol,
        partOfSpeech: partOfSpeech
      }]);
    },
    handleClear(){
      this.searchTerm = "";
    }
  },
  mounted() {
    this.fetchInitColumns().then((columns)=>this.columns=columns);
  },
  watch: {
    currentMessage: {
      handler(oldVal,newVal){
        const nextEvaluatedWord = newVal[newVal.length-1];
        this.columns = [];
        if (nextEvaluatedWord) {
          this.fetchColumnsFromWord(nextEvaluatedWord.word).then(
              (columns)=>{
                this.columns=columns
              });
        } else {
          this.fetchInitColumns().then(
              (columns)=>{
                this.columns=columns
              });
        }

        if (!this.columns){
          this.fetchInitColumns().then(
              (columns)=>{
                this.columns=columns
              });
        }

      },
      deep:true
    },
    searchTerm: {
      handler(){
        this.fetchSearchedWord(this.searchTerm).then((data)=>{
          this.searchResults = data;
          console.log(this.searchResults);
        })
      },
      deep:true
    }
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

      <div class="search-btn-container" v-if="searchOn">
        <input name="search" v-model="searchTerm" type="text" placeholder="Search here"/>
          <span>
            <button id="clear" class="btn" @click="handleClear">
              <img src="/clear.png" alt="Clear Icon" /> Clear search
            </button>
          </span>
      </div>

    </div>

    <!--Linear-->
    <div v-if="searchOn" class="linear-container">
      <div v-if="searchResults && searchTerm" class="search-section d-flex flex-wrap">
          <div v-for="word in searchResults">
              <WordPictureTile :word="word.word.toUpperCase()"
                               :symbol="word.symbol"
                                @click="addWord(word.id, word.word, word.symbol)"/>
            </div>
      </div>
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
                               :part-of-speech="partOfSpeech"
                                @click="addWord(word.id, word.word, word.symbol, partOfSpeech)"/>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.search-btn-container{
  display: flex;
}

.speaking-container {
  display: flex;
  flex-direction: column;
}

.toggle-wrapper{
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
.search-icon {
  width: 50px;
}
</style>
