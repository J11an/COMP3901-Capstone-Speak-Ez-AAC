import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/speaking",
      name: "speaking",
      component: () => import("../views/SpeakingView.vue"),
    },
    {
      path: "/typing",
      name: "typing",
      component: () => import("../views/TypingView.vue"),
    },
    {
      path: "/listening",
      name: "listening",
      component: () => import("../views/ListeningView.vue"),
    },
    {
      path: "/neweditword",
      name: "neweditword",
      component: () => import("../views/NewEditWordView.vue"),
    },
    {
      path: "/savedphrases",
      name: "savedphrases",
      component: () => import("../views/SavedPhrasesView.vue"),
    },
  ],
});

export default router;
