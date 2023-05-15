<script>
import WordPictureTile from "../WordPictureTile.vue";
import draggable from "vuedraggable";

export default {
  components: { WordPictureTile, draggable },
  props: {
    currentMessage: Array,
  },
  data() {
    return {
      searchOn: false,
      pinsOn: false,
      columns: [],
      columnSortOrder: {
        pronoun: 0,
        noun: 1,
        noun2: 1,
        verb: 2,
        verb2: 2,
        adjectives: 3,
        adjective2: 3,
        articles: 4,
        preposition: 5,
        conjunction: 6,
        adverb: 7,
      },
      searchTerm: "",
      searchResults: [],
      pinnedResults: [],
      hoverActiveAdd: false,
      hoverActiveDelete: false,
      currentHoveredWord: -1,
      csrf_token: "",
    };
  },
  methods: {
    toggleSwitch() {
      this.searchOn = !this.searchOn;
      this.pinsOn = false;
    },
    toggleActiveFolder() {
      this.hoverActiveAdd = !this.hoverActiveAdd;
    },
    toggleActiveDelete() {
      this.hoverActiveDelete = !this.hoverActiveDelete;
    },
    cachePinnedWord(word) {
      console.log(word);
      this.currentHoveredWord = word;
    },
    addPinnedWord() {
      this.addPinnedWordRequest(this.currentHoveredWord).then((data) => {
        this.pinnedResults = [];
        this.fetchPins().then((pins) => (this.pinnedResults = pins));
      });
      this.pinsOn = !this.pinsOn;
      this.hoverActiveAdd = !this.hoverActiveAdd;
      this.currentHoveredWord = "";
    },
    removePinnedWord() {
      this.deletePinnedWordRequest(this.currentHoveredWord).then((data) => {
        this.pinnedResults = [];
        this.fetchPins().then((pins) => (this.pinnedResults = pins));
      });
      this.hoverActiveDelete = !this.hoverActiveDelete;
      this.currentHoveredWord = "";
    },
    switchPins() {
      this.pinsOn = !this.pinsOn;
      this.searchOn = false;
    },
    sortColumns(columns) {
      const convertedArr = Object.keys(columns).map((key) => [
        key,
        columns[key],
      ]);
      const sortedArr = convertedArr.sort(
        (a, b) => this.columnSortOrder[a[0]] - this.columnSortOrder[b[0]]
      );
      console.log(sortedArr);
      return sortedArr;
    },
    deletePinnedWordRequest(wordID) {
      return fetch(`/api/pinned_words?id=${wordID}`, {
        method: "DELETE",
        headers: {
          "X-CSRFToken": this.csrf_token,
        },
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
    addPinnedWordRequest(wordID) {
      return fetch(`/api/pinned_words?word_id=${wordID}`, {
        method: "POST",
        headers: {
          "X-CSRFToken": this.csrf_token,
        },
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
      this.searchResults = [];
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
    fetchPins() {
      return fetch(`/api/pinned_words`, {
        method: "GET",
        headers: {
          "X-CSRFToken": this.csrf_token,
        },
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
    getCsrfToken() {
      let self = this;
      fetch("/api/csrf-token")
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          self.csrf_token = data.csrf_token;
        });
    },
  },
  mounted() {
    this.fetchInitColumns().then((columns) => (this.columns = columns));
    this.fetchPins().then((pins) => (this.pinnedResults = pins));
  },
  created() {
    this.getCsrfToken();
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
        });
      },
      deep: true,
    },
  },
};
</script>

<template>
  <!--Toggle-->
  <div class="toggle-wrapper">
    <button
      :class="pinsOn ? 'active btn' : 'btn'"
      @click="switchPins"
      @dragenter.prevent="toggleActiveFolder"
      @dragleave.prevent="toggleActiveFolder"
      @dragover.prevent
      @drop.prevent="addPinnedWord"
    >
      <img
        :class="
          hoverActiveAdd && !pinsOn ? 'btn-img-hovered btn-img' : 'btn-img'
        "
        :src="
          hoverActiveAdd || pinsOn ? '/open-folder.png' : '/pinned_folder.png'
        "
        alt="Speaker Icon"
      />
    </button>

    <button
      v-if="pinsOn"
      class="btn"
      @dragenter.prevent="toggleActiveDelete"
      @dragleave.prevent="toggleActiveDelete"
      @dragover.prevent
      @drop.prevent="removePinnedWord"
    >
      <img
        :class="hoverActiveDelete ? 'btn-img-hovered btn-img' : 'btn-img'"
        :src="hoverActiveDelete ? '/trashOpen.png' : '/trashClosed.png'"
        alt="Speaker Icon"
      />
    </button>

    <button
      class="refresh-container btn"
      @click="refreshResults"
      v-if="!searchOn && !pinsOn"
    >
      <img class="btn-img" src="/refresh-page-option.png" />
    </button>

    <button v-if="!pinsOn" :class="searchOn ? 'active btn' : 'btn'" @click="toggleSwitch">
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
  <div class="speaking-container container">
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
            draggable="true"
            @dragstart="cachePinnedWord(word.id)"
          />
        </div>
        <div v-if="searchResults.length <= 0">
          <p>
            Couldn't find {{ searchTerm }}. But you can still add it to your
            sentence
          </p>
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
          <div v-for="column in this.sortColumns(columns)">
            <Transition name="fade" appear>
              <div>
                <div v-for="word in column[1]">
                  <WordPictureTile
                    :id="word.id"
                    :word="word.word.toUpperCase()"
                    :symbol="word.symbol"
                    :part-of-speech="column[0]"
                    @click="addWord(word.id, word.word, word.symbol, column[0])"
                    @dragstart="cachePinnedWord(word.id)"
                    draggable="true"
                  />
                </div>
              </div>
            </Transition>
          </div>
        </div>
      </div>
    </div>

    <!-- Pins -->
    <div v-if="pinsOn" class="pinned-container">
      <div v-if="pinnedResults" class="search-section d-flex flex-wrap">
        <div v-for="word in pinnedResults" v-bind:key="word.id">
          <WordPictureTile
            :word="word.word.toUpperCase()"
            :symbol="word.symbol"
            @click="addWord(word.id, word.word, word.symbol)"
            draggable="true"
            @dragstart="cachePinnedWord(word.id)"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.clear-img {
  width: 50px;
}

.search-btn-container {
  display: flex;
}

.speaking-container {
  display: flex;
  flex-direction: column;
  overflow: auto;
  max-height: 100vh;
  @media (min-height: 300px) {
    max-height: 55vh;
  }
  @media (min-height: 808px) {
    max-height: 60vh;
  }
  @media (min-height: 1000px) {
    max-height: 65vh;
  }
}

.speaking-container {
  overflow-y: scroll;
}
.speaking-container::-webkit-scrollbar {
  width: 5px;
}
.speaking-container::-webkit-scrollbar-track {
  background: #eee;
}
.speaking-container::-webkit-scrollbar-thumb {
  border-radius: 1rem;
  background-color: #3a7bd5;
  background-image: linear-gradient(to top, #3a7bd5 0%, #3a7bd5 100%);
}

.toggle-wrapper {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  margin-bottom: 10px;
}
.btn-img {
  width: 60px;
  margin: 0 20px;
}

.btn-img:hover {
  width: 65px;
}

.btn-img-hovered {
  width: 100px;
}
.active {
  background-color: #9bb8e3;
}

#clear {
}
</style>
