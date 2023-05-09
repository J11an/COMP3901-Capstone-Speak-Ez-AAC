import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { io } from "socket.io-client";

const socket = io("http://localhost:8080", {
  withCredentials: true,
});

const app = createApp(App);

app.use(router);

app.mount("#app");
