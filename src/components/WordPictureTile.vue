<script>
export default {
  props: {
    word: String,
    imageUrl: String,
  },
  data() {
    return {};
  },
};
</script>

<template>
  <div class="card aac-card mx-auto" style="width: 18rem">
    <img class="card-img-top img-orientation" :src="imageUrl" alt="" />
    <p class="card-text tile-text">{{ word }}</p>
  </div>
</template>

<style>
.img-orientation {
  /*position: relative;*/
  width: 100px;
  height: 100px;
  top: 10px;
  left: 90px;
  justify-content: center;
}

.tile-text {
  font-family: "Thabit";
  font-style: normal;
  font-weight: 600;
  font-size: 32px;
  line-height: 100px;
  text-align: center;
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
  width: 150px;
  height: 272.67px;
  margin: 10px;
}

.aac-card:hover {
  transform: scale(1.01);
  transition: 100ms;
}
</style>
