<script>
import WordPictureTile from "./WordPictureTile.vue";

export default {
  name: "WordDisplay",
  components: { WordPictureTile },

  data() {
    return {
      searchOn: false,
      pinsOn: false,
      showForm: false,
      toggleEditWordForm: false,
      toggleAddWordForm: false,
      csrf_token: "",
      columns: [],
      newWord: "",
      newCategory: "",
      newSymbol: "",
      currentId: 0,
      toggleWordColumn: false,
      searchTerm: "",
      searchResults: [],
    };
  },

  mounted() {
    this.fetchInitColumns().then((columns) => (this.columns = columns));
    //this.getWords().then((columns) => (this.columns = columns));
  },
  created() {
    this.getCsrfToken();
  },
  watch: {
    currentMessage: {
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

  methods: {
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
    getWords() {
      return fetch("api/words", {
        method: "GET",
        headers: {
          "X-CSRFToken": this.csrf_token,
        },
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          console.log(data);
          return data;
        })
        .catch(function (error) {
          console.log(error);
          return error;
        });
    },

    addWord(word, category, symbol) {
      fetch(`/api/word?word=${word}&?category=${category}&?symbol=${symbol}`, {
        method: "POST",
        headers: {
          "X-CSRFToken": this.csrf_token,
        },
      })
        .then(function (response) {
          console.log(response);
        })
        .then(function (data) {
          console.log(data);
        })
        .catch((error) => {
          console.error("Error adding word:", error);
        });
    },
    updateWord(id, word, category, symbol) {
      fetch(
        `api/word?id=${id}&word=${word}&symbol=${symbol}&category=${category}`,
        {
          method: "PUT",
          headers: {
            "X-CSRFToken": this.csrf_token,
          },
        }
      )
        .then(function (response) {
          console.log(response);
        })
        .then(function (data) {
          console.log(data);
        })
        .catch((error) => {
          console.error("Error adding word:", error);
        });
    },

    expandEditForm(id, word, category, symbol) {
      let self = this;
      self.currentId = id;
      self.newWord = word;
      self.newCategory = category;
      self.newSymbol = symbol;
      this.toggleEditWordForm = true;
    },

    hideEditForm() {
      this.toggleEditWordForm = false;
    },
    expandAddForm() {
      this.toggleAddWordForm = true;
    },
    hideAddForm() {
      this.toggleAddWordForm = false;
    },

    expandWordColumn() {
      this.toggleWordColumn = !this.toggleWordColumn;
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
    toggleSwitch() {
      this.searchOn = !this.searchOn;
      this.pinsOn = false;
    },
  },
};
</script>

<template>
  <div class="word-container">
    <h1>Here you can add or edit a word</h1>
    <button class="toggle-container btn" @click="expandAddForm">
      <img id="add-icon" src="Add.png" />
      <p>ADD WORD</p>
    </button>
    <button class="toggle-container btn" @click="expandWordColumn">
      <img id="edit-icon" src="edit.png" />
      <p>EDIT WORD</p>
    </button>
    <button :class="searchOn ? 'active btn' : 'btn'" @click="toggleSwitch">
      <img class="btn-img" src="/search.png" />
    </button>
  </div>

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
            @click="
              expandEditForm(word.id, word.word, word.category, word.symbol)
            "
          />
        </div>
        <div v-if="searchResults.length <= 0">
          <p>
            Couldn't find {{ searchTerm }}. But you can still add it as a word
          </p>
          <WordPictureTile
            :word="searchTerm.toUpperCase()"
            symbol="/HelpIcon.png"
            @click="expandAddForm(null, searchTerm, '/HelpIcon.png')"
          />
        </div>
      </div>
    </div>
  </div>

  <div
    v-for="column in this.columns"
    class="word-display"
    v-if="toggleWordColumn"
  >
    <div v-for="word in column" @draggable="true">
      <WordPictureTile
        :id="word.id"
        :word="word.word.toUpperCase()"
        :symbol="word.symbol"
        :category="word.category"
        @click="expandEditForm(word.word, word.symbol, word.category)"
      />
    </div>
  </div>

  <!-- START OF ADD WORD MODAL -->
  <div v-if="toggleAddWordForm">
    <Transition name="modal">
      <div class="modal-mask">
        <div class="modal-container">
          <div class="modal-header">
            <slot name="header">
              <p id="modal-title">Add a Word</p>
            </slot>
            <!-- <button class="btn btn-dark" @click="hideEditForm">BACK</button> -->
            <button
              type="button"
              class="btn-close"
              data-mdb-dismiss="modal"
              aria-label="Close"
              @click="hideAddForm"
            ></button>
          </div>
          <div class="modal-body">
            <div class="form-outline row-mb-4"></div>
            <label class="form-label" for="newWord">Word</label>
            <input
              id="newWord"
              type="text"
              class="form-control"
              name="newWord"
              v-model="newWord"
              placeholder="Enter your word here"
            />
            <div class="form-outline mb-4">
              <label class="form-label" for="category">Category</label>
              <div class="input-group">
                <input
                  type="text"
                  name="newCategory"
                  list="categories"
                  v-model="newCategory"
                />
                <datalist id="categories">
                  <option value="Home">Home</option>
                  <option value="School">School</option>
                  <option value="Basic Info">Basic Info</option>
                  <option value="Emergency">Emergency</option>
                </datalist>
              </div>
              <label class="form-label" for="newSymbol">Symbol</label>
              <input
                id="newSymbol"
                type="text"
                class="form-control"
                name="newSymbol"
                v-model="newSymbol"
                placeholder="Enter your image url here"
              />
            </div>
            <button
              @click="addWord(newWord, newCategory, newSymbol)"
              class="btn btn-success btn-md submit-btn"
              type="submit"
            >
              Add Word
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </div>
  <!-- END OF ADD WORD MODAL -->

  <!-- START OF EDIT WORDS MODAL -->
  <div v-if="toggleEditWordForm">
    <Transition name="modal">
      <div class="modal-mask">
        <div class="modal-container">
          <div class="modal-header">
            <slot name="header">
              <p id="modal-title">Edit a Word</p>
            </slot>
            <!-- <button class="btn btn-dark" @click="hideEditForm">BACK</button> -->
            <button
              type="button"
              class="btn-close"
              data-mdb-dismiss="modal"
              aria-label="Close"
              @click="hideEditForm"
            ></button>
          </div>
          <div class="modal-body">
            <div class="form-outline row-mb-4"></div>
            <label class="form-label" for="newWord">Word</label>
            <input
              id="newWord"
              type="text"
              class="form-control"
              name="newWord"
              v-model="newWord"
              placeholder="Enter your word here"
            />
            <div class="form-outline mb-4">
              <label class="form-label" for="category">Category</label>
              <div class="input-group">
                <input
                  type="text"
                  name="newCategory"
                  list="categories"
                  v-model="newCategory"
                />
                <datalist id="categories">
                  <option value="Home">Home</option>
                  <option value="School">School</option>
                  <option value="Basic Info">Basic Info</option>
                  <option value="Emergency">Emergency</option>
                </datalist>
              </div>
              <label class="form-label" for="newSymbol">Symbol</label>
              <input
                id="newSymbol"
                type="text"
                class="form-control"
                name="newSymbol"
                v-model="newSymbol"
                placeholder="Enter your image url here"
              />
            </div>
            <button
              @click="updateWord(currentId, newWord, newCategory, newSymbol)"
              class="btn btn-success btn-md submit-btn"
              type="submit"
            >
              Save Changes
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </div>
  <!-- END OF EDIT word MODAL -->
</template>

<style>
.modal-container {
  display: flex;
  flex-direction: column;
  width: 50%;
  height: auto;
}

#modal-title {
  font-size: x-large;
  font-weight: bold;
  margin: 0;
}

.modal-body {
  text-align: center;
  justify-content: center;
  align-items: center;
}

.form-label {
  font-size: x-large;
  font-weight: bold;
}

input {
  padding: 5px;
  outline: none;
  width: 100%;
  border-radius: 5px;
}

#add-icon {
  width: 80%;
  height: auto;
  margin: auto;
}

#edit-icon {
  height: auto;
  width: 100px;
  margin: auto;
}

.word-display {
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
</style>
