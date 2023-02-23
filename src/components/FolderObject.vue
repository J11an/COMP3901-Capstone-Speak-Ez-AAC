<script>
export default {
  props: {
    title: String,
  },
  data() {
    return {};
  },
};
</script>

<template>
  <div class="phrases-con">
    <div class="saved-phrases">
      <img
        class="folder-img"
        src="/folder-img.png"
        alt="image of folder icon"
      />
      <p class="saved-phrase">{{ title }}</p>
    </div>
  </div>
</template>

<style>
.phrases-con {
  text-align: center;
  margin: 25px;
}
.saved-phrases {
  display: flex;
  flex: 1;
  flex-direction: row;
  /* flex-flow:row wrap; */
  flex-wrap: wrap;
  text-align: center;
  align-items: center;
  justify-content: space-around;
  margin: 10px;
  position: relative;
}

.folder-img {
  width: 200px;
}

.saved-phrase {
  position: absolute;
  top: 65%;
  left: 50%;
  transform: translate(-50%, -50%);
}

/* .folder-icon{
    width: 200px;
    height: 150px;
    border: 1px solid black;
    position: relative;
    clip-path: polygon(0 0, 30% 0, 34% 10%, 100% 10%, 100% 100%, 0 100%);
    margin: 100px;
    background-color: yellow; 
    content: "SOS"; } */
</style>
