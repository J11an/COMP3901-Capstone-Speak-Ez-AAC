<script>
export default {
  props: {
    title: ,
  },
  data() {
    return {};
  },
};
</script>

<template>
  <div class="phrase-btn">
    <button type="button" class="btn btn-primary btn-lg btn-block mt-4">
      {{ title }}
    </button>
  </div>
</template>

<style>
.phrase-btn {
  justify-content: center;
  align-items: center;
  text-align: center;
}
.phrase-btn button {
  width: 80%;
}
</style>
