<script>
import MessageBarListening from "../components/Listening/MessageBarListening.vue";
import Message from "../components/Listening/Message.vue";

export default {
  components: { MessageBarListening, Message },

  data() {
    return {
      messageList: [],
      speakerLabels: [],
      connection:null
    };
  },

  methods: {

  },

  computed : {

  },

  mounted() {
    const testFromArr = ["SPEAKER","LISTENER"];
    this.speakerLabels = ["Speaker1", "Speaker2"];
    for (let i = 0; i < 5; i++) {
        const from = testFromArr[Math.round(Math.random())];
        this.messageList.push({
          id: i,
          msg:`This is a test message from the ${from}`,
          from: from,
          label: Math.round(Math.random())
        })
    }
  }



};

</script>

<template>
  <p>State: {{ connection }}</p>
  <p>Server Msg : {{ serverMsg }} at {{ new Date() }}</p>

  <button @click="testSockConnection">Connect</button>
  <button @click="sendMessage('Hello')">Test Audio Connection</button>

  <div class="listening-container">

    <!-- Messages container at top -->
    <div class="conversation-container" id="con-container">

      <!-- Go through all messages -->
      <div class="msg-body-container" v-for="message in messageList" v-bind:key="message.id">
        <Message :msg="message.msg" :from="message.from" :label="message.label" :speaker-labels="speakerLabels" />
      </div>

      <div id="anchor"></div>

    </div>


    <!-- Message Bar at Bottom -->
    <MessageBarListening :msg-list="messageList" />
  </div>
</template>

<style>
.conversation-container{
  /*border: solid red 1px;*/
  margin: 10px;
  padding: 10px;
  overflow: auto;
  min-height: 80vh;
  max-height: 80vh;

  @media(max-height:1040px){
    min-height: 78vh;
    max-height: 78vh;
  }

  @media(max-height:876px){
    min-height: 73vh;
    max-height: 73vh;
  }

  @media(max-height:738px){
    min-height: 69vh;
    max-height: 69vh;
  }

}

.msg-body-container{
  display: flex;
  margin: 1vw;
}
</style>
