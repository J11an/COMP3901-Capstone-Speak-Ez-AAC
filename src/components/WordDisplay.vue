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
      message: "",
      error: "",
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
      return fetch(
        `/api/word?word=${word}&category=${category}&symbol=${symbol}`,
        {
          method: "POST",
          headers: {
            "X-CSRFToken": this.csrf_token,
          },
        }
      )
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          if (data.message || data.error) {
            return data;
          }
        })
        .catch((error) => {
          console.log("Error adding word:", error);
        });
    },
    updateWord(id, word, category, symbol) {
      return fetch(
        `api/word?id=${id}&word=${word}&symbol=${symbol}&category=${category}`,
        {
          method: "PUT",
          headers: {
            "X-CSRFToken": this.csrf_token,
          },
        }
      )
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          return data;
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
    },
    saveWord(word, category, symbol) {
      this.addWord(word, category, symbol).then((data) => {
        if (data.message) {
          this.message = data.message;
          this.error = "";
          setTimeout(() => {
            this.toggleAddWordForm = false;
            setTimeout(() => {
              this.error = "";
              this.message = "";
            }, 100);
          }, 3000);
        }
        if (data.error) {
          this.error = data.error;
        }
      });
    },
    editWord(id, word, category, symbol) {
      this.updateWord(id, word, category, symbol).then((data) => {
        if (data.message) {
          this.message = data.message;
          this.error = "";
          setTimeout(() => {
            this.toggleEditWordForm = false;
            setTimeout(() => {
              this.error = "";
              this.message = "";
            }, 100);
          }, 3000);
        }
        if (data.error) {
          this.error = data.error;
        }
      });
    },
  },
};
</script>

<template>
  <div class="container">
    <div class="word-container row">
      <h1>Here you can add or edit a word</h1>
      <div class="word-option col-sm">
        <button class="toggle-container btn" @click="expandAddForm">
          <img id="add-icon" src="Add.png" />
          <p>ADD WORD</p>
        </button>
      </div>
      <div class="word-option col-sm">
        <button class="toggle-container btn" @click="expandWordColumn">
          <img id="edit-icon" src="edit.png" />
          <p>EDIT WORD</p>
        </button>
      </div>
      <div class="word-option col-sm">
        <button :class="searchOn ? 'active btn' : 'btn'" @click="toggleSwitch">
          <img class="btn-img" src="/search.png" />
          <p>SEARCH WORD</p>
        </button>
      </div>
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
          @click="
            expandEditForm(word.id, word.word, word.category, word.symbol)
          "
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
            <div v-if="!message" class="modal-body">
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
                @click="saveWord(newWord, newCategory, newSymbol)"
                class="btn btn-success btn-md submit-btn"
                type="submit"
              >
                Add Word
              </button>
            </div>
            <div>
              <div class="success-group" v-if="message">
                <img class="success-wrapper-btn" src="/checked.png" />
                <p class="form-message">{{ message }}</p>
              </div>
              <div v-if="error">
                <p class="form-error">{{ error }}</p>
              </div>
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
            <div v-if="!message" class="modal-body">
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
                @click="editWord(currentId, newWord, newCategory, newSymbol)"
                class="btn btn-success btn-md submit-btn"
                type="submit"
              >
                Save Changes
              </button>
            </div>
            <div>
              <div class="success-group" v-if="message">
                <img class="success-wrapper-btn" src="/checked.png" />
                <p class="form-message">{{ message }}</p>
              </div>
              <div v-if="error">
                <p class="form-error">{{ error }}</p>
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </div>
    <!-- END OF EDIT word MODAL -->
  </div>
</template>

<style scoped>
.container {
  display: block;
  align-items: center;
  justify-content: center;
  text-align: center;
  width: 90%;
}

.word-container {
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 50px;
}

.word-option {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  text-align: center;
  box-shadow: 0px 2px 4px 2px rgba(0, 0, 0, 0.15);
  /* background-color: rgb(198, 216, 37); */
  border-radius: 10px;
  overflow: hidden;
  width: 200px;
  height: 200px;
  margin: 20px;
  padding: auto;
  float: right;
}

p {
  font-size: x-large;
  font-weight: bold;
  padding-top: 5px;
}

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
  background: transparent;
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
  width: 80px;
  margin: 10px 90px;
}

.btn-img:hover {
  width: 65px;
}

.btn-img-hovered {
  width: 100px;
}

.clear-img {
  width: 50px;
}
.form-error {
  font-size: 26px;
  font-weight: bolder;
  color: crimson;
}
.form-message {
  font-size: 26px;
  font-weight: bolder;
  color: #3a7bd5;
}

.success-wrapper-btn {
  width: 150px;
  height: 150px;
}
</style>
