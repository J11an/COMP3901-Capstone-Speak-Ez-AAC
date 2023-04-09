<script>
import DisplayPhrase from "../components/DisplayPhrase.vue";

export default {
  components: { DisplayPhrase },
  data() {
    return {
      phrasesList: ["Help", "My name is Jane"],
    };
  },
  methods: {},
};
</script>

<template>
  <div>
    <h2>SOS</h2>
    <DisplayPhrase
      v-for="phrase in phrasesList"
      :key="phrase"
      :title="phrase"
    />
  </div>
</template>
