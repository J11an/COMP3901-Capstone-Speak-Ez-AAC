<script>
export default {
  props: {
    title: String,
    imageUrl: String,
  },
  data() {
    return {};
  },
};
</script>

<template>
  <div class="card aac-card mb-4 mx-auto" style="width: 18rem">
    <p class="card-text tile-text">{{ title }}</p>
    <img class="card-img-top img-orientation" :src="imageUrl" alt="" />
  </div>
</template>

<style>
.img-orientation {
  position: relative;
  width: 164.19px;
  height: 165.32px;
  left: 60px;
}
.tile-text {
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 32px;
  line-height: 65px;
}

.aac-card {
  background: linear-gradient(
      0deg,
      rgba(103, 80, 164, 0.08),
      rgba(103, 80, 164, 0.08)
    ),
    #fffbfe;
  border: 5px solid #000000;
  box-shadow: 0px 2px 6px 2px rgba(0, 0, 0, 0.15);
  border-radius: 48px;
  width: 291.54px;
  height: 272.67px;
}
</style>
