import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
// import AddAgeView from "../views/AddAgeView.vue";
// import AddUserView from "../views/AddUserView.vue";
// import CategoriesProfileView from "../views/CategoriesProfileView.vue";
// import ConfirmProfileView from "../views/CategoriesProfileView.vue";
// import ProfileView from "../views/ProfileView.vue";
// import SelectLayoutView from "../views/SelectLayoutView.vue";

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
      path: "/listening",
      name: "listening",
      component: () => import("../views/ListeningView.vue"),
    },
    /*{
      path: "/neweditword",
      name: "neweditword",
      component: () => import("../views/NewEditWordView.vue"),
    },
    {
      path: "/savedphrases",
      name: "savedphrases",
      component: () => import("../views/SavedPhrasesView.vue"),
    },
    {
      path: "/phraseview",
      name: "phraseview",
      component: () => import("../views/PhraseView.vue"),
    },*/
  ],
  linkActiveClass: "active",
  linkExactActiveClass: "exact-active",
});

export default router;
