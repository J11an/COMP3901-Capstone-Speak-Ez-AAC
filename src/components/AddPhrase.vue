<script>
export default {
  name: "AddPhrase",
  emits: ["close-modal", "phrase-added"],

  data() {
    return { csrf_token: "", message: "", error: false };
  },
  created() {
    this.getCsrfToken();
  },
  methods: {
    savePhrase() {
      let self = this;
      let uploadForm = document.getElementById("registrationform");
      let form_data = new FormData(uploadForm);
      fetch("/api/saved_phrases", {
        method: "POST",
        body: form_data,
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
          self.$emit("phrase-added");
          console.log(data);
          if ("error" in data) {
            self.errors = data.error;
            self.error = true;
            console.log(self.error);
          } else {
            self.error = false;
            document.getElementById("registrationform").reset();
          }
        })
        .catch(function (error) {
          console.log(error);
          console.log(form_data);
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
  <div class="container-model modal" @click="$emit('close-modal')">
    <div class="modal-dialog d-flex justify-content-center" @click.stop>
      <div class="modal-content w-100 +">
        <div class="modal-header">
          <h5 id="exampleModalLabel1" class="modal-title">Save a Phrase</h5>
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
            id="registrationform"
            enctype="multipart/form-data"
            @submit.prevent="savePhrase"
          >
            <div class="form-outline row-mb-4">
              <label class="form-label" for="saved_phrases">Phrase</label>
              <input
                id="saved_phrases"
                type="text"
                class="form-control"
                name="saved_phrases"
                placeholder="Enter your phrase here"
              />
            </div>
            <br />

            <div class="form-outline mb-4">
              <label class="form-label" for="category">Category</label>
              <div class="input-group">
                <input type="text" name="category" list="categories" />
                <datalist id="categories">
                  <option value="Home">Home</option>
                  <option value="School">School</option>
                  <option value="Basic Info">Basic Info</option>
                  <option value="Emergency">Emergency</option>
                </datalist>
                <!-- <select class="form-select" name="category" placeholder="Select category">
                  <option value="Home">Home</option>
                  <option value="School">School</option>
                  <option value="Basic Info">Basic Info</option>
                  <option value="Emergency">Emergency</option>
                </select> -->
              </div>
            </div>

            <button
              @click="$emit('phrase-added')"
              class="btn btn-success btn-md"
              type="submit"
            >
              Add Phrase
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.close-img {
  width: 50px;
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
