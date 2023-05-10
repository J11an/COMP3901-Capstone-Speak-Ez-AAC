<script>
export default {
  name: "AddPhrase",
  emits: ["close-modal"],

  data() {
    return { csrf_token: "" };
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
  <div class="container-model" @click="$emit('close-modal')">
    <div class="modal-cont" @click.stop>
      <button>
        <div class="close" @click="$emit('close-modal')">
          <img class="close-img" src="/search.png" alt="" />
        </div>
      </button>
      <form
        id="registrationform"
        enctype="multipart/form-data"
        @submit.prevent="savePhrase"
      >
        <div class="row mb-3">
          <div class="col-6">
            <label for="saved_phrases" class="form-label font-weight-bold"
              >Saved Phrase
            </label>
            <input
              type="text"
              placeholder="Enter Phrase"
              name="saved_phrases"
              class="form-control"
              id="saved_phrases"
            />
          </div>
          <div class="col-6">
            <label for="category" class="form-label font-weight-bold"
              >Category
            </label>
            <input
              type="text"
              placeholder="Enter category"
              name="category"
              class="form-control"
            />
          </div>
        </div>
        <button class="btn btn-success btn-md" type="submit">Add Phrase</button>
      </form>
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

.modal-cont {
  text-align: center;
  background-color: white;
  height: 500px;
  width: 500px;
  margin-top: 10%;
  padding: 60px 0;
  border-radius: 20px;
}
</style>
