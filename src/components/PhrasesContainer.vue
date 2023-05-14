<script>
import WordPictureTile from "./WordPictureTile.vue";
import WordPictureTileMessage from "./WordPictureTileMessage.vue";

const tts = window.speechSynthesis;

export default {
  name: "PhrasesContainer",
  components: { WordPictureTile, WordPictureTileMessage },

  data() {
    return {
      phrases: {},
      toggleExpandedPhrase: false,
      showForm: false,
      toggleEditPhraseForm: false,
      toggleAddPhraseForm: false,
      categories: [],
      currentCategory: "",
      newCategory: "",
      newPhrase: "",
      currentId: 0,
    };
  },
  mounted() {
    this.getPhrases();
    this.getCategories();
  },
  methods: {
    getPhrases(category) {
      let self = this;
      fetch(`/api/saved_phrases?category=${category}`, {
        method: "GET",
        headers: {
          "X-CSRFToken": this.csrf_token,
        },
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          self.phrases = data;
          console.log("phrases", self.phrases);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    expandPhrase(category) {
      let self = this;
      this.toggleExpandedPhrase = true;
      self.currentCategory = category;
      this.getPhrases(category);
      console.log(category);
    },
    hidePhrases() {
      this.toggleExpandedPhrase = false;
    },
    expandEditForm(id) {
      let self = this;
      this.toggleEditPhraseForm = true;
      self.currentId = id;
    },
    hideEditForm() {
      this.toggleEditPhraseForm = false;
    },
    expandAddForm() {
      this.toggleAddPhraseForm = true;
    },
    hideAddForm() {
      this.toggleAddPhraseForm = false;
    },
    deletePhrase(id) {
      fetch(`/api/saved_phrases?id=${id}`, {
        method: "DELETE",
        headers: {
          "X-CSRFToken": this.csrf_token,
        },
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          console.log(data);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    savePhrase(phrase, category) {
      fetch(`/api/saved_phrases?category=${category}&saved_phrases=${phrase}`, {
        method: "POST",
        error: false,
        errors: [],
        headers: {
          "X-CSRFToken": this.csrf_token,
        },
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          console.log(data);
          if ("error" in data) {
            self.errors = data.error;
            self.error = true;
            console.log(self.error);
          } else {
            self.error = false;
            //document.getElementById("registrationform").reset();
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    updatePhrase(id, saved_phrases, category) {
      fetch(
        `/api/saved_phrases?id=${id}&saved_phrases=${saved_phrases}&category=${category}`,
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
          console.log(data);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    getCategories() {
      let self = this;
      fetch("/api/get_phrase_categories", {
        method: "GET",
        headers: {
          "X-CSRFToken": this.csrf_token,
        },
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          self.categories = data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    AutoDelete(id, category) {
      let self = this;
      this.deletePhrase(id);
      this.hidePhrases();
      this.expandPhrase(category);
    },
    texttospeech(phrase) {
      console.log(phrase);
      let utterance = new SpeechSynthesisUtterance(phrase);
      tts.speak(utterance);
    },
  },
};
</script>

<template>
  <div class="container">
    <div class="phrase-header">
      <h2>SELECT FROM OR ADD ONE OF YOUR PHRASES</h2>
      <!--  -->
      <button class="toggle-container btn" @click="expandAddForm">
        <img class="add-icon" src="Add.png" />
        <p>ADD PHRASE</p>
      </button>
    </div>

    <!-- START OF ADD PHRASE MODAL -->

    <div v-if="toggleAddPhraseForm">
      <Transition name="modal">
        <div class="modal-mask">
          <div class="modal-container">
            <div class="modal-header">
              <slot name="header">
                <p id="modal-title">Add a Phrase</p>
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
              <label class="form-label" for="phrase">Phrase</label>
              <input
                id="phrase"
                type="text"
                class="form-control"
                name="newPhrase"
                v-model="newPhrase"
                placeholder="Enter your phrase here"
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
              </div>
              <button
                @click="savePhrase(newPhrase, newCategory)"
                class="btn btn-success btn-md submit-btn"
                type="submit"
              >
                Add Phrase
              </button>
            </div>
          </div>
        </div>
      </Transition>
    </div>
    <!-- END OF ADD PHRASE MODAL -->

    <!-- START OF EDIT PHRASE MODAL -->
    <div v-if="toggleEditPhraseForm">
      <Transition name="modal">
        <div class="modal-mask">
          <div class="modal-container">
            <div class="modal-header">
              <slot name="header">
                <p id="modal-title">Edit a Phrase</p>
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
              <label class="form-label" for="phrase">Phrase</label>
              <input
                id="phrase"
                type="text"
                class="form-control"
                name="newPhrase"
                v-model="newPhrase"
                placeholder="Enter your phrase here"
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
              </div>
              <button
                @click="updatePhrase(currentId, newPhrase, newCategory)"
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
    <!-- END OF EDIT PHRASE MODAL -->

    <div>
      <!-- Folders -->
      <div class="category-container">
        <div
          v-for="(category, index) in categories"
          v-if="!toggleExpandedPhrase"
          :key="index"
          class="category"
        >
          <WordPictureTile
            :word="category.toUpperCase()"
            :symbol="category.symbol"
            @click="expandPhrase(category)"
          />
        </div>
      </div>

      <!-- Expanded Phrases -->
      <div v-if="toggleExpandedPhrase">
        <button class="btn btn-dark" @click="hidePhrases">BACK</button>
        <div class="phrase-container">
        <h1>{{currentCategory}}</h1>
          <div v-for="phrase in phrases" :key="phrase.id">
            <div class="phrase" @click="texttospeech(phrase.word)">
              <div v-for="(item, index) in phrase.word.split(' ')" :key="index">
                <WordPictureTileMessage :word="item" :tts="tts" />
              </div>
            </div>
            <div class="phrase-opts">
              <button
                type="button"
                class="btn delete-btn"
                @click="AutoDelete(phrase.id, currentCategory)"
              >
                <img src="delete.png" alt="" />
                <p>Delete</p>
              </button>
              <button
                type="button"
                class="btn delete-btn"
                @click="expandEditForm(phrase.id)"
              >
                <img src="edit.png" alt="" />
                <p>Edit</p>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.category-container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  flex: auto;
  align-items: center;
  justify-content: center;
}

.add-icon {
  width: 80%;
  height: auto;
  margin: auto;
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
  font-size: 18px;
  padding: 5px;
  outline: none;
  width: 100%;
  border-radius: 5px;
}

.submit-btn {
  width: 50%;
  padding: 5px;
  text-align: center;
}

.phrase-header {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.phrase {
  display: flex;
  flex-direction: row;
  border: 2px solid black;
  justify-content: center;
  align-items: center;
  padding: 5px;
  height: auto;
  min-width: fit-content;
  border-radius: 10px;
  margin: 20px;
}

.phrase-container {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.phrase-opts {
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding-top: 30px;
}

.delete-btn {
  height: 50%;
  width: 80px;
}

.delete-btn img {
  height: 100%;
  max-width: 100%;
}
</style>
