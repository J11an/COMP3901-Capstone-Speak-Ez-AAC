<script>
import WordPictureTile from "./WordPictureTile.vue";
import PinnedWordsContainer from "./PinnedWordsContainer.vue";

export default {
  components: { WordPictureTile, PinnedWordsContainer },
  props: {
    currentMessage: Array,
  },
  data() {
    return {
      searchOn: false,
      pinsOn: false,
      columns: [],
      searchTerm: "",
      searchResults: [],
    };
  },
  methods: {
    toggleSwitch() {
      this.searchOn = !this.searchOn;
      this.pinsOn = false;
    },
    switchPins(){
      this.pinsOn = !this.pinsOn;
      this.searchOn = false;
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
          return error;
        });
    },
    fetchColumnsFromWord(word) {
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
          return error;
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
          return data;
        })
        .catch(function (error) {
          return error;
        });
    },
    addWord(id, word, symbol, partOfSpeech) {
      this.$emit("updateSentence", [
        "add",
        {
          id: id,
          word: word,
          symbol: symbol,
          partOfSpeech: partOfSpeech,
        },
      ]);
    },
    handleClear() {
      this.searchTerm = "";
    },
    refreshResults() {
      const lastWord = this.currentMessage[this.currentMessage.length - 1];
      this.columns = [];
      if (lastWord) {
        this.fetchColumnsFromWord(lastWord.word).then((columns) => {
          this.columns = columns;
        });
      } else {
        this.fetchInitColumns().then((columns) => (this.columns = columns));
      }
    },
  },
  mounted() {
    this.fetchInitColumns().then((columns) => (this.columns = columns));
  },
  watch: {
    currentMessage: {
      handler(oldVal, newVal) {
        const nextEvaluatedWord = newVal[newVal.length - 1];
        this.columns = [];
        if (nextEvaluatedWord) {
          this.fetchColumnsFromWord(nextEvaluatedWord.word).then((columns) => {
            this.columns = columns;
          });
        } else {
          this.fetchInitColumns().then((columns) => {
            this.columns = columns;
          });
        }

        if (!this.columns) {
          this.fetchInitColumns().then((columns) => {
            this.columns = columns;
          });
        }
      },
      deep: true,
    },
    searchTerm: {
      handler() {
        this.fetchSearchedWord(this.searchTerm).then((data) => {
          this.searchResults = data;
          console.log(this.searchResults);
        });
      },
      deep: true,
    },
  },
};
</script>

<template>
  <!--Toggle-->
  <div class="speaking-container container">
    <div class="toggle-wrapper">
      <button :class="pinsOn ? 'active btn' : 'btn'" @click="switchPins">
        <img class="btn-img" src="/pinned_folder.png" alt="Speaker Icon" />
      </button>

      <button
        class="refresh-container btn"
        @click="refreshResults"
        v-if="!searchOn && !pinsOn"
      >
        <img class="btn-img" src="/refresh-page-option.png" />
      </button>

      <button :class="searchOn ? 'active btn' : 'btn'" @click="toggleSwitch">
        <img class="btn-img" src="/search.png" />
      </button>


      <div class="search-btn-container" v-if="searchOn">
        <input
          name="search"
          v-model="searchTerm"
          type="text"
          placeholder="Search here"
        />
        <span>
          <button id="clear" class="btn" @click="handleClear">
            <img src="/clear.png" class="clear-img" alt="Clear Icon" />
          </button>
        </span>
      </div>
    </div>

    <div>
      <PinnedWordsContainer v-if="pinsOn" />
    </div>

    <!--Linear-->
    <div v-if="searchOn" class="linear-container">
      <div
        v-if="searchResults && searchTerm"
        class="search-section d-flex flex-wrap"
      >
        <div v-if="searchResults.length" v-for="word in searchResults">
          <WordPictureTile
            :word="word.word.toUpperCase()"
            :symbol="word.symbol"
            @click="addWord(word.id, word.word, word.symbol)"
          />
        </div>
        <div v-if="searchResults.length <= 0">
          <p>Couldn't find {{ searchTerm }}. Would you like to add it?</p>
          <WordPictureTile
            :word="searchTerm.toUpperCase()"
            symbol="/HelpIcon.png"
            @click="addWord(null, searchTerm, '/HelpIcon.png')"
          />
        </div>
      </div>
    </div>

    <!--Dynamic-->
    <div v-if="!searchOn && !pinsOn" class="dynamic-container">
      <div>
        <div
          v-if="!searchOn"
          class="board-container d-flex justify-content-between mt-3"
        >
          <div v-for="(words, partOfSpeech) in columns">
            <div v-for="word in words">
              <WordPictureTile
                :word="word.word.toUpperCase()"
                :symbol="word.symbol"
                :part-of-speech="partOfSpeech"
                @click="addWord(word.id, word.word, word.symbol, partOfSpeech)"
              />
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<style scoped>
.clear-img{
  width: 50px;
}

.search-btn-container {
  display: flex;
}

.speaking-container {
  display: flex;
  flex-direction: column;
}

.toggle-wrapper {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
.btn-img {
  width: 60px;
  margin: 0 20px;
}

.active {
  background-color: #9bb8e3;
}

#clear{

}
</style>
