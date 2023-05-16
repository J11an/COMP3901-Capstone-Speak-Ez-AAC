<script>
import WordPictureTile from "./WordPictureTile.vue";
import WordPictureTileMessage from "./WordPictureTileMessage.vue";
import WordPictureTilePhrase from "./WordPictureTilePhrase.vue";
import WordPictureTilePhraseOpen from "./WordPictureTilePhraseOpen.vue";

const tts = window.speechSynthesis;

export default {
  name: "PhrasesContainer",
  components: {
    WordPictureTilePhraseOpen,
    WordPictureTilePhrase,
    WordPictureTile,
    WordPictureTileMessage,
  },

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
      error: "",
      message: "",
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
          self.phrases = [];
          self.phrases = data;
          console.log("phrases", self.phrases);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    expandPhrase(category) {
      console.log("Expanding ", category);
      let self = this;
      this.toggleExpandedPhrase = true;
      self.currentCategory = category;
      this.getPhrases(category);
      console.log(category);
    },
    hidePhrases() {
      this.toggleExpandedPhrase = false;
    },
    expandEditForm(id, phrase) {
      this.toggleEditPhraseForm = true;
      this.currentId = id;
      this.newPhrase = phrase;
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
      return fetch(`/api/saved_phrases?id=${id}`, {
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
    sendPhraseFetch(phrase, category) {
      return fetch(
        `/api/saved_phrases?category=${category}&saved_phrases=${phrase}`,
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
        .catch(function (error) {
          console.log(error);
        });
    },
    savePhrase(phrase, category) {
      this.sendPhraseFetch(phrase,category)
          .then((data)=>{
            if (data.message){
              this.getCategories();
              this.getPhrases(category);
              this.message = data.message;
              this.error = '';
              setTimeout(()=>{
                this.toggleAddPhraseForm = false;
                setTimeout(()=>{
                  this.error = '';
                  this.message = '';
                },100)
              },3000);
            }
            if (data.error) {
              this.error = data.error;
            }


          })
    },
    updatePhraseRequest(id, saved_phrases, category) {
      return fetch(
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
          if (data.message || data.error){
            return data;
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    updatePhrase(id, saved_phrases, category){
      this.updatePhraseRequest(id,saved_phrases,category)
          .then((data)=>{
            if (data.message){
              this.getCategories();
              this.getPhrases(category);
              this.message = data.message;
              this.error = '';
              setTimeout(()=>{
                this.toggleEditPhraseForm = false;
                setTimeout(()=>{
                  this.error = '';
                  this.message = '';
                },100)
              },3000);
            }
            if (data.error) {
              this.error = data.error;
            }
          })
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
          self.categories = [];
          self.categories = data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    removePhrase(id, category) {
      this.deletePhrase(id).then((data) => {
        this.phrases = [];
        console.log(this.phrases);
        this.getPhrases(category).then((data) => (this.phrases = data));
        console.log(category, this.phrases);
      });
    },
    texttospeech(phrase) {
      this.$emit("playAudio",phrase);
    },
  },
};
</script>

<template>
  <div class="container">
    <div class="phrase-header">
      <!--  -->
      <Transition name="fade" appear>
        <div v-if="toggleExpandedPhrase">
          <WordPictureTilePhraseOpen
            :word="currentCategory"
            @click="hidePhrases"
          />
        </div>
      </Transition>
      <button class="toggle-container btn p-4" @click="expandAddForm">
        <img class="add-icon" src="Add.png" />
        <p>Add a Phrase</p>
      </button>
    </div>

    <!-- START OF ADD PHRASE MODAL -->

    <Transition name="fade" appear>
      <div v-if="toggleAddPhraseForm" class="modal-mask">
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
          <div v-if="!message" class="modal-body">
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
                  v-model="currentCategory"
                />
                <datalist id="categories">
                  <div v-for="category in categories">
                    <option :value="category">{{ category }}</option>
                  </div>
                </datalist>
              </div>
            </div>
            <button
              @click="savePhrase(newPhrase, currentCategory)"
              class="btn btn-success btn-md submit-btn"
              type="submit"
            >
              Add Phrase
            </button>
          </div>
          <div>
            <div class="success-group" v-if="message">
              <img class="success-wrapper-btn" src="/checked.png"/>
              <p class="form-message">{{ message }}</p>
            </div>
            <div v-if="error">
              <p class="form-error">{{ error }}</p>
            </div>
          </div>
        </div>
      </div>
    </Transition>
    <!-- END OF ADD PHRASE MODAL -->

    <!-- START OF EDIT PHRASE MODAL -->
    <div v-if="toggleEditPhraseForm">
      <Transition name="fade" appear>
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
              <div v-if="!message" class="form-outline row-mb-4">
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
                        v-model="currentCategory"
                      />
                      <datalist id="categories">
                        <div v-for="category in categories">
                          <option  :value="category">{{ category }}</option>
                        </div>
                      </datalist>
                    </div>
                  </div>
                  <button
                    @click="updatePhrase(currentId, newPhrase, currentCategory)"
                    class="btn btn-success btn-md submit-btn"
                    type="submit"
                  >
                    Save Changes
                  </button>
              </div>
              <div>
                <div class="success-group" v-if="message">
                  <img class="success-wrapper-btn" src="/checked.png"/>
                  <p class="form-message">{{ message }}</p>
                </div>
                <div v-if="error">
                  <p class="form-error">{{ error }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </div>
    <!-- END OF EDIT PHRASE MODAL -->

    <div>
      <!-- Folders -->
      <div v-if="!toggleExpandedPhrase" class="category-container">
        <div
          v-for="(category, index) in categories"
          :key="index"
          class="category"
        >
          <WordPictureTilePhrase
            :word="category.toUpperCase()"
            :symbol="category.symbol"
            @click="expandPhrase(category)"
          />
        </div>
      </div>

      <!-- Expanded Phrases -->
      <Transition name="fade" appear>
          <div v-if="toggleExpandedPhrase" class="phrase-container">
            <h2>Tap your phrase to say it aloud</h2>
            <div class="phrase-group" v-for="phrase in phrases" :key="phrase.id">
              <Transition name="fade" appear>
              <div class="phrase-term-wrapper">
                <div class="phrase d-flex flex-wrap" @click="texttospeech(phrase.word)">
                  <div class="phrase-tile" v-for="(item, index) in phrase.word.split(' ')" :key="index">
                    <WordPictureTileMessage :word="item" :tts="tts" />
                  </div>
                </div>
                <div class="phrase-opts">
                  <button
                    type="button"
                    class="btn delete-btn"
                    @click="expandEditForm(phrase.id, phrase.word)"
                  >
                    <img class="modify-image" src="edit.png" alt="" />
                    <p>Edit Phrase</p>
                  </button>
                  <button
                    type="button"
                    class="btn delete-btn"
                    @click="removePhrase(phrase.id, currentCategory)"
                  >
                    <img class="modify-image" src="delete.png" alt="" />
                    <p>Delete Phrase</p>
                  </button>
                  
                </div>
              </div>
              </Transition>
            </div>
          </div>
      </Transition>
    </div>
  </div>
</template>

<style scoped>
.container{
  text-align: center;
  justify-content: center;
  align-items:center;
}

.success-group{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.back-btn-container{
  width: 200px;
  height: 200px;
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


.category-container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  flex: auto;
  align-items: center;
  justify-content: center;
  margin-bottom: -100px;
}

.category{
  margin: 5px;
}

.btn-back {
  width: 50px; 
  height: 50px;
}

.add-icon {
  width: 80%;
  height: auto;
  margin: auto;
}
.add-icon:hover {
  width: 95%;
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

.phrase-group {
  margin: 5px;
}

.phrase-term-wrapper {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  /*border: 2px solid black;*/
  /*background-color: antiquewhite;*/
}

.phrase-header {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: row;
}

.phrase {
  cursor: pointer;
  min-height: 150px;
  border: 4px solid rgb(53, 200, 112);
  border-radius: 20px;
  padding: 10px;
  margin: 10px;
  width: 80%;
}

.phrase:hover{
  background-color: lightblue;
  border: 5px solid black;
}

.phrase-container {
  display: flex;
  flex-direction: column;
  text-align: center;
  justify-content: center;
  overflow: auto;
  height: auto;
  width: 100%;
}

.modify-image{
  width: 60px;
  height: 60px;
}

.delete-btn img {
  width: 60px;
  height: 60px;
}

.delete-btn img:hover {
  width: 95px;
  height: 95px;
}

@media screen and (max-width:425px) {
  .category-container{
    display: grid;
    grid-template-columns: 70% 30%;
    gap: 2em;
    align-items: center;
    justify-content: center;
  }
}

</style>
