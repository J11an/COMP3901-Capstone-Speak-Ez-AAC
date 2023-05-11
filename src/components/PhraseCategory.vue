<script>
export default {
  name: "PhraseCategory",

  props: ["category"],

  data() {
    return {
      toggleExpand: false
    };
  },
  mounted() {},
  methods: {
  },
};
</script>

<template>
      <button class="btn-container">
        <div class="folder-btn">
          <p class="centered">{{ category.toUpperCase() }}</p>
        </div>
      </button>
</template>

<style scoped>

.add-icon{
  width: 100%;
  height: 20%;
}

.btn-container {
  background-color: transparent;
  border: none;
  cursor: pointer;
  margin:auto;
}

.folder-btn{
  padding: 70px 0;
  text-align: center;
  height: 200px;
  width:200px;
  background-image: url("folder.png");
  background-size: 100% 100%;
}
.centered{
  margin-top: 50px;
}

</style>
