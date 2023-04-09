<script>
import FolderObject from "../components/FolderObject.vue";

export default {
  components: { FolderObject },
  data: () => ({}),
};
</script>

<template>
  <div class="phrases-con">
    <h2>SELECT FROM YOUR SAVED PHRASES</h2>
    <div class="saved-phrases">
      <RouterLink to="/PhraseView">
        <FolderObject title="SOS" />
      </RouterLink>
      <RouterLink to="/School">
        <FolderObject title="School" />
      </RouterLink>
      <RouterLink to="/Illness">
        <FolderObject title="Illness" />
      </RouterLink>
      <RouterLink to="/addNew">
        <FolderObject title="ADD NEW" />
      </RouterLink>
    </div>
  </div>
</template>

<style></style>
