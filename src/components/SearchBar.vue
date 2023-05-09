<script setup>
import { ref } from "vue";

const searchTerm = ref("");
const results = ref([]);

function searchWord() {
  fetch(`api/search?query=${searchTerm.value}`, {
    method: "POST",
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      console.log(data);
      results.value = data;
      console.log(results);
    })
    .catch(function (error) {
      console.log(error);
      //console.log("test");
    });
}
</script>

<template>
  <div>
    <input
      v-model="searchTerm"
      type="text"
      placeholder="Search here"
      @keyup.enter="searchWord"
    />
    <ul>
      <li v-for="result in results" :key="result.id">{{ result }}</li>
    </ul>
  </div>
</template>
