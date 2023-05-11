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
  <div class="container-model modal" @click="$emit('close-modal')">
    <div class="modal-dialog d-flex justify-content-center" @click.stop>
      <div class="modal-content w-100
      +">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel1">Save a Phrase</h5>
          <button
            @click="$emit('close-modal')"
            type="button"
            class="btn-close"
            data-mdb-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>

        <div class="modal-body p-4">
          <form
            id="registrationform"
            enctype="multipart/form-data"
            @submit.prevent="savePhrase"
          >
            <div class="form-outline row-mb-4">
              <label class="form-label" for="email1">Phrase</label>
              <input
                type="email"
                id="email1"
                class="form-control"
                placeholder="Enter your phrase here"
              />
            </div>

            <div class="form-outline mb-4">
              <label class="form-label" for="password1">Category</label>
              <input
                type="password"
                id="password1"
                class="form-control"
                placeholder="Enter category"
              />
            </div>

            <button class="btn btn-success btn-md" type="submit">
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
