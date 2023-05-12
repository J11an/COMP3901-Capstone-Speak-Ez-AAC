<script>
export default {
  name: "EditPhrase",
  emits: ["close-modal", "phrase-edited"],

  props:["category","saved_phrases"],
  
  data() {
    return { csrf_token: "", message: "", error: false };
  },
  created() {
    this.getCsrfToken();
  },
  methods: {
    editPhrase() {
      let self = this;
      let editForm = document.getElementById("edit-form");
      let form_data = new FormData(editForm);
      fetch("/api/edit_phrase", {
        method: "PUT",
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
          self.$emit("phrase-edited");
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
          <h5 id="exampleModalLabel1" class="modal-title">Edit a Phrase</h5>
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
            @submit.prevent="editPhrase"
          >
            <div class="form-outline row-mb-4">
              <label class="form-label" for="edit_phrase">Phrase</label>
              <input
                id="edit_phrase"
                type="text"
                class="form-control"
                name="edit_phrase"
                placeholder="Enter your phrase here"
              />
            </div>
            <br />

            <div class="form-outline mb-4">
              <div class="input-group">
                <select class="form-select" name="category">
                  <option selected>Category</option>
                  <option value="Home">Home</option>
                  <option value="School">School</option>
                  <option value="Basic Info">Basic Info</option>
                  <option value="Emergency">Emergency</option>
                </select>
              </div>
            </div>

            <button
              @click="$emit('phrase-edited')"
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
