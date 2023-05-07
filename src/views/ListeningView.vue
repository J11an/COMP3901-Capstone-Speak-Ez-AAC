<script>
import MessageBar from "../components/MessageBar.vue";

export default {
  components: { MessageBar },

  data() {
    return {
      currentMessage: "",
      messageList: []
    };
  },

  methods: {
  },

  mounted() {
  }

};

</script>

<template>
  <div>

    <!-- Messages container at top -->


    <!-- Message Bar at Bottom -->
    <MessageBar />
  </div>
</template>

<style>
.conversation-container{
  border: solid red 1px;
}
</style>
