<script>
import EditPhrase from "./EditPhrase.vue";
import WordPictureTileMessage from "./WordPictureTileMessage.vue";

const tts = window.speechSynthesis;

export default {
  components: { WordPictureTileMessage, EditPhrase },

  name: "PhraseCategory",

  props: ["phraseID",'phrases',"category"],
  emits: ["close-modal", "phrase-edited"],

  data() {
    return { 
      csrf_token: "", 
      message: "",
      error: false,
      showForm: false,
      newPhrase: "",
      newCategory: "",
     };
  },
  mounted() {},
  created() {
    this.getCsrfToken();
  },
  methods: {
    texttospeech(phrase) {
      // let message = e;
      // console.log(message);
      console.log(phrase);
      let utterance = new SpeechSynthesisUtterance(phrase);
      tts.speak(utterance);
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
    /*updatePhrase(id,phrase,category) {
      let uploadForm = document.getElementById("edit-form");
      let form_data = new FormData(uploadForm);
      fetch(`/api/saved_phrases?id=${id}?phrase=${phrase}?category=${category}`, {
        method: "PUT",
        body: form_data,
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
    },*/
    editPhrase(id, newPhrase, newCategory) {
      console.log(id)
      fetch(
        `/api/phrase?id=${id}&?saved_phrases=${newPhrase}&?category=${newCategory}`,
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
          if ("error" in data) {
            self.errors = data.error;
            self.error = true;
            console.log(self.error);
          } else {
            self.error = false;
            document.getElementById("edit-form").reset();
          }
        })
        .catch(function (error) {
          console.log(error);
        });
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
};
</script>

<template>
  <div class="container">
    <h1 id="title">{{ category }}</h1>
    <h3 id="title">Tap the phrase you want them to hear!</h3>
    <br />
    <div class="d-grid gap-2 col-7 mx-auto" role="group">
      <div
        v-for="(phrase, index) in phrases"
        :key="index"
        class="phrase-container"
        :phraseID="phrase.id"
      >
      
        <div class="phrase" @click="texttospeech(phrase.word)">
          <div
            v-if="phrase.word"
            v-for="word in phrase.word.split(' ')"
            :key="word.id"
            :phraseID="phrase.id"
          >
            <div class="row-6 word">
              <WordPictureTileMessage
                :word="word"
                :symbol="word.symbol"
                :tts="tts"
              />
            </div>
          </div>
        </div>
        <div class="phrase-opts">
          <button
            type="button"
            class="btn delete-btn"
            @click="deletePhrase(phrase.id)"
          >
            <img src="delete.png" alt="" />
            <p>Delete</p>
          </button>
          <button type="button" class="btn delete-btn" @click="showForm = true">
            <img src="edit.png" alt="" />
            <p>Edit</p>
          </button>
          <editPhrase
            v-show="showForm"
            @close-modal="showForm = false"
          />
        </div>
      </div>
    </div>
  </div>

  <!-- Edit Phrase Modal -->
  <div v-show="showForm">
  <div class="container-model modal" @click="$emit('close-modal')">
    <div class="modal-dialog d-flex justify-content-center" @click.stop>
      <div class="modal-content w-100 +">
        <div class="modal-header">
          <h5 class="modal-title">Edit a Phrase</h5>
          <button
            type="button"
            class="btn-close"
            data-mdb-dismiss="modal"
            aria-label="Close"
            @click="$emit('close-modal')"
          ></button>
        </div>
        <div v-if="error" id="alert" class="alert alert-danger" role="alert">
          {{ errors }}
        </div>

        <div class="modal-body p-4">
          <form
            id="edit-form"
            enctype="multipart/form-data"
          >
            <div class="form-outline row-mb-4">
              <label class="form-label" for="phrase">Phrase</label>
              <input
                id="phrase"
                type="text"
                class="form-control"
                name="newPhrase"
                v-model="newPhrase"
                placeholder="Enter your phrase here"
              />
            </div>
            <br />

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
              @click="editPhrase(phraseID, newPhrase, newCategory)"
              class="btn btn-success btn-md"
              type="submit"
            >
              Save changes
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
}

#title {
  text-align: center;
}

.delete-btn {
  margin: 0;
  height: 50%;
  width: 80px;
}

.delete-btn img {
  height: 100%;
  max-width: 100%;
}

.phrase {
  display: flex;
  flex-direction: row;
  border: 2px solid black;
  justify-content: center;
  align-items: center;
  padding: 5px;
  height: 100%;
  max-width: 100%;
  border-radius: 10px;
}

.phrase-container {
  display: flex;
}

.phrase {
  flex: 1;
}

.phrase-opts {
  display: flex;
  align-items: center;
}
.container-model {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  background-color: #d8d8d8a8;
}

.modal-content {
  text-align: center;
  background-color: white;
  height: 500px;
  width: 500px;
  margin-top: 10%;
  border-radius: 20px;
}
</style>
